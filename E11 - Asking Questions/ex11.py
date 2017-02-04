# Exercise 11 - Asking Questions
print "Let's start the interview."

print "What is your name: ",
name_input = raw_input()

print "How old are you: ",
age_input = int(raw_input()) # Padding int() outside of raw_input() will convert input to int

print "How tall are you (in centimetres): ",
height_input = float(raw_input())

return_response = "Okay, %s, so you are %r years old and %rcm tall. You're hired!"
print return_response % (name_input, age_input, height_input)
