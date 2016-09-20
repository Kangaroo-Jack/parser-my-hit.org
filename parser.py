from grab import Grab
g = Grab(log_file='out.html')
g.go("https://my-hit.org/film/ah/")

site = [
    "https://my-hit.org/film/av/",
    "https://my-hit.org/film/ab/",
    "https://my-hit.org/film/az/",
    "https://my-hit.org/film/at/",
    "https://my-hit.org/film/aj/",
    "https://my-hit.org/film/a2/",
    "https://my-hit.org/film/ag/",
    "https://my-hit.org/film/ad/",
    "https://my-hit.org/film/aq/",
    "https://my-hit.org/film/af/",
    "https://my-hit.org/film/a6/",
    "https://my-hit.org/film/al/",
    "https://my-hit.org/film/ak/",
    "https://my-hit.org/film/a8/",
    "https://my-hit.org/film/a9/",
    "https://my-hit.org/film/ac/",
    "https://my-hit.org/film/a1/",
    "https://my-hit.org/film/a1b/",
    "https://my-hit.org/film/a2k/",
    "https://my-hit.org/film/a18/",
    "https://my-hit.org/film/a3/",
    "https://my-hit.org/film/ap/",
    "https://my-hit.org/film/ai/",
    "https://my-hit.org/film/ah/",
    "https://my-hit.org/film/aa/",
    "https://my-hit.org/film/a7/"
    ]

rusName = [
    "Биография",
    "Боевик",
    "Вестерн",
    "Военный",
    "Детектив",
    "Детский",
    "Документальный",
    "Драма",
    "Исторический",
    "Комедия",
    "Криминал",
    "Мелодрама",
    "Мистика",
    "Музыка",
    "Мультфильм",
    "Мюзикл",
    "Приключения",
    "Психологический",
    "Разное",
    "Романтический",
    "Семейный",
    "Спорт",
    "Триллер",
    "Ужасы",
    "Фантастика",
    "Фэнтези"
        ]

"""
Полчения всей информации о фильме
"""
mPages = []
counter_for_pages_what_pars = 0

"""

"""
def parsing_link(link):
    mName = []  # Название фильма
    mCountry = []  # Страна производитель
    mGenre = []  # Жанр фильма
    mYear = []  # Год выпуска
    mRating = []  # Рейтинг фильма
    mQuality = []  # Качество
    mDescription = []  # Описание
    g.go(link)
    for i in range(1, 25):
        try:
            mName.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/b/a")))  # вытаскиваем Название фильма
        except:
            mName.append(str("NULL"))
            print("Ошибка нахождения имени")
        try:
            mCountry.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/ul/li[3]/a")))  # вытаскиваем страну
        except:
            mCountry.append(str("NULL"))
            print("Ошибка нахождения страны")
        try:
            mGenre.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/ul/li[1]")[6:])) # вытаскиваем жанры
        except:
            mGenre.append(str("NULL"))
            print("Ошибка нахождения жанра")
        try:
            mYear.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/ul/li[2]/a")))  # вытаскиваем год
        except:
            mYear.append(str("NULL"))
            print("Ошибка нахождения года")
        try:
            mRating.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/span/ul/li[1]/span"))) # вытаскиваем рейтинг
        except:
            mRating.append(str("NULL"))
            print("Ошибка нахождения рейтинга")
        try:
            mQuality.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/span/ul/li[2]")[10:])) # вытаскиваем качество
        except:
            mQuality.append(str("NULL"))
            print("Ошибка нахождения качества")
        try:
            mDescription.append(str(g.xpath_text("/html/body/div[3]/div/div[2]/div[3]/div[" + str(i) + "]/div[2]/ul/li[5]")))  # вытаскиваем описание
        except :
            mDescription.append(str("NULL"))
            print("Ошибка нахождения описания")

    return mName, mCountry, mGenre, mYear, mRating, mQuality, mDescription



def write_massiv_of_films_to_xml(link, pages):
    mName, mCountry, mGenre, mYear, mRating, mQuality, mDescription = parsing_link(link)
    file = open('parser.xml', 'a', encoding='utf-8')
    for iName, iCountry, iGenre, iYear, iRating, iQuality, iDescription in zip(mName, mCountry, mGenre, mYear, mRating, mQuality, mDescription):
        file.write('<record>')
        file.write('<FilmName>' + str(iName) + '</FilmName>')
        file.write('<Quality>' + str(iQuality) + '</Quality>')
        file.write('<Genre>' + str(iGenre) + '</Genre>')
        file.write('<Rating>' + str(iRating) + '</Rating>')
        file.write('<Year>' + str(iYear) + '</Year>')
        file.write('<Country>' + str(iCountry) + '</Country>')
        file.write('<About>' + str(iDescription) + '</About>')
        file.write('</record>' + '\n')
        file.flush()
    return print("Good " + str(pages))


def count_pages(link):
    g.go(link)
    numbers = -1
    cPage = str(g.xpath_text('/html/body/div[3]/div/div[2]/div[4]/div[1]'))
    for i in cPage[9:]:
        numbers += 1
        if " " == i:
            return round(int(cPage[9:9+numbers])/24)


def type_of_film_for_user():
    persent = -4
    for isite in site:
        persent += 4
        mPages.append(count_pages(isite))
        print("Загрузились на " + str(persent) + "%")

    for number, filmname, cPages in zip(range(1, 27), rusName, mPages):
        print(str(number) + str(". ") + str(filmname) + str(" страниц: ") + str(cPages))


def ask_user():
    type_of_film_for_user()
    number = -1
    pages = 10000000
    while (number not in range(1, 27)):
        print("\nУкажите число (от 1 - 26) которое соответсвует жанру фильма который нужно парсить:\n")
        try:
            number = int(input())
        except ValueError:
            print("Это не число!")

    print("\nУкажите число страниц которое входит в диапазон:\n")
    while (pages not in range(1, int(mPages[int(number-1)]))):
        print("Максимально количество страниц для выбраного жанра Количество страниц " + str (mPages[int(number-1)]))
        try:
            pages = int(input())
        except ValueError:
            print("Это не число!")
    return number, pages

def start_parsing(nfilm, nPages):
    for pages in range(1, int(nPages)+1):
        write_massiv_of_films_to_xml(str(site[nfilm - 1]) + str("?p=" + str(pages)), pages)


def main_for_write_to_file():
    file = open('parser.xml', 'w', encoding='utf-8')
    file.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + '\n')
    file.write('<data-set xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' + '\n')
    file.flush()

    numbers, pages = ask_user()
    start_parsing(numbers, pages)
    file = open('parser.xml', 'a', encoding='utf-8')
    file.write('</data-set>')
    file.close()
    file = open('parser.xml', 'r', encoding='utf-8')
    y = file.read().replace('&', '')
    file = open('parser.xml', 'w', encoding='utf-8')
    file.write(y)
    file.close()
    return print("Парсинг удался =)")

main_for_write_to_file()