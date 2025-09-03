
# Input data diri
print("===== ISI PROFIL DIGITAL KAMU =====")
nama = (input(" Nama lengkap: "))
umur = int(input(" Umur: "))
kelas = input(" Kelas: ")
cita_cita = input(" Cita-cita atau  impian: ")
hobi = input(" Hobi favorit: ")
belajar = input(" Lebih suka belajar pagi atau malam?: ")

# Pilih gaya digital
print("\n=== TIPE DIGITAL KAMU ===")
print("1. Wibu ")
print("2. Gamer ")
print("3. K-Popers ")
print("4. Anak konten ")
print("5. Anak nongki ")
tipe = int(input("Ketik angka tipe kamu: ")) 

# Variabel tambahan sesuai tipe
tipe_text = ""
komentar = ""
jawaban_tambahan = ""

if tipe == 1:
    tipe_text = "Wibu"
    waifu = input("Siapa waifu  kamu? ")
    jawaban_tambahan = f"Waifu: {waifu}"
    komentar = f"Kamu pasti rajin nonton anime sambil belajar. Semangat, "

elif tipe == 2:
    tipe_text = "Gamer"
    game = input("Game favorit kamu apa? ")
    jawaban_tambahan = f"Game favorit: {game}"
    komentar = f"Wih, kamu pasti jago main {game} sambil ngoding."

elif tipe == 3:
    tipe_text = "K-Popers"
    bias = input("Siapa bias kamu? ")
    jawaban_tambahan = f"Bias: {bias}"
    komentar = f"Kalau ada lomba nyanyi sambil ngoding ,kamu pasti jagonya "

elif tipe  == 4:
    tipe_text = "Anak Konten"
    platform = input("Platform favorit kamu? TikTok? YouTube? ")
    jawaban_tambahan = f"Platform favorit: {platform}"
    komentar = f"Kamu pasti bisa jadi konten kreator sambil jadi coder! {platform} siap viral bareng kamu! 📱✨"

elif tipe == 5:
    tipe_text = "Anak Nongki"
    tempat = input("Nongkrong paling sering di mana? ")
    jawaban_tambahan = f"Tempat nongkrong: {tempat}"
    komentar = f"Belajar sambil nongkrong di {tempat}?  kamu pasti anak seribu koneksi! "

else:
    tipe_text = "Tidak diketahui"
    komentar = "Tipe tidak valid."

# Pertanyaan bonus
teman_bau = input("\n🤭 Apakah teman di sebelah kamu bau? (ya/tidak): ")

# Respon lucu
if teman_bau.lower() == "ya":
    reaksi = "Aduh... kasih pewangi darurat dong, darurat nasional ini 😷"
elif teman_bau.lower() == "tidak":
    reaksi = "Syukurlah, berarti belajar bisa fokus tanpa gangguan aroma 😄"
else:
    reaksi = "Hmm... jawab jujur dong 😆"

# Hitung tahun lahir
tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur

# Output
print("\n===== PROFIL DIGITAL KAMU =====")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Kelas: {kelas}")
print(f"Hobi: {hobi}")
print(f"Cita-cita: {cita_cita}")
print(f"Belajar paling enak pas: {belajar}")
print(f"Tahun lahir: {tahun_lahir}")

print("\n=== TIPE DIGITAL ===")
print(f"Tipe: {tipe_text}")
print(jawaban_tambahan)
print(f"Komentar: {komentar}")

print("\n=== FUN CHECK ===")
print(f"Teman sebelah bau? {teman_bau}")
print(reaksi)