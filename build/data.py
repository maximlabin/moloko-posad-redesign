# Контент, собранный с moloko-posad.ru (октябрь 2026)

# Картинки берутся с боевого сайта. Для выкладки на сервер поменяйте на "/".
IMG = "https://moloko-posad.ru/"

SITE = {
    "name": "Фёдоровские молочные продукты",
    "legal": "ООО «Фёдоровские молочные продукты»",
    "phone": "+7 (499) 110-01-04",
    "phone_href": "tel:+74991100104",
    "email": "info@moloko-posad.ru",
    "hours": "Пн–Вс: 10:00–19:00",
    "address": "141352, Московская область, Сергиево-Посадский район, д. Репихово, д. 126",
    "address_full": "141352, Московская область, Сергиево-Посадский район, д. Репихово, д. 126, комната 9, этаж 1",
    "ogrn": "1225000022378",
    "inn_kpp": "5042158574 / 504201001",
    "map": "https://yandex.ru/map-widget/v1/-/CCUJ4NxO9A",
    "logo": IMG + "img/logo.png",
}

CATEGORIES = [
    {"slug": "moloko", "name": "Молоко", "img": IMG + "img/cat-1.jpg",
     "text": "Цельное пастеризованное и сырое молоко с наших ферм"},
    {"slug": "kefir", "name": "Кисломолочные продукты", "img": IMG + "img/cat-2.jpg",
     "text": "Кефир, ряженка и йогурты — классический и с фруктами"},
    {"slug": "smetana", "name": "Сметана", "img": IMG + "img/cat-3.jpg",
     "text": "Густая натуральная сметана жирностью 30–40%"},
    {"slug": "tvorog", "name": "Творог", "img": IMG + "img/cat-4.jpg",
     "text": "Творог 9–12% и нежная творожная масса с изюмом"},
    {"slug": "maslo", "name": "Масло", "img": IMG + "img/cat-7.jpg",
     "text": "Сливочное масло из нашего молока — уточняйте наличие"},
    {"slug": "tvorozhnye-deserty", "name": "Творожные десерты", "img": IMG + "img/cat-8.jpg",
     "text": "Ваниль, манго, черника, яблоко с корицей, панна котта и другие"},
]


def _p(cat, slug, name, price, photo, fat, volume):
    return {"cat": cat, "slug": slug, "name": name, "price": price,
            "img": IMG + (photo if "/" in photo else f"assets/images/products/{photo}.jpg"),
            "fat": fat, "volume": volume}


# price=None — на сайте цена не указана
PRODUCTS = [
    _p("moloko", "moloko-celnoe-zhivoe", "Молоко цельное сырое (жирность 3,5–6%)", 150, "img/cat-1.jpg", "3,5–6%", "3 л"),
    _p("moloko", "moloko-celnoe-pasterizovannoe", "Молоко цельное пастеризованное (жирность 3,4–4,0%)", 110, "photo6", "3,4–4,0%", "1 л"),
    _p("kefir", "kefir1", "Кефир", 70, "photo5", "3,5–6%", "1 л"),
    _p("kefir", "ryazhenka", "Ряженка", 60, "photo65", "3,5–6%", "0,5 л"),
    _p("kefir", "jogurt-klassicheskij", "Йогурт классический", None, "photo3", "4%", "0,5 л"),
    _p("kefir", "jogurt-klubnika", "Йогурт (клубника)", None, "photo8", "4%", "0,5 л"),
    _p("kefir", "jogurt-chernika", "Йогурт (черника)", None, "photo7", "4%", "0,5 л"),
    _p("kefir", "jogurt-mango", "Йогурт (манго)", None, "photo3", "4%", "0,5 л"),
    _p("kefir", "jogurt-abrikos", "Йогурт (абрикос)", None, "photo3", "4%", "0,5 л"),
    _p("kefir", "jogurt-vishnya", "Йогурт (вишня)", None, "photo8", "4%", "0,5 л"),
    _p("smetana", "smetana1", "Сметана", None, "photo29", "30–40%", "0,2 л"),
    _p("tvorog", "tvorog1", "Творог", None, "photo11", "9–12%", "0,5 л"),
    _p("tvorog", "tvorozhnaya-massa-s-izyumom", "Творожная масса с изюмом", None, "photo48", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-natur.-grecheskij", "Творожный десерт (натур. греческий)", 100, "photo27", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "slivochnyj-desert-panna-kotta", "Сливочный десерт (панна котта)", None, "photo22", "15%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-oreh-shokolad", "Творожный десерт (орех шоколад)", None, "photo31", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-abrikos", "Творожный десерт (абрикос)", None, "photo34", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-chernika", "Творожный десерт (черника)", None, "photo52", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-klubnika", "Творожный десерт (клубника)", None, "photo44", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-yabloko-korica", "Творожный десерт (яблоко корица)", None, "photo58", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-mango", "Творожный десерт (манго)", None, "photo38", "10%", "0,25 л"),
    _p("tvorozhnye-deserty", "tvorozhnyj-desert-vanil", "Творожный десерт (ваниль)", None, "photo34", "10%", "0,25 л"),
]

# «Популярные товары» с главной исходного сайта
POPULAR = ["tvorozhnyj-desert-natur.-grecheskij", "jogurt-mango", "tvorozhnyj-desert-yabloko-korica", "jogurt-chernika"]

STORES = [
    ("Фирменный магазин", "г. Москва, ул. Тайнинская, д. 9"),
    ("Фирменный магазин", "г. Москва, Ярославское ш., д. 2, к. 2"),
    ("Фирменный магазин", "Моск. обл., Сергиево-Посадский г.о., дер. Митино, 27, стр. 1"),
    ("Фирменный магазин", "Моск. обл., Сергиево-Посадский г.о., дер. Федоровское, стр. 65"),
    ("Фирменный магазин", "Моск. обл., г. Сергиев Посад, ул. 1-й Ударной Армии, д. 12, ТЦ «Торговые ряды», молочный павильон, место 10Ж"),
]
FARMS = [
    ("МТФ Федоровское", "Моск. обл., Сергиево-Посадский г.о., д. Федоровское, стр. 65"),
    ("МТФ Митино", "Моск. обл., Сергиево-Посадский г.о., д. Митино, 27, стр. 1"),
]
PRODUCTION = [("Производство", "Моск. обл., Сергиево-Посадский г.о., д. Гальнево, д. 60, стр. 1, помещ. 9")]

ANNOUNCE = [
    "100% натуральные продукты — без консервантов и стабилизаторов",
    "Свежее молоко с собственных ферм Сергиево-Посадского района",
    "Звоните каждый день с 10:00 до 19:00 — +7 (499) 110-01-04",
]
