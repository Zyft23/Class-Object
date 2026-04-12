
class AkunBank:
  def __init__(self, nomor, pemilik, saldo_awal,riwayatsaldo):
    self.nomor = nomor 
    self.pemilik = pemilik
    self.saldo = saldo_awal
    self.riwayat = riwayatsaldo
  
  def cek_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
  def tarik_tunai(self, jumlah):
    if jumlah <= self.saldo:  
      if jumlah <= 0:
        print("jumlah tarik tunai harus lebih besar dari 0")
        return
      if jumlah > 1000000:
        print("Jumlah tarik tunai melebihi batas maksimal Rp1.000.000")
        return
      self.saldo -= jumlah
      self.riwayat.append(f"{self.pemilik} menarik Rp{jumlah}")
      print(f"{self.pemilik} menarik Rp{jumlah}")
    else:
      print("Saldo tidak cukup!")
      
  
  def transfer(self, tujuan, jumlah):
    if self.saldo >= jumlah:
      if jumlah <= 0:
        print("jumlah transfer harus lebih besar dari 0")
        return
      self.saldo -= jumlah
      self.saldo -= 2500
      tujuan.saldo += jumlah
      self.riwayat.append(f"{self.pemilik} transfer Rp{jumlah} ke {tujuan.pemilik}")
      print(f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil!")
    else:
      print("Transfer Gagal: Saldo tidak cukup.")
    
