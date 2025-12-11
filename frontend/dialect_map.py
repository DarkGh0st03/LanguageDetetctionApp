# Questo file mappa le etichette dei dialetti e delle lingue
# strettamente correlate alle loro lingue madri per "raggruppare"
# l'output e renderlo più user-friendly.

DIALECT_TO_PARENT = {
    # === Gruppo Inglese (Aggiornato) ===
    "cor": "eng",  # Cornish
    "sco": "eng",  # Scots
    "ang": "eng",  # Old English
    "jam": "eng",  # Jamaican Patois
    "srn": "eng",  # Sranan
    "cym": "eng",  # Welsh (Gallese)
    "gla": "eng",  # Scottish Gaelic
    "gle": "eng",  # Irish
    
    # === Gruppo Serbo-Croato ===
    # Usiamo 'hbs' (Serbo-Croatian) come genitore
    "bos": "hbs",  # Bosnian
    "hrv": "hbs",  # Croatian
    "srp": "hbs",  # Serbian
    
    # === Gruppo Malese/Indonesiano ===
    "ind": "msa",  # Indonesian
    "map-bms": "msa", # Banyumasan
    "bjn": "msa",  # Banjar
    "min": "msa",  # Minangkabau

    # === Gruppo Hindi ===
    "urd": "hin",  # Urdu
    "hif": "hin",  # Fiji Hindi
    "bho": "hin",  # Bhojpuri

    # === Gruppo Filippino ===
    "pam": "tgl",  # Pampanga
    "ceb": "tgl",  # Cebuano
    "war": "tgl",  # Waray
    "bcl": "tgl",  # Central Bikol
    "ilo": "tgl",  # Iloko

    # === Gruppo Portoghese ===
    "glg": "por",  # Galician
    
    # Dialetti/Lingue Italiane -> Italiano
    "scn": "ita",  # Sicilian
    "nap": "ita",  # Neapolitan
    "lij": "ita",  # Ligurian
    "vec": "ita",  # Venetian
    "lmo": "ita",  # Lombard
    "fur": "ita",  # Friulian
    "srd": "ita",  # Sardinian
    "roa-tara": "ita", # Tarantino
    "egl": "ita",  # Emilian
    "cos": "ita",  # Corsican
    
    # Dialetti/Lingue Germaniche -> Tedesco
    "als": "deu",  # Alemannic German
    "bar": "deu",  # Bavarian
    "ksh": "deu",  # Ripuarisch (Kölsch)
    "pdc": "deu",  # Pennsylvania German
    "pfl": "deu",  # Palatine German
    "nds": "deu",  # Low German
    "stq": "deu",  # Saterfriesisch
    "ltz": "deu",  # Luxembourgish
    "yid": "deu",  # Yiddish
    
    # Dialetti/Lingue Olandesi -> Olandese
    "nds-nl": "nld", # West Low German (Nedersaksisch)
    "zea": "nld",    # Zeeuws
    "vls": "nld",    # Vlaams
    "lim": "nld",    # Limburgan
    "fry": "nld",    # Western Frisian

    # Varianti Cinesi -> Cinese Standard
    "zh-yue": "zho", # Cantonese
    "nan": "zho",    # Min Nan Chinese
    "wuu": "zho",    # Wu Chinese
    "cdo": "zho",    # Min Dong
    "hak": "zho",    # Hakka Chinese
    "lzh": "zho",    # Literary Chinese
    
    # Arabo -> Arabo
    "arz": "ara",    # Egyptian Arabic
    "mlt": "ara",    # Maltese
    
    # Punjabi -> Punjabi
    "pnb": "pan",    # Western Panjabi
    
    # Francese -> Francese
    "frp": "fra",    # Arpitan
    "pcd": "fra",    # Picard
    "wln": "fra",    # Walloon
    "oci": "fra",    # Occitan
    "hat": "fra",    # Haitian Creole
    
    # Spagnolo -> Spagnolo
    "lad": "spa",    # Ladino
    "ext": "spa",    # Extremaduran
    "arg": "spa",    # Aragonese
    "ast": "spa",    # Asturian
    
    # Norvegese
    "nno": "nob",    # Norwegian Nynorsk -> Bokmål
}