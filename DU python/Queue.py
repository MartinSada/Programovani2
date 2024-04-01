p = open("VSTUP.txt", "r")
Q = []

for line in p:
    if(line[0] == "E"):
        print(line, end="")
        for x in line[2:].split(" "):
            Q.append(x)
        if "\n" in Q[-1]:
            Q[-1] = Q[-1][:-1]
    elif(line[0]=="D"):
        print(line[0])
        print(Q[0])
        Q.pop(0)
    elif(line[0] == "P"):
        print(line[0].strip())
        print('[',*Q,']')

p.close()