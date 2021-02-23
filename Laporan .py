#Nama : Endricho Abednego
#Kampus : Universitas Kristen Duta Wacana
"""
Sumber Soal : https://teamhannamy.blogspot.com/2021/02/17-contoh-soal-algoritma-percabangan.html
Buatlah suatu program untuk membantu penentuan harga dalam persewaan kendaraan pada Sumber Berkat!
Berapakah harga yang diperlukan jika seseorang ingin menyewa kendaraan dengan kapasitas 5 orang selama satu minggu?

input : 
org : kapasitas orang untuk kendaraan yang ingin disewa 
hari : berapa hari kendaraan akan disewa
kndrn : kendaraan apa yang akan dipilih 
harga : harga total  
mtr : harga motor per hari
mblKcl : harga mobil kecil per hari
mblBsr : harga mobil besar per hari
mnBus : harga mini bus per hari 

proses : 

harga = hari * (Kendaraan yang diinginkan)

output : 
Total harga yang diperlukan 
"""
#input : 

print("""Selamat datang di persewaan kendaraan Sumber Berkat
Silahkan pilih kendaraan yang diinginkan : 
1. Motor (1 - 2 orang, dengan harga Rp. 100.000/ hari)
2. Mobil Kecil (3 - 4 orang, dengan harga Rp. 200.000/ Hari)
3. Mobil Besar (5-6 orang, dengan harga Rp. 300.000/ hari)
4. Mini bus (7 - 8 orang, dengan harga Rp. 400.000/ hari)
""")

mtr = 100000
mblKcl = 200000
mblBsr = 300000
mnBus = 400000

org = int(input("Kendaraan digunakan untuk berapa orang? \n "))
hari = int(input("Kendaraan akan disewa selama berapa hari? \n"))

if org >= 1 and org <= 2 : 
    kndrn = int(input("""Silahkan memilih kendaraan yang diinginkan
(Kami merekomendasikan anda memilih motor) \n"""))
    if kndrn == 1 : 
        harga = mtr * hari 
        print("Total harga sewa motor selama ", hari ,"hari adalah Rp. ",harga)
    elif kndrn == 2 : 
        harga = mblKcl * hari 
        print("Total harga sewa mobil kecil selama", hari , "hari adalah Rp. ",harga )
    elif kndrn == 3 : 
        harga = mblBsr * hari 
        print("Total harga sewa mobil besar selama", hari ,"hari adalah Rp. ",  harga)
    elif kndrn == 4 : 
        harga = mnBus* hari 
        print("Total harga sewa mini bus selama",  hari , "hari adalah Rp. ", harga)
    else : 
        print("Kendaraan tersebut tidak ada")
elif org >= 3 and org <= 4 : 
    kndrn = int(input("""Silahkan memilih kendaraan yang diinginkan
(Kami merekomendasikan anda memilih mobil kecil \n"""))
    if kndrn == 1 : 
        harga = mtr * hari 
        print("Total harga sewa motor selama ", hari ,"hari adalah Rp. ",harga)
    elif kndrn == 2 : 
        harga = mblKcl * hari 
        print("Total harga sewa mobil kecil selama", hari , "hari adalah Rp. ",harga )
    elif kndrn == 3 : 
        harga = mblBsr * hari 
        print("Total harga sewa mobil besar selama", hari ,"hari adalah Rp. ",  harga)
    elif kndrn == 4 : 
        harga = mnBus* hari 
        print("Total harga sewa mini bus selama",  hari , "hari adalah Rp. ", harga)
    else : 
        print("Kendaraan tersebut tidak ada")
elif org >= 5 and org <= 6 :
    kndrn = int(input("""Silahkan memilih kendaraan yang diinginkan
(Kami merekomendasikan anda memilih mobil besar \n"""))
    if kndrn == 1 : 
        harga = mtr * hari 
        print("Total harga sewa motor selama ", hari ,"hari adalah Rp. ",harga)
    elif kndrn == 2 : 
        harga = mblKcl * hari 
        print("Total harga sewa mobil kecil selama", hari , "hari adalah Rp. ",harga )
    elif kndrn == 3 : 
        harga = mblBsr * hari 
        print("Total harga sewa mobil besar selama", hari ,"hari adalah Rp. ",  harga)
    elif kndrn == 4 : 
        harga = mnBus* hari 
        print("Total harga sewa mini bus selama",  hari , "hari adalah Rp. ", harga)
    else : 
        print("Kendaraan tersebut tidak ada")
elif org >= 7 and org <= 8 : 
    kndrn = int(input("""Silahkan memilih kendaraan yang diinginkan
(Kami merekomendasikan anda memilih mini besar \n"""))
    if kndrn == 1 : 
        harga = mtr * hari 
        print("Total harga sewa motor selama ", hari ,"hari adalah Rp. ",harga)
    elif kndrn == 2 : 
        harga = mblKcl * hari 
        print("Total harga sewa mobil kecil selama", hari , "hari adalah Rp. ",harga )
    elif kndrn == 3 : 
        harga = mblBsr * hari 
        print("Total harga sewa mobil besar selama", hari ,"hari adalah Rp. ",  harga)
    elif kndrn == 4 : 
        harga = mnBus* hari 
        print("Total harga sewa mini bus selama",  hari , "hari adalah Rp. ", harga)
    else : 
        print("Kendaraan tersebut tidak ada")
else :
    print("Kendaraan dengan kapasitas sebesar itu tidak tersedia")

print("Silahkan meninggalkan KTP sebagai jaminan jika terjadi apa apa")
