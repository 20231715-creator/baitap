# =========================
# 1. Hàm tính tổng 2 số
# =========================
def tong_2_so(a, b):
    return a + b


# =========================
# 2. Hàm tính tổng các số truyền vào
# =========================
def tong_cac_so(*args):
    return sum(args)


# =========================
# 3. Hàm kiểm tra số nguyên tố
# =========================
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# =========================
# 4. Chương trình tìm các số nguyên tố trong đoạn [a, b]
# =========================
def tim_so_nguyen_to_trong_doan(a, b):
    ds = []
    for n in range(a, b + 1):
        if la_so_nguyen_to(n):
            ds.append(n)
    return ds


# =========================
# 5. Hàm kiểm tra số hoàn hảo
# =========================
def la_so_hoan_hao(n):
    if n <= 0:
        return False

    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# =========================
# 6. Chương trình tìm các số hoàn hảo trong đoạn [a, b]
# =========================
def tim_so_hoan_hao_trong_doan(a, b):
    ds = []
    for n in range(a, b + 1):
        if la_so_hoan_hao(n):
            ds.append(n)
    return ds


# =========================
# 7. Menu chương trình
# =========================
def hien_thi_menu():
    print("\n========== MENU ==========")
    print("1. Tính tổng 2 số")
    print("2. Tính tổng các số truyền vào")
    print("3. Kiểm tra một số nguyên tố")
    print("4. Tìm các số nguyên tố trong đoạn [a, b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm các số hoàn hảo trong đoạn [a, b]")
    print("0. Thoát")
    print("==========================")

def main():
    while True:
        hien_thi_menu()
        chon = input("Nhập lựa chọn của bạn: ")

        if chon == "1":
            a = int(input("Nhập số a: "))
            b = int(input("Nhập số b: "))
            print("Tổng 2 số là:", tong_2_so(a, b))

        elif chon == "2":
            n = int(input("Nhập số lượng số muốn cộng: "))
            ds = []
            for i in range(n):
                x = float(input(f"Nhập số thứ {i+1}: "))
                ds.append(x)
            print("Tổng các số là:", tong_cac_so(*ds))

        elif chon == "3":
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_nguyen_to(n):
                print(n, "là số nguyên tố")
            else:
                print(n, "không phải là số nguyên tố")

        elif chon == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            if a > b:
                a, b = b, a
            ds = tim_so_nguyen_to_trong_doan(a, b)
            print(f"Các số nguyên tố trong đoạn [{a}, {b}] là: {ds}")

        elif chon == "5":
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_hoan_hao(n):
                print(n, "là số hoàn hảo")
            else:
                print(n, "không phải là số hoàn hảo")

        elif chon == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            if a > b:
                a, b = b, a
            ds = tim_so_hoan_hao_trong_doan(a, b)
            print(f"Các số hoàn hảo trong đoạn [{a}, {b}] là: {ds}")

        elif chon == "0":
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


# Chạy chương trình
main()