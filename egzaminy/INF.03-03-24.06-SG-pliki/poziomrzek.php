<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poziomy rzek</title>
    <link rel="stylesheet" type="text/css" href="style.css">

</head>
<body>
    <header id="baner1">
    <img src="obraz1.png" alt="Mapa Polski">
    </header>
    <header id="baner2">
    <h1>Rzeki w województwie dolnośląskim</h1>

    </header>
    <main>
    <form action="poziomRzek.php" method="POST">
    <p class="opcje">
        <input type="radio" name="ro" value="Wszystkie">Wszystkie 
        <input type="radio" name="ro" value="Ponad stan ostrzegawczy">Ponad stan ostrzegawczy
        <input type="radio" name="ro" value="Ponad stan alarmowy">Ponad stan alarmowy 
        <input type="Submit" value="Pokaż">
    </p>

    </form>
    </main>
    <section id="lewy">
    <h3>Stany na dzień 2022-05-05</h3>
    <table>
    <tr><th>Wodomierz</th><th>Rzeka</th><th>Ostrzegawczy</th><th>Alarmowy</th><th>Aktualny</th></tr>
    <!--Skrypt PHP tabela-->
    <?php
        $wp=mysqli_connect("localhost", "root", "", "rzeki2");
        if ((isset($_POST['ro']) && (!empty($_POST['ro']))))
        {
            $wybor=$_POST['ro'];
            echo $wybor;
            if ($wybor=="Wszystkie")
            {
                $zapytanie="SELECT nazwa, rzeka, stanOstrzegawczy, stanAlarmowy, pomiary.stanWody FROM wodowskazy INNER JOIN pomiary on wodowskazy.id=pomiary.wodowskazy_id WHERE pomiary.dataPomiaru='2022-05-05'";
            }
            if ($wybor=="Ponad stan ostrzegawczy")
            {
                $zapytanie='';
            }
            if ($wybor=="Ponad stan alarmowy")
            {
                $zapytanie='';
            }
            $wynik=mysqli_query($wp,$zapytanie);
            while ($wiersz=mysqli_fetch_array($wynik))
            {
                echo "<tr><td>$wiersz[0]</td><td>$wiersz[1]</td><td>$wiersz[2]</td><td>$wiersz[3]</td><td>$wiersz[4]</td></tr>";
            }
            mysqli_close($wp);
        }
    ?>
    </table>
    </section>
    <section id="prawy">
    <h3>Informacje</h3>
    <ul>
        <li>Brak ostrzeżeń o burzach z gradem</li>
        <li>Smog w mieście Wrocław</li>
        <li>Silny wiatr w Karkonoszach</li>
    </ul>
    <h3>Średnie stany wód</h3>
    <!--Skrypt 3-->


    <?php
    $zapytanie="SELECT dataPomiaru, avg('stanWody') FROM 'pomiary' GROUP BY 'dataPomiaru'";
    $wynik=mysqli_query($wp,$zapytanie);
        while($wiersz=mysqli_fetch_array($wynik))
        {
            echo "$wiersz";
        }

    ?>
    <a href="https://komunikaty.pl">Dowiedz się więcej</a>
    <img src="obraz2.jpg" alt="rzeka">
    </section>
    <footer>
    <p>Stronę wykonał Paweł</p>
    </footer>
</body>
</html>