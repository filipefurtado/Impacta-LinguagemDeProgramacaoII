def tabuada(a):
    for b in range(11):
        c = int(b) * a
        print(b, " X ", a, " = ", c)

a = int(input("Informe um número: "))

while (a <= 100):
    tabuada(a)
    print("\n")
    a += 1