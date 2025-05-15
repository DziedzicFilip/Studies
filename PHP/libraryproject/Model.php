<?php
abstract class Model {
    protected static $db;
    protected $table;
    protected $data = [];

    public function __construct() {
        if (!self::$db) {
            $this->connectDB();
        }
    }

    protected function connectDB() {
        try {
            self::$db = new PDO(
                "mysql:host=localhost;dbname=librarydb",
                "root",
                "",
                [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
                ]
            );
        } catch (PDOException $e) {
            die("Połączenie z bazą danych nieudane: " . $e->getMessage());
        }
    }

    public function save() {
        $now = date('Y-m-d H:i:s');
        error_log("Saving data: " . print_r($this->data, true));

        if (isset($this->data['Id']) && !empty($this->data['Id'])) {
            // Update
            $this->data['EditDateTime'] = $now;
            $sets = [];
            foreach ($this->data as $key => $value) {
                if ($key !== 'Id') {
                    $sets[] = "$key = :$key";
                }
            }
            $sql = "UPDATE {$this->table} SET " . implode(', ', $sets) . " WHERE Id = :Id";
        } else {
            // Insert
            $this->data['CreationDateTime'] = $now;
            $this->data['EditDateTime'] = $now;
            $this->data['IsActive'] = 1;
            $columns = implode(', ', array_keys($this->data));
            $values = implode(', ', array_map(fn($key) => ":$key", array_keys($this->data)));
            $sql = "INSERT INTO {$this->table} ($columns) VALUES ($values)";
        }

        error_log("SQL Query: " . $sql);

        try {
            $stmt = self::$db->prepare($sql);
            $result = $stmt->execute($this->data);
            if (!$result) {
                error_log("SQL Error: " . implode(", ", $stmt->errorInfo()));
            }
            return $result;
        } catch (PDOException $e) {
            error_log("Database Error: " . $e->getMessage());
            return false;
        }
    }

    public function find($id) {
        $stmt = self::$db->prepare("SELECT * FROM {$this->table} WHERE Id = :id AND IsActive = 1");
        $stmt->execute(['id' => $id]);
        $result = $stmt->fetch();
        if ($result) {
            $this->data = $result;
            return true;
        }
        return false;
    }

    public function findAll() {
        $stmt = self::$db->prepare("SELECT * FROM {$this->table} WHERE IsActive = 1 ORDER BY CreationDateTime DESC");
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function delete($id) {
        $stmt = self::$db->prepare("UPDATE {$this->table} SET IsActive = 0 WHERE Id = :id");
        return $stmt->execute(['id' => $id]);
    }

    public function getData() {
        return $this->data;
    }

    public function setData($data) {
        $this->data = $data;
    }
}
?>