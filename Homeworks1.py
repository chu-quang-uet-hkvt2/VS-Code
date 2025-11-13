#Bai 1
n = int(input("enter n:",))
print(2*n)

print(50*"-")

#Bai 2
a = float(input("enter a:",))
b = float(input("enter b:",))
print((a*b) - 3.14 * (b/2)**2)

print(50*"-")

#Bai 3
char = str(input("enter a character:",))
if char.isupper():
    print(char.swapcase())
else:
    print(char.swapcase())

print(50*"-")

#Bai 4
char1 = (input("enter a character:",))
if char1.isalpha():
    print( char1,"is an alphabet")
else:
    print(char1,"is not an alphabet")

print(50*"-")

#Bai 5
c = input("Enter letter: ")

if c == 'A':
    print("THDB, ko co chu cai lien trc 'a'")
else:
    print("chu cai thg lien trc:", chr(ord(c.lower()) - 1))

print(50*"-")

#Bai 6
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("S tam giac:", round(area, 1))
else:
    print("Ko phai 3 canh cua tam giac")

print(50*"-")

#Bai 7
s = input("Nhap chuoi ky tu thg (>=20 ký tự): ")

if len(s) >= 20:
    print("KT 5th:", s[4])
    print("KT 9th:", s[8])
else:
    print("STR qua ngan!")

print(50*"-")

#Bai 8
ten_chu_ho = input("Ho ten chu ho: ")
chi_so_truoc = int(input("Chi so dien thang trc: "))
chi_so_sau = int(input("chi so dien thang nay: "))

so_dien = chi_so_sau - chi_so_truoc

def tinh_tien_dien(kwh):
    tien = 0
    if kwh <= 50:
        tien += kwh * 1984
    elif kwh <= 100:
        tien += 50 * 1984 + (kwh - 50) * 2050
    elif kwh <= 200:
        tien += 50 * 1984 + 50 * 2050 + (kwh - 100) * 2380
    elif kwh <= 300:
        tien += 50 * 1984 + 50 * 2050 + 100 * 2380 + (kwh - 200) * 2998
    elif kwh <= 400:
        tien += 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (kwh - 300) * 3350
    else:
        tien += 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (kwh - 400) * 3460
    return tien

tien_dien = tinh_tien_dien(so_dien)
tien_vat = tien_dien * 0.08
tong_tien = round(tien_dien + tien_vat)

print(f"CHu ho: {ten_chu_ho}")
print(f"So dien tieu thu: {so_dien} kWh")
print(f"Tong tien dien(co ca VAT): {tong_tien} dong")
