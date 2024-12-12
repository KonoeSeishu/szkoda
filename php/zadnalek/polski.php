<html>
    <head>
        <meta charset="utf-8">
        <title>Szkola Ponadgimnazjalna</title>
        <link rel="stylesheet" href="styl.css">
    </head>
    <body>
        <div id="baner">
            <h1>Oceny uczniow: jezyk polski</h1>
        </div>
        <div id="plewy">
            <h1>Lista uczniow:</h1>
            <?php
            $wp=mysqli_connect('localhost', 'root', '', 'szkola') or die ("Brak polaczenia z baza danych");
            $wynik=mysqli_query($wp ,"SELECT imie, nazwisko from uczen");
            while ($wiersz=mysqli_fetch_array($wynik)) 
                {
                    echo "<li>".$wiersz[0].' '.$wiersz[1]."</li>";
                }
            ?>
            </ol>
        </div>

        <div id="pprawy">
            <h2>Uczen:
            <?php
            $wynik=mysqli_query($wp, "SELECT imie, nazwisko FROM uczen where id=2");

            
            while ($wiersz=mysqli_fetch_array($wynik))
                {
                    echo $wiersz[0].' '.$wiersz[1];
                }
            echo "</h2>";
            echo "</h4> Srednia ocen z jezyka polskiego ";
            $wynik=mysqli_query($wp, "SELECT avg(ocena), dataWystawienia FROM ocena WHERE przedmiot_id=1 AND uczen_id=2 ORDER BY ocena;");
            while ($wiersz=mysqli_fetch_array($wynik))
                {
                    echo $wiersz[0];
                }
            echo "</h4>";
            mysqli_close($wp);
            ?>
            </h2>
        </div>

        <div id="stopka">
            <h3>Zespol szkolponadgimnazjalnych<br>strone opracwal: XXX</h3>
        </div>
    </body>
</html>