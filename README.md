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






