"""Read problems from the file 'problem-instances-intermediate.txt' and convert them to a form that can be used by Dipankar's XML generator."""

import sys

f = open("problem-instances-intermediate.txt", 'r')

line = f.readline()
while line:
    stripped = "".join(line.split())
    if stripped != "" and stripped[0] != "#":
        bs = eval(line)
        user = eval(f.readline())
        print(len(user))
        print(len(bs))
        u = ['u' + str(x) for x in user]
        b = ['b' + str(x) for x in bs]
        entities = u + b
        entities.sort(key=lambda x: int(x[1:]))
        for i in entities:
            print(i)
        print()
    line = f.readline()

f.close()

def get_xml(input_file, output_file):
    """Get raw input (like the input formatted in the file 'problem-instances-intermediate.txt')
    and convert it in a format suitable for Frodo 2."""
    # This function basically does what the above code does, just gives a function so that we
    # can specify input and output files.

    f = open(input_file, 'r')
    g = open(output_file, 'w')

    line = f.readline()
    while line:
        stripped = "".join(line.split())
        if stripped != "" and stripped[0] != "#":
            bs = eval(line)
            user = eval(f.readline())
            g.write(str(len(user)) + "\n")
            g.write(str(len(bs)) + "\n")
            u = ['u' + str(x) for x in user]
            b = ['b' + str(x) for x in bs]
            entities = u + b
            entities.sort(key=lambda x: int(x[1:]))
            for i in entities:
                g.write(str(i) + "\n")
            g.write("\n")
        line = f.readline()

    f.close()
    g.close()
