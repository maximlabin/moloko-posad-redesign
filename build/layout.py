from html import escape as e

from data import ANNOUNCE, CATEGORIES, SITE

# Иконки (stroke, 24x24)
_ICONS = {
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "cart": '<path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20.5" r="1.3"/><circle cx="17" cy="20.5" r="1.3"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "store": '<path d="M4 10v10h16V10"/><path d="M3 10 5 4h14l2 6"/><path d="M3 10a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M10 20v-5h4v5"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "leaf": '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19c3-4 6-6 10-8"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "shield": '<path d="M12 3 5 6v5c0 4.5 3 8.3 7 10 4-1.7 7-5.5 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "box": '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="m3 7.5 9 4.5 9-4.5M12 12v9"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "vk": None,
    "yt": None,
}


def icon(name, size=20, sw=1.8):
    if name == "vk":
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                '<path d="M12.8 17.5C6.9 17.5 3.5 13.5 3.4 6.8h3c.1 4.9 2.2 7 3.9 7.4V6.8h2.8v4.2c1.7-.2 3.5-2.1 4.1-4.2H20c-.5 2.6-2.4 4.5-3.8 5.3 1.4.6 3.6 2.4 4.4 5.4h-3.1c-.7-2-2.3-3.6-4.3-3.8v3.8z"/></svg>')
    if name == "yt":
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                '<path d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2 27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8zM10 15V9l5.2 3z"/></svg>')
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_ICONS[name]}</svg>')


NAV = [
    ("index.html", "Главная"),
    ("o-kompanii.html", "О компании"),
    ("katalog.html", "Каталог"),
    ("oplata-i-dostavka.html", "Где купить"),
    ("kontakty.html", "Контакты"),
]


def price_html(p, cls="price"):
    if p["price"]:
        return f'<span class="{cls}">{p["price"]} ₽</span>'
    return '<span class="price price--ask">Цену уточняйте в магазинах</span>'


def product_url(p):
    return f'katalog/{p["cat"]}/{p["slug"]}.html'


def product_card(p, r, tag=None):
    tag_html = f'<span class="product-card__tag">{e(tag)}</span>' if tag else ""
    return f'''<article class="product-card reveal" data-cat="{p["cat"]}">
  {tag_html}
  <div class="product-card__img"><img src="{p["img"]}" alt="{e(p["name"])}" loading="lazy"></div>
  <div class="product-card__body">
    <h3 class="product-card__name"><a href="{r}{product_url(p)}">{e(p["name"])}</a></h3>
    <p class="product-card__meta">Жирность {p["fat"]} · {p["volume"]}</p>
    <div class="product-card__foot">
      {price_html(p)}
      <button class="add-btn" type="button" data-add="{p["slug"]}">{icon("plus", 16, 2.2)}В корзину</button>
    </div>
  </div>
</article>'''


def crumbs(items, r):
    out = []
    for href, label in items:
        out.append(f'<li><a href="{r}{href}">{e(label)}</a></li>' if href else f'<li aria-current="page">{e(label)}</li>')
    return '<ol class="crumbs">' + "".join(out) + "</ol>"


def page_head(title, trail, r, lead=None):
    lead_html = f'<p class="page-head__lead">{lead}</p>' if lead else ""
    return f'''<section class="page-head">
  <div class="wrap">
    <nav aria-label="Хлебные крошки">{crumbs([("index.html", "Главная")] + trail + [(None, title)], r)}</nav>
    <h1>{e(title)}</h1>
    {lead_html}
  </div>
</section>'''


def _header(active, r):
    msgs = "".join(f'<div class="announce__msg{" is-active" if i == 0 else ""}">{e(m)}</div>' for i, m in enumerate(ANNOUNCE))
    cats = "".join(f'<li><a href="{r}katalog/{c["slug"]}.html">{e(c["name"])}</a></li>' for c in CATEGORIES)
    nav = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        if href == "katalog.html":
            nav.append(f'<li><a href="{r}{href}"{cur}>{label}{icon("down", 16)}</a><ul class="dropdown">{cats}</ul></li>')
        else:
            nav.append(f'<li><a href="{r}{href}"{cur}>{label}</a></li>')
    return f'''<div class="announce" role="region" aria-label="Объявления">
  <div class="wrap">
    <button class="announce__arrow" type="button" data-announce="-1" aria-label="Предыдущее">{icon("left", 18, 2)}</button>
    <div class="announce__track" aria-live="polite">{msgs}</div>
    <button class="announce__arrow" type="button" data-announce="1" aria-label="Следующее">{icon("right", 18, 2)}</button>
  </div>
</div>
<header class="header">
  <div class="wrap header__top">
    <button class="icon-btn burger" type="button" data-open="menu" aria-label="Меню">{icon("menu", 24)}</button>
    <a class="logo" href="{r}index.html" aria-label="{SITE["name"]} — на главную">
      <img src="{SITE["logo"]}" alt="" width="110" height="68">
      <span class="logo__text">Фёдоровские<small>молочные продукты</small></span>
    </a>
    <form class="search" action="{r}rezultaty-poiska.html" method="get" role="search">
      {icon("search", 20)}
      <input type="search" name="search" placeholder="Найти молоко, творог, десерт…" autocomplete="off" aria-label="Поиск по каталогу">
      <div class="search__results" role="listbox"></div>
    </form>
    <div class="header__actions">
      <a class="header__phone" href="{SITE["phone_href"]}">Ежедневно 10:00–19:00<b>{SITE["phone"]}</b></a>
      <button class="icon-btn" type="button" data-open="cart" aria-label="Корзина">{icon("cart", 24)}<span class="cart-count">0</span></button>
    </div>
  </div>
  <div class="header__nav">
    <div class="wrap">
      <ul class="nav">{"".join(nav)}</ul>
      <a class="store-pick" href="{r}oplata-i-dostavka.html">{icon("store", 30, 1.5)}<span>Где купить?<b>5 фирменных магазинов {icon("down", 16)}</b></span></a>
    </div>
  </div>
</header>'''


def _drawers(active, r):
    cats = "".join(f'<li><a href="{r}katalog/{c["slug"]}.html">{e(c["name"])}</a></li>' for c in CATEGORIES)
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        sub = f"<ul>{cats}</ul>" if href == "katalog.html" else ""
        items.append(f'<li><a href="{r}{href}"{cur}>{label}</a>{sub}</li>')
    return f'''<div class="drawer drawer--left" id="menu" aria-hidden="true">
  <div class="drawer__overlay" data-close></div>
  <nav class="drawer__panel" aria-label="Меню">
    <div class="drawer__head"><h3>Меню</h3><button class="icon-btn" type="button" data-close aria-label="Закрыть">{icon("close", 24)}</button></div>
    <div class="drawer__body">
      <ul class="mnav">{"".join(items)}</ul>
      <div class="mcontacts"><a href="{SITE["phone_href"]}">{SITE["phone"]}</a><span>{SITE["hours"]}</span><span>{SITE["email"]}</span></div>
    </div>
  </nav>
</div>
<div class="drawer drawer--right" id="cart" aria-hidden="true">
  <div class="drawer__overlay" data-close></div>
  <aside class="drawer__panel" aria-label="Корзина">
    <div class="drawer__head"><h3>Корзина</h3><button class="icon-btn" type="button" data-close aria-label="Закрыть">{icon("close", 24)}</button></div>
    <div class="drawer__body" data-cart-list></div>
    <div class="drawer__foot" data-cart-foot>
      <div class="cart-total"><span>Итого</span><b data-cart-total>0 ₽</b></div>
      <p class="cart-note" data-cart-note></p>
      <a class="btn btn--green btn--block" href="{r}kontakty.html#form" data-cart-order>Оформить заказ</a>
    </div>
  </aside>
</div>
<div class="toast" role="status">{icon("check", 20, 2.4)}<span data-toast-text></span></div>'''


def _footer(r):
    cats = "".join(f'<li><a href="{r}katalog/{c["slug"]}.html">{e(c["name"])}</a></li>' for c in CATEGORIES)
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="{SITE["logo"]}" alt="{SITE["name"]}" loading="lazy">
        <p>Производим 100% натуральные продукты без химических добавок, консервантов и стабилизаторов.</p>
        <div class="footer__social">
          <a href="https://vk.com/" aria-label="ВКонтакте">{icon("vk", 20)}</a>
          <a href="https://youtube.com/" aria-label="YouTube">{icon("yt", 20)}</a>
        </div>
      </div>
      <div>
        <h4>Меню</h4>
        <ul>{"".join(f'<li><a href="{r}{h}">{l}</a></li>' for h, l in NAV)}</ul>
      </div>
      <div>
        <h4>Каталог</h4>
        <ul>{cats}</ul>
      </div>
      <div>
        <h4>Контакты</h4>
        <ul class="footer__contacts">
          <li>{icon("phone", 18)}<a href="{SITE["phone_href"]}">{SITE["phone"]}</a></li>
          <li>{icon("mail", 18)}<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
          <li>{icon("clock", 18)}<span>{SITE["hours"]}</span></li>
          <li>{icon("pin", 18)}<span>{SITE["address"]}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 {SITE["legal"]} · ОГРН {SITE["ogrn"]}</span>
      <nav aria-label="Документы">
        <a href="{r}politika-konfidencialnosti.html">Политика конфиденциальности</a>
        <a href="{r}polzovatelskoe-soglashenie.html">Пользовательское соглашение</a>
      </nav>
    </div>
  </div>
</footer>'''


def page(title, body, active, r, description=""):
    desc = description or "Фёдоровские молочные продукты — натуральное молоко, кефир, творог и десерты с собственных ферм в Сергиево-Посадском районе."
    full_title = SITE["name"] if title is None else f"{title} — {SITE['name']}"
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#2f6b2a">
<link rel="icon" href="{SITE["logo"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans+Extra+Condensed:ital,wght@0,800;1,800&family=Golos+Text:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
</head>
<body>
{_header(active, r)}
<main>
{body}
</main>
{_footer(r)}
{_drawers(active, r)}
<script>window.ROOT = "{r}";</script>
<script src="{r}assets/products.js"></script>
<script src="{r}assets/app.js"></script>
</body>
</html>
'''
