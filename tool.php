<?php
define("SERVER_URL","http://192.168.10.1/server-score/api/");
function calcul_point($couleur, $case){
    switch ($couleur) {
        case("rouge"):
            return $case * 3;
            break;
        case("vert2"):
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

    $response = SERVER_URL."equipe?equipe=".$equipe;
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
    $response = SERVER_URL."equipe?equipe=".$equipe."&score=".$score;
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

