tabby_cat = "\tI'm a tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t  Cat food
\t  Fishies
\t  Catnip\n\t  Grass
'''
#"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

## fun, really? kinda!
#while True:
#	for i in ["/", "-", "|", "\\", "-", "|"]:^
#		print "%s\r" % i,

# drill #3
header = "%s\n%s\n" %("%s\t%s","-"*20)
strange = "This is a very strange string!\rThis is a cool\n"

# drill #4
print header % ("Weight","[kg]")
print strange;
print "1a. %s\n1b. %r\n2a. %s\n2b. %r\n" %("double \" quotes", "double \" quotes", 'single \' quotes', 'single \' quotes')
double_escapes = "double \" and single \' quotes"
double_escapes_2 = 'double \" and single \' quotes'
print "3a. %s\n3b. %r\n" % (double_escapes, double_escapes)
print "4a. %s\n4b. %r\n" % (double_escapes_2, double_escapes_2)

# study drills
# 1. not done
# 2. no difference using ''' instead of """ - maybe when printing """ we should use another escape sequense thant the one we start the multi line text with?
# 3. see above, variables 'header' and 'strange'
# 4. see above, strings will be enclosed in opposite format, see next line to figure our how it behaves with two escaped quote types - looks like single quotes are the one python uses as primary quote char
