<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {
color: #ffffff
}

h1 {
font-family: "Lucida Console", "Lucida Sans Typewriter",
"monaco", "Bitstream Vera Sans Mono", monospace; font-size: 24px;
font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px;
}

p {
font-family: "Lucida Console", "Lucida Sans Typewriter", monaco, "Bitstream Vera Sans Mono", monospace;
font-size: 16px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; text-align: absolute;
}

 body {
	 background-color: #212121
 }

 table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
  color: black;
}

tr:nth-child(even) {
  background-color: #ffffff;
}
#animated_div {
width: 120px;
height: 100px;
background: #00c3ff;
color: #ffffff;
position: relative;
font-weight:bold;
font-size:20px;
padding:10px;
animation:animated_div 5s 1;
-moz-animation:animated_div 5s 1;
-webkit-animation:animated_div 5s 1;
-o-animation:animated_div 5s 1;
border-radius:5px;
-webkit-border-radius:5px;
}

@keyframes animated_div
{
0% {transform: rotate(0deg);left:0px;}
25% {transform: rotate(20deg);left:0px;}
50% {transform: rotate(0deg);left:500px;}
55% {transform: rotate(0deg);left:500px;}
70% {transform: rotate(0deg);left:500px;background:#1ec7e6;}
100% {transform: rotate(-360deg);left:0px;}
}

@-webkit-keyframes animated_div
{
0% {-webkit-transform: rotate(0deg);left:0px;}
25% {-webkit-transform: rotate(20deg);left:0px;}
50% {-webkit-transform: rotate(0deg);left:500px;}
55% {-webkit-transform: rotate(0deg);left:500px;}
70% {-webkit-transform: rotate(0deg);left:500px;background:#1ec7e6;}
100% {-webkit-transform: rotate(-360deg);left:0px;}
}

@-moz-keyframes animated_div
{
0%  {-moz-transform: rotate(0deg);left:0px;}
25% {-moz-transform: rotate(20deg);left:0px;}
50%  {-moz-transform: rotate(0deg);left:500px;}
55%  {-moz-transform: rotate(0deg);left:500px;}
70%  {-moz-transform: rotate(0deg);left:500px;background:#1ec7e6;}
100% {-moz-transform: rotate(-360deg);left:0px;}
}

@-o-keyframes animated_div
{
0% {transform: rotate(0deg);left:0px;}
25% {transform: rotate(20deg);left:0px;}
50%  {transform: rotate(0deg);left:500px;}
55%  {transform: rotate(0deg);left:500px;}
70%  {transform: rotate(0deg);left:500px;background:#167a8b;}
100% {transform: rotate(-360deg);left:0px;}
}
</style>
</head>
<body>
  <h1 id="animated_div" style="text-align: center"> Simple game using the pygame module in python. </h1>
  <p> A simple game code sample <br>
  In case you don't have python installed, you can install it from here: https://www.python.org/downloads/
<br>
<br>
After installing python, if you don't have pygame installed, open your default terminal and paste this code: pip install pygame.
<br>
Now, copy paste all the code from the file "main.py" to your default text editor. Finally, run the file!!!
<br> </p>
  <h4> Thank you for visiting. I'm Ewnet and this is ET64. </h4>
  </body>
  </html>
