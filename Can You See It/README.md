<h1 align='center'>Can You See It?<br>40</h1>

<p>

All we got is this video.
Can you please help?

Good Luck!</p>
___


<p>

We are give an about 12.5 hours long video. 
The video only has exactly 3 unique frame; white, black and gray.
 
</p>

<details>
  <summary>Solution</summary>
  <p>
  
  First of all, I noticed that each frame only consists of one color, either white, black or gray, 
  so I extracted the frames' colors grayscale value (between 0 and 1) into an array.
  Now I have exactly `455846` frames. What's interesting about that number that it has few 
  dividers: `2x227923, 317x1438, 634x719`. arranging the colors values from the video in those height x width configurations,
  I saw that 317x1438 gives us a clear image of the flag:<br>
  
  <center><img src="flag.png" width="680" height="150"></center>
    <br><br>

`CSA{Ev3ry_mov1e_must_hav3_a_Purpos3}`

  </p>
</details>
