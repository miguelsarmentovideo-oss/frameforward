#!/usr/bin/env python3
"""Generates the Frame Forward static site into ./site."""
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
DOMAIN = "https://frameforward.no"
PHONE = "+4741357424"
PHONE_DISPLAY = "+47 413 57 424"
EMAIL = "hello@frameforward.no"
WA = "https://wa.me/4741357424?text=" + "Hei%20Miguel!%20Jeg%20vil%20gjerne%20h%C3%B8re%20mer%20om%20innhold%20for%20bedriften%20min."
IG = "https://www.instagram.com/frameforward.no/"

ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4C2.6 15.6 2.1 13.8 2.1 12 2.1 6.5 6.5 2.2 12 2.2c2.6 0 5.1 1 7 2.9 1.9 1.9 2.9 4.3 2.9 7 0 5.4-4.4 9.7-9.9 9.7zm8.4-18.1C18.2 1.5 15.2.2 12 .2 5.4.2.1 5.5.1 12c0 2.1.5 4.1 1.6 5.9L0 24l6.3-1.7c1.7.9 3.7 1.4 5.7 1.4 6.6 0 11.9-5.3 11.9-11.8 0-3.2-1.2-6.1-3.5-8.2z"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>'

NAV = [("", "Hjem"), ("ourwork/", "Vårt arbeid"), ("proven-impact/", "Resultater")]


def page(path, title, desc, body, active, root=None):
    depth = path.count("/")
    r = root if root is not None else "../" * depth
    canonical = DOMAIN + "/" + path
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    nav += f'<a class="nav-cta" href="{r}contact/"{" aria-current=\"page\"" if active == "contact/" else ""}>Kontakt</a>'
    return f"""<!doctype html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg">
<meta property="og:locale" content="nb_NO">
<meta name="theme-color" content="#482B1E">
<link rel="icon" type="image/png" href="{r}img/favicon.png">
<link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="preload" href="{r}fonts/oswald-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Frame Forward AS","url":"{DOMAIN}/","email":"{EMAIL}","telephone":"{PHONE}","address":{{"@type":"PostalAddress","addressLocality":"Bergen","addressCountry":"NO"}},"sameAs":["{IG}"],"description":"Video, foto og sosiale medier for restauranter, barer, hoteller og eventer i Bergen."}}</script>
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r}" aria-label="Frame Forward – til forsiden"><img src="{r}img/logo-light.png" alt="Frame Forward" width="138" height="40"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="nav">Meny</button>
    <nav class="nav" id="nav" aria-label="Hovedmeny">{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div>
      <img src="{r}img/logo-light.png" alt="Frame Forward" width="131" height="38">
      <p>Video og foto for restauranter, barer, hoteller og eventer. Basert i Bergen – jobber overalt.</p>
    </div>
    <div>
      <h3>Sider</h3>
      <ul>
        <li><a href="{r}">Hjem</a></li>
        <li><a href="{r}ourwork/">Vårt arbeid</a></li>
        <li><a href="{r}produktfoto/">Produktfoto</a></li>
        <li><a href="{r}proven-impact/">Resultater</a></li>
        <li><a href="{r}contact/">Kontakt</a></li>
      </ul>
    </div>
    <div>
      <h3>Kontakt</h3>
      <ul>
        <li><a href="{WA}">WhatsApp</a></li>
        <li><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{IG}">Instagram</a></li>
      </ul>
    </div>
    <p class="legal">© Frame Forward AS, Bergen</p>
  </div>
</footer>
<a class="wa-float" href="{WA}" aria-label="Send melding på WhatsApp">{ICON_WA}</a>
<script>
  var t=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  t.addEventListener('click',function(){{var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o);t.textContent=o?'Lukk':'Meny';}});
  // Only one video with sound at a time
  document.addEventListener('play',function(e){{document.querySelectorAll('video[controls]').forEach(function(v){{if(v!==e.target)v.pause();}});}},true);
</script>
</body>
</html>
"""


def contact_buttons(dark=True):
    ghost = "btn ghost" if dark else "btn ghost"
    return f"""<div class="btn-row">
      <a class="btn" href="{WA}">{ICON_WA}Send melding på WhatsApp</a>
      <a class="{ghost}" href="mailto:{EMAIL}">{ICON_MAIL}Send e-post</a>
    </div>"""


RESULTS = [
    ("3M", "visninger", "Nabo Gastro Bar", "Én reel som gikk viralt.", "https://www.instagram.com/p/DeZ7gc3M0_P/", "Se reelen"),
    ("+600", "følgere", "Bjerck Restaurant & Bar", "Nye følgere fra én enkelt reel.", "https://www.instagram.com/p/DdYhu_Zuh5x/", "Se reelen"),
    ("28K+", "følgere", "Handball Premium", "Bygget fra null følgere.", "https://www.instagram.com/handballpremium/", "Se kontoen"),
]


def results_rows():
    rows = ""
    for num, unit, who, what, url, go in RESULTS:
        rows += f"""<a class="result" href="{url}" target="_blank" rel="noopener">
        <span class="num">{num}</span>
        <span class="what"><strong>{unit} for {who}</strong>{what}</span>
        <span class="go">{go} på Instagram</span>
      </a>"""
    return f'<div class="results">{rows}</div>'


CLIENTS = [
    ("debergenske", "De Bergenske"), ("charmante", "Charmante Skostredet Hotel"), ("bjerck", "Bjerck Restaurant & Bar"),
    ("engen", "Engen Steakhouse"), ("fresquito", "Fresquito"), ("ftesco", "Frescohallen"),
    ("izakaya", "Izakaya Skostredet"), ("old", "The Old Irish Pub"), ("skos", "Skostredet Hotel & Spa"),
    ("villani", "Villani Skostredet"), ("wessel", "Wesselstuen"), ("omakase", "Omakase"),
]


def home():
    services = [
        ("home-dsc01148-edit", "Video for sosiale medier", "Reels, TikTok og Shorts – laget for plattformen og klippet for å holde på seerne. Det er her rekkevidden skapes.", "To kokker anretter retter på et restaurantkjøkken"),
        ("home-dsc05378", "Eventdekning", "Lanseringer, smakinger og sesongkvelder – fanget i oppsummeringer og høydepunkter som fyller neste event.", "Gjester på en vinsmaking"),
        ("home-dsc06345", "Foto", "Mat, interiør og stemning – fotografert for å se like bra ut i feeden som på nettsiden og menyen.", "Kokk som holder en tallerken med mat"),
        ("home-1z4a7071", "Månedlig innhold", "En jevn strøm av video og foto hver måned, så kanalene dine aldri blir stille.", "Full restaurant med høyt hvelvet tak"),
    ]
    svc = "".join(
        f'<article class="service"><img src="img/{img}.webp" alt="{alt}" loading="lazy" width="800" height="1000"><h3>{h}</h3><p>{p}</p></article>'
        for img, h, p, alt in services
    )
    clients = "".join(f'<li><img src="img/home-{f}.webp" alt="{n}" loading="lazy" width="400" height="400"></li>' for f, n in CLIENTS)
    body = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <h1>Innhold som fyller bordene.</h1>
      <p class="lede">Video og foto for restauranter, barer, hoteller og eventer i Bergen – laget for å stoppe scrollingen.</p>
      <div class="btn-row">
        <a class="btn" href="contact/">Book en samtale</a>
        <a class="btn ghost" href="ourwork/">Se arbeidet vårt</a>
      </div>
      <p class="award-note"><img src="img/home-award-1299031-1280.webp" alt="" width="28" height="50">Kåret til «SoMe Company of the Year» på Digitaldagen Bergen (PwC Bergen) for arbeidet med Villani Skostredet.</p>
    </div>
    <div class="phone">
      <video src="video/hero-loop.mp4" poster="img/poster-restaurant-3.webp" autoplay muted loop playsinline aria-label="Klipp fra en restaurantreel laget av Frame Forward"></video>
      <span class="phone-tag">Laget av Frame Forward</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Det vi lager</h2>
      <p>Alt du trenger for å vises – og velges – i feeden.</p>
    </div>
    <div class="services">{svc}</div>
  </div>
</section>

<section class="section rust">
  <div class="wrap">
    <div class="section-head">
      <h2>Tall som betyr noe</h2>
      <p>Hvert tall er ekte og lenker til innlegget det kom fra.</p>
    </div>
    {results_rows()}
  </div>
</section>

<section class="section">
  <div class="wrap about">
    <img src="img/home-1z4a8772.webp" alt="Miguel fra Frame Forward med kamera og gimbal i Bergen" loading="lazy" width="800" height="1200">
    <div>
      <h2>Hei, jeg er Miguel.</h2>
      <p>Jeg står bak kamera i Frame Forward. Jeg lager video og foto for restauranter, barer og bedrifter i Bergen – innhold som er laget for å stoppe scrollingen og fylle bordene.</p>
      <p>Arbeidet mitt for Villani Skostredet ble kåret til «SoMe Company of the Year» på Digitaldagen Bergen. Du får én fast kontaktperson fra idé til ferdig innhold.</p>
      <div class="btn-row" style="margin-top:28px"><a class="btn" href="{WA}">{ICON_WA}Send meg en melding</a></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Innhold som fyller lokalet</h2></div>
    <div class="wall">
      <img class="a" src="img/home-use1z4a0077.webp" alt="Full selskapssal med gjester ved runde bord" loading="lazy">
      <img class="b" src="img/home-usedsc04161.webp" alt="Full restaurant med gjester som spiser" loading="lazy">
      <img class="c" src="img/home-usedsc04741.webp" alt="Travel restaurant en kveld" loading="lazy">
      <img class="d" src="img/home-usedsc04839.webp" alt="Restaurant pyntet med lysslynger" loading="lazy">
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="section-head"><h2>De stoler på oss</h2></div>
    <ul class="clients">{clients}</ul>
  </div>
</section>

<section class="section rust closing">
  <div class="wrap">
    <h2>La oss gjøre stedet ditt umulig å scrolle forbi.</h2>
    {contact_buttons()}
    <p class="contact-lines">Eller ring <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></p>
  </div>
</section>
"""
    return page("", "Frame Forward – Video, foto og sosiale medier i Bergen",
                "Prisvinnende innholdsprodusent i Bergen. Video, Reels, TikTok og foto for restauranter, barer og hoteller – innhold som fyller bordene og gir flere bookinger.",
                body, "")


def vid(name, poster, label, cls=""):
    return f'<video src="../video/{name}.mp4" poster="../img/poster-{poster}.webp" controls preload="none" playsinline aria-label="{label}"{cls}></video>'


def work():
    reels = [
        ("restaurant-2", "Kokken forteller"),
        ("restaurant-1", "Stemningen i salen"),
        ("restaurant-4", "Retten i fokus"),
        ("restaurant-5", "Fra panne til tallerken"),
        ("restaurant-3", "Et blikk inn i lokalet"),
    ]
    strip = "".join(f'<figure class="reel">{vid(n, n, c)}<figcaption>{c}</figcaption></figure>' for n, c in reels)
    photos = ["dsc06897-hdr-2", "dsc07193", "dsc06420", "dsc4790", "dsc06345", "dsc00558-hdr",
              "dsc02162-hdr", "dsc01307", "dji-fly-20240927-103214-0024-1727426403673-photo", "dsc00492", "dsc00275", "dsc07976"]
    ph = "".join(f'<img src="../img/ourwork-{p}.webp" alt="Foto av Frame Forward" loading="lazy">' for p in photos)
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Vårt arbeid</h1>
    <p>Reels, foto og eventfilm for restauranter, barer og hoteller i Bergen. Trykk på en video for å spille av med lyd.</p>
  </div>
</section>

<section class="chapter">
  <div class="wrap">
    <div class="chapter-head">
      <h2>Restauranter</h2>
      <p>Fra kokkeintervjuer og anretning bak kulissene til stemningen i hele restauranten – video som får frem sjelen i kjøkkenet.</p>
    </div>
    <div class="reels">{strip}</div>
    <p class="reels-hint">Sveip for flere.</p>
  </div>
</section>

<section class="chapter">
  <div class="wrap feature wide">
    <div>
      <h2>Bak kulissene</h2>
      <p>Liggende format for nettsider, skjermer og YouTube – samme stemning, større lerret.</p>
    </div>
    {vid("restaurant-6-wide", "restaurant-6-wide", "Kjøkkenet bak kulissene")}
  </div>
</section>

<section class="chapter">
  <div class="wrap feature">
    <div>
      <h2>Eventer</h2>
      <p>Vinsmaking – en hel kveld fortalt på litt over ett minutt. Folk, produkter og stemning, klippet så neste event selger seg selv.</p>
      <a class="btn" href="../contact/">Book eventdekning</a>
    </div>
    {vid("eventer-nores", "eventer-nores", "Event-reel fra en vinsmaking")}
  </div>
</section>

<section class="chapter">
  <div class="wrap feature">
    <div>
      <h2>Uteliv</h2>
      <p>The Old Irish Pub – livemusikk, fullt lokale og energien som får folk til å komme tilbake neste helg.</p>
    </div>
    {vid("uteliv-old-irish-pub", "uteliv-old-irish-pub", "Vertikal video fra The Old Irish Pub")}
  </div>
</section>

<section class="chapter">
  <div class="wrap feature wide">
    <div>
      <h2>Dronefilm</h2>
      <p>Luftfoto og dronevideo for eiendom, hoteller og beliggenheter som fortjener å ses ovenfra.</p>
    </div>
    {vid("dronefilm", "dronefilm", "Dronefilm av et boligområde")}
  </div>
</section>

<section class="chapter">
  <div class="wrap">
    <div class="chapter-head">
      <h2>Foto</h2>
      <p>Mat, interiør og folk – bilder som fungerer i feeden, på nettsiden og på menyen.</p>
    </div>
    <div class="photos">{ph}</div>
  </div>
</section>

<section class="chapter">
  <div class="wrap feature">
    <div>
      <h2>Produktfoto</h2>
      <p>Produktbilder for olivenoljeprodusenten Oliven – fotografert av oss, og videreutviklet med A.I. Se original og A.I.-versjon side om side.</p>
      <a class="btn" href="../produktfoto/">Se produktfoto</a>
    </div>
    <div class="pair-teaser">
      <img src="../img/oliven/oliven-golden-original.jpg" alt="Oliven Golden Selection – originalfoto" loading="lazy" width="1000" height="1500">
      <img src="../img/oliven/oliven-golden-ai.jpg" alt="Oliven Golden Selection – A.I.-versjon" loading="lazy" width="1000" height="1500">
    </div>
  </div>
</section>

<section class="section rust closing">
  <div class="wrap">
    <h2>Vil du ha noe lignende?</h2>
    {contact_buttons()}
  </div>
</section>
"""
    return page("ourwork/", "Vårt arbeid – restaurantvideo, Reels og foto i Bergen — Frame Forward",
                "Se video, Reels og foto vi har laget for restauranter, barer og eiendom i Bergen – kokkeintervjuer, stemning, uteliv og dronefilm.",
                body, "ourwork/")


def impact():
    proofs = [
        ("handball-premium", "Handball Premium – 28K+ følgere"),
        ("villani", "Villani Skostredet"),
        ("img-4243", "Villani Lagunen"),
        ("img-4240", "Charmante Skostredet Hotel"),
        ("img-4246", "Brasserie Chérie"),
        ("img-4244", "Taperia Bergen"),
    ]
    pr = "".join(f'<figure><img src="../img/proven-impact-{f}.webp" alt="Instagram-profil: {c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c in proofs)
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Resultater</h1>
    <p>Priser, følgere og visninger – målt, ikke lovet.</p>
  </div>
</section>

<section class="section">
  <div class="wrap award">
    <div>
      <blockquote>Kåret til «SoMe Company of the Year» på Digitaldagen Bergen.</blockquote>
      <p style="margin-top:24px;font-size:1.15rem">Innholdet vårt for Villani Skostredet vant i kategorien små og mellomstore bedrifter, delt ut av PwC Bergen.</p>
      <p style="font-size:1.15rem;color:var(--muted)">Prisen hedret en kreativ og strategisk tilnærming til sosiale medier – innhold som ikke bare så bra ut, men som ga ekte resultater for bedriften.</p>
    </div>
    <div class="award-photos">
      <img src="../img/proven-impact-img-9913.webp" alt="Prisutdeling på Digitaldagen Bergen" loading="lazy">
      <img src="../img/proven-impact-img-9911.webp" alt="Miguel på scenen med presentasjon om Villani Skostredet" loading="lazy">
      <img src="../img/proven-impact-img-9906.webp" alt="Fra Digitaldagen Bergen" loading="lazy">
    </div>
  </div>
</section>

<section class="section rust">
  <div class="wrap">
    <div class="section-head"><h2>Tallene</h2><p>Trykk for å se kilden på Instagram.</p></div>
    {results_rows()}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Fra null til tusenvis</h2>
      <p>Disse sidene ble bygget fra bunnen av – alle startet med null følgere. Hvert bilde, hver video og hver strategi bak dem er laget av Frame Forward.</p>
    </div>
    <div class="proofs">{pr}</div>
  </div>
</section>

<section class="section dark closing">
  <div class="wrap">
    <h2>Neste resultat kan være ditt.</h2>
    {contact_buttons()}
  </div>
</section>
"""
    return page("proven-impact/", "Resultater – prisvinnende sosiale medier i Bergen — Frame Forward",
                "Vinner av «SoMe Company of the Year» på Digitaldagen Bergen (PwC) for Villani Skostredet. Sider bygget fra null til tusenvis av følgere – og en reel med over 3 millioner visninger.",
                body, "proven-impact/")


PRODUCTS = [
    ("golden", "Golden Selection"),
    ("golden-ok", "Golden Selection – økologisk"),
    ("premier", "Premier Selection"),
]


def product():
    rows = ""
    for slug, name in PRODUCTS:
        cells = ""
        for suffix, cap in [("original", "Original"), ("ai", "A.I."), ("ai-hvit", "A.I. – hvit bakgrunn")]:
            cells += f'<figure><img src="../img/oliven/oliven-{slug}-{suffix}.jpg" alt="Oliven {name} – {cap}" loading="lazy" width="1000" height="1500"><figcaption>{cap}</figcaption></figure>'
        rows += f'<div class="compare"><h3>{name}</h3><div class="compare-row">{cells}</div></div>'
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Produktfoto</h1>
    <p>Produktbilder for Oliven – ekstra virgin olivenolje, kaldpresset og ublandet.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Original og A.I. side om side</h2>
      <p>Vi fotograferte flaskene, og brukte deretter A.I. for å komplementere arbeidet: jevnere lys og bakgrunn, og nye varianter av samme bilde – som en ren, hvit bakgrunn til nettbutikken. Originalen er alltid utgangspunktet. A.I. gir kunden flere bilder ut av ett og samme opptak.</p>
    </div>
    {rows}
  </div>
</section>

<section class="section rust closing">
  <div class="wrap">
    <h2>Trenger produktene dine bedre bilder?</h2>
    {contact_buttons()}
  </div>
</section>
"""
    return page("produktfoto/", "Produktfoto for Oliven – original og A.I. side om side — Frame Forward",
                "Produktfoto av olivenolje for Oliven. Se originalbildene og A.I.-versjonene side om side – slik bruker Frame Forward A.I. til å komplementere arbeidet.",
                body, "produktfoto/")


def contact():
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Kontakt</h1>
    <p>Klar for innhold som stopper scrollingen? Send en melding, så får du svar direkte fra meg.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="ways">
      <a class="way" href="{WA}">{ICON_WA}<strong>WhatsApp</strong><span>Raskest – skriv kort hva du trenger</span></a>
      <a class="way" href="tel:{PHONE}">{ICON_PHONE}<strong>Ring</strong><span>{PHONE_DISPLAY}</span></a>
      <a class="way" href="mailto:{EMAIL}?subject=Foresp%C3%B8rsel%20fra%20nettsiden">{ICON_MAIL}<strong>E-post</strong><span>{EMAIL}</span></a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Slik jobber vi</h2></div>
    <ol class="steps">
      <li><h3>En kort samtale</h3><p>Du forteller om stedet ditt, målene og hva som har fungert før.</p></li>
      <li><h3>Et konkret forslag</h3><p>Du får en plan for innhold, opptak og pris – ingen overraskelser.</p></li>
      <li><h3>Opptak og publisering</h3><p>Jeg filmer, klipper og leverer innhold klart for feeden.</p></li>
    </ol>
  </div>
</section>
"""
    return page("contact/", "Kontakt – book innholdsproduksjon i Bergen — Frame Forward",
                "Ta kontakt med Frame Forward for video, Reels, TikTok og foto til restauranten eller bedriften din i Bergen. E-post: hello@frameforward.no",
                body, "contact/")


def notfound():
    body = """
<section class="page-head" style="min-height:60vh">
  <div class="wrap">
    <h1>Siden finnes ikke</h1>
    <p>Lenken kan være gammel. Gå til forsiden eller se arbeidet vårt.</p>
    <div class="btn-row" style="margin-top:28px"><a class="btn" href="/">Til forsiden</a><a class="btn ghost" href="/ourwork/">Vårt arbeid</a></div>
  </div>
</section>"""
    return page("", "Siden finnes ikke — Frame Forward", "Siden finnes ikke.", body, None, root="/")


def main():
    (SITE / "index.html").write_text(home(), encoding="utf-8")
    (SITE / "ourwork" / "index.html").write_text(work(), encoding="utf-8")
    (SITE / "proven-impact" / "index.html").write_text(impact(), encoding="utf-8")
    (SITE / "contact" / "index.html").write_text(contact(), encoding="utf-8")
    (SITE / "produktfoto" / "index.html").write_text(product(), encoding="utf-8")
    (SITE / "404.html").write_text(notfound(), encoding="utf-8")
    # The CNAME file (frameforward.no) is added when the domain is moved from Squarespace.
    (SITE / ".nojekyll").write_text("")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{DOMAIN}/{p}</loc></url>" for p in ["", "ourwork/", "produktfoto/", "proven-impact/", "contact/"])
    (SITE / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    print("built")


if __name__ == "__main__":
    main()
