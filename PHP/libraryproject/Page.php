<?php

abstract class Page { 
   
    const ACTION_LIST = 'list';
    const ACTION_CREATE = 'create';
    const ACTION_EDIT = 'edit';
    const ACTION_DELETE = 'delete';
    const ACTION_SAVE = 'save';

    protected $title;
    protected $action;

    public function __construct($title = '') {
        $this->title = $title;
        $this->action = $_GET['action'] ?? self::ACTION_LIST;
    }

    protected function header() {
        return '
        <!DOCTYPE html>
        <html lang="pl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>'.$this->title.'</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="index.php"> '.$this->title.'</a>
                </div>
            </nav>
            <div class="container mt-4">
        ';
    }

    protected function footer() {
        return '
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        ';
    }

    public function render() {
        echo $this->header();
        
        switch ($this->action) {
            case self::ACTION_CREATE:
                echo $this->generateViewAdd();
                break;
            case self::ACTION_EDIT:
                echo $this->generateViewEdit();
                break;
            case self::ACTION_SAVE:
                echo $this->enterModelDataFromForm();
                break;
            case self::ACTION_DELETE:
                echo $this->delete();
                break;
            default:
                echo $this->generateViewAll();
        }
        
        echo $this->footer();
    }

  
    abstract public function generateViewAdd();
    abstract public function generateViewEdit();
    abstract public function generateViewAll();
    abstract public function addNew();
    abstract public function edit();
    abstract public function enterModelDataFromForm();
    abstract public function delete();
}
?>