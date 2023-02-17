"""
## url = https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
## kata names = Mumbling
### kata level = 7 kyu

### Description:

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(s):
    lst = list()
    for i in range(len(s)):
        string = s[i]*(i+1)
        string = string.capitalize()
        lst.append(string)
    return "-".join(lst)
