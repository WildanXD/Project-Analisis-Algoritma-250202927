import pandas as pd
import os
from Casting import row_to_buku
from Struktur import SortedList, BinarySearchTree

def muat_dataset(nama_file):
    """Membaca file CSV dan memuat data ke SortedList dan BST"""
    file_path = nama_file
    # Auto-detect jika file tidak ditemukan, coba cari dengan suffix _v2
    if not os.path.exists(file_path):
        nama_base, ext = os.path.splitext(nama_file)
        file_path = f"{nama_base}_v2{ext}"
    
    if not os.path.exists(file_path):
        print(f"Error: File {nama_file} tidak ditemukan!")
        return None, None

    df = pd.read_csv(file_path)
    sl = SortedList()
    bst = BinarySearchTree()
    
    for _, row in df.iterrows():
        buku = row_to_buku(row)
        sl.tambah_data(buku)
        bst.tambah_data(buku)
        
    return sl, bst

def cek_kode_duplikat(nama_file, kode_baru):
    """Fungsi pembantu untuk mengecek apakah kode sudah ada di CSV"""
    try:
        df = pd.read_csv(nama_file)
        # Menggunakan astype(str) agar perbandingan tetap akurat meski input berupa angka
        return str(kode_baru) in df['Kode Buku'].astype(str).values
    except FileNotFoundError:
        return False

def tambah_data_csv(nama_file, data_buku_dict):
    """Menambah data ke file CSV dengan validasi duplikat"""
    if cek_kode_duplikat(nama_file, data_buku_dict['Kode Buku']):
        return False, "Error: Kode Buku sudah terdaftar!"
    
    try:
        df = pd.read_csv(nama_file)
        new_row = pd.DataFrame([data_buku_dict])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(nama_file, index=False)
        return True, "Data berhasil ditambahkan!"
    except Exception as e:
        return False, f"Terjadi kesalahan saat menulis data: {e}"

def hapus_data_csv(nama_file, kode_buku):
    """Menghapus data dari CSV berdasarkan Kode Buku"""
    if not os.path.exists(nama_file):
        print("Error: File tidak ditemukan.")
        return

    df = pd.read_csv(nama_file)
    
    # Filter data: simpan semua yang TIDAK SAMA dengan kode yang akan dihapus
    # Kita gunakan astype(str) untuk memastikan perbandingan konsisten
    df_filtered = df[df['Kode Buku'].astype(str) != str(kode_buku)]
    
    # Cek apakah ada data yang berubah (berarti data ditemukan dan dihapus)
    if len(df) == len(df_filtered):
        print(f"Info: Kode Buku {kode_buku} tidak ditemukan.")
    else:
        df_filtered.to_csv(nama_file, index=False)
        print(f"Data dengan kode {kode_buku} berhasil dihapus dari {nama_file}.")