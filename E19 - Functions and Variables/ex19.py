def count_cheese_and_crackers(cheese_count, cracker_count):
    print "You have %d cheese(s)." % cheese_count
    print "You also have %d cracker(s)." % cracker_count
    print "Oh Gromit, look at all that cheeeeeeesseee."
    print "Enough for both of us, isn't that right, old chap?\n"

count_cheese_and_crackers(10, 50) # Passing values directly as arguments.
count_cheese_and_crackers(10 + 40, 50 + 40) # Passing direct values with math!

amount_of_cheese = 36
amount_of_crackers = 53

count_cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Passing variables as arguments.
count_cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 54) # Combining variables and math.
count_cheese_and_crackers(amount_of_cheese * 5, amount_of_crackers * 2) # Combinng variables AND math again!

count_cheese_and_crackers(amount_of_cheese, 46) # Passing variables and direct values
count_cheese_and_crackers(46, amount_of_crackers + 20) # Passing variables and direct values and MATH
count_cheese_and_crackers(int(raw_input("Enter amount of cheese: ")), int(raw_input("Enter amount of crackers: "))) # User inputs as arguments
count_cheese_and_crackers(int(raw_input("Enter amount of cheese: ")), amount_of_crackers) # User input and variables as arguments
count_cheese_and_crackers(int(raw_input("Enter amount of cheese: ")), amount_of_crackers + 45) # User input and variables as arguments AND MATH
