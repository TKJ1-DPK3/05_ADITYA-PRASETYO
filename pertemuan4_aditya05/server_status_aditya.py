print("==================================")
print("       CEK KONDISI SERVER")
print("==================================")

server = input("Masukan nama server: ")
temperatur = int(input("Masukan suhu CPU: "))

print()
print("--------- INFORMASI SERVER ---------")
print("Nama server :", server)
print("Temperatus  :", temperatur, "c")

if temperatur <40:
  keterangan = "Suhu terlalu rendah"
elif temperatur < 60:
  keterangan = "Suhu normal"
elif temperatur < 80:
  keterangan = "Suhu cukup tinggi"
else:
  keterangan = "WARNING! Suhu terlalu tinggi"

print()
print("Status      :", keterangan)

if temperatur >= 80:
  print("Peringatan: Segera cek pendingin server!")
elif temperatur >= 60:
  print("Catatan: Perhatian temperatur server.")
else:
  print("Server berada dalam kondisi aman.")