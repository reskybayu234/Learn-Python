class MyClass:
    x = 5


# Membuat Object

obj = MyClass()
print(obj.x)

# __init__() Function
# use the __init_() function to assign values to object properties, or other operations that are necessary to do when the object is being created

class Makanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
obj1 = Makanan("gorengan", 1000)

print(obj1.nama)
print(obj1.harga)


class Mahasiswa():
    nama = "nama"

bayu = Mahasiswa()
resky = Mahasiswa()

bayu.nama = "b"
resky.nama = "r"
print(bayu.nama)
print(resky.nama)