import streamlit as st
from babel.dates import format_date
import requests, datetime
from mpmath import mp


st.title('OIC - Chapitre 4 - Bonus mathématique')

st.divider()
st.subheader('Anniversaires')

date = st.date_input("Entrez une date d'anniversaire :", value=None, min_value=None, format="DD/MM/YYYY")

if date:
	nombre = date.strftime("%d%m%Y")
	url = "https://v2.api.pisearch.joshkeegan.co.uk/api/v1/Lookup?namedDigits=pi&find=" + nombre + "&resultId=0"
	r = requests.get(url)
	resultat = r.json()
	index = resultat['resultStringIdx']

	if index < 1000000:
		st.write(f"Cette date ({nombre}) se trouve dans le premier million de décimales de pi (à la position {index}) ! :balloon:")
	else:
		st.write(f"Désolée, cette date ({nombre}) ne se trouve pas dans le premier million de décimales de pi...")

	st.write(f"Il s'agissait d'un :orange[{format_date(date, format='EEEE', locale='fr')}].")

st.write("Réalisé grâce à : https://pisearch.joshkeegan.co.uk/")

st.markdown("Pour d'autres outils équivalents, voir par exemple [the Pi Searcher](https://www.angio.net/pi/bigpi.cgi), [subidiom.com](http://subidiom.com/pi/pi.asp), ou encore [piday](https://www.piday.org/find-birthday-in-pi/)")

st.divider()
st.subheader('Somme des décimales')


def somme_pi(length: int):
	mp.dps = length + 1
	pi = mp.pi
	somme = 0
	for digit in str(pi)[2:]:
		somme += int(digit)
	return(somme)


st.write(f"La somme des 20 premières décimales de pi vaut : **{somme_pi(20)}**.")
st.write(f"La somme des 12² premières décimales de pi vaut : **{somme_pi(12*12)}**.")


st.divider()
st.subheader('Petite vidéo instructive')

with open('./Somme-Entiers-Rittaud.mov', 'rb') as vid:
	video_bytes = vid.read()

st.video(video_bytes)

st.write("Source : VideoDiMath (CNRS), Benoît Rittaud, https://video.math.cnrs.fr/la-somme-de-tous-les-entiers")

st.divider()

st.subheader('Ressources complémentaires')

st.markdown('Pour une série de "fun facts" sur pi, voir [ici](https://www.piday.org/pi-facts/) (en anglais)')
