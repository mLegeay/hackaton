<?php
require_once("tool.php");

$equipe = "aylenTerabah";
$pass= "azerty";

//test création équipe

$json = file_get_contents("data.json");

$parsed_json = json_decode($json);
$case1 = $parsed_json->{'hit_1'}->{'case'};
$couleur1 = $parsed_json->{'hit_1'}->{'couleur'};
$case2 = $parsed_json->{'hit_2'}->{'case'};
$couleur2 = $parsed_json->{'hit_2'}->{'couleur'};
$case3 = $parsed_json->{'hit_3'}->{'case'};
$couleur3 = $parsed_json->{'hit_3'}->{'couleur'};

$score1 = calcul_point($couleur1, $case1);
$score2 = calcul_point($couleur2, $case2);
$score3 = calcul_point($couleur3, $case3);

$score_tour = calcul_score_tour($score1, $score2, $score3);

//test d'envoi des score
$outPut = envoi_donnee_score($equipe, $pass, $score_tour);
var_dump($outPut);
