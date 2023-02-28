# Tugas Kecil 2 IF2211 Strategi Algoritma

## Author
- Muhammad Habibi Husi (13521169)
## Deskripsi Program (Closest Pair Finder)
Program ini berfungsi untuk mencari sepasang titik terdekat dari sekumpulan titik pada ruang vektor $R^n$ dengan menggunakan algoritma
divide and conquer. Pada program ini, juga disediakan algoritma pencarian dengan menggunakan algoritma bruteforce agar dapat membandingkan keefisienan solusi divide and conquer yang telah diimplementasi. Algoritma divide and conquer pada program ini memiliki kompleksitas $O(n log n)$ dengan worst-case scenario $O(n^2)$.
## Requirement
- python 3
- pyinstaller (if want to build .exe)
- windows (if running ready-to-run .exe)

## How to Use
Install modul yang dibutuhkan dengan :
```
pip install -r requirements.txt
```

Jika ingin menjalankan program tanpa melakukan build, maka lakukan dengan command berikut pada terminal :
```
python3 src/main.py
```
Jika ingin melakukan build program, gunakan :
```
pyinstaller --onefile --distpath bin -n ShortestPair src/main.py
```
Dan jalankan hasil build dengan
```
./bin/ShortestPair.exe
```
Lalu ikuti perintah di dalam program.  
Anda juga dapat langsung menjalankan executable di dalam bin tanpa perlu melakukan compile terlebih dahulu.
