import sys, getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
    print(opts)
    print(args)
except:
    pass
    # print help information and exit: