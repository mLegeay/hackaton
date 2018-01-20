<?php
function main(){
    $equipe = "aylenTerabah";
    $pass= "azerty";

    //test création équipe
    $outPu = envoie_donnee_equipe($equipe, $pass);

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
$outPu = envoi_donnee_score($equipe, $pass, $score_tour);

    console.log($outPu);

}

function calcul_point($couleur, $case){
    switch ($couleur) {
        case("rouge"):
            return $case * 3;
            break;
        case("vert"):
            return $case * 2;
            break;
        default:
            return $case;
            break;
    }
}

function calcul_score_tour($score1, $score2, $score3){
    $score_tour = $score1 + $score2 + $score3;
    return $score_tour;
}

function envoie_donnee_equipe($equipe, $pass){

    $response = "http://192.168.10.1/server-score/api/equipe?equipe=".$equipe;
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, $response);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'accept: text/plain',
        'secret: '.$pass
    ));

    $Output = curl_exec($ch);
    curl_close($ch);

    return $Output;
}

function  envoi_donnee_score($equipe, $pass, $score ){
    $response = "http://192.168.10.1/server-score/api/equipe?equipe=".$equipe."&score=".$score;
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, $response);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'accept: text/plain',
        'secret: '.$pass
    ));

    $Output = curl_exec($ch);
    curl_close($ch);

    return $Output;
}

