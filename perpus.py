class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}"

class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-----------------")
            print("|| DAFTAR BUKU ||")
            print("-----------------")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("koleksi buku masih kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        print(f"Buku : '{judul}' tidak ditemukan.")
        return None

    def pinjam_buku(self, buku, anggota):
        if buku.status == "Tersedia":
            buku.status = "dipinjam"
            anggota.buku_pinjaman.append(buku)
            
            print(f"Buku '{buku.judul}' tersedia untuk dipinjam oleh {anggota.nama}.")
        else:
            print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, buku, anggota):
        if buku in anggota.buku_pinjaman:
            buku.status = "Tersedia"
            anggota.buku_pinjaman.remove(buku)
            print(f"Buku '{buku.judul}' berhasil dikembalikan oleh '{anggota.nama}'.")
        else:
            print(f"Buku '{buku.judul}' tidak sedang dipinjam oleh '{anggota.nama}'.")

class Anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- Buku Pinjaman ({self.nama}) --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

def main():
    # BUAT BEBERAPA BUKU
    buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
    buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
    buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam")

    # buat perpustakaan dan anggota
    perpustakaan = Perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

    anggota1 = Anggota("Ivan", 12345)
    anggota2 = Anggota("Suci", 56789)

    # jalankan program
    print("\n-- Menu Perpustakaan --")
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Keluar")
    angka = int(input("Pilih menu : "))

    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Input judul buku: ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        judul_buku = input("Masukkan judul buku yang dipinjam: ")
        nama_anggota = input("Nama anggota yang meminjam: ")

        buku = perpustakaan.cari_buku(judul_buku)
        anggota = next((a for a in [anggota1, anggota2] if a.nama.lower() == nama_anggota.lower()), None)

        if buku and anggota:
            perpustakaan.pinjam_buku(buku, anggota)
        elif not buku:
            print(f"Buku '{judul_buku}' tidak ditemukan.")
        elif not anggota:
            print(f"Anggota dengan nama '{nama_anggota}' tidak ditemukan.")
    elif angka == 4:
        buku_judul = input("Buku yang dikembalikan: ")
        for buku in perpustakaan.koleksi_buku:
            if buku.judul.lower() == buku_judul.lower():
                anggota_nama = input("Input nama anggota: ")
                for anggota in [anggota1, anggota2]:
                    if anggota.nama.lower() == anggota_nama.lower():
                        perpustakaan.kembalikan_buku(buku, anggota)
                        break
        else:
            print("Anda salah pilih.")

if __name__ == "__main__":
    main()
