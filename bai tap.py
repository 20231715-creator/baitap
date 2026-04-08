from math import gcd

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            raise ValueError("Lỗi: Mẫu số không được bằng 0!")
        
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.toi_gian()

    def toi_gian(self):
        ucln = gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

        # Đưa dấu âm lên tử số
        if self.mau_so < 0:
            self.tu_so *= -1
            self.mau_so *= -1

    def nhan(self, other):
        return PhanSo(self.tu_so * other.tu_so, self.mau_so * other.mau_so)

    def chia(self, other):
        if other.tu_so == 0:
            raise ValueError("Lỗi: Không thể chia cho phân số có tử số bằng 0!")
        return PhanSo(self.tu_so * other.mau_so, self.mau_so * other.tu_so)

    def cong(self, other):
        return PhanSo(
            self.tu_so * other.mau_so + other.tu_so * self.mau_so,
            self.mau_so * other.mau_so
        )

    def tru(self, other):
        return PhanSo(
            self.tu_so * other.mau_so - other.tu_so * self.mau_so,
            self.mau_so * other.mau_so
        )

    def __str__(self):
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"


# =========================
# Chương trình chính
# =========================
try:
    print("Nhập phân số thứ nhất:")
    tu1 = int(input("Tử số 1 = "))
    mau1 = int(input("Mẫu số 1 = "))

    print("\nNhập phân số thứ hai:")
    tu2 = int(input("Tử số 2 = "))
    mau2 = int(input("Mẫu số 2 = "))

    ps1 = PhanSo(tu1, mau1)
    ps2 = PhanSo(tu2, mau2)

    print("\nPhân số 1:", ps1)
    print("Phân số 2:", ps2)

    print("\nTổng 2 phân số:", ps1.cong(ps2))
    print("Hiệu 2 phân số:", ps1.tru(ps2))
    print("Nhân 2 phân số:", ps1.nhan(ps2))
    print("Chia 2 phân số:", ps1.chia(ps2))

except ValueError as e:
    print(e)