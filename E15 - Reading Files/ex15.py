from sys import argv
script, filename = argv

text = open(filename)
print "Reading contents from: %r:\n" % filename
print text.read()
text.close()

new_text_title = raw_input("Type in the name of another file: ")
new_text = open(new_text_title)
print "Reading contents from: %r:\n" % new_text_title
print new_text.read()
new_text.close()
