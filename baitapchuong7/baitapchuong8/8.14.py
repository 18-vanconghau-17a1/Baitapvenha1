numbers_str = input("Nhập chuỗi các số, cách nhau bằng dấu phẩy: ")
numbers_list = [int(num) for num in numbers_str.split(",")]

A = sum(numbers_list)
print("Tổng của chuỗi số là:",A)