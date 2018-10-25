
def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return print("00" + s[2:-2])
        else:
            return print(s[:-2])
    else:
        if s[:2] == '12':
            return print(s[:-2])
        else:
            remove_datetime = s[:-2]
            hours, minutes, secons = remove_datetime.split(":")
            hours = int(hours) + 12
            return print("{}:{}:{}".format(hours, minutes, secons))


timeConversion('12:05:45PM')
