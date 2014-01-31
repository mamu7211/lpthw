print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)

# drill #2
print "And your body type is %r." % raw_input("Body type?")

# study drills
# 1. offline, but i assuem it waits for some input and returns at a newline or carriage returns
# 2. good question, saw something like raw_input(input_var) but that was wrong, one can use the questions text in the parenthesis
# 3. see ex11.drill3.py - has an type error, lets figure this out soon
# 4. as raw input takes in a string (just a guess, as q 1. is not ansered right now) and %r outputs the raw input (again a guess) it escapes it so it's a valid and thus escaped string; both quotes, double and single are present, so python needs to escape one of them 