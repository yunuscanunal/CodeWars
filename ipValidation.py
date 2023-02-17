"""
## url = https://www.codewars.com/kata/515decfd9dcfc23bb6000006
## kata names = IP Validation
### kata level = 6 kyu

### Description:

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples

Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

"""
def is_valid_IP(strng):
    str=strng.split(".")
    
    if len(str) != 4:
        return False
    
    for i in str:
        if not i.isdigit():
            return False
        if -1 > int(i):
            return False
        elif 255 < int(i):
            return False
        else:
            if i.startswith("0"):
                if i != "0":
                    return False
    return True
    
