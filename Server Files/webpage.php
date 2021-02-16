<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
  border: 1px solid #ddd;
  font-size: 14;
  margin-left: 50px
}
div {
    height:300px; 
    overflow:auto; 
    align:left;
    width:47%;
}
th, h1 {
  text-align: Center;
  padding: 8px;
}
td {
  text-align: Left;
  padding: 8px;
}
tr:nth-child(even){background-color: #f2f2f2}
</style>
</head>
<body>
    <br><h1>Sentiment Analysis of 3 News Channels </h1><br><hr><br>
    <img src='Images/1stNews.svg' align= 'right'; height= 350px; width= 600px; style="margin: -10px 20px">
<tbody>
<td>
   <div>
     <table>
         <th>Tweets of 1st News Channel</th>

<?php
$file = fopen("1stNews.txt", "r") or die("Unable to open file!");
while (!feof($file)){   
    $data = fgets($file); 
    echo "<tr><td>" . str_replace('|','</td><td>',$data) . '</td></tr>';
}
?>
    
    </table>
    </div>
</td>
<br><br><hr><br><br>

<?php
fclose($file);
?>

<img src='Images/2ndNews.svg' align= 'right'; height= 350px; width= 600px; style="margin: -10px 20px">
<td>
   <div>
    <table>
        <th>Tweets of 2nd News Channel</th>

<?php
$file2 = fopen("2ndNews.txt", "r") or die("Unable to open file!");
while (!feof($file2)){   
    $data2 = fgets($file2); 
    echo "<tr><td>" . str_replace('|','</td><td>',$data2) . '</td></tr>';
}
?>
    </table>
    </div>
</td>
<br><br><hr><br><br>

<?php
fclose($file2);
?>

<img src='Images/3rdNews.svg' align= 'right'; height= 350px; width= 600px; style="margin: -10px 20px">
<td>
   <div>
    <table>
        <th>Tweets of 3rd News Channel</th>

<?php
$file3 = fopen("3rdNews.txt", "r") or die("Unable to open file!");
while (!feof($file3)){   
    $data3 = fgets($file3); 
    echo "<tr><td>" . str_replace('|','</td><td>',$data3) . '</td></tr>';
}
?>
    </table>
    </div>
</td><br><br><hr><br>


<?php
fclose($file3);
?>
</tbody>

<h1>Comparison of all 3 News Channels</h1>
<img src='Images/FinalComparison.svg' height= 90%; width= 90% style="margin: -10px 40px">

</body>