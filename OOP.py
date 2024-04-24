class kantor: #class parent 
    def __init__(self, karyawan, jabatan, gaji): #atribut / properti
        self.karyawan = karyawan 
        self.jabatan = jabatan 
        self.gaji = gaji 

    def info(self): #method / fungsi
        print(f'nama: ${self.karyawan}, jabatan: ${self.jabatan}, gaji: ${self.gaji}')


class boss(kantor): #inheritance class
    def info(self):
        print(f'nama: ${self.karyawan}, jabatan: ${self.jabatan}, gaji: ${self.gaji}')

bos = boss('Adit', 'manager', 20000000) #object
ob = boss('Boby', 'OB', 1200000)

print(f' Nama {bos.karyawan}, jabatan {bos.jabatan}, gaji Rp.{bos.gaji}')
print(f' Nama {ob.karyawan}, jabatan {ob.jabatan}, gaji Rp.{ob.gaji}')
