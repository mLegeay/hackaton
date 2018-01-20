<?php
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
function envoie_donnée_equipe($equipe, $pass){

    $response = "http://192.168.10.1/server-score/api/equipe?equipe=".$equipe;
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, $response);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'accept: text/plain',
        'secret: '.$pass
    ));

    curl_exec($ch);
    curl_close($ch);


}

