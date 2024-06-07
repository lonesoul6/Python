# *args and *kwargs are used for getting n number of inputs in a function:

def myfunc(args):
    out = []
    for i in range(len(args)):
        if i%2==0:
            out.append((args[i].lower()))
        else:
            out.append((args[i].upper()))
    return ''.join(out)

myfunc('hariharan')

