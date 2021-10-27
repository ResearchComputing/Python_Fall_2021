### The Collatz Sequence

Given an positive integer *n*, we can generate a sequence of numbers according to the following algorithm:
1. If *n* is even, create a new number by dividing *n* by 2.  If *n* is odd, multiply by 3 and add 1.
2. Repeat this process until you arrive at the number 1.

The sequence of numbers generated according to these rules is known as the Collatz (also Hailstone) sequence associated with *n*.   The Collatz Conjecture states that, given any positive starting number n, the sequence will eventually terminate at 1.   This conjecture remains to be proven, but it is known to be true for every number tested to date.

Write a function that returns the Collatz sequence of a given number.  The sequence should be returned as a list of numbers.

For example, evaluating collatz_seq(5) should return the list   
  
[ 5,16,8,4,2,1 ], 

and collatz_seq(20) should yield  
  
[ 20, 10, 5, 16, 8, 4, 2, 1 ] .

