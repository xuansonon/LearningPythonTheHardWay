
def print_arg_star(*args):
    arg1, arg2, arg3 = args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

def print_arg_one_param(arg1):
    print "arg1: %r" % arg1

def print_arg_two_params(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_no_params():
    print "No params here!"

print_arg_star('Hello','There',3)
print_arg_one_param('Wow')
print_arg_two_params('Hi','Cool')
print_no_params()
