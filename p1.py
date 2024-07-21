# Đề bài:
# Viết chương trình Python nhập vào 2 số a, b từ bàn phím. Nhập vào một trong hai phép toán “+” hoặc “–”. Thực hiện phép toán a + b hoặc a – b và in ra kết quả. 

# Họ và tên: Trần Ngọc Nhật Minh
# Bài làm:

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
sign = input("Dấu: ")
if sign=="+":
  print(a+b)
else:
  print(a-b)
