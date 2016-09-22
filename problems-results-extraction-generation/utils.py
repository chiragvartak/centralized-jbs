def get_xml(input_file, output_file):
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

if __name__ == '__main__':
    get_xml('RawInput.txt', '1DJBSInput.txt')
