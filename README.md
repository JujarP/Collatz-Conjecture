# Collatz-Conjecture
The Collatz Conjecture also known as the "3n+1 problem", introduced in 1937 is a simple Mathematics problem that has dumbfounded mathematicians. The rules are simple:
1. Pick a random positive integer
2. If it's even, divide it by 2
3. If it's odd, multiply by 3 and add 1
4. Then, repeat with the result, and keep repeating
5. Eventually the sequence will always reach 1, irrespective of the random positive integer you chose in step 1

## Example
1. Begin with a completely random positive integer. Let's take 5.
2. 5 is odd, so we muliply by 3 and add 1, yielding 16.
3. 16 is even, so we divide by 2, yielding 8.
4. 8 is even, we we divide by 2, yielding 4
5. 4 is even, so we divide by 2, yielding 2
6. 2 is even, so we divide by 2, yielding 1

You can pick any positive integer, and it will always reach 1.

# Using CollatzConjecture.py
This is a fully automated Collatz conjecture solver and plotter.
There are three user inputs:
1. initial_int -> enter your random positive integer here
2. iter_limit -> the number of iterations you want the solver to cycle through. Set this to an arbitrary large number.
3. verbose -> if you want the output of the calculation

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://choosealicense.com/licenses/mit/)
