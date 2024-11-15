class Restoran:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size
    
    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size
    
    def _probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self._linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
    
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size
    
    def tambahReservasi(self,key,value):
        key_hash = self._getHash(key)
        key_value = [key,value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            print(f"Reservasi atas nama {key} berhasil dalam {value}")
            return True
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                print(f"Reservasi atas nama {key} tidak dapat masuk karena penuh")
                return False
            self.map[key_hash] = list([key_value])
            print(f"Reservasi atas nama {key} berhasil dalam {value}")
            return True
    def lihatReservasi(self,key):
        key_hash = self._getHash(key)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != "deleted"):
            for index in range(self.size):
                key_hash = self._linearProbing(key,index)
                if (self.map[key_hash] [0][0] == key):
                    return (f"Data Berhasil ditemukan untuk reservasi {self.map[key_hash][0][1]}")
        return (f"Data {key} Tidak Berhasil Ditemukan")
    def reserveDone(self,key):
        key_hash = self._getHash(key)
        if (self.map[key_hash] is None):
            return False
        else:
            for index in range(self.size):
                key_hash = self._linearProbing(key,index)
                if (self.map[key_hash] [0] [0] == key):
                    self.map[key_hash] = "deleted"
                    print(f"Tamu atas nama {key} hadir")
            print(f"Data tamu {key} tidak ditemukan") 
            return False
                
        # key_hash = self._getHash(key)
        # if self.map[key_hash] is None:
        #     return False
        # for i in range(self.size):
        #     key_hash = self._linearProbing(key, i)
        #     if(self.map[key_hash][0][0] == key):
        #         self.map[key_hash] = "deleted"
        #         print(f'Tamu dengan nama {key} sudah datang')
        #         return True
        # print(f'Pelanggan atas nama {key} tidak ditemukan')
        # return False
    def printAll(self):
        # print ("=== Data Antrian ===")
        # count = 1
        # for item in self.map:
        #     if item is not None:
        #         if item != "deleted":
        #             print(f"{count}. {(item)[0][0]} - {(item)[0][1]}")
        #             count += 1
        # print ()
        print(f"===== Data Antrian =====")
        hitung = 1
        for items in self.map:
            if items is not None and items != "deleted":
                print(f"{hitung}. {items[0][0]} dengan pemesanan {items[0][1]}")
        print()
    
if __name__ == "__main__":
    rak1 = Restoran()
    rak1.tambahReservasi("Draine", "Family Dinner")
    rak1.tambahReservasi("Perry", "Birthday Party")
    rak1.tambahReservasi("Octo", "Romantic Dinner")
    rak1.tambahReservasi("Peter", "Lunch")
    rak1.tambahReservasi("Hrain", "Test Food Wedding")
    rak1.tambahReservasi("Gura", "Garden Party")
    print(rak1.lihatReservasi("Octo"))
    print(rak1.lihatReservasi("Buna"))
    rak1.reserveDone("Pery")
    rak1.reserveDone("Draine")
    rak1.printAll()
