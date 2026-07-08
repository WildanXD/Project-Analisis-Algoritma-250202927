
# PETUNJUK PENGGUNAAN SISTEM (USER GUIDE)
Sistem ini berbasis Command Line Interface (CLI) yang interaktif dan modular. Pastikan semua file source code (Main.py, Algoritma.py, Dataset.py, Model.py, Struktur.py) dan file dataset (data_buku_100.csv hingga data_buku_5000.csv) berada di dalam satu folder/direktori yang sama.

---


## LANGKAH 1: PERSIAPAN PERANGKAT LUNAK
Sebelum menjalankan program, pastikan komputer Anda telah menginstal komponen berikut:

1. Python 3.8 atau versi di atasnya.

2. Library Pandas (digunakan untuk manajemen I/O file CSV).

- Cara Instalasi Library: Buka Terminal atau Command Prompt, lalu ketik perintah berikut:

      pip install pandas

---

## LANGKAH 2: CARA MENJALANKAN PROGRAM (RUNNING PROGRAM)
1. Buka Terminal, Command Prompt (CMD), atau Terminal bawaan di VS Code. 

2. Masuk ke direktori/folder tempat file project disimpan dengan menggunakan perintah 
 
     ```cd```. Contoh:
```bash
   cd D:\Project-Analisis-Algoritma
```

3.  Jalankan file utama program (Main.py) dengan mengetik perintah:
```bash
   python Main.py
```

5.  Jika berhasil, layar akan menampilkan Menu Utama Interaktif seperti di bawah ini:
```bash
   =============================================
       SISTEM ANALISIS ALGORITMA BUKU
=============================================
1. Jalankan Eksperimen Otomatis
2. Lihat Seluruh Daftar Data
3. Tambah Data Buku Baru
4. Hapus Data Buku
5. Cari Buku
6. Keluar
---------------------------------------------
Pilih menu (1-6):
```
---

## LANGKAH 3: PANDUAN PENGGUNAAN FITUR & MENU
1. Menu 1: Jalankan Eksperimen Otomatis  
- Fungsi: Menguji kecepatan running time Sequential Search dan BST Search pada skenario terburuk (Worst Case).
- Cara Menggunakan: Ketik 1 lalu tekan Enter. Program akan otomatis memuat 4 skala dataset (100, 500, 1000, 5000) secara bergantian, melakukan pencarian pada elemen terakhir sebanyak 5 kali iterasi, dan langsung menampilkan tabel detail hasil pengujian milidetik (ms) beserta nilai rata-ratanya di layar.

2. Menu 2: Lihat Seluruh Daftar Data 
- Fungsi: Menampilkan seluruh isi data buku yang tersimpan di database CSV tertentu.
- Cara Menggunakan: Ketik 2 -> Enter. Masukkan angka pilihan dataset yang ingin dilihat (1 untuk 100 data, 2 untuk 500 data, dst.). Sistem akan menampilkan tabel data buku secara terstruktur di terminal.

3. Menu 3: Tambah Data Buku Baru (Fitur Proteksi Duplikat)  
- Fungsi: Memasukkan data buku baru ke dalam database file CSV pilihan.
- Cara Menggunakan:
    1. Pilih Menu 3 -> Enter. Pilih target dataset yang ingin ditambahkan data.
    2. Sistem akan meminta Kode Buku terlebih dahulu.
    3. Validasi Sistem: Jika Kode Buku yang dimasukkan sudah ada di dalam file CSV, sistem akan langsung memunculkan pesan error: [X] GAGAL: Kode Buku sudah terdaftar! dan membatalkan proses. User tidak perlu membuang waktu mengisi judul atau penulis.
    4. Jika Kode Buku unik (belum ada), sistem baru akan meminta kelengkapan data lainnya (Judul, Penulis, Kategori, Tahun, Status) kemudian menyimpannya ke CSV.

4. Menu 4: Hapus Data Buku (Fitur Konfirmasi Aman)
- Fungsi: Menghapus data buku tertentu berdasarkan Kode Buku dari file CSV.
- Cara Menggunakan:
    1. Pilih Menu 4 -> Enter. Pilih lokasi dataset.
    
    2. Masukkan Kode Buku yang ingin dihapus.
    
    3. Validasi Sistem: Jika kode buku tidak ditemukan, program langsung membatalkan operasi dengan pesan error.
    
    4. Jika kode buku ditemukan, sistem akan memunculkan prompt konfirmasi: Apakah kamu yakin ingin menghapus buku? (y/t): . Ketik y untuk menyetujui penghapusan permanen atau t untuk membatalkan.

5. Menu 5: Cari Buku (Pencarian Manual)
- Fungsi: Melakukan pencarian data buku secara manual berbasis kata kunci tertentu (wildcard search pada judul).
- Cara Menggunakan: Pilih Menu 5 -> Enter. Pilih dataset, lalu ketik kata kunci judul buku yang dicari. Sistem akan menampilkan detail buku yang cocok dengan kata kunci tersebut.

6. Menu 6: Keluar
- Fungsi: Menghentikan jalannya program dengan aman.
- Cara Menggunakan:
  1. Ketik 6 -> Enter. Program akan menutup koneksi file dan selesai.
