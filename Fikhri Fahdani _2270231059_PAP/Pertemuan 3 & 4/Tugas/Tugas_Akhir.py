# Tugas Akhir Praktikum Algoritma Pemrograman
# Create by Muhammad Fakhri

"""
Kasir paket reguler ID EXPRESS

Program ini berfungsi untuk melakukan pengelolaan paket reguler dan same day. Program akan 
meminta memasukan identitas customer, kemudian menghitung biaya dari layanan jasa laundry tersebut dan
mencetak bon hasil transaksi.
"""
import datetime

identitas = ["Nama Pelanggan", "Alamat", "No Telepon", "berat paket", "service"]
data = []
biayaLayanan = 0
tanggal = datetime.datetime.now()

print(30*"="+"""
Nama\t: fikhri fahdani
NIM\t: 2270231059
Program\t: ID EXPRESS
""" + 30*"=" + "\n")

for x in range(len(identitas)):
    val = input("Masukkan " + identitas[x] + ": ")
    data.append(val)

serviceCheck = str(data[4]).upper()

if(serviceCheck == "REGULER"):
    biayaLayanan = 7500* int(data[3])
elif(serviceCheck == "SAME DAY"):
    biayaLayanan = 10000 * int(data[3])
else:
    print("Harap masukkan layanan service")

print("\n"+8*"=" + "Transaksi Paket yang akan dikirim" + 8*"="+"\n") 

print("Tanggal : " + tanggal.strftime("%d - %m - %Y %X"))

for x in range(4):
    print(identitas[x] + " : " + data[x])

if(biayaLayanan % 7500 == 0):
    print("Service : 7500/kg")
else:
    print("Service : 10000/kg")
print("Total biaya: " + str(biayaLayanan))