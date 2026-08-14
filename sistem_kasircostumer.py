#input:
nama=input('masukan nama anda:')
laptop = int(input('masukan harga leptop:'))
mouse = int(input('masukan harga mouse:'))
keyboard = int(input('masukan harga keyboard:'))
#proses:
total = laptop + mouse + keyboard

if total >=8000000:
    diskon = total * 10 / 100
    bayar = total - diskon 
    print("nama:",nama )
    print("harga awal:",total)
    print('dapat diskon:',diskon)
    print('yg harus dibayar:',bayar)

