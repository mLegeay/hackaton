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
                <div class="col-md-1">
                </div>
                <div class="col-md-10">
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
                        $NbrLigne = 5;//le nombre d'équipe
                        // -------------------------------
                        $scores = array ('18', '5', '14', '17', '28', '75', '158', '2', '1', '3');

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
                        // pour afficher les libellés de chaque équipe
                        for ($i=1; $i<=$NbrLigne; $i++)
                        {
                            ?>
                            <tr>
                                <td class="text text-center">
                                    <?=
                                        $i;
                                    ?>
                                </td>
                                <?php		// boucle pour chaque tour (de l'équipe)
                                for ($j=1; $j<=$NbrCol; $j++)
                                {
                                    ?>
                                        <td class="table-light text text-dark text-center">
                                    <?=			// -------------------------
                                    // score à afficher
                                        $scores[$j-1];
                                    // -------------------------
                                    ?>		</td>
                                <?php	} // end for
                                ?>
                                <td class="text text-center">
                                    <?=
                                        count($scores);
                                    ?>
                                </td>
                            </tr>
                            <?php
                        } // end for
                        ?>
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




<!-- AJOUT DES GRAPHIQUES -->

<html>
<head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="js/loader.js"></script>
    <script type="text/javascript">

        // Load the Visualization API and the corechart package.
        google.charts.load('current', {'packages':['corechart']});

        // Set a callback to run when the Google Visualization API is loaded.
        google.charts.setOnLoadCallback(drawChart);

        // Callback that creates and populates a data table,
        // instantiates the pie chart, passes in the data and
        // draws it.
        function drawChart() {

            // Create the data table.
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Topping');
            data.addColumn('number', 'Slices');
            data.addRows([
                ['Équipe 1', 3],
                ['Équipe 2', 1],
                ['Équipe 3', 1],
                ['Équipe 4', 1],
                ['Équipe 5', 2]
            ]);

            // Set chart options
            var options = {'title':'Répartition des points par équipe',
                'width':400,
                'height':300};

            // Instantiate and draw our chart, passing in some options.
            var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
            chart.draw(data, options);
        }
    </script>
</head>

<body>
<!--Div that will hold the pie chart-->
<div id="chart_div"></div>
</body>
</html>