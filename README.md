# Random Number Generator Program
Program ini bertujuan untuk menghasilkan sejumlah bilangan acak desimal dalam rentang tertentu (antara 0 dan 0.5) dan menampilkannya dengan format yang mudah dibaca. Setiap angka acak yang dihasilkan akan ditampilkan dengan nomor urut sesuai jumlah yang ditentukan oleh pengguna.

## Cara Kerja Program :
#### 1. Input Pengguna:
- Program meminta pengguna untuk memasukkan sebuah angka bulat (n), yang menunjukkan jumlah bilangan acak yang akan dihasilkan.

#### 2. Pengulangan (Looping):
- Program akan melakukan pengulangan sebanyak n-1 kali untuk menghasilkan bilangan acak. Setiap iterasi menghasilkan satu bilangan acak desimal.

#### 3. Menghasilkan Bilangan Acak:
- Pada setiap iterasi, program menghasilkan bilangan acak desimal dalam rentang 0 hingga 0.5.

#### 4. Menampilkan Hasil:
- Program menampilkan setiap bilangan acak yang dihasilkan bersama dengan nomor urutnya.


## Kode Program
```python
import random

n = int(input("Masukan Nilai N:"))

for i in range(1, n):
    a = random.uniform(0, 0.5)
    print(f"data ke {i}: {a}")

```

## Penjelasan Kode
- import random: Mengimpor modul random yang digunakan untuk menghasilkan bilangan acak.

- n = int(input("Masukan Nilai N:")): Meminta input dari pengguna dalam bentuk angka bulat (int). Nilai ini menunjukkan berapa banyak angka yang akan dihasilkan (n-1 kali).

- for i in range(1, n):: Menggunakan for loop untuk menghasilkan angka acak n-1 kali. Indeks i dimulai dari 1 hingga n-1.

- a = random.uniform(0, 0.5): Menghasilkan sebuah angka acak desimal dalam rentang 0 hingga 0.5 menggunakan random.uniform(0, 0.5).

- print(f"data ke {i}: {a}"): Menampilkan hasil bilangan acak dan nomor urutnya.

## Contoh Output 
Misalkan pengguna memasukkan nilai 5 saat diminta:
```
Masukan Nilai N: 5
data ke 1: 0.3452
data ke 2: 0.1234
data ke 3: 0.4567
data ke 4: 0.2143
```
Dalam contoh ini, program menghasilkan 4 angka acak desimal antara 0 dan 0.5, dan menampilkan setiap angka dengan nomor urutnya.

## Catatan
Program ini menggunakan fungsi random.uniform() untuk menghasilkan bilangan acak desimal. Jika ingin mengubah rentang angka acak, cukup sesuaikan argumen pada fungsi random.uniform(min, max).

#     

#  

# Program Perhitungan Laba Investasi Bulanan
Program ini menghitung laba bulanan dari suatu investasi berdasarkan modal awal yang diinvestasikan. Setiap bulan, laba dihitung sesuai dengan persentase tertentu dari modal awal. Laba kemudian dijumlahkan selama 8 bulan untuk mendapatkan total laba.

## Detail Program
#### 1. Modal Awal
- Modal awal (modalAwal) diinisialisasi dengan nilai 100 juta rupiah.

#### 2. Total Laba
- Variabel totalLaba diinisialisasi sebagai 0. Variabel ini digunakan untuk menyimpan akumulasi laba selama 8 bulan.

#### 3. Perhitungan Laba Bulanan
- Program menggunakan loop for untuk iterasi dari bulan ke-1 hingga bulan ke-8, di mana setiap bulan memiliki ketentuan laba sebagai berikut:

    - Bulan 1 dan 2: Tidak ada laba (0% dari modal awal).
    - Bulan 3 dan 4: Laba sebesar 1% dari modal awal.
    - Bulan 5, 6, dan 7: Laba sebesar 5% dari modal awal.
    - Bulan 8: Laba sebesar 2% dari modal awal.

#### 4. Total Laba Akhir
- Setiap laba bulanan ditambahkan ke totalLaba. Setelah loop selesai, totalLaba akan berisi jumlah laba yang dihasilkan selama 8 bulan.

## Kode Program

```python
modalAwal = 100000000
totalLaba = 0
for bulan in range(1,9):
    if bulan == 1:
        operation = 0
        print(f'Laba bulan ke- {bulan} Sebesar 0')
    elif bulan == 2:
        operation = 0
        print(f'Laba bulan ke- {bulan} Sebesar 0')
    elif bulan == 3:
        operation = modalAwal * 1 /100
        print(f'Laba bulan ke- {bulan} Sebesar {modalAwal * 1 /100}')
    elif bulan == 4:
        operation = modalAwal * 1 /100
        print(f'Laba bulan ke- {bulan} Sebesar {modalAwal * 1 /100}')
    elif bulan == 5:
        operation = modalAwal * 5 /100
        print(f'Laba bulan ke- {bulan} Sebesar {modalAwal * 5 /100}')
    elif bulan == 6:
        operation = modalAwal * 5 /100  
        print(f'Laba bulan ke- {bulan} Sebesar {modalAwal * 5 /100}')
    elif bulan == 7:
        operation = modalAwal * 5 /100
        print(f'Laba bulan ke- {bulan} Sebesar {operation}')
    elif  bulan == 8 : 
        operation = modalAwal * 2 /100
        print(f'Laba bulan ke- {bulan} Sebesar {modalAwal * 2/100}')
    totalLaba += operation
print('Maka Total Laba adalah : ', totalLaba)
```

## Contoh Output
Output dari program di atas adalah sebagai berikut:

```
Laba bulan ke- 1 Sebesar 0
Laba bulan ke- 2 Sebesar 0
Laba bulan ke- 3 Sebesar 1000000.0    
Laba bulan ke- 4 Sebesar 1000000.0    
Laba bulan ke- 5 Sebesar 5000000.0    
Laba bulan ke- 6 Sebesar 5000000.0    
Laba bulan ke- 7 Sebesar 5000000.0    
Laba bulan ke- 8 Sebesar 2000000.0    
Maka Total Laba adalah :  19000000.0  
```

## Penjelasan Output
#### 1. Bulan 1 dan 2: Laba sebesar 0.

#### 2. Bulan 3 dan 4: Laba sebesar 1% dari modal awal (100 juta), yaitu 1 juta per bulan.

#### 3. Bulan 5, 6, dan 7: Laba sebesar 5% dari modal awal, yaitu 5 juta per bulan.

#### 4. Bulan 8: Laba sebesar 2% dari modal awal, yaitu 2 juta.

Total laba yang dihasilkan selama 8 bulan adalah 19 juta rupiah.

#  

#  

# Python ATM Simulator
Program ini adalah simulasi sederhana dari mesin ATM menggunakan bahasa pemrograman Python. Program ini memungkinkan pengguna untuk melakukan beberapa operasi dasar perbankan, seperti mengecek saldo, menambah saldo, menarik uang, dan keluar dari sistem. Program ini menggunakan konsep perulangan, percabangan, dan fungsi untuk mengimplementasikan fitur ATM.

## Fitur Program
#### 1. Cek Saldo: Menampilkan saldo saat ini yang dimiliki oleh pengguna.

#### 2. Isi Saldo: Menambah saldo pengguna dengan jumlah nominal yang dimasukkan.

#### 3. Tarik Uang:  Mengurangi saldo pengguna sesuai dengan nominal penarikan yang dimasukkan. Jika saldo tidak mencukupi, program akan menampilkan pesan kesalahan.

#### 4. Keluar: Menghentikan program dan mengucapkan terima kasih kepada pengguna.


##  Struktur Kode
Program terdiri dari beberapa fungsi utama, yaitu:

- show_balance(balance): Menampilkan saldo pengguna dengan format yang rapi.

- deposit(): Meminta pengguna untuk memasukkan jumlah saldo yang akan ditambahkan.   Memvalidasi bahwa jumlah harus bernilai positif.
  
- withdraw(balance): Meminta pengguna untuk memasukkan jumlah yang akan ditarik. Memeriksa   apakah saldo cukup untuk penarikan dan jumlah yang dimasukkan valid.

- main(): Fungsi utama yang menjalankan antarmuka ATM, menampilkan menu, dan memproses pilihan pengguna.

## Cara Kerja Program
#### 1. Program memulai dengan saldo awal yang telah ditentukan (misalnya Rp 10,000,000).

#### 2. Pengguna akan diberikan menu untuk memilih salah satu dari empat opsi: cek saldo, isi saldo, tarik uang, atau keluar.

#### 3. Berdasarkan pilihan pengguna:
 - Jika pengguna memilih cek saldo, saldo akan ditampilkan.
 - Jika pengguna memilih isi saldo, pengguna akan diminta memasukkan jumlah yang akan ditambahkan ke saldo.
 - Jika pengguna memilih tarik uang, pengguna akan diminta memasukkan jumlah yang akan ditarik dari saldo. Program akan memeriksa apakah saldo mencukupi sebelum melakukan penarikan.
 - Jika pengguna memilih keluar, program akan berhenti dan menampilkan pesan penutupan.

#### 4. Program terus berjalan hingga pengguna memilih opsi keluar.


## Contoh Output
```
*********************
******Mesin ATM******
*********************
Saldo Kamu : 10000000
*********************
Pilih Metode
1.Cek Saldo
2.Isi Saldo
3.Tarik Uang
4.Keluar
*********************
Pilih Menu (1/4) : 1

*********************
Saldo Kamu : 10000000.00
*********************

Saldo Kamu : 10000000
*********************
Pilih Metode
1.Cek Saldo
2.Isi Saldo
3.Tarik Uang
4.Keluar
*********************
Pilih Menu (1/4) : 2
Masukan Nominal : 500000

*********************
Saldo Kamu : 10500000.00
*********************

Saldo Kamu : 10500000.0
*********************
Pilih Metode
1.Cek Saldo
2.Isi Saldo
3.Tarik Uang
4.Keluar
*********************
Pilih Menu (1/4) : 3
Masukan jumlah penarikan : 2000000

*******************
Sisa Saldo Kamu : 8500000.0
*******************

Saldo Kamu : 8500000.0
*********************
Pilih Metode
1.Cek Saldo
2.Isi Saldo
3.Tarik Uang
4.Keluar
*********************
Pilih Menu (1/4) : 4

Anda keluar dari ATM
Terimakasih telah menggunakan ATM

```

## Catatan
Program ini adalah simulasi sederhana dan ditujukan untuk keperluan pembelajaran. Pada aplikasi ATM yang sebenarnya, diperlukan lebih banyak keamanan dan validasi data yang lebih ketat.
























