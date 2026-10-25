"""Собирает статический сайт в ../site. Запуск: python3 build/build.py"""
import json
from pathlib import Path

from data import CATEGORIES, PRODUCTS
from layout import page, page_head
from pages_home import about, home
from pages_info import contacts, legal, stores
from pages_shop import catalog, category, product

OUT = Path(__file__).resolve().parent.parent / "site"


def write(rel, html):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return rel


def search_page():
    body = f'''{page_head("Результаты поиска", [], "")}
<section class="section--tight" style="padding-bottom:96px">
  <div class="wrap">
    <div class="catalog-bar"><h2 data-search-title>Поиск</h2><span data-search-count></span></div>
    <div class="grid grid--4" data-search-grid></div>
  </div>
</section>'''
    return page("Поиск", body, None, "")


def products_js():
    cats = {c["slug"]: c["name"] for c in CATEGORIES}
    data = [{"slug": p["slug"], "name": p["name"], "price": p["price"], "img": p["img"],
             "url": f'katalog/{p["cat"]}/{p["slug"]}.html', "cat": cats[p["cat"]],
             "fat": p["fat"], "volume": p["volume"]} for p in PRODUCTS]
    return "window.PRODUCTS = " + json.dumps(data, ensure_ascii=False, indent=0) + ";\n"


def main():
    pages = [
        write("index.html", home()),
        write("o-kompanii.html", about()),
        write("katalog.html", catalog()),
        write("oplata-i-dostavka.html", stores()),
        write("kontakty.html", contacts()),
        write("politika-konfidencialnosti.html", legal("Политика конфиденциальности")),
        write("polzovatelskoe-soglashenie.html", legal("Пользовательское соглашение")),
        write("rezultaty-poiska.html", search_page()),
    ]
    pages += [write(f'katalog/{c["slug"]}.html', category(c)) for c in CATEGORIES]
    pages += [write(f'katalog/{p["cat"]}/{p["slug"]}.html', product(p)) for p in PRODUCTS]
    write("assets/products.js", products_js())
    print(f"Готово: {len(pages)} страниц в {OUT}")


if __name__ == "__main__":
    main()
