nama = "Rai Husnul Arifah"
program = "Massa Jenis"

print(f'Program {program} oleh {nama}')

# TUGAS : buat fungsi_APA SAJA YANG KALIAN TAU
def hitung_massajenis(massa, volume):
    massajenis = massa / volume
    print(f'massa = {massa / 20}kg diperoleh dari volume = {volume / 10}liter')
    print(f'sehingga massajenis = {massajenis} kg/liter')

# massa = 20
# volume = 10
massajenis = hitung_massajenis(20, 10)

def hitung_massa(massajenis, volume):
    massa = massajenis * volume
    print(f'massajenis = {massajenis / 10}kg/liter diperoleh dari volume = {volume / 50}liter')
    print(f'sehingga massa = {massa} kg')

# massajenis = 10
# volume = 50
massa = hitung_massa(10,50)

def hitung_volume(massajenis, massa):
    volume = massajenis / massa
    print(f'massajenis = {massajenis / 5}kg/liter diperoleh dari massa = {massa / 20}kg')
    print(f'sehingga volume = {volume} liter')

# massajenis = 5
# massa = 20
volume = hitung_volume(5,20)
