from sys import argv
script, file_name = argv

print "We are going to be overwriting the file, %r, today." % file_name
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("> ")
text_file = open(file_name, "w")
#text_file = open(file_name, "a") - For Appending data

print "Truncating the file. Goodbye old data!" # Truncating is redundant. A simple open([filename], "w") will suffice to overwrite.
text_file.truncate() # Remove if appending

print "Let's add some new lines to the file."
line1 = raw_input("Enter some text for line 1: ")
line2 = raw_input("Enter some text for line 2: ")
line3 = raw_input("Enter some text for line 3: ")

print "System will now begin to write to file..."
text_file.write(line1 + "\n")
text_file.write(line2 + "\n")
text_file.write(line3 + "\n")

print "Overwriting complete! You can now view the file for changes."

text_file.close()
