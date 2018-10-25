
"""Find the Minimum Number
Constraints
2 <= n <= 50

Output Format

Print the string on a single line. Each integer in the string should
be written as 'int' and the string must accurately show how functions can be called to find the smallest of integers.

Sample Input 0

2

Sample Output 0

min(int, int)"""

n = 3
min_fun = "min(int, int)"
if n == 2:
    print(min_fun)
else:
    string = "min(int, int)"
    for i in range(2, n):
        index = string.rfind("int")
        string_1 = string[0:index-1]
        string_2 = string[index: len(string)]
        string_2 = string_2.replace("int", min_fun)
        string = string_1 +" "+ string_2
    print(string)
