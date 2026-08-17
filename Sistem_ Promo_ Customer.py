nama = input('masukkan nama anda:')
total_belanja = int(input('masukan total belanja anda:'))
member = input('apakah anda punya member,masukan salah satu huruf dengan huruf besar(Y/N) :')
voucher = input('apakah anda punya voucher,masukan salah satu huruf dengan huruf besar(Y/N) :')

if total_belanja >= 300000 and member == 'Y' :
    promo = '10%'
    diskon = total_belanja * 10 / 100
    total = total_belanja - diskon


elif member == 'Y' or voucher == 'Y' :
    promo = '5%'
    diskon = total_belanja * 5 / 100
    total = total_belanja - diskon


else :
    promo = 'maaf tidak dapat'
    total = total_belanja - 0

print ('nama costumer:',nama)
print('Total belanja:',total_belanja)
print('status diskon dapat berapa:',promo)
print('harga akhir yg di bayar;',total)



