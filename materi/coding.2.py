print("materi 9c - python function")

# higher order function (map, sorted, filter)
uang_jajan = [100000, 200000, 300000, 1000000]

# map mentranformasi data item 
kurangi_jajan = map(lambda uang: uang - 50000, uang_jajan)
list_kurangi_jajan = list(kurangi_jajan)
print(f"uang jajan: {uang_jajan} ")
print(f"kurangi jajan : {list_kurangi_jajan}")

#sorted mengurutkan data
urutkan_uang = sorted(uang_jajan)
balik_uang = sorted(uang_jajan)
print(f"urutkan uang: {urutkan_uang}")
print(f"urutkan uang terbalik: {balik_uang}")
# filter menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 400000, uang_jajan)
list_uang_gede = list(filter_uang_gede)
print(f"")