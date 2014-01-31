name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk abbout %s." %name
print "He's %d inches tall." %height
print "He's %d punds heavy." %weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffeee." %teeth

#this line is tricky, tried to get it right
print "If I add %d, %d and %d I get %d." %(
	age, height, weight, age + height + weight)

# drills
# 1. removed my_ using sublimes multiselect [ctrl]+[d] instead of find/replace
# 2. using %r to print out anything
print "%r and %r are formatted using %r." %(name, weight, 'percent+r, which is essentially %r')
print "%r is a floating point number, rounding it, will be %r, displaying it with %r will be %d" %(
    9.25, round(9.25), '%d', round(9.25))
# 3. format characters > http://docs.python.org/2/library/stdtypes.html#string-formatting
print "Formatting characters..."
print " - 'd' signed integer decimal '%'"
print " - Signed integer decimal. using 'd' > %d" %-2
print " - Signed integer decimal. using 'i' > %i" %-2
print " - Signed octal value. using 'o' > %o" %-16
print " - Obsolete type - it is identical to 'd'. using 'u' > %u" %-3
print " - Lowercase signed hexadecimal. using 'x' > %x" %0xab12
print " - Uppercase signed hexadecimal. using 'X' > %X" %0x98fe
print " - Lowercase floating point exponential format. using 'e' > %e" %99e22
print " - Uppercase floating point exponential format. using 'E' > %E" %99e22
print " - Floating point decimal format. using 'f' > %f" %3.3
print " - Floating point decimal format. using 'F' > %F" %4.4
print " - Single character (accepts integer or single character string). using 'c' > %c" %'s'
print " - '%' No argument is converted, results in a '%' character in the result."
print " - escaping format characters like '%%s' writing by writing '%%%%s' does %s!" % 'work'
# 4. converting inches and centimeters and pounds to kg
cm_per_inch = 2.54
kg_per_point = 0.45
print "%s weights %.2f[kg], being %d[cm] in height." %(
    name,
    round(weight * kg_per_point,2),
    height * cm_per_inch )