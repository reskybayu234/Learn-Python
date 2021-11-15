data = input ("masukan data : ")

print(data)

# jika kita ingin mengambil int
angkaFloat = float(input("masukan angka : "))
angkaInt = int(input("masukan angka :"))

print("data = ", angkaFloat,"tipe : ", type(angkaFloat))
print("data = ", angkaInt,"tipe : ", type(angkaInt))

# boolean
biner = bool(int(input("masukan nilai boolean : ")))
print("data = ", biner, ", tipe = ", type(biner))