# LIGHT:
#
# Реализовать собственный класс с использованием магических методов
# (не менее 5ти). Например, можно использовать класс из вебинара Point2D.
#
# PRO:
#
# Реализовать собственный класс с использованием магических методов
# (не менее 10ти). Можно использовать собственный класс из вебинара 10
import datetime
import random

class Geologic_time_scale: # определяет, какой геологический период был n лет назад

    def __init__(self, year): # аргумент - year лет назад
        self.d = datetime.date.today()
        self.year = year
        self.year_ago = self.d.year - year # отнимает от сегодняшнего года year (количество лет назад), что позволяет попасть в конкртеный период (2020 - 2 года = 2018)

    def __str__(self): # возвращает описание периода
        return self.eon()

    # def __add__(self, other): # складывает продолжительность периодов
    #     return self.year_ago + other.year_ago

    def __len__(self): # Выдает продолжительность периода, испольщуя написанную функцию с длинами периодов len_eon()
        return self.len_eon()

    def __getitem__(self, key): # возвращает по ключу название периода
        self.list_eon = ['Катархей', 'Эоархей', 'Палеоархей', 'Мезоархей', 'Неоархей', 'Сидерий','Рясий', 'Орозорий','Статерий', 'Калимий', 'Эктазий', 'Стений', 'Тоний', 'Криогений', 'Эдиакарий', 'Кэмбрийский', 'Ордовикский', 'Силурийский', 'Девонский', 'Каменноугольный', 'Пермский', 'Триасовый', 'Юрский', 'Меловой', 'Палеоцен', 'Эоцен', 'Олигоцен', 'Миоцен', 'Плиоцен', 'Плейстоцен', 'Голоцен', 'Антропоцен']
        return self.list_eon[key]

    def __eq__(self, other): # = - относятся ли даты к одному и тому же периоду
        if self.return_eon() == other.return_eon():
            return True
        else:
            return False

    def __ne__(self, other): # относятся ли даты к разным периодам
        if self.return_eon() != other.return_eon():
            return True
        else:
            return False

    def __lt__(self, other): #< какой период был раньше
        a1 = self.return_eon()
        a2 = other.return_eon()
        if self.list_eon.index(a1) < self.list_eon.index(a2): # определяет по индкесу списка - какой период в списке встречается раньше
            return True
        else:
            return False

    def __gt__(self, other): #> какой период был позже
        a1 = self.return_eon()
        a2 = other.return_eon()
        if self.list_eon.index(a1) > self.list_eon.index(a2): # определяет по индкесу списка - какой период в списке встречается позже
            return True
        else:
            return False

    def __le__(self, other): #<= какой период был раньше или это могут быть одинаковые периоды
        a1 = self.return_eon()
        a2 = other.return_eon()
        if self.list_eon.index(a1) <= self.list_eon.index(a2):
            return True
        else:
            return False

    def __ge__(self, other): #>= какой период был позже или это могут быть одинаковые периоды
        a1 = self.return_eon()
        a2 = other.return_eon()
        if self.list_eon.index(a1) >= self.list_eon.index(a2):
            return True
        else:
            return False

    def __add__(self, other): # + складывает длительности периодов
        return len(self) + len(other)

    def __getstate__(self): # pickle - сохраняет в файл
        return self.eon()

    def __setstate__(self, state): # pickle - должен открывать файл - ВЫДАЕТ ОШИБКУ
        a = self.eon()
        a = state

    def round_year(self, n): # заменяет нули на "млрд", "млн", "тысяч"
        self.n = n
        self.n_str = str(self.n)
        if len(self.n_str) == 10:
            return self.n//10**9, 'млрд лет'
        if len(self.n_str) == 9:
            return self.n//10**6, 'млн лет'
        if len(self.n_str) == 8:
            return self.n//10**6, 'млн лет'
        if len(self.n_str) == 7:
            return self.n//10**6, 'млн лет'
        if len(self.n_str) == 6:
            return self.n//10**3, 'тысяч лет'
        if len(self.n_str) == 5:
            return self.n//10**3, 'тысяч лет'
        if len(self.n_str) == 4:
            return self.n//10**3, 'тысяч лет'


    def eon(self): # Описывает период. Источник: ru.wikipedia.org/wiki/Геохронологическая_шкала
        # Суперэон - Докембрий
        if self.year_ago >= (self.d.year - 4600000000) and self.year_ago <= (self.d.year - 541000000):
            # Эон - Катархей
            if self.year_ago >= (self.d.year - 4600000000) and (self.year_ago < self.d.year - 4000000000):
                print(f'Что было {self.year} лет назад', self.round_year(self.year))
                print('Эон: Докэмбрий - Катархей. \nОписание: ~4,6 млрд лет назад — формирование Земли.')
                return 'Катархей'
            # Эон Докембрий - Архей
            elif self.year_ago >= (self.d.year - 4000000000) and (self.year_ago < self.d.year - 2500000000):
                # Эра Докембрий - Архей - Эоархей
                if self.year_ago >= (self.d.year - 4000000000) and (self.year_ago < self.d.year - 3600000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print('Эон: Докэмбрий - Архей. \nЭра: Эоархей. \nОписание: Образование гидросферы. Появление примитивных одноклеточных организмов (образовавших строматолиты)')
                    return 'Эоархей'
                # Эра Докембрий - Архей - Палеоархей
                elif self.year_ago >= (self.d.year - 3600000000) and (self.year_ago < self.d.year - 3200000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print('Эон: Докэмбрий - Архей. \nЭра: Палеоархей. \nОписание: Завершилось формирование твердого ядра Земли. Формирование первого суперконтинента — Ваальбара')
                    return 'Палеоархей'
                # Эра Докембрий - Архей - Мезоархей
                elif self.year_ago >= (self.d.year - 3200000000) and (self.year_ago < self.d.year - 2800000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print('Эон: Докэмбрий - Архей. \nЭра: Мезоархей. \nОписание: Раскол суперконтинента Ваальбары')
                    return 'Мезоархей'
                # Эра Докембрий - Архей - Неоархей
                elif self.year_ago >= (self.d.year - 2800000000) and (self.year_ago < self.d.year - 2500000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print('Эон: Докэмбрий - Архей. \nЭра: Неоархей. \nОписание: Формирование настоящей континентальной земной коры. Появление кислородного фотосинтеза.')
                    return 'Неоархей'
            # Эон - Докембрий - Протерозой
            elif self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 541000000):
                # Эра - Докембрий - Протерозой - Палеопротерозой
                if self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 1600000000):
                    #return 'Докэмбрий - Протерозой - Палеопротерозой'
                    # Период Докембрий - Протерозой - Палеопротерозой - Сидерий
                    if self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 2300000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докэмбрий - Протерозой. \nЭра: Палеопротерозой. \nПериод: Сидерий. \nОписание: Пик проявления полосчатых железистых кварцитов. Кислородная катастрофа. Начало гуронского оледенения')
                        return 'Сидерий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Рясий
                    elif self.year_ago >= (self.d.year - 2300000000) and (self.year_ago < self.d.year - 2050000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докэмбрий - Протерозой. \nЭра: Палеопротерозой. \nПериод: Рясий. \nЗавершается гуронское оледенение. Появляются предпосылки появления ядра у организмов.')
                        return 'Рясий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Орозирий
                    elif self.year_ago >= (self.d.year - 2050000000) and (self.year_ago < self.d.year - 1800000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докэмбрий - Протерозой. \nЭра: Палеопротерозой. Период: Орозирий. Описание: Интенсивное горообразование. Вероятно, атмосфера Земли стала окислительной (богатой кислородом)')
                        return 'Орозорий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Статерий
                    elif self.year_ago >= (self.d.year - 1800000000) and (self.year_ago < self.d.year - 1600000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докэмбрий - Протерозой. \nЭра: Палеопротерозой. \nПериод: Статерий. \nОписание: Сформировались ядерные живые организмы. Формируется суперконтинент Колумбия.')
                        return 'Статерий'
                # Докембрий - Протерозой - Мезопротерозой
                if self.year_ago >= (self.d.year - 1600000000) and (self.year_ago < self.d.year - 1000000000):
                    # Период Докембрий - Протерозой - Мезопротерозой - Калимий
                    if self.year_ago >= (self.d.year - 1600000000) and (self.year_ago < self.d.year - 1400000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Мезопротерозой. \nПериод: Калимий. \nОписание: Раскол Колумбии')
                        return 'Калимий'
                    # Период Докембрий - Протерозой - Мезопротерозой - Эктазий
                    elif self.year_ago >= (self.d.year - 1400000000) and (self.year_ago < self.d.year - 1200000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Мезопротерозой. \nПериод: Эктазий. \nОписание: Первые многоклеточные растения (красные водоросли)')
                        return 'Эктазий'
                    # Период Докембрий - Протерозой - Мезопротерозой - Стений
                    elif self.year_ago >= (self.d.year - 1200000000) and (self.year_ago < self.d.year - 1000000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Мезопротерозой. \nПериод: Стений. \nОписание: Суперконтинент Родиния, суперокеан Мировия')
                        return 'Стений'
                # Докембрий - Протерозой - Непротерозой
                if self.year_ago >= (self.d.year - 1000000000) and (self.year_ago < self.d.year - 541000000):
                    # Период Докембрий - Протерозой - Неопротерозой - Тоний
                    if self.year_ago >= (self.d.year - 1000000000) and (self.year_ago < self.d.year - 720000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Неопротерозой. \nПериод: Тоний. \nОписание: Начало распада суперконтинента Родиния. Хайнаньская биота')
                        return 'Тоний'
                    # Докембрий - Протерозой - Неопротерозой - Криогений
                    if self.year_ago >= (self.d.year - 720000000) and (self.year_ago < self.d.year - 635000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Неопротерозой. \nПериод: Криогений. \nОписание: Одно из самых масштабных оледенений Земли. Начал формироваться суперконтинент Паннотия')
                        return 'Криогений'
                    # Докембрий - Протерозой - Неопротерозой - Эдиакарий
                    if self.year_ago >= (self.d.year - 636000000) and (self.year_ago < self.d.year - 541000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Докембрий - Протерозой. \nЭра: Неопротерозой. \nПериод: Эдиакарий. \nОписание: Многоклеточные животные — вендобионты и фауна Доушаньто. Разделение Паннотии на континент Гондвана и мини-континенты Балтики, Сибири и Лавразии')
                        return 'Эдиакарий'
        # Эон - Фанерозой
        elif self.year_ago >= (self.d.year - 541000000) and (self.year >=0):
            # Эра Палеозой
            if self.year_ago >= (self.d.year - 541000000) and (self.year_ago < self.d.year - 252170000):
                # Период Кэмбрийский
                if self.year_ago >= (self.d.year - 541000000) and (self.year_ago < self.d.year - 485400000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Кэмбрийский. \nДлился: {541000000 - 48540000} лет. \nОписание: Появление большого количества новых групп организмов («Кембрийский взрыв»).')
                    return 'Кэмбрийский'
                # Период Ордовикский
                elif self.year_ago >= (self.d.year - 485400000) and (self.year_ago < self.d.year - 443800000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Ордовикский. \nДлился: {485400000 - 443800000} лет. \nОписание: Ракоскорпионы, первые сосудистые растения.' )
                    return 'Ордовикский'
                # Период Силурийский
                elif self.year_ago >= (self.d.year - 443800000) and (self.year_ago < self.d.year - 419200000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Силурийский. \nДлился: {443800000 - 419200000} лет. \nОписание: Ордовикско-силурийское вымирание. Выход жизни на сушу: скорпионы; появление челюстноротых.' )
                    return 'Силурийский'
                # Период Девонский
                elif self.year_ago >= (self.d.year - 419200000) and (self.year_ago < self.d.year - 358900000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Девонский. \nДлился: {419200000 - 358900000} лет. \nОписание: Появление земноводных и споровых растений. Начало формирования уральских гор.' )
                    return 'Девонский'
                # Период Каменноугольный
                elif self.year_ago >= (self.d.year - 358900000) and (self.year_ago < self.d.year - 298900000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Каменноугольный. \nДлился: {358900000 - 298900000} лет. \nОписание: Появление деревьев и пресмыкающихся.')
                    return 'Каменноугольный'
                # Период Пермский
                elif self.year_ago >= (self.d.year - 298900000) and (self.year_ago < self.d.year - 252170000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Палеозой. \nПериод: Пермский. \nДлился: {298900000 - 252170000} лет. \nОписание: Вымерло около 95 % всех существовавших видов (Массовое пермское вымирание). Закончилось формирование Гондваны, столкнулись два континента, в результате которого образовались Пангея и Аппалачские горы. Океан Панталасса.')
                    return 'Пермский'

            # Эра Мезозой
            elif self.year_ago >= (self.d.year - 252170000) and (self.year_ago < self.d.year - 66000000):
                # Триасовый
                if self.year_ago >= (self.d.year - 252170000) and (self.year_ago < self.d.year - 201300000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Мезозой. \nПериод: Триасовый. \nДлился: {252170000 - 201300000} лет. \nОписание: Первые динозавры и яйцекладущие млекопитающие.')
                    return 'Триасовый'
                # Юрский
                elif self.year_ago >= (self.d.year - 201300000) and (self.year_ago < self.d.year - 145000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Мезозой. \nПериод: Юрский. \nДлился: {201300000 - 145000000} лет. \nОписание: Появление сумчатых млекопитающих и первых птиц. Расцвет динозавров.')
                    return 'Юрский'
                # Меловой
                elif self.year_ago >= (self.d.year - 145000000) and (self.year_ago < self.d.year - 66000000):
                    print(f'Что было {self.year} лет назад', self.round_year(self.year))
                    print(f'Эон: Фанерозой. \nЭра: Мезозой. \nПериод: Меловой. \nДлился: {145000000 - 66000000} лет. \nОписание: Первые плацентарные млекопитающие. Вымирание динозавров.')
                    return 'Меловой'
            # Эра Кайонозой
            elif self.year_ago >= (self.d.year - 66000000) and (self.year >=0): #(self.year_ago <= self.d.year):
                # Палеогеновый
                if self.year_ago >= (self.d.year - 66000000) and (self.year_ago < self.d.year - 23030000):
                    # Палеоцен
                    if self.year_ago >= (self.d.year - 66000000) and (self.year_ago < self.d.year - 56000000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Палеогеновый. \nЭпоха: Палеоцен. \nДлилась: {66000000 - 56000000} лет. \nОписание: Выделение из парнокопытных предков древних китов. В позднем палеоцене от кондилартр произошли непарнокопытные.')
                        return 'Палеоцен'
                    # Эоцен
                    elif self.year_ago >= (self.d.year - 56000000) and (self.year_ago < self.d.year - 33900000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Палеогеновый. \nЭпоха: Эоцен. \nДлилась: {56000000 - 33900000} лет. \nОписание: Появление первых «современных» млекопитающих.')
                        return 'Эоцен'
                    # Олигоцен
                    elif self.year_ago >= (self.d.year - 33900000) and (self.year_ago < self.d.year - 23030000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Палеогеновый. \nЭпоха: Олигоцен. \nДлилась: {33900000 - 23030000} лет. \nОписание: Появление первых человекообразных обезьян.')
                        return 'Олигоцен'
                # Неогеновый
                elif self.year_ago >= (self.d.year - 23030000) and (self.year_ago < self.d.year - 2588000):
                    # Миоцен
                    if self.year_ago >= (self.d.year - 23030000) and (self.year_ago < self.d.year - 5333000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print('Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Неогеновый. \nЭпоха: Миоцен. \nДлилась: {23030000 - 5333000} лет. \nОписание: В конце миоцена произошло несколько циклов частичного или практически полного высыхания Средиземного моря.')
                        return 'Миоцен'
                    # Плиоцен
                    elif self.year_ago >= (self.d.year - 5333000) and (self.year_ago < self.d.year - 2588000):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Неогеновый. \nЭпоха: Плиоцен. \nДлилась: {5333000 - 2588000} лет. \nОписание: Появились и скорее всего вымерли родственные человеку австралопитеки. Появились первые люди (род Homo).')
                        return 'Плиоцен'
                # Четвертичный
                elif self.year_ago >= (self.d.year - 2588000) and (self.year >=0):
                    # Плейстоцен
                    if self.year_ago >= (self.d.year - 2588000) and (self.year_ago < self.d.year - 11700):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Четвертичынй. \nЭпоха: Плейстоцен. \nДлилась: {2588000 - 11700} лет. \nОписание: Вымирание многих крупных млекопитающих. Появление современного человека.')
                        return 'Плейстоцен'
                    # Голоцен
                    elif self.year_ago >= (self.d.year - 11700) and (self.year_ago < self.d.year - 70):
                        print(f'Что было {self.year} лет назад')
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Четвертичынй. \nЭпоха: Голоцен. \nДлилась: {11700 - 70} лет. \nОписание: Конец последнего ледникового периода. Возникновение цивилизаций.')
                        return 'Голоцен'
                    # Антропоцен
                    elif self.year_ago >= (self.d.year - 70) and (self.year_ago >= 0):
                        print(f'Что было {self.year} лет назад', self.round_year(self.year))
                        print(f'Эон: Фанерозой. \nЭра: Кайнозой. \nПериод: Четвертичынй. \nЭпоха: Антропоцен. \nДлится: {70} лет. \nОписание: Уровень человеческой активности играет существенную роль в экосистеме Земли.')
                        return 'Антропоцен'

    def return_eon(self): # возвращает период без описания (без print('xxx'))
        # Суперэон - Докембрий
        if self.year_ago >= (self.d.year - 4600000000) and self.year_ago <= (self.d.year - 541000000):
            # Эон - Катархей
            if self.year_ago >= (self.d.year - 4600000000) and (self.year_ago < self.d.year - 4000000000):
                return 'Катархей'
            # Эон Докембрий - Архей
            elif self.year_ago >= (self.d.year - 4000000000) and (self.year_ago < self.d.year - 2500000000):
                # Эра Докембрий - Архей - Эоархей
                if self.year_ago >= (self.d.year - 4000000000) and (self.year_ago < self.d.year - 3600000000):
                    return 'Эоархей'
                # Эра Докембрий - Архей - Палеоархей
                elif self.year_ago >= (self.d.year - 3600000000) and (self.year_ago < self.d.year - 3200000000):
                    return 'Палеоархей'
                # Эра Докембрий - Архей - Мезоархей
                elif self.year_ago >= (self.d.year - 3200000000) and (self.year_ago < self.d.year - 2800000000):
                    return 'Мезоархей'
                # Эра Докембрий - Архей - Неоархей
                elif self.year_ago >= (self.d.year - 2800000000) and (self.year_ago < self.d.year - 2500000000):
                    return 'Неоархей'
            # Эон - Докембрий - Протерозой
            elif self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 541000000):
                # Эра - Докембрий - Протерозой - Палеопротерозой
                if self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 1600000000):
                    # return 'Докэмбрий - Протерозой - Палеопротерозой'
                    # Период Докембрий - Протерозой - Палеопротерозой - Сидерий
                    if self.year_ago >= (self.d.year - 2500000000) and (self.year_ago < self.d.year - 2300000000):
                        return 'Сидерий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Рясий
                    elif self.year_ago >= (self.d.year - 2300000000) and (self.year_ago < self.d.year - 2050000000):
                        return 'Рясий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Орозирий
                    elif self.year_ago >= (self.d.year - 2050000000) and (self.year_ago < self.d.year - 1800000000):
                        return 'Орозорий'
                    # Период Докембрий - Протерозой - Палеопротерозой - Статерий
                    elif self.year_ago >= (self.d.year - 1800000000) and (self.year_ago < self.d.year - 1600000000):
                        return 'Статерий'
                # Докембрий - Протерозой - Мезопротерозой
                if self.year_ago >= (self.d.year - 1600000000) and (self.year_ago < self.d.year - 1000000000):
                    # Период Докембрий - Протерозой - Мезопротерозой - Калимий
                    if self.year_ago >= (self.d.year - 1600000000) and (self.year_ago < self.d.year - 1400000000):
                        return 'Калимий'
                    # Период Докембрий - Протерозой - Мезопротерозой - Эктазий
                    elif self.year_ago >= (self.d.year - 1400000000) and (self.year_ago < self.d.year - 1200000000):
                        return 'Эктазий'
                    # Период Докембрий - Протерозой - Мезопротерозой - Стений
                    elif self.year_ago >= (self.d.year - 1200000000) and (self.year_ago < self.d.year - 1000000000):
                        return 'Стений'
                # Докембрий - Протерозой - Непротерозой
                if self.year_ago >= (self.d.year - 1000000000) and (self.year_ago < self.d.year - 541000000):
                    # Период Докембрий - Протерозой - Неопротерозой - Тоний
                    if self.year_ago >= (self.d.year - 1000000000) and (self.year_ago < self.d.year - 720000000):
                        return 'Тоний'
                    # Докембрий - Протерозой - Неопротерозой - Криогений
                    if self.year_ago >= (self.d.year - 720000000) and (self.year_ago < self.d.year - 635000000):
                        return 'Криогений'
                    # Докембрий - Протерозой - Неопротерозой - Эдиакарий
                    if self.year_ago >= (self.d.year - 636000000) and (self.year_ago < self.d.year - 541000000):
                        return 'Эдиакарий'
        # Эон - Фанерозой
        elif self.year_ago >= (self.d.year - 541000000) and (self.year >= 0):
            # Эра Палеозой
            if self.year_ago >= (self.d.year - 541000000) and (self.year_ago < self.d.year - 252170000):
                # Период Кэмбрийский
                if self.year_ago >= (self.d.year - 541000000) and (self.year_ago < self.d.year - 485400000):

                    return 'Кэмбрийский'
                # Период Ордовикский
                elif self.year_ago >= (self.d.year - 485400000) and (self.year_ago < self.d.year - 443800000):

                    return 'Ордовикский'
                # Период Силурийский
                elif self.year_ago >= (self.d.year - 443800000) and (self.year_ago < self.d.year - 419200000):

                    return 'Силурийский'
                # Период Девонский
                elif self.year_ago >= (self.d.year - 419200000) and (self.year_ago < self.d.year - 358900000):
                    return 'Девонский'
                # Период Каменноугольный
                elif self.year_ago >= (self.d.year - 358900000) and (self.year_ago < self.d.year - 298900000):
                    return 'Каменноугольный'
                # Период Пермский
                elif self.year_ago >= (self.d.year - 298900000) and (self.year_ago < self.d.year - 252170000):
                    return 'Пермский'

            # Эра Мезозой
            elif self.year_ago >= (self.d.year - 252170000) and (self.year_ago < self.d.year - 66000000):
                # Триасовый
                if self.year_ago >= (self.d.year - 252170000) and (self.year_ago < self.d.year - 201300000):
                    return 'Триасовый'
                # Юрский
                elif self.year_ago >= (self.d.year - 201300000) and (self.year_ago < self.d.year - 145000000):
                    return 'Юрский'
                # Меловой
                elif self.year_ago >= (self.d.year - 145000000) and (self.year_ago < self.d.year - 66000000):
                    return 'Меловой'
            # Эра Кайонозой
            elif self.year_ago >= (self.d.year - 66000000) and (self.year >= 0):  # (self.year_ago <= self.d.year):
                # Палеогеновый
                if self.year_ago >= (self.d.year - 66000000) and (self.year_ago < self.d.year - 23030000):
                    # Палеоцен
                    if self.year_ago >= (self.d.year - 66000000) and (self.year_ago < self.d.year - 56000000):
                        return 'Палеоцен'
                    # Эоцен
                    elif self.year_ago >= (self.d.year - 56000000) and (self.year_ago < self.d.year - 33900000):
                        return 'Эоцен'
                    # Олигоцен
                    elif self.year_ago >= (self.d.year - 33900000) and (self.year_ago < self.d.year - 23030000):
                        return 'Олигоцен'
                # Неогеновый
                elif self.year_ago >= (self.d.year - 23030000) and (self.year_ago < self.d.year - 2588000):
                    # Миоцен
                    if self.year_ago >= (self.d.year - 23030000) and (self.year_ago < self.d.year - 5333000):
                        return 'Миоцен'
                    # Плиоцен
                    elif self.year_ago >= (self.d.year - 5333000) and (self.year_ago < self.d.year - 2588000):
                        return 'Плиоцен'
                # Четвертичный
                elif self.year_ago >= (self.d.year - 2588000) and (self.year >= 0):
                    # Плейстоцен
                    if self.year_ago >= (self.d.year - 2588000) and (self.year_ago < self.d.year - 11700):
                        return 'Плейстоцен'
                    # Голоцен
                    elif self.year_ago >= (self.d.year - 11700) and (self.year_ago < self.d.year - 70):
                        return 'Голоцен'
                    # Антропоцен
                    elif self.year_ago >= (self.d.year - 70) and (self.year_ago >= 0):
                        return 'Антропоцен'

        else:
            raise ValueError('Нет информации')


    def is_homo(self): # появился ли человек
        if self.year_ago >= (self.d.year - 5333000) and self.year_ago <= self.d.year:
            print('Homo')
            return True
        else:
            print('Homo')
            return False


    def len_eon(self): # считает длину периода
        self.period_name = self.return_eon()
        if self.period_name == 'Катархей':
            len_katarchean = 4600000000 - 541000000
            return len_katarchean#, self.round_year(len_katarchean)
        if self.period_name == 'Эоархей':
            len_eoarchean = 4000000000 - 2500000000
            return len_eoarchean#, self.round_year(len_eoarchean)
        if self.period_name == 'Палеоархей':
            len_paleoarchean = 3600000000 - 3200000000
            return len_paleoarchean#, self.round_year(len_paleoarchean)
        if self.period_name == 'Мезоархей':
            len_mesoarchean = 3200000000 - 2800000000
            return len_mesoarchean
        if self.period_name == 'Неоархей':
            return 2800000000 - 2500000000
        if self.period_name == 'Сидерий':
            return 2500000000 - 2300000000
        if self.period_name == 'Рясий':
            return 2300000000 - 2050000000
        if self.period_name == 'Орозорий':
            return  2050000000 - 1800000000
        if self.period_name == 'Статерий':
            return 1800000000 - 1600000000
        if self.period_name == 'Калимий':
            return 1600000000 - 1400000000
        if self.period_name == 'Эктазий':
            return 1400000000 - 1200000000
        if self.period_name == 'Стений':
            return 1200000000 - 1000000000
        if self.period_name == 'Тоний':
            return 1000000000 - 720000000
        if self.period_name == 'Криогений':
            return 720000000 - 635000000
        if self.period_name == 'Эдиакарий':
            return 636000000 - 541000000
        if self.period_name == 'Кэмбрийский':
            return 541000000 - 485400000
        if self.period_name == 'Ордовикский':
            return 485400000 - 443800000
        if self.period_name == 'Силурийский':
            return 443800000 - 419200000
        if self.period_name == 'Девонский':
            return 419200000 - 358900000
        if self.period_name == 'Каменноугольный':
            return 358900000 - 298900000
        if self.period_name == 'Пермский':
            return 298900000 - 252170000
        if self.period_name == 'Триасовый':
            return 252170000 - 201300000
        if self.period_name == 'Юрский':
            return 201300000 - 145000000
        if self.period_name == 'Меловой':
            return 145000000 - 66000000
        if self.period_name == 'Палеоцен':
            return 66000000 - 56000000
        if self.period_name == 'Эоцен':
            return 56000000 - 33900000
        if self.period_name == 'Олигоцен':
            return 33900000 - 23030000
        if self.period_name == 'Миоцен':
            return 23030000 - 5333000
        if self.period_name == 'Плиоцен':
            return 5333000 - 2588000
        if self.period_name == 'Плейстоцен':
            return 2588000 - 11700
        if self.period_name == 'Голоцен':
            return 11700 - 70
        if self.period_name == 'Антропоцен':
            return 70

if __name__ == '__main__':

    a = random.randint(0, 4600000000)
    b = random.randint(0, 4600000000)
    c = random.randint(0, 4600000000)
    d = random.randint(0, 4600000000)
    e = random.randint(0, 4600000000)
    f = random.randint(0, 4600000000)
    g = random.randint(0, 4600000000)
    h = random.randint(0, 4600000000)
    i = random.randint(0, 4600000000)
    j = random.randint(0, 4600000000)

    a_geo = Geologic_time_scale(a)
    b_geo = Geologic_time_scale(b)
    c_geo = Geologic_time_scale(c)
    d_geo = Geologic_time_scale(d)
    e_geo = Geologic_time_scale(e)
    f_geo = Geologic_time_scale(f)
    g_geo = Geologic_time_scale(g)
    h_geo = Geologic_time_scale(h)
    i_geo = Geologic_time_scale(i)
    j_geo = Geologic_time_scale(j)
    k_geo = Geologic_time_scale(4500000000)
    l_geo = Geologic_time_scale(720000000)
    m_geo = Geologic_time_scale(20000000)
    n_geo = Geologic_time_scale(1000000)
    o_geo = Geologic_time_scale(500000)
    p_geo = Geologic_time_scale(50000)
    q_geo = Geologic_time_scale(5000)


    print(a_geo.eon())
    print()
    print(b_geo.eon())
    print()
    print(c_geo.eon())
    print()
    print(d_geo.eon())
    print()
    print(e_geo.eon())
    print()
    print(f_geo.eon())
    print()
    print(g_geo.eon())
    print()
    print(h_geo.eon())
    print()
    print(i_geo.eon())
    print()
    print(j_geo.eon())
    print()
    print(k_geo.eon())
    print()
    print(l_geo.eon())
    print()
    print(m_geo.eon())
    print()
    print(n_geo.eon())
    print()
    print(o_geo.eon())
    print()
    print(p_geo.eon())
    print()
    print(q_geo.eon())
    print()
    print(q_geo.is_homo())
