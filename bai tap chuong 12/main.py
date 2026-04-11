from math_utils import phanso, hinhhoc, hinhhoc2

# ===== PHÂN SỐ =====
print("=== TÍNH TOÁN PHÂN SỐ ===")
a = int(input("Nhập tử số 1: "))
b = int(input("Nhập mẫu số 1: "))
c = int(input("Nhập tử số 2: "))
d = int(input("Nhập mẫu số 2: "))

tu, mau = phanso.cong(a, b, c, d)
print("Cộng:", tu, "/", mau)

tu, mau = phanso.tru(a, b, c, d)
print("Trừ:", tu, "/", mau)

tu, mau = phanso.nhan(a, b, c, d)
print("Nhân:", tu, "/", mau)

tu, mau = phanso.chia(a, b, c, d)
print("Chia:", tu, "/", mau)


# ===== HÌNH HỌC =====
print("\n=== HÌNH TRÒN ===")
r = float(input("Nhập bán kính: "))
print("Chu vi:", hinhhoc.chu_vi_hinh_tron(r))
print("Diện tích:", hinhhoc.dien_tich_hinh_tron(r))

print("\n=== HÌNH CHỮ NHẬT ===")
d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))
print("Chu vi:", hinhhoc.chu_vi_hcn(d, r))
print("Diện tích:", hinhhoc.dien_tich_hcn(d, r))


# ===== HÌNH HỌC 2 =====
print("\n=== HÌNH VUÔNG ===")
a = float(input("Nhập cạnh: "))
print("Chu vi:", hinhhoc2.chu_vi_hinh_vuong(a))
print("Diện tích:", hinhhoc2.dien_tich_hinh_vuong(a))