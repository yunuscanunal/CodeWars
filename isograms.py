"""
## url = https://www.codewars.com/kata/54ba84be607a92aa900000f1
## kata names = Isograms
### kata level = 7 kyu

### Description:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

"""
def is_isogram(string):
    count = {}
    string = string.lower()
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    if len(set(count.values())) > 1:
        return False
    elif len(set(count.values())) == 0:
        return True
    else:
        return True
