# drill #3
name = raw_input("Your name is?")
color = raw_input("Your hair color?")
height = float(raw_input("Your height in [m]?"))
weight = float(raw_input("Your weight in [kg]?"))
print "Name:\t%s\nHair:\t%s\n" % (name, color) ,
bmi = weight / (height * height) 
print "BMI:\t%s [kg/m^2]" % round(bmi,1)