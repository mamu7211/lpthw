# imports command line argument variable argv from package/lib sys
from sys import argv

script, filename = argv # assigns variables script and filename with elements of the argv array 

txt = open(filename) # creates a file instance given in argv[1]

print "Here's your file %r:" %filename # prints the filename given in argv[0]
print txt.read() # prints the files content
txt.close() # 8.1

print  "Type the filename again:" # prompts the user to enter again a filename
file_again = raw_input("> ") # displays a prompt and assigns user input (raw) to a variable called file_again

txt_again = open(file_again) # creates a file instance called txt_again

print txt_again.read() # reads the file contents and prints it
txt_again.close() # 8.2

# study drills
#
# 1. write above each line what it does
# 2. TODO search the web for "python open" - currently offline, so postponed
# 3. TODO search the web for "python methods", "~functions" or "~commands" - currently offline, so postponed
# 4. getting rid of lines 10 - 15 > txt_again is not defined
# 5. use raw_input only? don't get that, instead of having filename from argv?
# 6. TODO pydoc is not installed - how to install this file
# 7. use open from python command line - done >>> open("ex15.py").read
# 8. close the files you opened - see #8.1 and #8.2 above