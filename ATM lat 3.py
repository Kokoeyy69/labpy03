# python Program Mesin ATM

def show_balance(balance):
    print("*********************")
    print(f"Saldo Kamu :{balance: .2f}")
    print("*********************")

def deposit():
    jumlah = float(input("Masukan Nominal :"))
    print("*********************")
    
    if jumlah < 0:
        print("Jumlah tidak valid")
        return 0
    else:
        return jumlah

def withdraw(balance):
    jumlah = float(input("Masukan jumlah penarikan :"))
    
    if jumlah > balance:
        print("*********************")
        print("Penarikan Gagal")
        print("Saldo Tidak Cukup")
        print("*********************")
        return 0
    elif jumlah < 0:
        print("Angka Tidak Valid")
        return 0
    else:
        return jumlah

def main():

    
    balance = 10000000

    is_running = True

    print("*********************")
    print("******Mesin ATM******")
    print("*********************")

    while is_running:
        print(f"Saldo Kamu : {balance}")
        print("*********************")
        print("Pilih Metode")
        print("1.Cek Saldo")
        print("2.Isi Saldo")
        print("3.Tarik Uang")
        print("4.Keluar") 
        print('*********************')
        
        pilihan = input("Pilih Menu (1/4) :")

        if pilihan == '4':
            print("Anda keluar dari ATM")
            print("Terimakasih telah menggunakan ATM")
            break
        elif pilihan == '':
            print("Anda keluar dari ATM")
            print("Terimakasih telah menggunakan ATM")
            break
            
        if pilihan == '1':
            show_balance(balance)
        elif pilihan == '2':
            balance += deposit()
        elif pilihan == '3':
            balance -= withdraw(balance)
            print('*******************')
            print(f"Sisa Saldo Kamu : {balance}")
            print('*******************')

if __name__ == '__main__':
    main()
    