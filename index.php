<?php
require_once("tool.php");

$tour = 1;

function fin_de_tour(equipe $equipe){
    $shell_cmd = escapeshellarg('python/data.json');
    $resultat = shell_exec($shell_cmd);
    $parsed_json = json_decode($resultat);

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

    $outPut = envoi_donnee_score($equipe->getEquipeName(), $equipe->getEquipePass(), $score_tour);

    $equipe->addScore($this->tour, $score_tour);

    if($this->tour <= 10){
        $this->tour++;
    }else{
        $this->tour = 1;
    }
    return $equipe;
}

//initialisation equipe
$equipe = new equipe();

$equipe_name = "aylenTerabah";
$pass= "azerty";

//$json = file_get_contents("data.json");
//
//$parsed_json = json_decode($json);
//$case1 = $parsed_json->{'hit_1'}->{'case'};
//$couleur1 = $parsed_json->{'hit_1'}->{'couleur'};
//$case2 = $parsed_json->{'hit_2'}->{'case'};
//$couleur2 = $parsed_json->{'hit_2'}->{'couleur'};
//$case3 = $parsed_json->{'hit_3'}->{'case'};
//$couleur3 = $parsed_json->{'hit_3'}->{'couleur'};

$couleur1 ="rouge";
$couleur2 ="vert2";
$couleur3 ="vert";

$case1=18;
$case2=1;
$case3=20;

$score1 = calcul_point($couleur1, $case1);
$score2 = calcul_point($couleur2, $case2);
$score3 = calcul_point($couleur3, $case3);

$score_tour = calcul_score_tour($score1, $score2, $score3);


//test création équipe
$equipe->setEquipeName($equipe_name);
$equipe->setEquipePass($pass);
$equipe->addScore($tour, $score_tour);

//test d'envoi des score
$outPut = envoi_donnee_score($equipe->getEquipeName(), $equipe->getEquipePass(), $score_tour);


if($tour <= 10){
    $tour++;
}else{
    $tour = 1;
}
