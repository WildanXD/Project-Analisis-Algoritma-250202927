from Model import Buku

class NodeBST:
    def __init__(self, buku):
        self.buku = buku
        self.kiri = None
        self.kanan = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def tambah_data(self, buku):
        if self.root is None:
            self.root = NodeBST(buku)
            return
        current = self.root
        while True:
            if buku.kode < current.buku.kode:
                if current.kiri is None:
                    current.kiri = NodeBST(buku)
                    break
                current = current.kiri
            elif buku.kode > current.buku.kode:
                if current.kanan is None:
                    current.kanan = NodeBST(buku)
                    break
                current = current.kanan
            else:
                break

    def get_height(self):
        if self.root is None:
            return 0
        
        queue = [self.root]
        height = 0
        
        while queue:
            height += 1
            next_level = []
            for node in queue:
                if node.kiri:
                    next_level.append(node.kiri)
                if node.kanan:
                    next_level.append(node.kanan)
            queue = next_level
            
        return height

class SortedList:
    def __init__(self):
        self.data = []

    def tambah_data(self, buku):
        self.data.append(buku)