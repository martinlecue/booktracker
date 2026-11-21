#!/usr/bin/env python3
"""Génère le site BookTracker (anglais à la racine, français sous /fr/) dans public/.

Usage : python3 build.py
Les textes sont dans le dictionnaire T ci-dessous ; la mise en page dans les fonctions page_*.
"""
from pathlib import Path
from html import escape

SITE_URL = "https://booktracker.martin-lecue.site"  # adresse publique du site (domaine perso branché sur Firebase Hosting), sans / final
SITE_HOST = SITE_URL.split("//", 1)[1]
CONTACT = "mail@martin-lecue.site"
APP_ID = "6761607240"
APPSTORE = f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt=128656298&ct=website&mt=8"
YEAR = 2026
OUT = Path(__file__).parent / "public"

APPLE_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>')

ICONS = {
    "scan": '<path d="M4 7V5a1 1 0 0 1 1-1h2M17 4h2a1 1 0 0 1 1 1v2M20 17v2a1 1 0 0 1-1 1h-2M7 20H5a1 1 0 0 1-1-1v-2"/><path d="M8 8v8M11 8v8M14 8v8M17 8v8"/>',
    "timer": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6"/>',
    "flame": '<path d="M12 22c4 0 7-2.7 7-6.8 0-3.7-2.6-6.3-4.3-8.6-.4 2.3-1.5 3.6-2.7 4.2C12 7.6 10.6 4.6 8.4 2.5 8.4 6.6 5 9.4 5 14.6 5 18.9 8 22 12 22z"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "story": '<rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M9 6.5h6M9 17.5h6"/><path d="M10 10.5l2-1.5 2 1.5v3l-2-1.2-2 1.2z"/>',
    "widget": '<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="18" height="8" rx="2"/>',
}

T = {
    "en": {
        "lang": "en", "prefix": "", "locale": "en_US",
        "title": "BookTracker — Reading tracker for iPhone & iPad",
        "desc": "Track your books, build a daily reading habit and see your year in books. Scan ISBNs, time your sessions with ambient sounds, keep your streak and level up.",
        "get": "Get the app",
        "dl_small": "Download on the", "dl_big": "App Store",
        "eyebrow": "Your reading companion",
        "h1": 'Read more,<br><span class="grad">every day.</span>',
        "lead": "BookTracker turns reading into a habit you actually keep. Add a book in seconds, time your sessions, watch your streak grow and look back on your year in books.",
        "note": "Free on iPhone and iPad · 7 languages",
        "hero_img": "en-01-accueil.jpg", "hero_alt": "BookTracker home screen with a reading streak, XP level and current reads",
        "gal_kicker": "Inside the app", "gal_title": "Designed to make you want to read.",
        "gallery": [
            ("02-decouvrir", "Discover, search and scan"),
            ("03-fiche", "Every detail of a book"),
            ("04-chrono", "Reading timer"),
            ("05-stats", "Your stats"),
            ("06-recap", "Your year in books"),
        ],
        "feat_kicker": "Features", "feat_title": "Everything you need, nothing you don't.",
        "features": [
            ("scan", "Scan, search or import", "Scan an ISBN barcode, search by title or author, or bring your whole Goodreads or StoryGraph library in one go."),
            ("timer", "Reading timer", "A calm timer with ambient sounds (rain, forest, fireplace) that logs your pages and minutes for you."),
            ("flame", "Streaks, XP and levels", "Every page earns XP. Keep your daily streak alive and level up as you read."),
            ("chart", "Stats and goals", "Books, pages, reading pace and a yearly goal, all in clear, beautiful charts."),
            ("story", "Your year in books", "A story-style recap of your reading year, ready to share with your friends."),
            ("widget", "Widgets, reminders, sync", "Home Screen widgets, a gentle daily reminder and your library synced across iPhone and iPad."),
        ],
        "price_kicker": "Pricing", "price_title": "Start free. Go Premium when you're hooked.",
        "price_text": "No ads, no account selling, no tricks. Download BookTracker for free and upgrade only if you want more.",
        "plans": [
            ("Free", "Download for free and track up to 10 books in your library."),
            ("Premium", "Unlimited books, shelves, reviews, ambient sounds and more. Monthly subscription or a one-time lifetime purchase."),
        ],
        "band_title": "Your next book is waiting.",
        "band_text": "Free, ad-free, in 7 languages.",
        "nav_home": "Home", "nav_privacy": "Privacy Policy", "nav_support": "Support",
        "rights": "All rights reserved.",
        # Support
        "sup_title": "Support",
        "sup_desc": "Help and answers about BookTracker, the reading tracker for iPhone and iPad.",
        "sup_lead": "A question, a bug, an idea? Check the answers below or write to me directly. I read every message and usually reply within a couple of days.",
        "sup_btn": "Email support",
        "sup_faq": "Frequently asked questions",
        "faq": [
            ("Is BookTracker free?", "Yes. You can download it for free and track up to 10 books. BookTracker Premium unlocks an unlimited library and extras like shelves, reviews and ambient sounds, as a monthly subscription or a one-time lifetime purchase."),
            ("How do I import my books from Goodreads or StoryGraph?", "First export your library as a CSV file. On Goodreads: My Books → Import and export → Export Library. On StoryGraph: Manage Account → Export StoryGraph Library. Then, in BookTracker, open Discover, tap “Import list” and choose the file. Your ratings, reading dates and statuses come along."),
            ("I bought Premium but it isn't active.", "Open the Premium screen and tap “Restore purchases”, using the same Apple Account you paid with. If it still doesn't work, email me with the date of the purchase."),
            ("Does BookTracker work on iPad?", "Yes, on iPhone and iPad. Sign in with the same account and your library syncs between your devices."),
            ("How do I delete my account?", "In the app, open your Profile and tap “Delete my account”. Your online data is erased. For security reasons, the app may ask you to sign in again first."),
            ("Which languages are available?", "English, French, German, Spanish, Italian, Brazilian Portuguese and Dutch. BookTracker follows your iPhone's language."),
        ],
        # Privacy
        "pp_title": "Privacy Policy",
        "pp_desc": "How BookTracker collects, uses and protects your personal data.",
        "pp_updated": "Last updated: November 20, 2026",
        "pp_html": """
<h2>Introduction</h2>
<p>This privacy policy explains how BookTracker (“the App”), published by Martin Le Cué, collects, uses and protects your personal information.</p>
<div class="summary"><p><strong>In short:</strong> we only collect what the App needs to work. We never sell your data, and there are no ads in the App.</p></div>

<h2>Information we collect</h2>
<ul>
<li><strong>Account information</strong>: email address and display name, provided when you sign up through Firebase Authentication (email or Sign in with Apple).</li>
<li><strong>Library data</strong>: the books you add, reading statuses, notes, ratings, reviews and progress.</li>
<li><strong>Reading sessions</strong>: pages read, duration and date of each session.</li>
<li><strong>Goals, shelves and achievements</strong> you create or earn in the App.</li>
<li><strong>Social features (optional)</strong>: if you choose a username and add reading buddies, your username and your reading activity (book started, pages read, book finished) are visible to the friends you connect with.</li>
<li><strong>Creator code (optional)</strong>: if you enter a creator's code, it is attached to your purchases so that creator can be thanked.</li>
</ul>
<p>We do not collect your location, contacts or photos. The camera is only used, on your device, to scan a book's barcode.</p>

<h2>How we use your information</h2>
<ul>
<li>Sync your library across your devices</li>
<li>Show your statistics, streaks and reading progress</li>
<li>Let you sign in and access your account</li>
<li>Provide the optional social features you turn on</li>
</ul>

<h2>Third-party services</h2>
<ul>
<li><strong>Firebase (Google)</strong>: authentication and data storage. <a href="https://firebase.google.com/support/privacy" rel="noopener">Firebase privacy</a></li>
<li><strong>RevenueCat</strong>: in-app purchase and subscription management. <a href="https://www.revenuecat.com/privacy" rel="noopener">RevenueCat privacy</a></li>
<li><strong>Google Books API</strong> and <strong>Open Library</strong>: book search, covers and details. Only your search terms are sent. <a href="https://policies.google.com/privacy" rel="noopener">Google privacy</a> · <a href="https://archive.org/about/terms" rel="noopener">Open Library terms</a></li>
</ul>
<p>Some book pages include a link to buy the book on Amazon. These are affiliate links: if you tap one, Amazon may know you came from BookTracker, under Amazon's own privacy policy. No personal data is sent by the App.</p>

<h2>Storage and security</h2>
<p>Your data is stored on Firebase servers (Google Cloud). We use standard security measures to protect it against unauthorised access, alteration or disclosure.</p>
<p>Data is kept as long as your account is active. You can delete your account at any time from your Profile in the App (“Delete my account”); your online data is then erased.</p>

<h2>In-app purchases</h2>
<p>BookTracker offers in-app purchases (monthly subscription and lifetime access). Payments are processed by Apple through the App Store and managed with RevenueCat. We never see or store your payment details.</p>

<h2>Your rights</h2>
<p>Under the GDPR and similar laws, you have the right to access, correct, delete and export your personal data (CSV export is available in the App). To exercise these rights, contact us at the address below.</p>

<h2>Children</h2>
<p>BookTracker is not intended for children under 13. We do not knowingly collect personal data from children. If you think a child has given us data, please contact us.</p>

<h2>Changes to this policy</h2>
<p>We may update this policy. Changes will be posted on this page with a new date.</p>

<h2>Contact</h2>
<p>Martin Le Cué<br>Email: <a href="mailto:{contact}">{contact}</a></p>
""",
    },
    "fr": {
        "lang": "fr", "prefix": "fr/", "locale": "fr_FR",
        "title": "BookTracker — Suivi de lecture pour iPhone et iPad",
        "desc": "Suis tes livres, prends l'habitude de lire chaque jour et revis ton année de lecture. Scan ISBN, chrono avec sons d'ambiance, séries quotidiennes et niveaux.",
        "get": "Télécharger",
        "dl_small": "Télécharger dans", "dl_big": "l'App Store",
        "eyebrow": "Ton compagnon de lecture",
        "h1": 'Lis plus,<br><span class="grad">chaque jour.</span>',
        "lead": "BookTracker fait de la lecture une habitude qui tient. Ajoute un livre en quelques secondes, chronomètre tes sessions, regarde ta série grandir et revis ton année en livres.",
        "note": "Gratuit sur iPhone et iPad · 7 langues",
        "hero_img": "fr-01-accueil.jpg", "hero_alt": "Écran d'accueil de BookTracker avec la série de lecture, le niveau et les lectures en cours",
        "gal_kicker": "Dans l'app", "gal_title": "Pensée pour donner envie de lire.",
        "gallery": [
            ("02-decouvrir", "Découvrir, chercher, scanner"),
            ("03-fiche", "Tout sur un livre"),
            ("04-chrono", "Chrono de lecture"),
            ("05-stats", "Tes statistiques"),
            ("06-recap", "Ton année en livres"),
        ],
        "feat_kicker": "Fonctionnalités", "feat_title": "Tout ce qu'il faut, rien de trop.",
        "features": [
            ("scan", "Scanne, cherche ou importe", "Scanne le code-barres ISBN, cherche par titre ou auteur, ou importe toute ta bibliothèque Goodreads ou StoryGraph d'un coup."),
            ("timer", "Chrono de lecture", "Un minuteur apaisant avec sons d'ambiance (pluie, forêt, cheminée) qui note tes pages et tes minutes à ta place."),
            ("flame", "Séries, XP et niveaux", "Chaque page rapporte de l'XP. Garde ta série quotidienne et monte de niveau en lisant."),
            ("chart", "Statistiques et objectifs", "Livres, pages, rythme de lecture et objectif annuel, dans des graphiques clairs."),
            ("story", "Ton année en livres", "Un récap façon story de ton année de lecture, prêt à partager avec tes amis."),
            ("widget", "Widgets, rappels, synchro", "Widgets sur l'écran d'accueil, rappel quotidien et bibliothèque synchronisée entre iPhone et iPad."),
        ],
        "price_kicker": "Tarifs", "price_title": "Gratuit pour commencer. Premium quand tu es accro.",
        "price_text": "Pas de pub, pas de revente de données, pas de piège. Télécharge BookTracker gratuitement et passe à Premium seulement si tu veux plus.",
        "plans": [
            ("Gratuit", "Téléchargement gratuit, jusqu'à 10 livres dans ta bibliothèque."),
            ("Premium", "Livres illimités, étagères, avis, ambiances sonores et plus. Abonnement mensuel ou achat unique à vie."),
        ],
        "band_title": "Ton prochain livre t'attend.",
        "band_text": "Gratuit, sans pub, en 7 langues.",
        "nav_home": "Accueil", "nav_privacy": "Confidentialité", "nav_support": "Assistance",
        "rights": "Tous droits réservés.",
        "sup_title": "Assistance",
        "sup_desc": "Aide et réponses sur BookTracker, l'app de suivi de lecture pour iPhone et iPad.",
        "sup_lead": "Une question, un bug, une idée ? Regarde les réponses ci-dessous ou écris-moi directement. Je lis chaque message et réponds en général sous deux jours.",
        "sup_btn": "Écrire à l'assistance",
        "sup_faq": "Questions fréquentes",
        "faq": [
            ("BookTracker est-il gratuit ?", "Oui. L'app se télécharge gratuitement et permet de suivre jusqu'à 10 livres. BookTracker Premium débloque une bibliothèque illimitée et des extras comme les étagères, les avis et les ambiances sonores, en abonnement mensuel ou en achat unique à vie."),
            ("Comment importer mes livres depuis Goodreads ou StoryGraph ?", "Exporte d'abord ta bibliothèque en fichier CSV. Sur Goodreads : My Books → Import and export → Export Library. Sur StoryGraph : Manage Account → Export StoryGraph Library. Ensuite, dans BookTracker, ouvre Découvrir, touche « Importer liste » et choisis le fichier. Tes notes, dates de lecture et statuts suivent."),
            ("J'ai acheté Premium mais il n'est pas actif.", "Ouvre l'écran Premium et touche « Restaurer mes achats », avec le même compte Apple que celui de l'achat. Si ça ne marche toujours pas, écris-moi en précisant la date de l'achat."),
            ("BookTracker fonctionne-t-il sur iPad ?", "Oui, sur iPhone et iPad. Connecte-toi avec le même compte et ta bibliothèque se synchronise entre tes appareils."),
            ("Comment supprimer mon compte ?", "Dans l'app, ouvre ton Profil et touche « Supprimer mon compte ». Tes données en ligne sont effacées. Par sécurité, l'app peut te demander de te reconnecter avant."),
            ("Quelles langues sont disponibles ?", "Français, anglais, allemand, espagnol, italien, portugais du Brésil et néerlandais. BookTracker suit la langue de ton iPhone."),
        ],
        "pp_title": "Politique de confidentialité",
        "pp_desc": "Comment BookTracker collecte, utilise et protège tes données personnelles.",
        "pp_updated": "Dernière mise à jour : 20 novembre 2026",
        "pp_html": """
<h2>Introduction</h2>
<p>Cette politique de confidentialité explique comment BookTracker (« l'Application »), éditée par Martin Le Cué, collecte, utilise et protège vos informations personnelles.</p>
<div class="summary"><p><strong>En résumé :</strong> nous collectons uniquement ce dont l'Application a besoin pour fonctionner. Nous ne vendons jamais vos données et l'Application ne contient aucune publicité.</p></div>

<h2>Informations collectées</h2>
<ul>
<li><strong>Informations de compte</strong> : adresse e-mail et nom d'affichage, fournis à l'inscription via Firebase Authentication (e-mail ou Se connecter avec Apple).</li>
<li><strong>Données de bibliothèque</strong> : livres ajoutés, statuts de lecture, notes, évaluations, avis et progression.</li>
<li><strong>Sessions de lecture</strong> : pages lues, durée et date de chaque session.</li>
<li><strong>Objectifs, étagères et succès</strong> que vous créez ou obtenez dans l'Application.</li>
<li><strong>Fonctions sociales (facultatives)</strong> : si vous choisissez un pseudo et ajoutez des amis lecteurs, votre pseudo et votre activité de lecture (livre commencé, pages lues, livre terminé) sont visibles par les amis avec qui vous êtes connecté.</li>
<li><strong>Code créateur (facultatif)</strong> : si vous saisissez le code d'un créateur, il est associé à vos achats pour que ce créateur puisse être remercié.</li>
</ul>
<p>Nous ne collectons ni votre localisation, ni vos contacts, ni vos photos. L'appareil photo sert uniquement, sur votre appareil, à scanner le code-barres d'un livre.</p>

<h2>Utilisation des informations</h2>
<ul>
<li>Synchroniser votre bibliothèque entre vos appareils</li>
<li>Afficher vos statistiques, séries et progression de lecture</li>
<li>Vous permettre de vous connecter à votre compte</li>
<li>Fournir les fonctions sociales facultatives que vous activez</li>
</ul>

<h2>Services tiers</h2>
<ul>
<li><strong>Firebase (Google)</strong> : authentification et stockage des données. <a href="https://firebase.google.com/support/privacy" rel="noopener">Confidentialité Firebase</a></li>
<li><strong>RevenueCat</strong> : gestion des achats intégrés et abonnements. <a href="https://www.revenuecat.com/privacy" rel="noopener">Confidentialité RevenueCat</a></li>
<li><strong>API Google Books</strong> et <strong>Open Library</strong> : recherche de livres, couvertures et informations. Seuls vos termes de recherche sont transmis. <a href="https://policies.google.com/privacy" rel="noopener">Confidentialité Google</a> · <a href="https://archive.org/about/terms" rel="noopener">Conditions Open Library</a></li>
</ul>
<p>Certaines fiches livres proposent un lien pour acheter le livre sur Amazon. Ce sont des liens d'affiliation : si vous en touchez un, Amazon peut savoir que vous venez de BookTracker, selon sa propre politique de confidentialité. L'Application ne transmet aucune donnée personnelle.</p>

<h2>Stockage et sécurité</h2>
<p>Vos données sont stockées sur les serveurs de Firebase (Google Cloud). Nous appliquons des mesures de sécurité standards pour les protéger contre tout accès non autorisé, altération ou divulgation.</p>
<p>Les données sont conservées tant que votre compte est actif. Vous pouvez supprimer votre compte à tout moment depuis votre Profil dans l'Application (« Supprimer mon compte ») ; vos données en ligne sont alors effacées.</p>

<h2>Achats intégrés</h2>
<p>BookTracker propose des achats intégrés (abonnement mensuel et accès à vie). Les paiements sont traités par Apple via l'App Store et gérés avec RevenueCat. Nous ne voyons ni ne stockons jamais vos informations de paiement.</p>

<h2>Vos droits</h2>
<p>Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement et de portabilité de vos données (export CSV disponible dans l'Application). Pour les exercer, contactez-nous à l'adresse ci-dessous. Vous pouvez aussi adresser une réclamation à la CNIL.</p>

<h2>Mineurs</h2>
<p>BookTracker n'est pas destiné aux enfants de moins de 13 ans. Nous ne collectons pas sciemment de données personnelles auprès de mineurs. Si vous pensez qu'un mineur nous a fourni des données, contactez-nous.</p>

<h2>Modifications</h2>
<p>Nous pouvons mettre à jour cette politique. Les modifications seront publiées sur cette page avec une nouvelle date.</p>

<h2>Contact</h2>
<p>Martin Le Cué<br>E-mail : <a href="mailto:{contact}">{contact}</a></p>
""",
    },
}

PAGES = {"home": "", "privacy": "privacy-policy.html", "support": "support.html"}


def url(lang, page):
    return f"{SITE_URL}/{T[lang]['prefix']}{PAGES[page]}"


def rel(lang_from, lang_to, page):
    """Lien relatif d'une page de lang_from vers la page équivalente en lang_to."""
    up = "../" if T[lang_from]["prefix"] else ""
    target = T[lang_to]["prefix"] + PAGES[page]
    return (up + target) or "./"


def appstore_button(t):
    return (f'<a class="appstore" href="{APPSTORE}" aria-label="{escape(t["dl_small"])} {escape(t["dl_big"])}">'
            f'{APPLE_SVG}<span><small>{t["dl_small"]}</small><strong>{t["dl_big"]}</strong></span></a>')


def layout(lang, page, title, desc, body, robots_extra=""):
    t = T[lang]
    up = "../" if t["prefix"] else ""
    other = "fr" if lang == "en" else "en"
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{url(l, page)}">' for l in ("en", "fr"))
    alt += f'<link rel="alternate" hreflang="x-default" href="{url("en", page)}">'
    pref_js = ""
    if lang == "en" and page == "home":
        # Visiteur francophone sans préférence enregistrée : on propose directement la version française.
        pref_js = ("<script>try{var p=localStorage.getItem('bt-lang');"
                   "if(!p&&/^fr\\b/i.test(navigator.language||'')){location.replace('fr/');}}catch(e){}</script>")
    lang_links = (f'<nav class="lang" aria-label="Language">'
                  f'<a href="{rel(lang, "en", page)}" hreflang="en" lang="en" data-lang="en" aria-current="{str(lang == "en").lower()}">EN</a>'
                  f'<a href="{rel(lang, "fr", page)}" hreflang="fr" lang="fr" data-lang="fr" aria-current="{str(lang == "fr").lower()}">FR</a>'
                  f'</nav>')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url(lang, page)}">
<script>if(/\.(web\.app|firebaseapp\.com)$/.test(location.hostname)){{location.replace("https://{SITE_HOST}"+location.pathname+location.search+location.hash);}}</script>
{alt}
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta name="msvalidate.01" content="07277EAEC65A68B22AFDDA81D904E2AE">
<meta name="theme-color" content="#f6f5ff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e0d24" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BookTracker">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url(lang, page)}">
<meta property="og:image" content="{SITE_URL}/assets/img/og.jpg">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" href="{up}favicon.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/style.css?v=2">
{pref_js}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{rel(lang, lang, 'home')}"><img src="{up}assets/img/icon-256.png" alt="" width="32" height="32">BookTracker</a>
<div class="top-right">{lang_links}<a class="btn-get" href="{APPSTORE}">{t['get']}</a></div>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<nav>
<a href="{rel(lang, lang, 'home')}">{t['nav_home']}</a>
<a href="{rel(lang, lang, 'support')}">{t['nav_support']}</a>
<a href="{rel(lang, lang, 'privacy')}">{t['nav_privacy']}</a>
<a href="{APPSTORE}">App Store</a>
</nav>
<p>© {YEAR} Martin Le Cué. {t['rights']}</p>
</div></footer>
<script>document.querySelectorAll('.lang a').forEach(function(a){{a.addEventListener('click',function(){{try{{localStorage.setItem('bt-lang',a.dataset.lang)}}catch(e){{}}}})}});</script>
</body>
</html>
"""


def svg_icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def page_home(lang):
    t = T[lang]
    up = "../" if t["prefix"] else ""
    gallery = "".join(
        f'<figure><img src="{up}assets/img/{lang}-{key}.jpg" alt="{escape(cap)}" width="598" height="1300" loading="lazy" decoding="async">'
        f'<figcaption>{escape(cap)}</figcaption></figure>' for key, cap in t["gallery"])
    feats = "".join(
        f'<article class="feature"><div class="ficon">{svg_icon(ic)}</div><h3>{escape(h)}</h3><p>{escape(p)}</p></article>'
        for ic, h, p in t["features"])
    plans = "".join(
        f'<div class="plan{" hl" if i == 1 else ""}"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>'
        for i, (h, p) in enumerate(t["plans"]))
    body = f"""
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow">{t['eyebrow']}</span>
<h1>{t['h1']}</h1>
<p class="lead">{escape(t['lead'])}</p>
<div class="ctas">{appstore_button(t)}<span class="note">{escape(t['note'])}</span></div>
</div>
<div class="hero-shot"><img src="{up}assets/img/{t['hero_img']}" alt="{escape(t['hero_alt'])}" width="598" height="1300" fetchpriority="high"></div>
</div></section>

<section id="screens"><div class="wrap">
<p class="kicker">{t['gal_kicker']}</p>
<h2>{t['gal_title']}</h2>
<div class="gallery">{gallery}</div>
</div></section>

<section id="features"><div class="wrap">
<p class="kicker">{t['feat_kicker']}</p>
<h2>{t['feat_title']}</h2>
<div class="features">{feats}</div>
</div></section>

<section id="pricing"><div class="wrap">
<div class="pricing">
<div><p class="kicker" style="color:#b7b2ff">{t['price_kicker']}</p><h2>{t['price_title']}</h2><p>{escape(t['price_text'])}</p></div>
<div>{plans}</div>
</div>
</div></section>

<section class="band"><div class="wrap">
<img src="{up}assets/img/icon-256.png" alt="" width="84" height="84" loading="lazy">
<h2>{t['band_title']}</h2>
<p class="sub" style="margin:0 auto 26px">{escape(t['band_text'])}</p>
<div class="ctas">{appstore_button(t)}</div>
</div></section>
"""
    return layout(lang, "home", t["title"], t["desc"], body)


def page_support(lang):
    t = T[lang]
    faq = "".join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in t["faq"])
    body = f"""
<div class="doc">
<h1>{t['sup_title']}</h1>
<p class="lead">{escape(t['sup_lead'])}</p>
<div class="contact-box"><a class="btn-mail" href="mailto:{CONTACT}?subject=BookTracker">{t['sup_btn']}</a><span class="note">{CONTACT}</span></div>
<h2 style="margin-top:44px">{t['sup_faq']}</h2>
<div class="faq">{faq}</div>
</div>
"""
    return layout(lang, "support", f"{t['sup_title']} — BookTracker", t["sup_desc"], body)


def page_privacy(lang):
    t = T[lang]
    body = f"""
<div class="doc">
<h1>{t['pp_title']}</h1>
<p class="meta">BookTracker · {t['pp_updated']}</p>
<div class="card">{t['pp_html'].replace('{contact}', CONTACT)}</div>
</div>
"""
    return layout(lang, "privacy", f"{t['pp_title']} — BookTracker", t["pp_desc"], body)


def main():
    for lang in ("en", "fr"):
        base = OUT / T[lang]["prefix"]
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(page_home(lang), encoding="utf-8")
        (base / "privacy-policy.html").write_text(page_privacy(lang), encoding="utf-8")
        (base / "support.html").write_text(page_support(lang), encoding="utf-8")
    (OUT / "404.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — BookTracker</title><meta name="robots" content="noindex">
<link rel="icon" type="image/png" href="/favicon.png"><link rel="stylesheet" href="/assets/style.css?v=2"></head>
<body><main class="doc" style="text-align:center;padding-top:96px">
<img src="/assets/img/icon-256.png" alt="" width="84" height="84" style="margin:0 auto 20px;border-radius:20px">
<h1>Page not found</h1><p class="lead" style="margin:0 auto 24px">This page doesn't exist (anymore).<br><span lang="fr">Cette page n'existe pas (ou plus).</span></p>
<p><a class="btn-mail" href="/">BookTracker</a></p>
</main></body></html>
""", encoding="utf-8")
    # Vérification Google Search Console (ne pas supprimer).
    (OUT / "google48537651521c34e2.html").write_text("google-site-verification: google48537651521c34e2.html", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    urls = "".join(f"<url><loc>{url(l, p)}</loc></url>" for l in ("en", "fr") for p in PAGES)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    print("Site généré dans", OUT)


def gh_redirects():
    """Remplace les anciennes pages GitHub Pages (racine du dépôt) par des redirections vers le nouveau site."""
    root = Path(__file__).parent
    targets = {
        "index.html": "",
        "landingpage": "",
        "404.html": "",
        "privacy-policy.html": "privacy-policy.html",
        "privacy-policy": "privacy-policy.html",
    }
    for name, page in targets.items():
        en = f"{SITE_URL}/{page}"
        fr = f"{SITE_URL}/fr/{page}"
        (root / name).write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BookTracker has moved</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{en}">
<meta http-equiv="refresh" content="0; url={en}">
<script>location.replace(/^fr\\b/i.test(navigator.language||'') ? "{fr}" : "{en}");</script>
</head>
<body>
<p>BookTracker has moved to <a href="{en}">{en}</a>.</p>
<p lang="fr">BookTracker a déménagé : <a href="{fr}">{fr}</a>.</p>
</body>
</html>
""", encoding="utf-8")
    print("Redirections GitHub Pages écrites vers", SITE_URL)


if __name__ == "__main__":
    import sys
    if "--gh-redirects" in sys.argv:
        gh_redirects()
    else:
        main()
