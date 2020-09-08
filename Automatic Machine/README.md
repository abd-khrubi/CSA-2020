<h1 align='center'>Automatic Machine <br>50</h1>
<p>You stand before a custom Virtual Machine.
Once you understand the code, the flag will be just there.

The machine is waiting for you at `auto-machine.csa-challenge.com`

Good Luck!</p>
___

<p>
Following the given link, we arrive at a what seems to be a shell terminal, asking for password.
We need to guess the correct password to get the flag.

Upon inspecting the HTML source code of the page, turns out that the shell is not connected to any server, and any 
input to the shell is passed down to an obfuscated script `am.js`.
We need to reverse engineer that script in order to find the correct password.

</p>

<details>
<summary>Spoiler: Solution</summary>
    To reverse the script, first of all I copied the javascript code into python, and then simply ran the script,
    modified the script to take input a special class that I made to mimic a list, and in each iteration, that list 
    initializes in each index (only when accessed by the script) an array with all possible characters, and while 
    iterating, eliminating any character that cause the password check to fail.
    In the end, the list would have 41 cells, and each cell contains exactly one possibility, printing those characters,
    we get the flag:    <br>
<h3 align="center">`CSA{w0w_th4t_wa$_re@lly_s1mpLe_wasn7_1t}`</h3>
     
Script reverse is in `solver.py`
    
</details>