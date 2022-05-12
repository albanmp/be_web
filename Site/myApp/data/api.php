<?php
require_once("config.php");
$db = new PDO($dsn, $username, $password, $options);

function read($db, $requestParams){
    $queryParams = [];
    $queryText = "SELECT * FROM `events`";
    $query = $db->prepare($queryText);
    $query->execute($queryParams);
    $events = $query->fetchAll();
    return $events;
}

switch ($_SERVER["REQUEST_METHOD"]) {
    case "GET":
        $result = read($db, $_GET);
        break;
    case "POST":
        // we'll implement this later
    break;
    default: 
        throw new Exception("Unexpected Method"); 
    break;
}
header("Content-Type: application/json");
echo json_encode($result);