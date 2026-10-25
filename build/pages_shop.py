from html import escape as e

from data import CATEGORIES, PRODUCTS, SITE
from layout import icon, page, page_head, price_html, product_card

CAT = {c["slug"]: c for c in CATEGORIES}


def _chips(r, active=None, filter_mode=False):
    total = len(PRODUCTS)
    out = []
    if filter_mode:
        out.append(f'<button class="chip is-active" type="button" data-filter="all">Все <small>{total}</small></button>')
        for c in CATEGORIES:
            n = sum(1 for p in PRODUCTS if p["cat"] == c["slug"])
            out.append(f'<button class="chip" type="button" data-filter="{c["slug"]}">{e(c["name"])} <small>{n}</small></button>')
    else:
        out.append(f'<a class="chip" href="{r}katalog.html">Все <small>{total}</small></a>')
        for c in CATEGORIES:
            n = sum(1 for p in PRODUCTS if p["cat"] == c["slug"])
            cur = ' aria-current="page"' if c["slug"] == active else ""
            out.append(f'<a class="chip" href="{r}katalog/{c["slug"]}.html"{cur}>{e(c["name"])} <small>{n}</small></a>')
    return '<nav class="chips" aria-label="Категории">' + "".join(out) + "</nav>"


def catalog():
    r = ""
    cards = "".join(product_card(p, r, CAT[p["cat"]]["name"]) for p in PRODUCTS)
    body = f'''{page_head("Каталог", [], r, "Натуральная молочная продукция собственного производства — без консервантов и стабилизаторов.")}
<section class="section--tight">
  <div class="wrap">
    {_chips(r, filter_mode=True)}
    <div class="grid grid--4" data-grid>{cards}</div>
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="wrap">
    <div class="empty reveal">
      <div class="empty__icon">{icon("store", 32, 1.6)}</div>
      <h2>Цены и наличие</h2>
      <p>Цены на часть товаров уточняйте в фирменных магазинах или по телефону {SITE["phone"]}.</p>
      <div class="empty__btns"><a class="btn btn--green" href="oplata-i-dostavka.html">Где купить</a><a class="btn btn--ghost" href="{SITE["phone_href"]}">Позвонить</a></div>
    </div>
  </div>
</section>'''
    return page("Каталог", body, "katalog.html", r, "Каталог натуральной молочной продукции: молоко, кефир, ряженка, йогурты, сметана, творог и творожные десерты.")


def category(c):
    r = "../"
    items = [p for p in PRODUCTS if p["cat"] == c["slug"]]
    if items:
        content = f'<div class="grid grid--4">{"".join(product_card(p, r) for p in items)}</div>'
    else:
        content = f'''<div class="empty">
  <div class="empty__icon">{icon("box", 32, 1.6)}</div>
  <h2>Скоро в продаже</h2>
  <p>Товары этой категории пока не добавлены на сайт. Наличие уточняйте в фирменных магазинах или по телефону {SITE["phone"]}.</p>
  <div class="empty__btns"><a class="btn btn--green" href="{r}katalog.html">Весь каталог</a><a class="btn btn--ghost" href="{r}oplata-i-dostavka.html">Где купить</a></div>
</div>'''
    body = f'''{page_head(c["name"], [("katalog.html", "Каталог")], r, e(c["text"]))}
<section class="section--tight">
  <div class="wrap">
    {_chips(r, c["slug"])}
    {content}
  </div>
</section>'''
    return page(c["name"], body, "katalog.html", r)


def product(p):
    r = "../../"
    c = CAT[p["cat"]]
    related = [x for x in PRODUCTS if x["cat"] == p["cat"] and x["slug"] != p["slug"]]
    related += [x for x in PRODUCTS if x["cat"] != p["cat"]]
    related_html = "".join(product_card(x, r) for x in related[:4])
    if p["price"]:
        price = f'<div class="pdp__price">{price_html(p)}<small>за {p["volume"]}</small></div>'
    else:
        price = f'<div class="pdp__price"><span class="price" style="font-size:30px">Цену уточняйте</span><small>в магазинах или по телефону</small></div>'
    body = f'''<section class="page-head page-head--slim">
  <div class="wrap">
    <nav aria-label="Хлебные крошки"><ol class="crumbs"><li><a href="{r}index.html">Главная</a></li><li><a href="{r}katalog.html">Каталог</a></li><li><a href="{r}katalog/{c["slug"]}.html">{e(c["name"])}</a></li><li aria-current="page">{e(p["name"])}</li></ol></nav>
  </div>
</section>
<section class="section--tight">
  <div class="wrap pdp">
    <div class="pdp__media"><img src="{p["img"]}" alt="{e(p["name"])}"></div>
    <div class="pdp__info">
      <a class="eyebrow" href="{r}katalog/{c["slug"]}.html">{e(c["name"])}</a>
      <h1>{e(p["name"])}</h1>
      {price}
      <div class="specs">
        <div class="spec"><span>Жирность</span><b>{p["fat"]}</b></div>
        <div class="spec"><span>Объём</span><b>{p["volume"]}</b></div>
      </div>
      <div class="buy">
        <div class="qty qty--lg"><button type="button" data-step="-1" aria-label="Меньше">−</button><input type="number" value="1" min="1" max="99" aria-label="Количество" data-qty><button type="button" data-step="1" aria-label="Больше">+</button></div>
        <button class="btn btn--green" type="button" data-add="{p["slug"]}" data-with-qty>{icon("cart", 20)}В корзину</button>
      </div>
      <ul class="perks">
        <li>{icon("leaf", 22)}100% натуральный продукт</li>
        <li>{icon("drop", 22)}Без консервантов, стабилизаторов и химических добавок</li>
        <li>{icon("shield", 22)}Молоко с собственных ферм, контроль качества на всех этапах</li>
      </ul>
      <a class="perks-link" href="{r}oplata-i-dostavka.html">Где купить в магазине {icon("arrow", 18)}</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Вас также заинтересует</h2></div>
    <div class="grid grid--4">{related_html}</div>
  </div>
</section>'''
    return page(p["name"], body, "katalog.html", r, f'{p["name"]} — жирность {p["fat"]}, {p["volume"]}. Натуральный продукт без консервантов от «Фёдоровских молочных продуктов».')
