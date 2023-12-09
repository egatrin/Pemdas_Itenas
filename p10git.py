import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

datagaji = pd.DataFrame(data)
print("Gaji Awal :")
print(datagaji)

# Pertanyaan 1: Peningkatan gaji 5%
for index, row in datagaji.iterrows():
    datagaji.at[index, 'Gaji'] = (lambda x: x + x * 0.05)(row['Gaji'])

# Pertanyaan 2: Tampilkan DataFrame setelah perubahan
print("\nSetelah gaji ditambah 5%:")
print(datagaji)

# Salin DataFrame setelah perubahan untuk membandingkan
tdatagaji5 = datagaji.copy()

# Pertanyaan 3: Peningkatan tambahan 2% untuk usia di atas 30 tahun
for index, row in datagaji.iterrows():
    if row['Usia'] > 30:
        datagaji.at[index, 'Gaji'] = (lambda x: x + x * 0.02)(row['Gaji'])

# Pertanyaan 4: Tampilkan DataFrame setelah peningkatan gaji tambahan
print("\nSetelah peningkatan gaji umur di atas 30:")
print(datagaji[['Nama', 'Usia', 'Gaji']])

# Salin DataFrame setelah peningkatan untuk membandingkan
tdatagaji30 = datagaji.copy()

# Output ringkasan hasil
print("\nRingkasan hasil setelah peningkatan gaji:")
ringkas = pd.concat([datagaji[['Nama', 'Gaji']], tdatagaji5[['Gaji']], tdatagaji30[['Gaji']]], axis=1)
ringkas.columns = ['Nama', 'Gaji Awal', 'Gaji +5%', 'Gaji Umur>30']
print(ringkas)
