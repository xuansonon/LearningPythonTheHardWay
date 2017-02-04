from sys import argv
script, first, second, third = argv

argument_text = "Here are the following arguments found: %r, %r, %r, %r"
print argument_text % (script, first, second, third)

user_input = raw_input("What is your name: ")
print "Hello %s, I am %r" % (user_input, script)
