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
