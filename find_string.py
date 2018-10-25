"""Sample Input
    ABCDCDC
    CDC

    ininini
    ini
Sample Output: 2"""


# def count_substring(string, sub_string):
#      index = string.find(sub_string)
#      if index > 0:
#          new_string = string[index + 1:len(string)]
#          return 1 + count_substring(new_string,sub_string)
#      else:
#          return 0

def count_substring(string, sub_string):
    for i in range(0, len(string)):
        index = string.find(sub_string, i, len(string))
        if index == -1:
            return 0
        else:
            new_string = string[index + 1:len(string)]
            return 1 + count_substring(new_string, sub_string)


count = count_substring('ininini', 'ini')
print(count)
