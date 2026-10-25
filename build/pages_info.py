from html import escape as e
from urllib.parse import quote

from data import FARMS, PRODUCTION, SITE, STORES
from layout import icon, page, page_head


def _store(kind, addr):
    route = "https://yandex.ru/maps/?text=" + quote(addr)
    return f'''<div class="store reveal">
  <div class="store__pin">{icon("pin", 22)}</div>
  <div>
    <span class="store__type">{e(kind)}</span>
    <h3>{e(addr)}</h3>
    <a class="link" href="{route}" target="_blank" rel="noopener">Построить маршрут {icon("arrow", 16)}</a>
  </div>
</div>'''


def stores():
    r = ""
    body = f'''{page_head("Где купить", [], r, "Свежая продукция «Фёдоровских молочных продуктов» в фирменных магазинах Москвы и Сергиево-Посадского района.")}
<section class="section--tight">
  <div class="wrap">
    <div class="addr-group">
      <h2>Фирменные магазины</h2>
      <div class="stores">{"".join(_store(k, a) for k, a in STORES)}</div>
    </div>
    <div class="addr-group">
      <h2>Фермы и производство</h2>
      <div class="stores">{"".join(_store(k, a) for k, a in FARMS + PRODUCTION)}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="map-card reveal">
      <iframe src="{SITE["map"]}" title="Карта: {e(SITE["address"])}" loading="lazy"></iframe>
      <div class="map-card__text">
        <p class="eyebrow">Остались вопросы?</p>
        <h2>Уточните наличие по телефону</h2>
        <p>Подскажем, где ближе купить нужный продукт и что сейчас есть в магазинах.</p>
        <ul class="map-card__list">
          <li>{icon("phone", 18)}<a href="{SITE["phone_href"]}">{SITE["phone"]}</a></li>
          <li>{icon("clock", 18)}<span>{SITE["hours"]}</span></li>
        </ul>
        <a class="btn btn--dark" href="kontakty.html">Все контакты</a>
      </div>
    </div>
  </div>
</section>'''
    return page("Где купить", body, "oplata-i-dostavka.html", r, "Адреса фирменных магазинов «Фёдоровских молочных продуктов» в Москве и Сергиево-Посадском районе.")


def contacts():
    r = ""
    body = f'''{page_head("Контакты", [], r, "Мы на связи каждый день. Позвоните, напишите на почту или оставьте сообщение — ответим как можно скорее.")}
<section class="section--tight">
  <div class="wrap">
    <div class="contact-cards">
      <a class="contact-card reveal" href="{SITE["phone_href"]}"><span class="contact-card__icon">{icon("phone", 24)}</span><span>Телефон</span><b>{SITE["phone"]}</b></a>
      <a class="contact-card reveal" href="mailto:{SITE["email"]}"><span class="contact-card__icon">{icon("mail", 24)}</span><span>Электронная почта</span><b>{SITE["email"]}</b></a>
      <div class="contact-card reveal"><span class="contact-card__icon">{icon("clock", 24)}</span><span>Режим работы</span><b>{SITE["hours"]}</b></div>
    </div>
  </div>
</section>
<section class="section--tight" id="form">
  <div class="wrap contact-layout">
    <div class="form-card reveal" id="contacts">
      <h2>Напишите нам</h2>
      <p>Вопрос о продукции, оптовые поставки или отзыв — мы прочитаем каждое сообщение.</p>
      <form class="form" method="post" action="kontakty.html#contacts" novalidate data-contact-form>
        <input type="hidden" name="formid" value="contForm">
        <div class="field"><label for="f-name">Имя</label><input id="f-name" type="text" name="name" autocomplete="name" required><span class="field__err">Укажите имя</span></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" type="email" name="email" autocomplete="email" required><span class="field__err">Укажите корректный email</span></div>
        <div class="field field--full"><label for="f-msg">Сообщение</label><textarea id="f-msg" name="message" required></textarea><span class="field__err">Напишите сообщение</span></div>
        <div class="form__note" data-form-note></div>
        <div class="form__foot">
          <p>Нажимая «Отправить», я соглашаюсь с <a href="politika-konfidencialnosti.html">Политикой конфиденциальности</a> и <a href="polzovatelskoe-soglashenie.html">Пользовательским соглашением</a>.</p>
          <button class="btn btn--green" type="submit">Отправить</button>
        </div>
      </form>
    </div>
    <aside class="info-card reveal">
      <h2>Офис</h2>
      <dl>
        <div><dt>Адрес</dt><dd>{SITE["address"]}</dd></div>
        <div><dt>Производство</dt><dd>{e(PRODUCTION[0][1])}</dd></div>
        <div><dt>Реквизиты</dt><dd>{SITE["legal"]}<br>ОГРН {SITE["ogrn"]}<br>ИНН / КПП {SITE["inn_kpp"]}</dd></div>
      </dl>
      <a class="btn btn--ghost-light" href="oplata-i-dostavka.html">Где купить</a>
    </aside>
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="wrap">
    <div class="map-frame reveal"><iframe src="{SITE["map"]}" title="Карта: {e(SITE["address"])}" loading="lazy"></iframe></div>
  </div>
</section>'''
    return page("Контакты", body, "kontakty.html", r, "Контакты «Фёдоровских молочных продуктов»: телефон +7 (499) 110-01-04, info@moloko-posad.ru, адрес в Сергиево-Посадском районе.")


def legal(title):
    r = ""
    body = f'''{page_head(title, [], r)}
<section class="section--tight" style="padding-bottom:96px">
  <div class="wrap">
    <article class="doc">
      <p class="doc__placeholder">На текущем сайте этот документ пока пустой. Вставьте сюда текст документа — оформление заголовков, абзацев и списков уже настроено.</p>
      <p>Оператор: {SITE["legal"]}, ОГРН {SITE["ogrn"]}, ИНН / КПП {SITE["inn_kpp"]}. Адрес: {SITE["address_full"]}. Связь: <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>, {SITE["phone"]}.</p>
    </article>
  </div>
</section>'''
    return page(title, body, None, r)
