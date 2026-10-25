from html import escape as e

from data import CATEGORIES, IMG, POPULAR, PRODUCTS, SITE, STORES
from layout import icon, page, page_head, product_card

HERO = [
    (IMG + "img/03.jpg", "Сергиево-Посадский район · с 1968 года", "Молоко с наших ферм",
     "100% натуральные продукты без химических добавок, консервантов и стабилизаторов."),
    (IMG + "assets/images/slider/slider_2.jpg", "Две собственные фермы", "Современное оборудование",
     "Молочные линии и система очистки молока DeLaval (Швеция) на каждом этапе производства."),
    (IMG + "assets/images/slider/slider_3.jpg", "800 голов голштинской породы", "Заботливое отношение к животным",
     "Строго соблюдаем гигиенические нормы при кормлении и содержании стада."),
]

STATS = [("1968", "поставляем молоко в Сергиево-Посадском районе"), ("800", "голов в дойном стаде"),
         ("2", "собственные молочно-товарные фермы"), ("0", "консервантов и стабилизаторов")]

BENEFITS = [
    (IMG + "img/01.png", "Собственная кормовая база", "Мы сами производим корма для наших животных."),
    (IMG + "img/04.png", "Контроль качества", "Тщательно проверяем продукцию на всех этапах — от фермы до упаковки."),
    (IMG + "img/02.png", "Две молочные фермы", "МТФ Митино и МТФ Федоровское с дойным стадом в 800 голов."),
]


def _count(slug):
    n = sum(1 for p in PRODUCTS if p["cat"] == slug)
    if n == 0:
        return "Скоро в продаже"
    word = "товар" if n % 10 == 1 and n % 100 != 11 else "товара" if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else "товаров"
    return f"{n} {word}"


def stats_section():
    items = "".join(f'<div class="stat reveal"><b>{n}</b><span>{t}</span></div>' for n, t in STATS)
    return f'<div class="stats">{items}</div>'


def dark_section(r, img=IMG + "assets/images/slider/slider_3.jpg"):
    return f'''<section class="dark">
  <div class="wrap dark__grid">
    <div class="dark__text">
      <p class="eyebrow">Собственное производство · с 1968 года</p>
      <h2>Молоко <span class="accent">прямо</span> с наших ферм.</h2>
      <p class="dark__lead">Две молочно-товарные фермы, стадо голштинской породы и своя переработка — от фермы до вашего стола.</p>
      <div class="dark__points"><span>Собственная кормовая база</span><span>Оборудование DeLaval</span><span>Контроль качества</span></div>
      <div class="dark__btns">
        <a class="btn btn--green" href="{r}oplata-i-dostavka.html">Где купить</a>
        <a class="btn btn--ghost-light" href="{r}o-kompanii.html">О компании</a>
      </div>
    </div>
    <div class="dark__media"><img src="{img}" alt="Фермер с телятами на ферме" loading="lazy"></div>
  </div>
</section>'''


def map_section(r):
    stores = "".join(f'<li>{icon("pin", 18)}<span>{e(a)}</span></li>' for _, a in STORES[:3])
    return f'''<section class="section">
  <div class="wrap">
    <div class="map-card reveal">
      <iframe src="{SITE["map"]}" title="Карта: {e(SITE["address"])}" loading="lazy"></iframe>
      <div class="map-card__text">
        <p class="eyebrow">Фирменные магазины</p>
        <h2>Ищете, где купить?</h2>
        <p>Пять фирменных магазинов в Москве и Сергиево-Посадском районе — свежая продукция каждый день.</p>
        <ul class="map-card__list">{stores}</ul>
        <a class="btn btn--dark" href="{r}oplata-i-dostavka.html">Все адреса</a>
      </div>
    </div>
  </div>
</section>'''


def home():
    r = ""
    slides = []
    for i, (img, eyebrow, title, text) in enumerate(HERO):
        tag = "h1" if i == 0 else "h2"
        slides.append(f'''<div class="hero__slide{" is-active" if i == 0 else ""}" aria-roledescription="слайд" aria-label="{i + 1} из {len(HERO)}">
    <img src="{img}" alt="" {"fetchpriority=\"high\"" if i == 0 else "loading=\"lazy\""}>
    <div class="hero__content">
      <p class="eyebrow">{eyebrow}</p>
      <{tag}>{title}</{tag}>
      <p>{text}</p>
      <div class="hero__btns">
        <a class="btn btn--green" href="katalog.html">Смотреть каталог</a>
        <a class="btn btn--ghost-light" href="oplata-i-dostavka.html">Где купить</a>
      </div>
    </div>
  </div>''')
    dots = "".join(f'<button type="button" aria-label="Слайд {i + 1}"{" class=\"is-active\"" if i == 0 else ""}></button>' for i in range(len(HERO)))
    cats = "".join(f'''<a class="feature-card reveal" href="katalog/{c["slug"]}.html">
  <div class="feature-card__img"><img src="{c["img"]}" alt="{e(c["name"])}" loading="lazy"></div>
  <div class="feature-card__body">
    <span class="feature-card__count">{_count(c["slug"])}</span>
    <h3>{e(c["name"])}</h3>
    <p>{e(c["text"])}</p>
    <span class="btn btn--dark btn--sm">Смотреть</span>
  </div>
</a>''' for c in CATEGORIES)
    by_slug = {p["slug"]: p for p in PRODUCTS}
    popular = "".join(product_card(by_slug[s], r) for s in POPULAR)
    benefits = "".join(f'''<div class="benefit reveal"><img src="{img}" alt="" loading="lazy"><div><h3>{t}</h3><p>{d}</p></div></div>''' for img, t, d in BENEFITS)

    body = f'''<section class="hero" aria-roledescription="карусель" aria-label="Главное">
  {"".join(slides)}
  <button class="hero__nav hero__nav--prev" type="button" aria-label="Предыдущий слайд">{icon("left", 24, 2)}</button>
  <button class="hero__nav hero__nav--next" type="button" aria-label="Следующий слайд">{icon("right", 24, 2)}</button>
  <div class="hero__dots">{dots}</div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Наша продукция</h2><p>Всё делаем сами — из молока собственных ферм.</p></div>
    <div class="grid grid--3">{cats}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Популярные товары</h2></div>
    <div class="grid grid--4">{popular}</div>
    <p style="text-align:center;margin-top:36px"><a class="btn btn--ghost" href="katalog.html">Весь каталог</a></p>
  </div>
</section>

{dark_section(r)}

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">ООО «ФМП»</p><h2 style="margin-top:10px">Почему выбирают нас</h2></div>
    {stats_section()}
    <div class="grid grid--3" style="margin-top:20px">{benefits}</div>
  </div>
</section>

{map_section(r)}'''
    return page(None, body, "index.html", r)


def about():
    r = ""
    gallery = "".join(f'<figure class="reveal"><img src="{IMG}assets/images/products/{n}.jpg" alt="Продукция «Фёдоровские молочные продукты»" loading="lazy"></figure>'
                      for n in ["photo6", "photo5", "photo65", "photo2", "photo29", "photo22", "photo31", "photo11"])
    body = f'''{page_head("О компании", [], r, "Производим и поставляем молоко предприятиям и магазинам Сергиево-Посадского района с 1968 года.")}

<section class="section">
  <div class="wrap split">
    <div class="prose reveal">
      <p class="eyebrow">Наша история</p>
      <h2>Две фермы, своё стадо и <span class="accent">честный</span> продукт</h2>
      <p>ООО «ФМП» расположено в Сергиево-Посадском районе Московской области и владеет двумя молочно-товарными фермами — <strong>МТФ Митино</strong> и <strong>МТФ Федоровское</strong>. Дойное стадо — 800 голов голштинской породы, завезённой из Дании в 2017 году.</p>
      <p>При производстве молока, кормлении и содержании животных мы уделяем большое внимание соблюдению всех гигиенических норм и требований. Предприятия оснащены современными молочными линиями и системой очистки молока компании <strong>DeLaval (Швеция)</strong>.</p>
      <p>На собственном перерабатывающем предприятии мы производим 100% натуральные продукты — без химических добавок, консервантов и стабилизаторов.</p>
    </div>
    <div class="split__media reveal"><img src="{IMG}assets/images/slider/slider_2.jpg" alt="Коровы на молочной ферме" loading="lazy"></div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">{stats_section()}</div>
</section>

{dark_section(r, IMG + "img/03.jpg")}

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Наша продукция</h2><p>Молоко, кисломолочные продукты, сметана, творог и десерты.</p></div>
    <div class="gallery">{gallery}</div>
    <p style="text-align:center;margin-top:36px"><a class="btn btn--dark" href="katalog.html">Перейти в каталог</a></p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Реквизиты</h2></div>
    <div class="req reveal">
      <div><span>Организация</span><b>{SITE["legal"]}</b></div>
      <div><span>ОГРН</span><b>{SITE["ogrn"]}</b></div>
      <div><span>ИНН / КПП</span><b>{SITE["inn_kpp"]}</b></div>
      <div style="grid-column:1/-1"><span>Юридический адрес</span><b>{SITE["address_full"]}</b></div>
    </div>
  </div>
</section>'''
    return page("О компании", body, "o-kompanii.html", r)
