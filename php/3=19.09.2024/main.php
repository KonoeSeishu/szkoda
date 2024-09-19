
<?php

$tab = array("Adam" => "Stone", "Annie" => "Max", "Mark" => "Stark", "Hans" => "Aber");

$size_tab = count($tab);
$size_tab = sizeof($tab);


show($tab);

asort($tab);
show($tab);
arsort($tab);
show($tab);
ksort($tab);
show($tab);
krsort($tab);

function show($tab)
{
    foreach($tab as $key => $thing)
    {
        echo "$key $thing", "<br>";
    }
    echo "<br>";
}