<h1 align='center'>Fix Me If You Can<br>50</h1>

<p>

Fix me if you can and you will be half way to find the flag.

Good Luck!</p>
___


<p>

We are given a corrupted doc file and asked to fix it.

</p>

<details>
  <summary>Solution</summary>
  <p>
  
  1. Fixing the doc file: The correct signature for a doc file (first 8 bytes) is `D0 CF 11 E0 A1 B1 1A E1` but the given
  has `D0 CF 11 E0 A1 B1 1A 1E` as first byte, so by fixing the signature, we fix the doc file.
  2. Getting the flag: The fixed document has 27 pages, the first page contains the text<br>
  ```Hello, 

R U looking for the flag? (-:
You probably succeeded to fix me, now you should find me. 
I hope U R in the right direction, keep going…

Good Luck!
```
<br> And in page 19 contains an image and under it a text in white says:<br>

![Dickinson](image2.png)
```
Maybe 
she 
will 
help
you
```
<br> 

Using Google's image search, I found out that the picture is of [Velvalee Dickinson](https://en.wikipedia.org/wiki/Velvalee_Dickinson).
She used to be a spy for the Japanese during WWII and she used [steganographic messages](https://en.wikipedia.org/wiki/Steganography)
to leak information.<br>

Decoding the image using [LSB Steganography](https://itnext.io/steganography-101-lsb-introduction-with-python-4c4803e08041)
yields this: `48:UTFOQmUxTjBNemxoVGpCZklXNWZaREJqWHpGelgwNHhZek45`. The "48:" indicates the length of the code 
(which comes right after it). This code looks like a Base64 code. so when decoding it using Base64 decode we 
get: `Q1NBe1N0MzlhTjBfIW5fZDBjXzFzX04xYzN9` which also looks like a Base64 code, so when decoding it again using
Base64 I got the flag which is `CSA{St39aN0_!n_d0c_1s_N1c3}`

  </p>
</details>
