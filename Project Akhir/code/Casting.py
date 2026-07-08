from Model import Buku

def row_to_buku(row):
    return Buku(
        kode=row['Kode Buku'],
        judul=row['Judul'],
        penulis=row['Penulis'],
        kategori=row['Kategori'],
        tahun=row['Tahun'],
        status=row['Status']
    )