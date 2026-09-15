barang = input("Nama barang: ")
harga = int(input("Harga satuan: "))
jumlah = int(input("Jumlah barang: "))

bayar = int(input("Uang pembayaran: "))

total = harga * jumlah
kembali = bayar - total

print("\n=== STRUK PEMBAYARAN ===")
print()
print("Nama Barang    :", barang)
print("Harga          :", harga)
print("Jumlah         :", jumlah)
print("Total          :", total)
print("Bayar          :", bayar)
print("Kembali        :", kembali)

print("TERIMAKASIH TELAH BERBELANJA")