from sys import argv
script, file_input = argv

def unload_contents(f):
    print f.read()

def rewind(f):
    f.seek(0) # Seek will move to position given of a file

def print_single_line(f, line_count):
    print "Line", line_count, f.readline()

current_file = open(file_input)

print "Let's print everything: "
unload_contents(current_file)

print "We'll rewind to start of file."
rewind(current_file)

print "Now, let's print line, by line."
current_line = 1
print_single_line(current_file, current_line)

current_line += 1
print_single_line(current_file, current_line)

current_line += 1
print_single_line(current_file, current_line)

current_file.close()
