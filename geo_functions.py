from home_work import Geologic_time_scale
import random

geo_1 = Geologic_time_scale(100)
# print(geo_1)
#


geo_2 = Geologic_time_scale(4600000000)
geo_3 = Geologic_time_scale(4500000000)

#str
print('1 - str')
print()
print(geo_1)
print()
print(geo_2)
print()

# len
print('2 - len')
print(f'Длина периода: {geo_2.return_eon()} : {len(geo_2)}, {geo_2.round_year(len(geo_2))}') # почему-то печатат еще функцию print(), а не только длину
print(f'Длина периода: {geo_1.return_eon()} : {len(geo_1)}, {geo_2.round_year(len(geo_1))}') # почему-то печатат еще функцию print(), а не только длину

print()
# getitem
print('3.1 - getitem')
for item in geo_2:
    print(item)
print()
# in
print('3.2 - in')
print('Катархей' in geo_2)
print('Плиоцен' in geo_1)
print()
# eq - принадлежат ли даты одному и тому же периоду
print('4 - eq - принадлежат ли даты одному и тому же периоду')
print(geo_2 == geo_3) # Катархей == Катархей
print(geo_2 == geo_1) # Катархей != Голоцен
print()
print('5 - ne') # неравенство !=
print(geo_2 != geo_3)
print(geo_2 != geo_1)
print()
print('6 - lt - какой период был раньше') # Какой период был раньше
print(geo_2 < geo_3) # Катархей не раньше Катархея - False
print(geo_2 < geo_1) # Катархей раньше Голоцена - True
print()
print('7 - gt - какой период был позже') # Какой период был позже
print(geo_2 > geo_3) # Катархей не позже Катархея - False
print(geo_2 > geo_1) # Катархей не позже Голоцена - False
print(geo_1 > geo_2) # Голоцен позже Катархея - True
print()
print('8 - le - какой период был раньше') # Какой период был раньше
print(geo_2 <= geo_3)  # Катархей <= Катархей - True
print(geo_2 <= geo_1)  # Катархей <= Голоцен - True
print(geo_1 <= geo_2)  # Голоцен <= Катархей - False
print()
print('9 - ge - какой период был позже') # Какой период был позже
print(geo_2 >= geo_3) # Катархей >= Катархей - True
print(geo_2 >= geo_1) # Катархей >= Голоцен - False
print(geo_1 >= geo_2) # Голоцен >= Катархей - True
print()
print('10 - + - складываются длины периодов') # складываются длины периодов
print(f'Длительность периода {geo_2.return_eon()} и {geo_3.return_eon()} равна {geo_2 + geo_3}')
print(f'Длительность периода {geo_2.return_eon()} и {geo_1.return_eon()} равна {geo_2 + geo_1}')
print()