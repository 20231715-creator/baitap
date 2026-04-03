def b1_doc_n_dong():
    n = int(input("Nhập số dòng cần đọc: "))
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            print("\n--- Nội dung ---")
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except:
        print("Không tìm thấy file input.txt")


def b2_ghi_va_doc_file():
    text = input("Nhập nội dung cần ghi: ")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("\n--- Nội dung trong file ---")
    with open("output.txt", "r", encoding="utf-8") as f:
        print(f.read())


def b3_xu_ly_file():
    with open("demo_file1.txt", "w", encoding="utf-8") as f:
        f.write("Thuc\nhanh\nvoi\nfile\nIO\n")

    print("\n1. In 1 dòng")
    print("2. In từng dòng")
    chon = input("Chọn: ")

    if chon == "1":
        with open("demo_file1.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print(content.replace("\n", " "))
    elif chon == "2":
        with open("demo_file1.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    else:
        print("Chọn sai!")


def b4_nhap_va_luu_thong_tin():
    ten = input("Nhập tên: ")
    tuoi = input("Nhập tuổi: ")
    email = input("Nhập email: ")
    skype = input("Nhập skype: ")
    dia_chi = input("Nhập địa chỉ: ")
    noi_lam_viec = input("Nhập nơi làm việc: ")

    with open("setInfo.txt", "w", encoding="utf-8") as f:
        f.write("Tên: " + ten + "\n")
        f.write("Tuổi: " + tuoi + "\n")
        f.write("Email: " + email + "\n")
        f.write("Skype: " + skype + "\n")
        f.write("Địa chỉ: " + dia_chi + "\n")
        f.write("Nơi làm việc: " + noi_lam_viec + "\n")

    print("\nĐã lưu thông tin vào file setInfo.txt")


def b4_doc_thong_tin():
    try:
        with open("setInfo.txt", "r", encoding="utf-8") as f:
            print("\n--- Thông tin trong file ---")
            print(f.read())
    except:
        print("Không tìm thấy file setInfo.txt")


def b5_dem_so_lan_xuat_hien_tu():
    try:
        with open("demo_file2.txt", "r", encoding="utf-8") as f:
            content = f.read()

        words = content.split()
        dem = {}

        for tu in words:
            if tu in dem:
                dem[tu] += 1
            else:
                dem[tu] = 1

        print("\n--- Kết quả đếm từ ---")
        print(dem)

    except:
        print("Không tìm thấy file demo_file2.txt")


def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. B1 - Đọc n dòng đầu tiên của file")
        print("2. B2 - Ghi và đọc file")
        print("3. B3 - Tạo và xử lý file")
        print("4. B4a - Nhập và lưu thông tin cá nhân")
        print("5. B4b - Đọc thông tin từ file setInfo.txt")
        print("6. B5 - Đếm số lần xuất hiện của từ trong file")
        print("0. Thoát")
        print("==========================")

        chon = input("Nhập lựa chọn: ")

        if chon == "1":
            b1_doc_n_dong()
        elif chon == "2":
            b2_ghi_va_doc_file()
        elif chon == "3":
            b3_xu_ly_file()
        elif chon == "4":
            b4_nhap_va_luu_thong_tin()
        elif chon == "5":
            b4_doc_thong_tin()
        elif chon == "6":
            b5_dem_so_lan_xuat_hien_tu()
        elif chon == "0":
            print("Đã thoát!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


menu()