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

#using %r to print out anything
print "%r and %r are formatted using %r." %(name, weight, 'percent+r, which is essentially %r')
print "%r is a floating point number, rounding it, will be %r, displaying it with %r will be %d" %(
	9.25, round(9.25), '%d', round(9.25))