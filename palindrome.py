"""
Script name : palindrome
Version     : 1.0
Py version  : 3.6.0
Description : Print out the lowest base palindrome for all numbers up to 1000
"""

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])


def checkPal(string1):
    string2 = string1[::-1]
    if string1 == string2:
        return True
    return False


if __name__ == '__main__':
    for intNum in range(1000):
        for base in range(2,36):
            result = baseN(intNum, base)
            if checkPal(str(result)):
                print(str(intNum) + " base: " + str(base) + " palindrome: " + result)
                break
