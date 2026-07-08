def sequential_search(sorted_list, target_kode):
    for buku in sorted_list.data:
        if buku.kode == target_kode:
            return buku
    return None

def bst_search(bst, target_kode):
    current = bst.root
    while current is not None:
        if current.buku.kode == target_kode:
            return current.buku
        elif target_kode < current.buku.kode:
            current = current.kiri
        else:
            current = current.kanan
    return None

def cari_buku_by_judul(sorted_list, keyword):
    """Mencari buku yang judulnya mengandung keyword (Case Insensitive)"""
    hasil = []
    for buku in sorted_list.data:
        if keyword.lower() in buku.judul.lower():
            hasil.append(buku)
    return hasil