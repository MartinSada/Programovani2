n = 0
n_str = ""
result = ""


while (True):
    b = True
    n = int(input())
    if (n == 0):
        break
    else:
        n_str = str(n)
        if n_str[-1] == "0":
            b = False
        else:
            if n_str != n_str[::-1]:
                b = False
        if(b):
            result += n_str + " "
print(result)







