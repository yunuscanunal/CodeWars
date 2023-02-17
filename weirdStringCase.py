"""
## url = https://www.codewars.com/kata/52b757663a95b11b3d00062d
## kata names = WeIrD StRiNg CaSe
### kata level = 6 kyu

### Description:

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

"""
def to_weird_case(string):
    wordToWeirdCase = lambda s: ''.join([c.lower() if i%2 else c.upper() for i,c in enumerate(s)])
    toWeirdCase = lambda s: ' '.join([wordToWeirdCase(w) for w in s.split(' ')])
    return toWeirdCase(string)
