(function () {
  "use strict";
  var ROOT = window.ROOT || "";
  var PRODUCTS = window.PRODUCTS || [];
  var BY_SLUG = {};
  PRODUCTS.forEach(function (p) { BY_SLUG[p.slug] = p; });
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  }
  function rub(n) { return n.toLocaleString("ru-RU") + " ₽"; }
  function store(key, val) {
    try {
      if (val === undefined) return JSON.parse(localStorage.getItem(key) || "null");
      localStorage.setItem(key, JSON.stringify(val));
    } catch (e) { return null; }
  }

  /* Бегущая строка объявлений */
  var msgs = $$(".announce__msg"), msgIdx = 0;
  function showMsg(i) {
    msgs[msgIdx].classList.remove("is-active");
    msgIdx = (i + msgs.length) % msgs.length;
    msgs[msgIdx].classList.add("is-active");
  }
  if (msgs.length > 1) {
    var msgTimer = setInterval(function () { showMsg(msgIdx + 1); }, 5000);
    $$("[data-announce]").forEach(function (b) {
      b.addEventListener("click", function () {
        clearInterval(msgTimer);
        showMsg(msgIdx + Number(b.dataset.announce));
      });
    });
  }

  /* Тень у шапки при прокрутке */
  var header = $(".header");
  window.addEventListener("scroll", function () { header.classList.toggle("is-scrolled", window.scrollY > 40); }, { passive: true });

  /* Выезжающие панели: меню и корзина */
  function openDrawer(id) {
    var d = document.getElementById(id);
    d.classList.add("is-open");
    d.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    var btn = $("[data-close]", d.querySelector(".drawer__panel"));
    if (btn) btn.focus();
  }
  function closeDrawers() {
    $$(".drawer.is-open").forEach(function (d) { d.classList.remove("is-open"); d.setAttribute("aria-hidden", "true"); });
    document.body.style.overflow = "";
  }
  $$("[data-open]").forEach(function (b) { b.addEventListener("click", function () { openDrawer(b.dataset.open); }); });
  $$("[data-close]").forEach(function (b) { b.addEventListener("click", closeDrawers); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDrawers(); });

  /* Слайдер на главной */
  var hero = $(".hero");
  if (hero) {
    var slides = $$(".hero__slide", hero), dots = $$(".hero__dots button", hero), cur = 0, timer;
    var go = function (i) {
      slides[cur].classList.remove("is-active"); dots[cur].classList.remove("is-active");
      cur = (i + slides.length) % slides.length;
      slides[cur].classList.add("is-active"); dots[cur].classList.add("is-active");
    };
    var play = function () { if (!reduceMotion) { clearInterval(timer); timer = setInterval(function () { go(cur + 1); }, 6500); } };
    dots.forEach(function (d, i) { d.addEventListener("click", function () { go(i); play(); }); });
    $(".hero__nav--prev", hero).addEventListener("click", function () { go(cur - 1); play(); });
    $(".hero__nav--next", hero).addEventListener("click", function () { go(cur + 1); play(); });
    hero.addEventListener("mouseenter", function () { clearInterval(timer); });
    hero.addEventListener("mouseleave", play);
    play();
  }

  /* Корзина (хранится в браузере) */
  var cart = store("fmp-cart") || {};
  var toastTimer;
  function toast(text) {
    var t = $(".toast");
    $("[data-toast-text]", t).textContent = text;
    t.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.classList.remove("is-visible"); }, 2600);
  }
  function renderCart() {
    var slugs = Object.keys(cart).filter(function (s) { return BY_SLUG[s]; });
    var count = slugs.reduce(function (n, s) { return n + cart[s]; }, 0);
    $$(".cart-count").forEach(function (b) { b.textContent = count; b.classList.toggle("is-visible", count > 0); });
    var list = $("[data-cart-list]"), foot = $("[data-cart-foot]");
    if (!slugs.length) {
      list.innerHTML = '<div class="cart-empty"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20.5" r="1.3"/><circle cx="17" cy="20.5" r="1.3"/></svg><p>Корзина пока пуста</p><p style="margin-top:18px"><a class="btn btn--dark btn--sm" href="' + ROOT + 'katalog.html">Перейти в каталог</a></p></div>';
      foot.hidden = true;
      return;
    }
    foot.hidden = false;
    var total = 0, unknown = 0;
    list.innerHTML = slugs.map(function (s) {
      var p = BY_SLUG[s], q = cart[s];
      if (p.price) total += p.price * q; else unknown++;
      return '<div class="cart-item"><img src="' + p.img + '" alt=""><div><div class="cart-item__name">' + esc(p.name) + '</div>' +
        '<div class="cart-item__price">' + (p.price ? rub(p.price) + " × " + q : "Цену уточняйте") + '</div>' +
        '<button class="cart-item__remove" type="button" data-remove="' + s + '">Удалить</button></div>' +
        '<div class="qty"><button type="button" data-cart-step="-1" data-slug="' + s + '" aria-label="Меньше">−</button><input type="number" value="' + q + '" readonly aria-label="Количество"><button type="button" data-cart-step="1" data-slug="' + s + '" aria-label="Больше">+</button></div></div>';
    }).join("");
    $("[data-cart-total]").textContent = rub(total);
    $("[data-cart-note]").textContent = unknown ? "Цену " + unknown + " " + (unknown === 1 ? "товара" : "товаров") + " уточнит менеджер." : "";
  }
  function addToCart(slug, qty) {
    cart[slug] = Math.min(99, (cart[slug] || 0) + qty);
    store("fmp-cart", cart);
    renderCart();
    toast("«" + BY_SLUG[slug].name + "» в корзине");
  }
  document.addEventListener("click", function (e) {
    var add = e.target.closest("[data-add]");
    if (add) {
      var qtyInput = add.hasAttribute("data-with-qty") ? $("[data-qty]") : null;
      addToCart(add.dataset.add, qtyInput ? Math.max(1, parseInt(qtyInput.value, 10) || 1) : 1);
      add.classList.add("is-added");
      setTimeout(function () { add.classList.remove("is-added"); }, 1200);
      return;
    }
    var step = e.target.closest("[data-cart-step]");
    if (step) {
      var s = step.dataset.slug;
      cart[s] = (cart[s] || 0) + Number(step.dataset.cartStep);
      if (cart[s] <= 0) delete cart[s];
      store("fmp-cart", cart); renderCart();
      return;
    }
    var rm = e.target.closest("[data-remove]");
    if (rm) { delete cart[rm.dataset.remove]; store("fmp-cart", cart); renderCart(); }
  });
  var orderLink = $("[data-cart-order]");
  if (orderLink) orderLink.addEventListener("click", function () {
    var lines = Object.keys(cart).filter(function (s) { return BY_SLUG[s]; }).map(function (s) { return "— " + BY_SLUG[s].name + " × " + cart[s]; });
    store("fmp-order", "Здравствуйте! Хочу заказать:\n" + lines.join("\n"));
    closeDrawers();
  });
  renderCart();

  /* Количество на странице товара */
  $$("[data-step]").forEach(function (b) {
    b.addEventListener("click", function () {
      var input = $("[data-qty]");
      input.value = Math.min(99, Math.max(1, (parseInt(input.value, 10) || 1) + Number(b.dataset.step)));
    });
  });

  /* Поиск с подсказками */
  function norm(s) { return s.toLowerCase().replace(/ё/g, "е").trim(); }
  function find(q) {
    q = norm(q);
    if (!q) return [];
    return PRODUCTS.filter(function (p) { return norm(p.name + " " + p.cat).indexOf(q) !== -1; });
  }
  $$(".search").forEach(function (form) {
    var input = $("input", form), box = $(".search__results", form), active = -1;
    function render() {
      var res = find(input.value).slice(0, 6);
      active = -1;
      if (!input.value.trim()) { box.classList.remove("is-open"); return; }
      box.innerHTML = res.length ? res.map(function (p) {
        return '<a class="search__item" role="option" href="' + ROOT + p.url + '"><img src="' + p.img + '" alt=""><div><b>' + esc(p.name) + '</b><span>' + esc(p.cat) + (p.price ? " · " + rub(p.price) : "") + "</span></div></a>";
      }).join("") : '<div class="search__empty">Ничего не нашли. Попробуйте «творог» или «йогурт».</div>';
      box.classList.add("is-open");
    }
    input.addEventListener("input", render);
    input.addEventListener("focus", render);
    input.addEventListener("keydown", function (e) {
      var items = $$(".search__item", box);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!items.length) return;
        if (active >= 0) items[active].classList.remove("is-active");
        active = (active + (e.key === "ArrowDown" ? 1 : -1) + items.length) % items.length;
        items[active].classList.add("is-active");
      } else if (e.key === "Enter" && active >= 0) {
        e.preventDefault(); location.href = items[active].href;
      } else if (e.key === "Escape") { box.classList.remove("is-open"); }
    });
    document.addEventListener("click", function (e) { if (!form.contains(e.target)) box.classList.remove("is-open"); });
  });

  function cardHTML(p) {
    return '<article class="product-card is-in reveal"><div class="product-card__img"><img src="' + p.img + '" alt="' + esc(p.name) + '" loading="lazy"></div>' +
      '<div class="product-card__body"><h3 class="product-card__name"><a href="' + ROOT + p.url + '">' + esc(p.name) + '</a></h3>' +
      '<p class="product-card__meta">Жирность ' + p.fat + " · " + p.volume + '</p><div class="product-card__foot">' +
      (p.price ? '<span class="price">' + rub(p.price) + "</span>" : '<span class="price price--ask">Цену уточняйте в магазинах</span>') +
      '<button class="add-btn" type="button" data-add="' + p.slug + '">+ В корзину</button></div></div></article>';
  }
  var searchGrid = $("[data-search-grid]");
  if (searchGrid) {
    var q = new URLSearchParams(location.search).get("search") || "";
    var res = q ? find(q) : PRODUCTS;
    $(".search input").value = q;
    $("[data-search-title]").textContent = q ? "«" + q + "»" : "Все товары";
    $("[data-search-count]").textContent = "Найдено: " + res.length;
    searchGrid.innerHTML = res.length ? res.map(cardHTML).join("") :
      '<div class="empty" style="grid-column:1/-1"><h2>Ничего не нашли</h2><p>Попробуйте другой запрос или загляните в каталог.</p><div class="empty__btns"><a class="btn btn--green" href="' + ROOT + 'katalog.html">Весь каталог</a></div></div>';
  }

  /* Фильтр категорий в каталоге */
  var grid = $("[data-grid]");
  $$("[data-filter]").forEach(function (chip) {
    chip.addEventListener("click", function () {
      $$("[data-filter]").forEach(function (c) { c.classList.toggle("is-active", c === chip); });
      $$("[data-cat]", grid).forEach(function (card) {
        card.hidden = chip.dataset.filter !== "all" && card.dataset.cat !== chip.dataset.filter;
      });
    });
  });

  /* Форма обратной связи */
  var form = $("[data-contact-form]");
  if (form) {
    var draft = store("fmp-order");
    if (draft && location.hash === "#form") { form.message.value = draft; store("fmp-order", null); }
    form.addEventListener("submit", function (e) {
      var ok = true;
      $$(".field", form).forEach(function (f) {
        var input = $("input, textarea", f);
        var bad = !input.value.trim() || (input.type === "email" && !/^\S+@\S+\.\S+$/.test(input.value));
        f.classList.toggle("is-invalid", bad);
        if (bad && ok) { input.focus(); ok = false; }
      });
      if (!ok) { e.preventDefault(); return; }
      // На боевом сайте форма уходит в обработчик CMS (formid=contForm). В превью — только показываем подсказку.
      if (location.hostname !== "moloko-posad.ru") {
        e.preventDefault();
        var note = $("[data-form-note]", form);
        note.textContent = "Это демо-версия: после переноса на сайт форма будет отправляться в тот же обработчик, что и сейчас.";
        note.classList.add("is-visible");
      }
    });
    $$("input, textarea", form).forEach(function (i) { i.addEventListener("input", function () { i.closest(".field").classList.remove("is-invalid"); }); });
  }

  /* Плавное появление блоков */
  var reveals = $$(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }
})();
