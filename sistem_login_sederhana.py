"""
program minta:
1.username
2.password
3.apakah member?
"""
users = [ 'bagas','farhan','gavi','fermin','yamal']
sandi = 12345

username = input('masukan nama:')
password = int(input('masukan password 4 digit:'))
member = input("apakah member (Y/N)?")

if username not in users :
    print ('user name tidak terdaftar')

elif password != sandi  :
     print ('password salah')

elif member == 'Y' :
     print('Selamat datang member')
else :
     print('Selamat datang')
     

    




