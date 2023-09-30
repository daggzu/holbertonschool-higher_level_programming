#!/usr/bin/python3
# This is a shebang line, specifying the path to the Python interpreter
# that should be used to execute the script.

if __name__ == "__main__":
    import sys
    args = len(sys.argv)


if args == 1:
    
    print("0")
   
else:
    sum = 0
 
    for i in range(1, args):
    

        sum += int(sys.argv[i])

    print("{}".format(sum))
