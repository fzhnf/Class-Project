#Program Python untuk menghitung luas permukaan tabung

#import math module dari library untuk perhitungan
import math

#ubah nilai jari-jari dan tinggi untuk hasil yang berbeda
radius = float(input("Masukkan Jari-Jari Tabung : "))
height = float(input("Masukkan Tinggi Tabung : "))

#menghitung luas permukaan
surface_area = 2*math.pi*radius*(radius+height)
surface_area = format(surface_area, ".2f")
#menampilkan hasil dari perhitungan
print(f"""
Luas Permukaan Tabung
=2πr(r+t)
=2 x π x {radius}m({radius}m + {height}m)
= {surface_area}m³
""")
