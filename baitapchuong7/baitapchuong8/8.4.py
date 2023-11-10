a=float(input("độ dài cạnh:"))
b=float(input("độ dài cạnh:"))
c=float(input("độ dài cạnh:"))
p=(a+b+c)/2
dien_tich_tam_giac=(p*(p-a)*(p-b)*(p-c))**0.5
print("diện tích tam giác là:",dien_tich_tam_giac)