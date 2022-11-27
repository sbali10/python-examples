Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  and the integer value .


Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.

--------------------------------------------------------------------
# /usr/bin/env python3

from itertools import permutations


S , N = input().split()

for i in list(permutations(sorted(S), int(N))):
    print(''.join(i))
	
-----------------------------------------------------------------------	