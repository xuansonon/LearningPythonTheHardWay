from sys import argv
from os.path import exists

script, read_file_name, write_file_name = argv

start_message = "We will be going to copy the contents of %r into %r today."
print start_message % (read_file_name, write_file_name)
copied_from = "Contents were copied from: %r." % read_file_name
input_file = open(read_file_name)
input_file_contents = input_file.read()
print "The input file is found. File length: %d bytes" % len(input_file_contents)
input_file.close()

print "Checking if the output file exists: %r" % exists(write_file_name)
print "When you are ready to copy file contents, hit RETURN - otherwise Ctrl + C to abort."
raw_input("> Ready?")

output_file = open(write_file_name, "w")

output_file.write(input_file_contents + "\n" + copied_from)
output_file.close()

print "Copy complete. Check %r for changes." % write_file_name
