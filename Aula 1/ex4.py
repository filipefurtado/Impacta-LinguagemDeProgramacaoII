def tabuada(a):
    for b in range(11):
        c = int(b) * a
        d = str(b) + ' X ' + str(a) + ' = ' + str(c)
        f.write(d)
        f.write("\n")
    f.write("\n")

f = open('teste.txt', '+a')

a = int(input("Informe um número: "))

while (a <= 100):
    tabuada(a)
    a += 1

f.close()