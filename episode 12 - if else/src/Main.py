a = 20
b = 10
c = 30
if a > b:
    print("right!")

# ELIF dan ELSE
if a < b:
    print("a lebih kecil dari b")
elif a == b:
    print("a sama dengan b")
else:
    print("a lebih besar dari b")

# AND
if a > b and b < c:
    print("kedua kondisi adalah Benar!")

# OR
if a < b or b < c:
    print("At least one of the conditions is True")

# NESTED IF
if a > 10:
    print("diatas 10")
    if a > 15:
        print("masih diatas 15")
    else:
        print("tidak dibawah 15")