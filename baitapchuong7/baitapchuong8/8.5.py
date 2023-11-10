n = int(input("nhập ăm kiểm tra:"))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("năm nhuận")
else:
    print("năm không nhuận")