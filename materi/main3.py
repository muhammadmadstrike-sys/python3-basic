# profil digital Muhammad 
profil = {
    "Nama": "Muhammad",
    "Umur": 15,
    "Kelas": "X",
    "Hobi": "Main futsal",
    "Cita-cita": "jadi orang yang pintar ",
    "Belajar paling enak pas": "malam",
    "Tahun lahir": 2010
}

tipe_digital = {
    "Tipe": "Gamer",
    "Game favorit": "zenless zone zero ",
    "Komentar": "Wih, kamu pasti jago main zzz sambil ngoding. GG gaming! 🎮🔥"
}

fun_check = {
    "Teman sebelah bau?": "ya",
    "Komentar": "Aduh... kasih pewangi darurat dong, darurat nasional ini 😷"
}

# Menampilkan data
print("===== PROFIL DIGITAL KAMU =====")
for k, v in profil.items():
    print(f"{k}: {v}")

print("\n=== TIPE DIGITAL ===")
for k, v in tipe_digital.items():
    print(f"{k}: {v}")

print("\n=== FUN CHECK ===")
for k, v in fun_check.items():
    print(f"{k}: {v}")
