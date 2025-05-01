#-------------------------Program Kasir Sederhana----------------------------

nama = input("\nMasukkan nama Anda: ")

print("\n=== Daftar Menu ===")
print("1. Nasi Goreng   : Rp. 15.000")
print("2. Ayam Goreng   : Rp. 20.000")
print("3. Es Teh        : Rp. 5.000")
print("4. Es Jeruk      : Rp. 5.000")
print("5. Es Kelapa     : Rp. 5.000")
print("=============================")

# Daftar untuk menyimpan pesanan
pesanan = []
total_harga = 0

while True:
    menu = int(input("Masukkan nomor menu yang ingin Anda beli (ketik 0 untuk selesai): "))
    if menu == 0:
        break
    elif menu in [1, 2, 3, 4, 5]:
        jumlah = int(input("Masukkan jumlah pesanan: "))
        harga = 0
        if menu == 1:
            harga = 15000
            nama_menu = "Nasi Goreng"
        elif menu == 2:
            harga = 20000
            nama_menu = "Ayam Goreng"
        elif menu == 3:
            harga = 5000
            nama_menu = "Es Teh"    
        elif menu == 4:
            harga = 5000
            nama_menu = "Es Jeruk"
        elif menu == 5:
            harga = 5000
            nama_menu = "Es Kelapa"

        # Hitung total harga untuk item ini
        total_item = harga * jumlah
        total_harga += total_item

         # Simpan pesanan
        pesanan.append((nama_menu, jumlah, total_item))
    else:
        print("Menu tidak valid. Silakan coba lagi.")

# Menampilkan struk pembelian
print("\n=== Struk Pembelian ===")
print("Nama:", nama)
for item, jumlah, total in pesanan:
    print(f"- {item} x{jumlah} : Rp. {total}")
print(f"Total keseluruhan: Rp. {total_harga}")