[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/nHIh47i4)
# UG11_HASH

Dengan memodifikasi Hash Table yang telah diajarkan pada kelas Struktur Data, anda diminta untuk mengubah fungsi add dan delete agar sesuai dengan permintaan soal. Berikut adalah penjelasan terkait fungsi-fungsi tersebut.

a) tambahReservasi() merupakan fungsi add yang membutuhkan argumen nama sebagai key dan jenis reservasi sebagai value. Fungsi ini digunakan untuk menambahkan item kedalam hash table. Nilai kembalian dari fungsi ini adalah Boolean (True/False).

b) lihatReservasi() merupakan fungsi yang digunakan untuk mengecek reservasi dengan key yang serupa. Fungsi ini akan mengembalikan value berupa String yang pertama kali ditemukan pada index map. Jika key tidak ditemukan akan mengembalikan “None”

c) reserveDone() merupakan fungsi delete yang membutuhkan argumen nama (key). Fungsi ini menghapus key yang pertama kali ditemukan dengan cara menimpa index pada map dengan string “deleted”. Fungsi ini mengembalikan Boolean (True/False)

d) printAll() merupakan fungsi print yang digunakan untuk menampilkan list reservasi yang terdapat pada resto.

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
