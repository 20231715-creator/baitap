while True:
    print("\n========== MENU BÀI TẬP WHILE ==========")
    print("1. Tính tích của 10 số tự nhiên đầu tiên")
    print("2. Tính giai thừa n!")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tính tổng các số chẵn nhỏ hơn n")
    print("0. Thoát")
    
    chon = int(input("Nhập lựa chọn của bạn: "))

    if chon == 1:
        tich = 1
        i = 1
        while i <= 10:
            tich = tich * i
            i = i + 1
        print("Tích của 10 số tự nhiên đầu tiên là:", tich)

    elif chon == 2:
        n = int(input("Nhập số nguyên dương n: "))
        giai_thua = 1
        i = 1
        while i <= n:
            giai_thua = giai_thua * i
            i = i + 1
        print(n, "! =", giai_thua)

    elif chon == 3:
        n = int(input("Nhập số nguyên dương n: "))
        if n < 2:
            print("Không phải số nguyên tố.")
        else:
            i = 2
            la_so_nguyen_to = True
            while i <= n // 2:
                if n % i == 0:
                    la_so_nguyen_to = False
                    break
                i = i + 1

            if la_so_nguyen_to:
                print("Đây là số nguyên tố.")
            else:
                print("Không phải số nguyên tố.")

    elif chon == 4:
        n = int(input("Nhập số nguyên n: "))
        tong = 0
        i = 0
        while i < n:
            if i % 2 == 0:
                tong = tong + i
            i = i + 1
        print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)

    elif chon == 0:
        print("Đã thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")