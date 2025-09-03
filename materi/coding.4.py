import json

print("MATERI 12 - JSON")
print("----------------")
file_json_path = r"C:\Users\USER\.vscode\extensions\rukun_islam.json"
with open (file_json_path, "r") as file_json:
    data_json = json.load(file_json)
    print(f"judul file: {data_json['judul']}")
    print(f"jumlah rukun islam: {data_json['jumlah']}")
    print(f"daftar rukun islam:")
    for item_rukun in data_json['rukun']:
        print(item_rukun)
    
    print('-' * 45) # buat garis panjang
    print("Daftar 3 surah di Al-Qur'an")
    print('-' * 45)
    # Tampilkan surah sebagai tabel garis sederhana
    # Keys: nomor, nama, jumlah_ayat, tempat_turun
    print("| No | Nama | Jumlah Ayat | Tempat Turun")
    print('-' * 45)
    for surah in data_json['surah']:
        print(f"| {surah['nomor']} | {surah['nama']} | {surah['jumlah_ayat']} | {surah['tempat_turun']}")