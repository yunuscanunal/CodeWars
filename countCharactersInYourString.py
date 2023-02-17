"""
## url = https://www.codewars.com/kata/52efefcbcdf57161d4000091
## kata names = Count Characters in Your String
### kata level = 6 kyu

### Description:

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""
def count(string):
    counter = {}
    for i in set(string):
        counter[i] = string.count(i)
    return counter 
