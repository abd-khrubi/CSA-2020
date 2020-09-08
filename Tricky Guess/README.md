<h1 align='center'>Tricky Guess<br>50</h1>

<p>

All you need to know is: netcat `tricky-guess.csa-challenge.com 2222`

Good luck!</p>
___

<p>
We are given a words file `words.txt` that contains 10000 different words, each of them is 12 unique characters long.
Our task is to connect to the server and guess the correct word within the time limit and in less than 15 attempts.
If the guess is wrong, the server prints the amount of correct character in the guessed word, but without the indication
of what characters or their position.
</p>

<details>
  <summary>Solution</summary>
  <p>
  
  The solution is very simple, I just stored all the 10000 words in a set and each time, I choose a word at random from 
  that set, if its wrong I filter the set so only the possible correct answers are left.<br>
  So when guessing the correct word, the server prints the flag:
  </p>
  
  <p align="center">
  
`csa{4ll_th3sE_3v1l_c475_g3n3r4T1nG_w0rd5}`

  </p>
</details>
