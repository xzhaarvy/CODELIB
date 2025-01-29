# user input harga barang
harga_barang = float(input("Masukkan harga barang: "))

# besarnya pajak
pajak = 0.11

# hitungan pajak yang harus di bayar
pajak_bayar = harga_barang * pajak

# hitungan setelah kena ppn 11% 😒
total_harga = harga_barang + pajak_bayar

# hasilnya bosqu
print("Harga barang segini: Rp", harga_barang)
print("PPN 11% YAGESYA: Rp", pajak_bayar)
print("Total harga setelah pajak: Rp", total_harga)
