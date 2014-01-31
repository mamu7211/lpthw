from sys import argv

script, user_name, prompt = argv

#prompt = "\t\t\tYour answer: "

print "Hi %s, I'm script %r" %(user_name, script)
print "I'd like to ask you some questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)
print "Where do you live %s?" %user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# study drills
# 1. offline, damn
# 2. added some tab's, like 'prompt = "\t\t\tYour answer: "'
# 3. added prompt as 
# 4. nothing special, just a string...