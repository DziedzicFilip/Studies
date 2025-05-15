<?php
require_once 'Model.php';

class Book extends Model {
    protected $table = 'books';

    public function validate($data) {
        $errors = [];
        
        if (empty($data['Title'])) {
            $errors[] = "Tytuł jest wymagany";
        }
        if (empty($data['Author'])) {
            $errors[] = "Autor jest wymagany";
        }
        if (!empty($data['PublishYear'])) {
            if (!is_numeric($data['PublishYear']) || $data['PublishYear'] < 1000 || $data['PublishYear'] > date('Y')) {
                $errors[] = "Rok wydania jest nieprawidłowy";
            }
        }

        return $errors;
    }
}
?>