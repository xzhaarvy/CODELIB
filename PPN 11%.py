# user input harga barang
harga_barang = float(input("Masukkan harga barang: "))

# besarnya pajak
pajak = 0.11

# hitungan pajak yang harus di bayar
pajak_bayar = harga_barang * pajak

# total setelah pajak
total_harga = harga_barang + pajak_bayar

# hasil yang harus dibayar
print("Input Jumlah Barang: Rp", harga_barang)
print("Total Pajak 11%: Rp", pajak_bayar)
print("Total Harga Yang Harus Dibayar: Rp", total_harga)
