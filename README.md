# BookTracker — site web

Site vitrine de l'app iOS BookTracker, en anglais (racine) et en français (`/fr/`).
Hébergé sur Firebase Hosting (projet `booktracker-692cb`, site `booktracker-reader`) : https://booktracker-reader.web.app

- Textes et mise en page : `build.py` (dictionnaire `T`). Générer : `python3 build.py` → dossier `public/`.
- Aperçu local : `python3 -m http.server 8765 --directory public`, puis http://127.0.0.1:8765
- Mise en ligne : `firebase deploy --only hosting`
- Les fichiers à la racine du dépôt (`index.html`, `privacy-policy.html`, …) ne sont plus que des redirections
  GitHub Pages vers le nouveau site (`python3 build.py --gh-redirects`).
