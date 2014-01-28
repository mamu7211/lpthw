# assigns x a formatted string
x = "There are %d types of people." % 10
# declaring two string variables
binary = "binary"
do_not = "don't"
# declares y and assigns it the result of a string formatting
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x and y...
print x
# ...each in a different line
print y

# prints two formatted strings, the first using variable x...
print "I said: %r." % x
# the second using variable y as parameter
print "I also said: '%s'." % y

# declares a flag
hilarious = False
# assigns joke_evaluation a question having a debug formatting parameter
joke_evaluation = "Isn't that joke so funny?! %r"

# prints out the question using hilarious as formatting parameter value
print joke_evaluation % hilarious

# declaring two strings...
w = "This is the left side of ..."
e = "a string with a right side."

# ...and print their concatenation
print w + e

# study drills
# 1. again commenting
# 2. two times in line seven, one time in line 15 and one more time in line 17
# 3. i am sure, there is one %d, three %s, two %r - of those %r only line 15 uses a string, line 22 prints a bool, or whatever the boolean type is called in pyhton
# 4. concatenation; maybe that's the way the + operator is implemented to used in python on strings, in php it does not work using +, they use '.', other languages such as VB use '&'...

# sidenote ---
# tried to clear the console within pythons shell and came upon a solution
# 1: import os
# 2. def cls():
# 3.    os.system(['clear','cls'][os.name == 'nt'])
# 4.
# >>> cls()
# that's hilarious, equality "os.name=='nt'" is used as an index to an array
# suggestion was to write >>> os.system('cls' if os.name=='nt' else 'clear')
# looking forward to pythons 'if/then' stuff :-)
