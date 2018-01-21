<!--<?php include("css/ihm_score.less") ?>-->
<!--<?php include("js/ihm_score.js") ?>-->
<?php include ("../equipe.php");?>
<?php include ("../index.php");
$total = 0; ?>

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
                <div class="col-md-1">
                </div>
                <div class="col-md-10">

                    <form>
                        <input type="button" name="tour" id="tour" value="Fin de tour" />
                    </form>
                    <!-- affichage du tableau des scores -->
                    <table class="table table-bordered table-dark table-hover table-responsive table-striped"> <!-- table-striped permet d'afficher une ligne sur deux fond gris pour le tableau -->
                        <tbody>
                        <div class="h1 text text-center text-primary">
                        <?=
                         'Tableau des scores';
                        ?>
                         </div>
                        <?php
                        $NbrCol = 10; //le nombre de tours
                        // -------------------------------

                        // affichage de l'en-tête du tableau
                       ?>
                        <td class="text text-center">
                            <?php
                                echo ' Équipe / Tours ';
                            ?>
                        </td>
                        <?php
                        for ($i=1; $i<=$NbrCol; $i++) {
                            ?>
                            <td class="text text-center">
                                <?=
                                    'Tour '.$i;
                                ?>
                            </td>
                            <?php
                        }
                        ?>
                            <td>
                                <?=
                                    'Total';
                                ?>
                            </td>
                        <?php

                            ?>
                            <tr>
                                <td class="text text-center">
                                    NSFW
                                </td>
                                <?php		// boucle pour chaque tour (de l'équipe)
                                for ($j=1; $j<=$NbrCol; $j++)
                                {
                                    ?>
                                        <td class="table-light text text-dark text-center" name="col<?= $j ?>">
                                    <?php		// -------------------------
                                    // score à afficher
                                    //    $scores[$j-1];
                                    // -------------------------
                                    ?>	</td>
                                <?php	} // end for
                                ?>
                                <td class="text text-center">
                                   <!-- total -->
                                    <?= $total ?>
                                </td>
                            </tr>

                        </tbody>
                    </table>

                </div>
                <div class="col-md-1">
                    <!-- -->
                </div>
            </div>
        </div>
        <script src="js/ihm_score.js"></script>
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>


<form action="../equipe.php" method="post">

        <p>
            <label>Nom d'équipe : </label><input type="text" name="equipe" id="equipe" />
            <label>Mot de passe : </label><input type="password" name="password" id="password" />
        </p>

    <button id="test">test</button>
</form>

<script>
    $('#test').onclick(function(e){
        $equipe1 = new equipe();
        $equipe1->setEquipeName($("input[name=equipe]").val());
        $equipe1->setEquipePass($("input[name=password]").val());
        var_dump(envoie_donnee_equipe($equipe->getEquipeName(),$equipe->getEquipePass()));
    });
    $('#tour').onclick(function(){
        $equipe1 = fin_de_tour($equipe1);
       for($i=0; $1<10; $i++){
           if($equipe1->score_tours[$i] != null ){
                $('col<?= $i ?>').html($equipe1->score_tours[$i]);
                $total += score_tours[$i];
           }
       }
        });
</script>
