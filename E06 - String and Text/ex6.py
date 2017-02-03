x = "There are %d type of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) # Two arguments

print x
print y

print "I said: %r." % x
print "I also said: %r." % y

is_this_joke_funny = True
joke_eval = "Isn't this joke so funny?! %r"

answer_joke_eval = joke_eval % is_this_joke_funny
print answer_joke_eval # One string, and parameter with an argument.


w = "Where are you, E. I miss you!..."
e = "I am here, my love!"

print w + e # Concatenation
