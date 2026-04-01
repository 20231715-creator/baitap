def bai1():
    n = int(input("Nhập n: "))
    print("Kết quả:")
    for i in range(1, n):
        print(f"{2*i} = 2 * {i}")


def bai2():
    n = int(input("Nhập n: "))
    if n > 10:
        print("Số nhập vào phải bé hơn 10")
    else:
        print("Các số chẵn từ 1 đến n:")
        for i in range(2, n + 1, 2):
            print(i, end=" ")


def bai3():
    print("Các số từ 80 đến 100 chia hết cho 2 và 3:")
    for i in range(80, 101):
        if i % 2 == 0 and i % 3 == 0:
            print(i, end=" ")


def bai4():
    n = int(input("Nhập n < 20: "))
    if n >= 20:
        print("n phải nhỏ hơn 20")
    else:
        print("Các số chia hết cho 5 hoặc 7:")
        for i in range(1, n + 1):
            if i % 5 == 0 or i % 7 == 0:
                print(i, end=" ")


# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("0. Thoát")

    choice = int(input("Chọn bài: "))

    if choice == 1:
        bai1()
    elif choice == 2:
        bai2()
    elif choice == 3:
        bai3()
    elif choice == 4:
        bai4()
    elif choice == 0:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ!")