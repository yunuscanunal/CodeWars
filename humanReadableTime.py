"""
## url = https://www.codewars.com/kata/52685f7382004e774f0001f7
## kata names = Human Readable Time
### kata level = 5 kyu

### Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""
def make_readable(seconds):
    hour = seconds//3600
    minute = (seconds%3600)//60
    second = seconds%60
    
    if len(str(hour)) != 2:
        if len(str(minute)) != 2:
            if len(str(second)) != 2:
                return "0{}:0{}:0{}".format(hour,minute,second)
            else:
                return "0{}:0{}:{}".format(hour,minute,second)
            
        else:
            if len(str(second)) != 2:
                return "0{}:{}:0{}".format(hour,minute,second)
            else:
                return "0{}:{}:{}".format(hour,minute,second)
    
    elif len(str(minute)) != 2:
        if len(str(second)) != 2:
                return "{}:0{}:0{}".format(hour,minute,second)
        else:
            return "{}:0{}:{}".format(hour,minute,second)
    
    elif len(str(second)) != 2:
        return "{}:{}:0{}".format(hour,minute,second)
    
    else:
        return "{}:{}:{}".format(hour,minute,second)
