print("Materi 1a - python data structures")
print("----------------------------------")
# Lits -> [] -> berurutan, berubah, boleh duplikat
daftar_belanja = [
    "pisang kembung", # index 0
    "gabin", # index 1
    "tahu goolek",# index 2
    "kapal api",# index 3
]
print("tas belanja:", daftar_belanja)
# akses item dengan index
print(daftar_belanja[1])
# append() untuk menambah item ke akhir List
daftar_belanja.append("kapal api")
# insert untuk() untuk menambah item tertentu
daftar_belanja.insert(1, "batagor")
# remove() untuk menghapus item
daftar_belanja.remove("gabin")
print("tas belanja skrg :" ,daftar_belanja)
# menggabungkan List dengan +
jajanan_ishaq = ["olive chicken", "macaroni", "keripik singkong"]
jajanan_bilal = ["naspad kawan lamo", "indomie", "gorengan"]
titip_belanjaan = jajanan_bilal + jajanan_ishaq
print("Titipan belanja:", titip_belanjaan)
# menggandakan otem list dengan +
print("bilal nambah:", jajanan_bilal * 3)

#List bercabang (List multi dimensi)
daftar_menu = [
    ["kopi", "teh", "susu jahe"], #baris 0
    ["jus apel", "jus jeruk", "jus alpukat", "jus mangga"], # baris 1
    ["es teler", "es campur", "es dawet"], # baris 2
]
print("daftar menu :",daftar_menu)
print(daftar_menu[1][2])
print("    ")
# tuple () berurutan, tidak berubah, boleh duplikat
ttl = ("purworejo", 21, "januari", 2009)
print("ttl :", ttl )
print("bulan lahir ujang:", ttl[2])
# unpacking variable (mengestrak tuple ke variable baru sesuai urutan)
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("Thn_lahir:",thn_lahir)
