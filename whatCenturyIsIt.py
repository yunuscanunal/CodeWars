"""
## url = https://www.codewars.com/kata/52fb87703c1351ebd200081f
## kata names = What Century is it?
### kata level = 6 kyu

### Description:

Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples

"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"

"""
def what_century(year):
    if year[-2:] == "00":
        cent = str((int(year) // 100))
    else:
        cent = str((int(year) // 100)+1)
        
    if cent == "11" or cent == "12" or cent == "13":
        return cent+"th"
    elif cent[-1] == "1":
        return cent+"st"
    elif cent[-1] == "2":
        return cent+"nd"
    elif cent[-1] == "3":
        return cent+"rd"
    else:
        return cent+"th"
