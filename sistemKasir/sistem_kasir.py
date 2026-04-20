member = False
class Produk:
  def __init__(self, nama, harga, stok):
    self.nama = nama
    self.harga = harga
    self.stok = stok
    
class Keranjang:
  def __init__(self, ):
    self.daftar_barang = [] 
  
  def tambah_produk(self, produk_baru, jumlah=1,):
    if produk_baru.stok < jumlah:
      print(f"Stok {produk_baru.nama} tidak cukup. Stok tersedia: {produk_baru.stok}")
      return
    for _ in range(jumlah):
      self.daftar_barang.append(produk_baru)
    print(f"Berhasil menambah: {produk_baru.nama} (x{jumlah}) ke keranjang.")
  
  def hapus_produk(self, produk_hapus):
    if produk_hapus in self.daftar_barang:
      self.daftar_barang.remove(produk_hapus)
      print(f"Berhasil menghapus: {produk_hapus.nama} dari keranjang.")
    else:
      print(f"{produk_hapus.nama} tidak ditemukan di keranjang.")
  
  def hitung_total(self):
    total = 0
    for barang in self.daftar_barang:
      total += barang.harga
    return total
  
  def bayar(self, jumlah_bayar, kembalian):
    total_belanja = self.hitung_total()
    if jumlah_bayar >= total_belanja:
      print(f'berhasil bayar Rp{jumlah_bayar}')
    else:
      print('kurang duit')
    if jumlah_bayar > total_belanja:
      kembalian = jumlah_bayar - total_belanja
      print(f'kembalian: Rp{kembalian}')
  
  def cetak_struk(self):
    print("\n=== Struk Belanja ===")
    for barang in self.daftar_barang:
      print(f"- {barang.nama} : Rp{barang.harga}")
      
    total_akhir = self.hitung_total()
    if member is True and total_akhir >= 100000:
      diskon = total_akhir * 0.15
      print(f"\nDiskon (15%) \t: -Rp{diskon}")
      total_akhir -= diskon
    elif member is False and total_akhir >= 100000:
      diskon = total_akhir * 0.1
      print(f"\nDiskon (10%) \t: -Rp{diskon}")
      total_akhir -= diskon
    else:      
      print("\nTidak ada diskon")
    ppn = total_akhir * 0.11
    print(f"PPN (11%) \t: Rp{ppn}")
    total_akhir += ppn
    print(f"Total Akhir \t: Rp{total_akhir}")
    