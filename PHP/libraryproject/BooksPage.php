<?php 
require_once 'Page.php';
require_once 'Book.php';

class BooksPage extends Page { 
    private $book;

    public function __construct() {
        parent::__construct('Biblioteka - Książki');
        $this->book = new Book();
    }

    public function generateViewAll() {
        $books = $this->book->findAll();
        
        $html = <<<HTML
        <h1>Lista książek</h1>
        <a href="index.php?action=create" class="btn btn-primary mb-3">Dodaj nową książkę</a>
        <div class="row row-cols-1 row-cols-md-3 g-4">
        HTML;

        foreach ($books as $book) {
            $html .= <<<HTML
            <div class="col">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">{$book['Title']}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">{$book['Author']}</h6>
                        <p class="card-text">
                            <strong>Gatunek:</strong> {$book['Genre']}<br>
                            <strong>Rok wydania:</strong> {$book['PublishYear']}<br>
                        </p>
                        <p class="card-text">
                            <small class="text-muted">
                                {$book['Summary']}
                            </small>
                        </p>
                    </div>
                    <div class="card-footer">
                        <div class="btn-group" role="group">
                            <a href="index.php?action=edit&id={$book['Id']}" class="btn btn-warning btn-sm">Edytuj</a>
                            <a href="index.php?action=delete&id={$book['Id']}" 
                               class="btn btn-danger btn-sm" 
                               onclick="return confirm('Czy na pewno chcesz usunąć tę książkę?')">Usuń</a>
                        </div>
                    </div>
                </div>
            </div>
            HTML;
        }

        $html .= "</div>";
        return $html;
    }

    public function generateViewAdd() {
        return $this->generateForm("Dodaj nową książkę", self::ACTION_SAVE);
    }

    public function generateViewEdit() {
        $id = $_GET['id'] ?? null;
        if (!$id || !$this->book->find($id)) {
            return '<div class="alert alert-danger">Książka nie została znaleziona.</div>';
        }
        return $this->generateForm("Edytuj książkę", self::ACTION_SAVE, $this->book->getData());
    }

    private function generateForm($title, $action, $data = []) {
        $id = $data['Id'] ?? '';
        $bookTitle = $data['Title'] ?? '';
        $author = $data['Author'] ?? '';
        $genre = $data['Genre'] ?? '';
        $publishYear = $data['PublishYear'] ?? '';
        $summary = $data['Summary'] ?? '';
        $notes = $data['Notes'] ?? '';

        return <<<HTML
        <h1>{$title}</h1>
        <form method="post" action="index.php?action={$action}">
            <input type="hidden" name="Id" value="{$id}">
            <div class="mb-3">
                <label for="Title" class="form-label">Tytuł</label>
                <input type="text" class="form-control" id="Title" name="Title" value="{$bookTitle}" required>
            </div>
            <div class="mb-3">
                <label for="Author" class="form-label">Autor</label>
                <input type="text" class="form-control" id="Author" name="Author" value="{$author}" required>
            </div>
            <div class="mb-3">
                <label for="Genre" class="form-label">Gatunek</label>
                <input type="text" class="form-control" id="Genre" name="Genre" value="{$genre}">
            </div>
            <div class="mb-3">
                <label for="PublishYear" class="form-label">Rok wydania</label>
                <input type="number" class="form-control" id="PublishYear" name="PublishYear" value="{$publishYear}">
            </div>
            <div class="mb-3">
                <label for="Summary" class="form-label">Streszczenie</label>
                <textarea class="form-control" id="Summary" name="Summary" rows="3">{$summary}</textarea>
            </div>
            <div class="mb-3">
                <label for="Notes" class="form-label">Notatki</label>
                <textarea class="form-control" id="Notes" name="Notes" rows="3">{$notes}</textarea>
            </div>
            <button type="submit" class="btn btn-primary">Zapisz</button>
            <a href="index.php" class="btn btn-secondary">Anuluj</a>
        </form>
        HTML;
    }

    public function addNew() {
        error_log("AddNew called");
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            error_log("POST data in addNew: " . print_r($_POST, true));
            $errors = $this->book->validate($_POST);
            if (empty($errors)) {
                $this->book->setData($_POST);
                if ($this->book->save()) {
                    header('Location: index.php');
                    exit;
                }
                error_log("Error saving book: " . print_r($_POST, true));
                return '<div class="alert alert-danger">Błąd podczas zapisywania książki.</div>';
            }
            error_log("Validation errors: " . implode(", ", $errors));
            return '<div class="alert alert-danger">' . implode('<br>', $errors) . '</div>';
        }
        return $this->generateViewAdd();
    }

    public function edit() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $errors = $this->book->validate($_POST);
            if (empty($errors)) {
                $this->book->setData($_POST);
                if ($this->book->save()) {
                    header('Location: index.php');
                    exit;
                }
                return '<div class="alert alert-danger">Błąd podczas aktualizacji książki.</div>';
            }
            return '<div class="alert alert-danger">' . implode('<br>', $errors) . '</div>';
        }
    }

    public function enterModelDataFromForm() {
        error_log("POST data: " . print_r($_POST, true));
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            if (isset($_POST['Id']) && !empty($_POST['Id'])) {
                return $this->edit();
            } else {
                return $this->addNew();
            }
        }
        return '<div class="alert alert-danger">Brak danych do zapisania.</div>';
    }

    public function delete() {
        if (isset($_GET['id'])) {
            if ($this->book->delete($_GET['id'])) {
                header('Location: index.php');
                exit;
            }
            return '<div class="alert alert-danger">Błąd podczas usuwania książki.</div>';
        }
        return '<div class="alert alert-danger">Nie podano identyfikatora książki.</div>';
    }
}
?>