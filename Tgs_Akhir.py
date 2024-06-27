import os
os.system('cls')
acc=[['a','aa'],['b','bb'],['c','cc'],['d','dd']]
sl=[1000000000000,9999999,888888,777777]
def register():
    os.system('cls')
    print(f'''
==========================================
                 Register
==========================================
Ketik 1 untuk kembali''')
    reg1=input("Silahkan buat nama username       : ")
    reg2=input("Silahkan buat Password            : ")
    reg3=input("Silahkan masukkan kembali Password: ")
    fix=False
    for reg4 in acc:
        if reg1 in reg4:
            fix=True
    if reg1 == '1' or reg2 == '1' or reg3 == '1':
        os.system('cls')
    elif len(reg2) and len(reg3) <= 7 :
        os.system('cls')
        print('''
=====================================================================
                 Masukkan password minimal 8 karakter
=====================================================================''')
        input('tekan [ENTER] untuk coba lagi')
        os.system('cls')
        register2()
    elif reg2!=reg3:
        os.system('cls')
        print('''
=====================================================================
            [^^] Maaf Password Yang Anda Masukkan Berbeda[^^]
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')
        register2()
    elif (fix):
        os.system('cls')
        print('''
=====================================================================
 [^^] Maaf username sudah tersedia, Silahkan pilih username lain [^^]
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')
        register2()
    else:
        b.append(reg1)
        b.append(reg2)
        acc.append(b)
        sl.append(0)
        os.system('cls')
        print('''
=====================================================================
            [o^o] Selamat akun anda telah didaftarkan [o^o]
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')
def register2():
    register()

def login():
    global b,log1,log2
    b=[]
    os.system('cls')
    print(f'''
==========================================
                  Login
==========================================''')
    log1=input("Silahkan Masukkan username      : ")
    log2=input("Silahkan Masukkan Password      : ")
    b.append(log1)
    b.append(log2)
    if b in acc:
        os.system('cls')
        print('''
=====================================================================
                    (: Anda Berhasil Masuk 🙂
=====================================================================''')
        input('tekan [ENTER] untuk kembali ke halaman utama')
        os.system('cls')
        mainmenu()
    else:
        os.system('cls')
        print('''
=====================================================================
                 ):  Akun Anda Belum Didaftarkan 🙁
=====================================================================''')
        input('tekan [ENTER] untuk kembali ke halaman login')
        os.system('cls')

def isi_saldo():
    os.system('cls')
    print(f'''
==========================================
               1. Isi Saldo
==========================================
Ketik 1 untuk kembali''')
    isi_sl=int(input('Masukkan nominal yang ingin anda isi : '))
    if isi_sl <= 1 :
        os.system('cls')
        mainmenu()
    else:
        sl.pop(repeat1-1)
        sl.insert(repeat1-1,isi_sl+len_sl)
        os.system('cls')
        print('''
=====================================================================
            [^^] Selamat anda berhasil mengisi saldo [^^]
=====================================================================''')
        input('tekan [ENTER] untuk kembali kembali')
        os.system('cls')
        mainmenu()

def tf_saldo():
    os.system('cls')
    print(f'''
==========================================
            2. Transfer Saldo
Anda memiliki saldo sebesar Rp.{len_sl}
==========================================
Ketik 1 untuk kembali''')
    tf_pw=input('Masukkan Password Anda      :')
    if tf_pw == "1":
        os.system('cls')
        mainmenu()
    elif tf_pw != log2:
        os.system('cls')
        print('''
=====================================================================
           [^^] Maaf Password Yang Anda Masukkan Salah[^^]
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')
        tf_saldo1()
    else:
        tf_t=input("Masukkan username tujuan    :")
        tf_sl=int(input('Masukkan nominal            :'))
        if tf_t == log1:
            os.system('cls')
            print('''
=====================================================================
        Maaf anda tidak bisa menrasfer ke akun anda sendiri :3
=====================================================================''')
            input('Tekan [ENTER] untuk kembali')
            os.system('cls')
            tf_saldo1()
        elif tf_sl > len_sl or tf_sl < 1:
            os.system('cls')
            print('''
=====================================================================
                    Maaf saldo anda tidak cukup
=====================================================================''')
            input('Tekan [ENTER] untuk kembali')
            os.system('cls')
            tf_saldo1()
        elif tf_pw == log2:
            repeat3=0
            repeat4=0
            fix=False
            for acctf in range(len(acc)):
                repeat3+=1
                if (acc[acctf][0]) == tf_t:
                    fix=True
                    break
            if (fix):
                for tfsl in sl:
                    repeat4+=1
                    if repeat4 == repeat3:
                        sl.pop(repeat3-1)
                        sl.insert(repeat3-1,tfsl+tf_sl)
                        sl.pop(repeat1-1)
                        sl.insert(repeat1-1,len_sl-tf_sl)
                        os.system('cls')
                        print('''
=====================================================================
                    [^^] Transfer Berhasil ;D [^^]
=====================================================================''')
                        input('Tekan [ENTER] untuk kembali')
                        os.system('cls')
                        mainmenu()
            else:
                os.system('cls')
                print('''
=====================================================================
        [^^] Maaf penerima yang anda tuju tidak ada [^^]
=====================================================================''')
                input('Tekan [ENTER] untuk kembali')
                os.system('cls')
                tf_saldo1()

def tf_saldo1():
    tf_saldo()

def tarik():
    os.system('cls')
    print(f'''
==========================================
              3. Tarik tunai
Anda memiliki saldo sebesar Rp.{len_sl}
==========================================
Ketik 1 untuk kembali''')
    tr_sl=int(input('Masukkan nominal yang ingin anda tarik :'))
    if tr_sl <= 1:
        os.system('cls')
        mainmenu()
    elif tr_sl > len_sl :
        os.system('cls')
        print('''
=====================================================================
                     Maaf saldo anda tidak cukup
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')
        mainmenu()
    else:
        sl.pop(repeat1-1)
        sl.insert(repeat1-1,len_sl-tr_sl)
        os.system('cls')
        print(f'''
=====================================================================
        [^^] Anda berhasil menarik saldo sebesar {tr_sl} [^^]
=====================================================================''')
        input('tekan [ENTER] untuk kembali kembali')
        os.system('cls')
        mainmenu()

def gantipw():
    global acc,log2
    os.system('cls')
    print(f'''
==========================================
             4. Ganti Password
==========================================
Ketik 1 untuk kembali''')
    pw=input('Silahkan Masukkan Password anda     : ')
    if pw == '1':
        os.system('cls')
        mainmenu()
    elif pw ==(acc[repeat1-1][1]):
        pw1=input('Silahkan Masukkan Password Baru     : ')
        pw2=input('Silahkan Masukkan kembali password  : ')
        if len(pw1) and len(pw2) <= 7 :
            os.system('cls')
            print('''
=====================================================================
                    Masukkan password minimal 8 karakter
=====================================================================''')
            input('tekan [ENTER] untuk coba lagi')
            os.system('cls')
            gantipw1()
        elif pw1!=pw2:
            os.system('cls')
            print('''
=====================================================================
            [^^] Maaf Password Yang Anda Masukkan Berbeda[^^]
=====================================================================''')
            input('Tekan [ENTER] untuk kembali')
            os.system('cls')
            gantipw1()
        elif pw2 == log2:
            os.system('cls')
            print('''
=====================================================================
 [^^] Anda sudah menggunakan sandi ini, Silahkan pilih yang lain [^^]
=====================================================================''')
            input('Tekan [ENTER] untuk kembali')
            os.system('cls')
        else:
            log2=pw2
            b.pop(1)
            b.append(pw1)
            acc.pop(repeat1-1)
            acc.insert(repeat1-1,b)
            os.system('cls')
            print('''
=====================================================================
                 [^^] Password telah dirubah [^^]
=====================================================================''')
            input('Tekan [ENTER] untuk kembali')
            os.system('cls')
            mainmenu()
    else:
        os.system('cls')
        print('''
=====================================================================
                       ):  Password salah 🙁
=====================================================================''')
        input('tekan [ENTER] untuk kembali ke halaman login')
        os.system('cls')
        gantipw1()
def gantipw1():
    gantipw()

def contact():
    os.system('cls')
    print('''
=====================================================================
   Silahkan Hubungi Nomor 085334853966 bila ada bug pada program ;)
=====================================================================''')
    input('tekan [ENTER] untuk kembali ke halaman login')
    os.system('cls')
    mainmenu()

def mainmenu():
    global repeat1,len_sl
    repeat=0
    repeat1=0
    for len_acc in acc:
        repeat+=1
        if len_acc == b:
            for len_sl in sl:
                repeat1+=1
                if repeat1==repeat:
                    break
    print(f'''==========================================
Selamat datang {log1}
Anda Memiliki Saldo Sebesesar : Rp.{len_sl}
==========================================
1. isi saldo
2. transfer Saldo
3. tarik tunai
4. ganti password
5. logout
6. contact us\n''')
    mm=input("Silahkan Pilih Opsi : ")
    if mm == '1'or mm=='isi saldo'or mm=='1.isi saldo':
        isi_saldo()
    elif mm == '2'or mm=='transfer saldo'or mm=='2.transfer saldo':
        tf_saldo()
    elif mm == '3'or mm=='tarik tunai'or mm=='3.tarik tunai':
        tarik()
    elif mm == '4'or mm=='ganti password'or mm=='4.ganti password':
        gantipw()
    elif mm == '5'or mm=='logout'or mm=='5.logout':
        os.system('cls')
        print('''
=====================================================================
                       Anda berhasil logout
=====================================================================''')
        input('tekan [ENTER] untuk kembali ke halaman login')
        os.system('cls')
    elif mm == '6'or mm=='contact us'or mm=='6. contact us':
        contact()
    else:
        os.system('cls')
        print('''
=====================================================================
              Maaf opsi yang anda pilih tidak tersedia
=====================================================================''')
        input('tekan [ENTER] untuk kembali ke halaman login')
        os.system('cls')
        mainmenu()

while True:
    b=[]
    repeat=0
    print("""=====================================================================
            *[0_0]* Selamat datang di aplikasi dan@ *[0_0]*
=====================================================================
Silahkan masuk untuk mengakses dan@ 😀
1. login
2. register
3. exit """)
    hal=input("Silahkan Masukkan Pilihan anda : ")
    if hal == '1' or hal=='login' or hal=='1.login':
        login()
    elif hal == '2' or hal=='register' or hal=='2.register':
        register()
    elif hal == '3' or hal=='exit' or hal=='3.exit':
        os.system('cls')
        print('''
=====================================================================
                    Terimakasih Anak2 Monyet
=====================================================================''')
        break
    else:
        os.system('cls')
        print('''
=====================================================================
        [++] Maaf input anda salah, Silahkan input kembali [++]
=====================================================================''')
        input('Tekan [ENTER] untuk kembali')
        os.system('cls')