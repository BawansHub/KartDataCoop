import folium
from jinja2 import Template
import re

# Coop-lagerdata
lager_data = [
    {
        "navn": "C-Log (Gardermoen)",
        "adresse": "Vilbergvegen 130, 2067 Jessheim",
        "beskrivelse": "Hovedlager, høy trafikk, moderne og automatisert. Nær E6 og Oslo Lufthavn.",
        "koordinater": [60.18024352472979, 11.158885611257535],
        "adt": "50 000+ kjøretøy per døgn",
        "inntjening": "1,250,000 kr per dag"
    },
    {
        "navn": "Langhus (Viken)",
        "adresse": "Regnbueveien 5, 1405 Langhus",
        "beskrivelse": "Automatisert logistikksenter nær E6, sør for Oslo.",
        "koordinater": [59.77134150117978, 10.842567540069313],
        "adt": "35 000–45 000 kjøretøy per døgn",
        "inntjening": "1,125,000 kr per dag"
    },
    {
        "navn": "Trondheim Regionlager",
        "adresse": "Østre Rosten 108, 7075 Tiller",
        "beskrivelse": "Regionlager for Midt-Norge. God tilgjengelighet til E6.",
        "koordinater": [63.341171780178996, 10.36926375562959],
        "adt": "25 000–30 000 kjøretøy per døgn",
        "inntjening": "750,000 kr per dag"
    },
    {
        "navn": "Stavanger Regionlager",
        "adresse": "Nesflåtveien 4, 4018 Stavanger",
        "beskrivelse": "Regionlager for Sørvestlandet. Ligger i trafikkert næringsområde.",
        "koordinater": [58.93242369678288, 5.742498482347647],
        "adt": "20 000–25 000 kjøretøy per døgn",
        "inntjening": "625,000 kr per dag"
    },
    {
        "navn": "Bergen Regionlager",
        "adresse": "Sandbrekkevegen 81, 5225 Nesttun",
        "beskrivelse": "Regionlager med god tilgang til hovedveinettet i Bergen.",
        "koordinater": [60.32525961860274, 5.363368011266229],
        "adt": "30 000–35 000 kjøretøy per døgn",
        "inntjening": "875,000 kr per dag"
    },
    {
        "navn": "Tromsø Regionlager",
        "adresse": "Ringvegen 770, 9015 Tromsø",
        "beskrivelse": "Regionlager for Nord-Norge. Viktig knutepunkt i nord.",
        "koordinater": [69.67886854794241, 18.924602313704195],
        "adt": "15 000–20 000 kjøretøy per døgn",
        "inntjening": "500,000 kr per dag"
    }
]

# Ønskede CoopGo-lokasjoner i høytrafikkområder
coopgo_steder = [
    {
        "navn": "E6 Alnabru, Oslo",
        "koordinater": [59.9245, 10.8232],
        "adt": "Over 100 000 kjøretøy per døgn",
        "inntjening": "2,500,000 kr per dag"
    },
    {
        "navn": "E18 Skøyen, Bærum",
        "koordinater": [59.9171, 10.6750],
        "adt": "Opp mot 90 000 kjøretøy per døgn",
        "inntjening": "2,250,000 kr per dag"
    },
    {
        "navn": "Ring 3 Ryen-krysset, Oslo",
        "koordinater": [59.8896, 10.8052],
        "adt": "70 700 kjøretøy per døgn",
        "inntjening": "1,767,500 kr per dag"
    },
    {
        "navn": "E6 Sluppen, Trondheim",
        "koordinater": [63.4051, 10.3918],
        "adt": "47 500 kjøretøy per døgn",
        "inntjening": "1,187,500 kr per dag"
    },
    {
        "navn": "E39 Forus, Stavanger",
        "koordinater": [58.8955, 5.7316],
        "adt": "Over 57 000 kjøretøy per døgn",
        "inntjening": "1,425,000 kr per dag"
    },
    {
        "navn": "E39 Lagunen, Bergen",
        "koordinater": [60.2962, 5.3479],
        "adt": "Ukjent",
        "inntjening": "Estimert basert på lokasjon"
    }
]

# Lag kart
kart = folium.Map(location=[63.4, 10.4], zoom_start=5)

# Grønne markører – lager
for lager in lager_data:
    popup_html = f"""
    <strong>{lager['navn']}</strong><br>
    Adresse: {lager['adresse']}<br>
    {lager['beskrivelse']}<br><br>
    <strong>ÅDT:</strong> {lager['adt']}<br>
    <strong>Est. inntjening:</strong> {lager['inntjening']}
    """
    folium.Marker(
        location=lager["koordinater"],
        popup=popup_html,
        icon=folium.Icon(color="green", icon="shopping-cart", prefix="fa")
    ).add_to(kart)

# Røde markører – CoopGo-stasjoner
for sted in coopgo_steder:
    popup_html = f"""
    <strong>{sted['navn']}</strong><br>
    <strong>ÅDT:</strong> {sted['adt']}<br>
    <strong>Est. inntjening:</strong> {sted['inntjening']}
    """
    folium.Marker(
        location=sted["koordinater"],
        popup=popup_html,
        icon=folium.Icon(color="red", icon="road", prefix="fa")
    ).add_to(kart)

# Lagre kart
kart_path = "coop_lagerkart_oppdatert.html"
kart.save(kart_path)

# Lag HTML-tabeller
lager_tabell = """
<h2>Tabell: Coop Lagerlokasjoner</h2>
<table border="1" style="border-collapse: collapse; width: 100%;">
<thead><tr><th>Navn</th><th>Adresse</th><th>Beskrivelse</th><th>ÅDT</th><th>Inntjening</th></tr></thead><tbody>
"""
for l in lager_data:
    lager_tabell += f"<tr><td>{l['navn']}</td><td>{l['adresse']}</td><td>{l['beskrivelse']}</td><td>{l['adt']}</td><td>{l['inntjening']}</td></tr>"
lager_tabell += "</tbody></table>"

coopgo_tabell = """
<h2>Tabell: Ønskede CoopGo-stasjoner</h2>
<table border="1" style="border-collapse: collapse; width: 100%;">
<thead><tr><th>Navn</th><th>ÅDT</th><th>Inntjening</th></tr></thead><tbody>
"""
for s in coopgo_steder:
    coopgo_tabell += f"<tr><td>{s['navn']}</td><td>{s['adt']}</td><td>{s['inntjening']}</td></tr>"
coopgo_tabell += "</tbody></table>"

# HTML-mal
template = Template("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Coop Lager og CoopGo-stasjoner</title>
</head>
<body>
    <h1>CoopKart med Trafikkdata</h1>
    <iframe src="{{ kartfil }}" width="100%" height="600px" style="border:none;"></iframe>
    <br><br>
    {{ lager }}
    <br><br>
    {{ go }}
</body>
</html>
""")

# Lag full HTML-side
output_html = "index.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(template.render(kartfil="coop_lagerkart_oppdatert.html", lager=lager_tabell, go=coopgo_tabell))
