print "Let's start the interview."

name_input = raw_input("What is your name: ") # Simple raw_input() -> String
age_input = int(raw_input("How old are you: "))
height_input = float(raw_input("How tall are you in centimetres: "))

response_eval = "Okay, %s, so you are %r years old and %r centimetres tall."
print response_eval % (name_input, age_input, height_input)
