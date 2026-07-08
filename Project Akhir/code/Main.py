import time
import pandas as pd
import os
from Dataset import muat_dataset, tambah_data_csv, hapus_data_csv, cek_kode_duplikat
from Algoritma import sequential_search, bst_search, cari_buku_by_judul

def pilih_dataset():
    print("\nPilih Dataset:")
    print("1. Data 100 | 2. Data 500 | 3. Data 1000 | 4. Data 5000")
    pilihan = input("Masukkan pilihan (1-4): ")
    files = {
        '1': "data_buku_100.csv",
        '2': "data_buku_500.csv",
        '3': "data_buku_1000.csv",
        '4': "data_buku_5000.csv"
    }
    nama_file = files.get(pilihan)
    if not nama_file:
        print("Pilihan tidak valid.")
        return None
    return nama_file

def menu_utama():
    print("\n" + "="*45)
    print("   SISTEM ANALISIS ALGORITMA BUKU")
    print("="*45)
    print("1. Jalankan Eksperimen")
    print("2. Lihat Seluruh Daftar Data")
    print("3. Tambah Data Buku")
    print("4. Hapus Data Buku")
    print("5. Cari Buku")
    print("6. Keluar")
    return input("Pilih menu (1-6): ")

def tampilkan_daftar_data():
    nama_file = pilih_dataset()
    if nama_file and os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
        print(f"\n--- Menampilkan SELURUH data dari {nama_file} ---")
        print(df.to_string())
    elif nama_file:
        print("File tidak ditemukan.")

def jalankan_eksperimen():
    ITERASI = 5 
    files = {
        100: "data_buku_100.csv",
        500: "data_buku_500.csv",
        1000: "data_buku_1000.csv",
        5000: "data_buku_5000.csv"
    }

    print("\n" + "="*70)
    print("      DETAIL PENGUJIAN (5 KALI PERCOBAAN PER DATASET)")
    print("="*70)
    
    for ukuran, nama_file in files.items():
        if not os.path.exists(nama_file):
            print(f"\n[!] Dataset {ukuran}: File tidak ditemukan.")
            continue
            
        sl, bst = muat_dataset(nama_file)
        if not sl or len(sl.data) == 0: continue
        
        target = sl.data[-1].kode 
        
        waktu_seq = []
        for i in range(ITERASI):
            t0 = time.perf_counter()       
            sequential_search(sl, target)  
            t1 = time.perf_counter()       
            waktu_seq.append((t1 - t0) * 1000)
            
        waktu_bst = []
        for i in range(ITERASI):
            t0 = time.perf_counter()
            bst_search(bst, target)
            t1 = time.perf_counter()
            waktu_bst.append((t1 - t0) * 1000)
            
        # Tampilkan Detail
        print(f"\n--- DATASET: {ukuran} Buku ---")
        print(f"Sequential (ms) : {[f'{x:.4f}' for x in waktu_seq]}")
        print(f"BST        (ms) : {[f'{x:.4f}' for x in waktu_bst]}")
        print(f"Rata-rata Seq   : {sum(waktu_seq)/ITERASI:.6f} ms")
        print(f"Rata-rata BST   : {sum(waktu_bst)/ITERASI:.6f} ms")
        print("-" * 40)
        print("-" * 55)

def menu_tambah_data():
    nama_file = pilih_dataset()
    if not nama_file: return

    kode = input("Masukkan Kode Buku: ")
    if cek_kode_duplikat(nama_file, kode):
        print("\n" + "="*40)
        print(f" [X] GAGAL: Kode Buku '{kode}' sudah terdaftar!")
        print(" Silakan gunakan kode lain.")
        print("="*40)
        return
    
    print("\n--- Lengkapi Data Buku ---")
    data = {
        'Kode Buku': kode,
        'Judul': input("Judul: "),
        'Penulis': input("Penulis: "),
        'Kategori': input("Kategori: "),
        'Tahun': input("Tahun: "),
        'Status': input("Status: ")
    }
    
    sukses, pesan = tambah_data_csv(nama_file, data)
    if sukses:
        print(f"\n[√] BERHASIL: {pesan}")
    else:
        print(f"\n[X] GAGAL: {pesan}")

def menu_hapus_data():
    nama_file = pilih_dataset()
    if not nama_file: return
    
    kode = input("Masukkan Kode Buku yang akan dihapus: ")
    if not cek_kode_duplikat(nama_file, kode):
        print("\n" + "="*40)
        print(f" [X] GAGAL: Kode Buku '{kode}' tidak ditemukan!")
        print(" Silakan periksa kembali kode buku tersebut.")
        print("="*40)
        return
    
    konfirmasi = input(f"Apakah kamu yakin ingin menghapus buku '{kode}'? (y/t): ")
    if konfirmasi.lower() == 'y':
        hapus_data_csv(nama_file, kode)
        print(f"\n[√] BERHASIL: Data dengan kode {kode} telah dihapus.")
    else:
        print("\n[!] Penghapusan dibatalkan.")

def menu_cari_buku():
    nama_file = pilih_dataset()
    if not nama_file: return
    
    sl, bst = muat_dataset(nama_file)
    if not sl: return

    print("\nCari berdasarkan:")
    print("1. Kode Buku (BST)")
    print("2. Judul Buku (Sequential)")
    tipe = input("Pilih (1/2): ")

    if tipe == '1':
        kode = input("Masukkan Kode Buku: ")
        t0 = time.perf_counter()
        hasil = bst_search(bst, kode)
        t1 = time.perf_counter()
        
        tinggi_tree = bst.get_height()
        waktu_ms = (t1 - t0) * 1000

        if hasil:
            print(f"\n--- HASIL PENCARIAN ---")
            print(f"Buku: {hasil.judul} | Penulis: {hasil.penulis}")
            print(f"Waktu Cari : {waktu_ms:.6f} ms")
            print(f"Tinggi Tree: {tinggi_tree}")
        else:
            print("\nBuku tidak ditemukan.")
            
    elif tipe == '2':
        keyword = input("Masukkan Judul: ")
        t0 = time.perf_counter()
        hasil = cari_buku_by_judul(sl, keyword)
        t1 = time.perf_counter()
        waktu_ms = (t1 - t0) * 1000
        
        if hasil:
            print(f"\n[DITEMUKAN {len(hasil)} buku]")
            print(f"Waktu Cari : {waktu_ms:.6f} ms")
            for b in hasil:
                print(f"- {b.kode} | {b.judul}")
        else:
            print("\nBuku tidak ditemukan.")

def main():
    while True:
        pilihan = menu_utama()
        if pilihan == '1': jalankan_eksperimen()
        elif pilihan == '2': tampilkan_daftar_data()
        elif pilihan == '3': menu_tambah_data()
        elif pilihan == '4': menu_hapus_data()
        elif pilihan == '5': menu_cari_buku()
        elif pilihan == '6':
            print("Program selesai.")
            break
        else: print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()