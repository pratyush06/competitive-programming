import re
phoneNumberregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo=phoneNumberregex.search("my number is 456-123-345 and another number is 123-345-333")
print("numbers are", mo.group())

# | in regex is used to match one of given choices

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) 

# The (wo)? part of the regular expression means that the pattern wo is
# an optional group. The regex will match text that has zero instances or
# one instance of wo in it. This is why the regex matches both 'Batwoman' and
# 'Batman'. 

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

#matching zero or more with star with *

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

# matching one or more with +
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

# matching specific repetation with curly braces

haRegex = re.compile(r'(Ha){3}|(Ha){1,5}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

#In addition to the search() method, Regex objects also have a findall()
# method. While search() will return a Match object of the first matched text
# in the searched string, the findall() method will return the strings of every
# match in the searched string.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

charactermatch=re.compile(r'\w\w\w')
print(charactermatch.findall('123'))

# Shorthand character class Represents
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character.
# (Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the
# underscore character.
# \s Any space, tab, or newline character. (Think of this as
# matching “space” characters.)
# \S Any character that is not a space, tab, or newline.


beginsWithHello = re.compile('[^Hello]')
print(beginsWithHello.search('Hello world!'))

removeSpecialCharacter=re.compile(r'[^a-zA-z0-9]')
print(removeSpecialCharacter.findall('123@#$&&')) 
ans=re.sub('[^a-zA-z0-9]', '', '123@@@@#####')
print(ans)

## summary

# Review of Regex Symbols
# This chapter covered a lot of notation, so here’s a quick review of what
# you learned:
# •	 The ? matches zero or one of the preceding group.
# •	 The * matches zero or more of the preceding group.
# •	 The + matches one or more of the preceding group.
# •	 The {n} matches exactly n of the preceding group.
# •	 The {n,} matches n or more of the preceding group.
# •	 The {,m} matches 0 to m of the preceding group.
# •	 The {n,m} matches at least n and at most m of the preceding group.
# •	 {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# •	 ^spam means the string must begin with spam.
# •	 spam$ means the string must end with spam.
# •	 The . matches any character, except newline characters.
# •	 \d, \w, and \s match a digit, word, or space character, respectively.
# •	 \D, \W, and \S match anything except a digit, word, or space character,
# respectively.
# •	 [abc] matches any character between the brackets (such as a, b, or c).
# •	 [^abc] matches any character that isn’t between the brackets.

