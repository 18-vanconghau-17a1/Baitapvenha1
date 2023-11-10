n = int(input("Nhập một số nguyên n: "))
A = sum(x for x in range(1, n + 1) if x % 2 != 0)
print("A=:",A)
B = sum(x for x in range(1, n + 1) if x % 2 == 0)
print("B=:",B)
C = 1
for i in range(1, n + 1):
    C *= i
    print("C=",C)
D = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        D *= i
        print("D=",D)
E = 0
for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        E += i
        print("E=",E)
        F = ""
for i in range(1, n):
    F += str(i) + "-"
F += str(n)
print("F",F)