"""
## url = https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
## kata names = Strings end with?
### kata level = 7 kyu

### Description:

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""
def solution(string, ending):
    string2 = ""
    if not len(ending) > len(string):
        for i in range(-len(ending),0):
            string2 += string[i]
        if string2 == ending:
            return True
        elif ending == "":
            return True
    
        else:
            return False
    else:
        return False
    pass
