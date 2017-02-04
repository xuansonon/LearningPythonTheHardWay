from sys import argv
script, user_name = argv

prompt = "~> "

print "Hello %r, I am %r" % (script, user_name)
print "I'd like to ask you a few questions."

print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Okay, so, you're name is %s and
you said %s about liking me. You
live in %s, I have no idea where that is.
Finally, you have a %s computer. Nice!
""" % (user_name, likes, lives, computer)
