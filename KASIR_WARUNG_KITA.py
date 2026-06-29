from datetime import datetime

# ======================================
# DATA PRODUK
# ======================================

data_produk = {
    'P001': {'nama': 'Beras 1kg', 'harga': 15000, 'stok': 50},
    'P002': {'nama': 'Minyak Goreng 1L', 'harga': 20000, 'stok': 30},
    'P003': {'nama': 'Gula Pasir 1kg', 'harga': 14000, 'stok': 40},
    'P004': {'nama': 'Mie Instan', 'harga': 3500, 'stok': 100}
}

riwayat_transaksi = []


# ======================================
# TAMPILKAN KATALOG
# ======================================

def tampil_katalog():
    print("\n===== KATALOG BARANG =====")

    for kode, barang in data_produk.items():
        print(
            f"{kode} | {barang['nama']} | "
            f"Harga: Rp{barang['harga']:,} | "
            f"Stok: {barang['stok']}"
        )


# ======================================
# TAMBAH PRODUK
# ======================================

def tambah_produk():

    print("\n===== TAMBAH PRODUK =====")

    kode = input("Masukkan kode produk: ").upper()

    if kode in data_produk:
        print("Kode produk sudah digunakan!")
        return

    nama = input("Masukkan nama produk: ")

    try:
        harga = int(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))

        if harga <= 0 or stok < 0:
            print("Harga dan stok harus bernilai positif.")
            return

    except ValueError:
        print("Harga dan stok harus berupa angka.")
        return

    data_produk[kode] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    print(f"Produk '{nama}' berhasil ditambahkan.")


# ======================================
# TRANSAKSI
# ======================================

def transaksi():

    daftar_belanja = []
    total = 0

    while True:

        tampil_katalog()

        kode = input(
            "\nMasukkan kode barang "
            "(ketik SELESAI jika selesai): "
        ).upper()

        if kode == "SELESAI":
            break

        if kode not in data_produk:
            print("Kode barang tidak ditemukan!")
            continue

        produk = data_produk[kode]

        while True:

            try:
                jumlah = int(
                    input(
                        f"Jumlah {produk['nama']} "
                        f"(Stok: {produk['stok']}): "
                    )
                )

                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    continue

                if jumlah > produk['stok']:
                    print(
                        f"Maaf stok tidak cukup. "
                        f"Tersedia: {produk['stok']}"
                    )
                    continue

                break

            except ValueError:
                print("Input harus berupa angka!")

        subtotal = jumlah * produk["harga"]

        produk["stok"] -= jumlah

        total += subtotal

        daftar_belanja.append({
            "kode": kode,
            "nama": produk["nama"],
            "jumlah": jumlah,
            "harga": produk["harga"],
            "subtotal": subtotal
        })

    if total == 0:
        print("Tidak ada transaksi.")
        return

    # Diskon
    if total >= 100000:
        diskon = int(total * 0.10)
    else:
        diskon = 0

    bayar = total - diskon

    id_transaksi = f"TRX{len(riwayat_transaksi)+1:03d}"

    data_transaksi = {
        "id_transaksi": id_transaksi,
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "barang": daftar_belanja,
        "total": total,
        "diskon": diskon,
        "bayar": bayar
    }

    riwayat_transaksi.append(data_transaksi)

    print("\nTransaksi berhasil!")
    print("Total Bayar : Rp{:,.0f}".format(bayar))


# ======================================
# CETAK STRUK
# ======================================

def cetak_struk():

    if not riwayat_transaksi:
        print("Belum ada transaksi.")
        return

    trx = riwayat_transaksi[-1]

    print("\n========== STRUK ==========")
    print("ID      :", trx["id_transaksi"])
    print("Waktu   :", trx["waktu"])
    print("---------------------------")

    for item in trx["barang"]:
        print(
            f"{item['nama']} "
            f"x{item['jumlah']} "
            f"= Rp{item['subtotal']:,}"
        )

    print("---------------------------")
    print(f"Total  : Rp{trx['total']:,}")
    print(f"Diskon : Rp{trx['diskon']:,}")
    print(f"Bayar  : Rp{trx['bayar']:,}")
    print("===========================")


# ======================================
# CEK STOK
# ======================================

def cek_stok():

    print("\n===== STOK BARANG =====")

    for kode, barang in data_produk.items():
        print(
            f"{kode} | "
            f"{barang['nama']} | "
            f"Stok: {barang['stok']}"
        )


# ======================================
# RIWAYAT TRANSAKSI
# ======================================

def tampilkan_riwayat():

    print("\n===== RIWAYAT TRANSAKSI =====")

    if not riwayat_transaksi:
        print("Belum ada transaksi.")
        return

    laporan = sorted(
        riwayat_transaksi,
        key=lambda x: x["bayar"],
        reverse=True
    )

    total_omset = 0

    print(
        f"{'ID TRX':<10} | "
        f"{'WAKTU':<19} | "
        f"{'TOTAL BAYAR':<15}"
    )

    print("-" * 50)

    for trx in laporan:

        print(
            f"{trx['id_transaksi']:<10} | "
            f"{trx['waktu']:<19} | "
            f"Rp{trx['bayar']:<12,}"
        )

        total_omset += trx["bayar"]

    print("-" * 50)
    print(f"Total Omset Penjualan : Rp{total_omset:,}")


# ======================================
# MENU UTAMA
# ======================================

while True:

    print("""
=================================
         SELAMAT DATANG
              DI
  APLIKASI KASIR WARUNG KITA
=================================
1. Tampilkan Katalog
2. Tambah Produk
3. Transaksi
4. Cetak Struk
5. Cek Stok
6. Riwayat Transaksi
7. Keluar
=================================
""")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampil_katalog()

    elif pilihan == "2":
        tambah_produk()

    elif pilihan == "3":
        transaksi()

    elif pilihan == "4":
        cetak_struk()

    elif pilihan == "5":
        cek_stok()

    elif pilihan == "6":
        tampilkan_riwayat()

    elif pilihan == "7":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Menu tidak tersedia.")
