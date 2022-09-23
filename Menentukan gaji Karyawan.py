# Program python untuk Menghitung total Gaji karyawan dalam Seminggu

#ubah nilai untuk jumlah gaji untuk yang berbeda
gaji_pegawai = float(input("Jumlah Gaji Pegawai per jam = "))

#menghitung gaji total dari gaji pegawai dan total jam dan hari dalam seminggu
gaji_total = float(gaji_pegawai * 8 * 7)


#menampilkan hasil hitung
print(f"""
gaji total pegawai dalam seminggu adalah
= gaji pegawai {gaji_pegawai} x 8 jam x 7 hari
= %d Ribu Rupiah 
""" % gaji_total)
