<!--<?php include("css/ihm_score.less") ?>-->
<!--<?php include("js/ihm_score.js") ?>-->

<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- bloque la compatibilité IE -->
        <link href="css/ihm_score.less" rel="stylesheet">
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <title>Tableau des scores</title>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-md-2">
                </div>
                <div class="col-md-8">
                    <!-- affichage du tableau des scores -->
                    <table border = 1>
                        <tbody>
                        <?php
                        $NbrCol = 10; //le nombre de tours
                        $NbrLigne = 5;//le nombre d'équipe
                        // -------------------------------
                        $scores = array ('score1', 'score2', 'score3', 'score4', 'score5', 'score6', 'score7', 'score8', 'score9', 'score10');

                        // affichage de l'en-tête du tableau
                       ?>
                        <td>
                            <?php
                                echo ' Équipe / Tours ';
                            ?>
                        </td>
                        <?php
                        for ($i=1; $i<=$NbrCol; $i++) {
                            ?>
                            <td>
                                <?php
                                echo 'Tour n° '.$i;
                                ?>
                            </td>
                            <?php
                        }
                        // pour chaque équipe
                        for ($i=1; $i<=$NbrLigne; $i++)
                        {
                            ?>
                            <tr>

                                <td>
                                    <?php
                                        echo 'Équipe n° '. $i;
                                    ?>
                                </td>


                                <?php		// pour chaque tour (de l'équipe)
                                for ($j=1; $j<=$NbrCol; $j++)
                                {
                                    ?>		<td>
                                    <?php			// -------------------------
                                    // score à afficher
                                    echo ' nb'.$scores[$j-1].' ';
                                    // -------------------------
                                    ?>		</td>
                                <?php	} // end for
                                ?>
                            </tr>
                            <?php
                        } // end for
                        ?>
                        </tbody>
                    </table>

                </div>
                <div class="col-md-2">
                    <!-- -->
                </div>
            </div>
        </div>
        <script src="js/ihm_score.js"></script>
        <script src="bootstrap/js/jquery.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
    </body>
</html>