<h1 align='center'>Dinner Party<br>20</h1>

<p>

Five women sat in a row at the dinner table. Each had got there in a different way, each was eating a different kind of food, each had brought with her a different object and each had left at home a different pet. 
How were the women arranged, and which woman owned what object?
Invoke submit.py with your solution to obtain the flag. The solution should consist of "woman object" pairs (without quotes, case sensitive), in order of seating from left to right. 

For example:
submit.py Lovelace telescope Germain abacus Franklin laptop Curie pencil Noether scales
IMPORTANT: Give the program a minute or two to produce the flag for you.

Good Luck!</p>
___


<p>


With this challenge attached 3 files:
* flag.txt.enc      - Encrypted flag
* submit.py         - Decryption algorithm
* dinner_party.txt  - The riddle

This is a similar to [Einstein's Riddle](https://udel.edu/~os/riddle.htm), You just need to apply logic in order
to narrow down all the possibilities
 
</p>

<details>
  <summary>Solution</summary>
  <p>
  
  There are two ways to solve this; you can apply logic and narrow down all the possible solutions, or you can use
  a Constraint Satisfaction Problem (CSP) system to solve (which I did here in `dinner.py`).
  
  Doing so I ended up with four possible solutions, among them, this is the correct one:
  
|Seat <br>(from left to right) |Name        |Item       |
|------------------------------|-------     |----       |
|1                             |Germain     |abacus     |
|2                             |Franklin    |laptop     |
|3                             |Noether     |scales     |
|4                             |Lovelace    |pencil     |
|5                             |Curie       |telescope  |

So by invoking<br>

`python3 submit.py Germain abacus Franklin laptop Noether scales Lovelace pencil Curie telescope`

I got the flag:<br>

`CSA{70n19H7_We_d1Ne_1n_HELL}`

  </p>
</details>
