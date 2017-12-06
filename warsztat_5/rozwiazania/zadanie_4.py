# Requests: Wszystkie postaci z “Gwiezdnych Wojen”
#
# Na podstawie API: https://swapi.co/ napisz generator listujący wszystkie postaci pochodzące
# z sagi Star Wars `sw_person_generator`. Postaci zwracaj wg kolejności z API.
# Jeśli generator nie będzie mógł się połączyć z API, to powinien się zakończyć - generacja osób nie jest możliwa.
# Proszę użyć modułu requests.



BASE_URL = 'https://swapi.co/api/people/{person_id}/'

import requests
from requests.exceptions import RequestException

def sw_person_generator():
	person_counter = 1
	not_found_in_row = 0
	while True:
		current_url = BASE_URL.format(person_id=person_counter) # może od razu coś lepszego do składania urli??? (Żeby brało pod uwagę kodowanie)
		# print('przed requestem nr {}, url: {}'.format(person_counter, current_url))
		try:
			r = requests.get(url=current_url)
		except RequestException:
			return # cannot connect to api, generation process finished
		person_counter += 1
		print(r.status_code, current_url)#, r.headers)
		if r.ok:
			not_found_in_row = 0
			person = r.json()
			yield person.get('name')
		elif r.status_code == 404:
			not_found_in_row += 1
			if not_found_in_row > 5:
				return
			else:
				continue
		else:
			return

if __name__ == '__main__':
	assert list(sw_person_generator()) == ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars', 'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Wilhuff Tarkin', 'Chewbacca', 'Han Solo', 'Greedo', 'Jabba Desilijic Tiure', 'Wedge Antilles', 'Jek Tono Porkins', 'Yoda', 'Palpatine', 'Boba Fett', 'IG-88', 'Bossk', 'Lando Calrissian', 'Lobot', 'Ackbar', 'Mon Mothma', 'Arvel Crynyd', 'Wicket Systri Warrick', 'Nien Nunb', 'Qui-Gon Jinn', 'Nute Gunray', 'Finis Valorum', 'Padmé Amidala', 'Jar Jar Binks', 'Roos Tarpals', 'Rugor Nass', 'Ric Olié', 'Watto', 'Sebulba', 'Quarsh Panaka', 'Shmi Skywalker', 'Darth Maul', 'Bib Fortuna', 'Ayla Secura', 'Ratts Tyerell', 'Dud Bolt', 'Gasgano', 'Ben Quadinaros', 'Mace Windu', 'Ki-Adi-Mundi', 'Kit Fisto', 'Eeth Koth', 'Adi Gallia', 'Saesee Tiin', 'Yarael Poof', 'Plo Koon', 'Mas Amedda', 'Gregar Typho', 'Cordé', 'Cliegg Lars', 'Poggle the Lesser', 'Luminara Unduli', 'Barriss Offee', 'Dormé', 'Dooku', 'Bail Prestor Organa', 'Jango Fett', 'Zam Wesell', 'Dexter Jettster', 'Lama Su', 'Taun We', 'Jocasta Nu', 'R4-P17', 'Wat Tambor', 'San Hill', 'Shaak Ti', 'Grievous', 'Tarfful', 'Raymus Antilles', 'Sly Moore', 'Tion Medon', 'Finn', 'Rey', 'Poe Dameron', 'BB8', 'Captain Phasma']


# 200 https://swapi.co/api/people/1/
# Luke Skywalker
# 200 https://swapi.co/api/people/2/
# C-3PO
# 200 https://swapi.co/api/people/3/
# R2-D2
# 200 https://swapi.co/api/people/4/
# Darth Vader
# 200 https://swapi.co/api/people/5/
# Leia Organa
# 200 https://swapi.co/api/people/6/
# Owen Lars
# 200 https://swapi.co/api/people/7/
# Beru Whitesun lars
# 200 https://swapi.co/api/people/8/
# R5-D4
# 200 https://swapi.co/api/people/9/
# Biggs Darklighter
# 200 https://swapi.co/api/people/10/
# Obi-Wan Kenobi
# 200 https://swapi.co/api/people/11/
# Anakin Skywalker
# 200 https://swapi.co/api/people/12/
# Wilhuff Tarkin
# 200 https://swapi.co/api/people/13/
# Chewbacca
# 200 https://swapi.co/api/people/14/
# Han Solo
# 200 https://swapi.co/api/people/15/
# Greedo
# 200 https://swapi.co/api/people/16/
# Jabba Desilijic Tiure
# 404 https://swapi.co/api/people/17/
# 200 https://swapi.co/api/people/18/
# Wedge Antilles
# 200 https://swapi.co/api/people/19/
# Jek Tono Porkins
# 200 https://swapi.co/api/people/20/
# Yoda
# 200 https://swapi.co/api/people/21/
# Palpatine
# 200 https://swapi.co/api/people/22/
# Boba Fett
# 200 https://swapi.co/api/people/23/
# IG-88
# 200 https://swapi.co/api/people/24/
# Bossk
# 200 https://swapi.co/api/people/25/
# Lando Calrissian
# 200 https://swapi.co/api/people/26/
# Lobot
# 200 https://swapi.co/api/people/27/
# Ackbar
# 200 https://swapi.co/api/people/28/
# Mon Mothma
# 200 https://swapi.co/api/people/29/
# Arvel Crynyd
# 200 https://swapi.co/api/people/30/
# Wicket Systri Warrick
# 200 https://swapi.co/api/people/31/
# Nien Nunb
# 200 https://swapi.co/api/people/32/
# Qui-Gon Jinn
# 200 https://swapi.co/api/people/33/
# Nute Gunray
# 200 https://swapi.co/api/people/34/
# Finis Valorum
# 200 https://swapi.co/api/people/35/
# Padmé Amidala
# 200 https://swapi.co/api/people/36/
# Jar Jar Binks
# 200 https://swapi.co/api/people/37/
# Roos Tarpals
# 200 https://swapi.co/api/people/38/
# Rugor Nass
# 200 https://swapi.co/api/people/39/
# Ric Olié
# 200 https://swapi.co/api/people/40/
# Watto
# 200 https://swapi.co/api/people/41/
# Sebulba
# 200 https://swapi.co/api/people/42/
# Quarsh Panaka
# 200 https://swapi.co/api/people/43/
# Shmi Skywalker
# 200 https://swapi.co/api/people/44/
# Darth Maul
# 200 https://swapi.co/api/people/45/
# Bib Fortuna
# 200 https://swapi.co/api/people/46/
# Ayla Secura
# 200 https://swapi.co/api/people/47/
# Ratts Tyerell
# 200 https://swapi.co/api/people/48/
# Dud Bolt
# 200 https://swapi.co/api/people/49/
# Gasgano
# 200 https://swapi.co/api/people/50/
# Ben Quadinaros
# 200 https://swapi.co/api/people/51/
# Mace Windu
# 200 https://swapi.co/api/people/52/
# Ki-Adi-Mundi
# 200 https://swapi.co/api/people/53/
# Kit Fisto
# 200 https://swapi.co/api/people/54/
# Eeth Koth
# 200 https://swapi.co/api/people/55/
# Adi Gallia
# 200 https://swapi.co/api/people/56/
# Saesee Tiin
# 200 https://swapi.co/api/people/57/
# Yarael Poof
# 200 https://swapi.co/api/people/58/
# Plo Koon
# 200 https://swapi.co/api/people/59/
# Mas Amedda
# 200 https://swapi.co/api/people/60/
# Gregar Typho
# 200 https://swapi.co/api/people/61/
# Cordé
# 200 https://swapi.co/api/people/62/
# Cliegg Lars
# 200 https://swapi.co/api/people/63/
# Poggle the Lesser
# 200 https://swapi.co/api/people/64/
# Luminara Unduli
# 200 https://swapi.co/api/people/65/
# Barriss Offee
# 200 https://swapi.co/api/people/66/
# Dormé
# 200 https://swapi.co/api/people/67/
# Dooku
# 200 https://swapi.co/api/people/68/
# Bail Prestor Organa
# 200 https://swapi.co/api/people/69/
# Jango Fett
# 200 https://swapi.co/api/people/70/
# Zam Wesell
# 200 https://swapi.co/api/people/71/
# Dexter Jettster
# 200 https://swapi.co/api/people/72/
# Lama Su
# 200 https://swapi.co/api/people/73/
# Taun We
# 200 https://swapi.co/api/people/74/
# Jocasta Nu
# 200 https://swapi.co/api/people/75/
# R4-P17
# 200 https://swapi.co/api/people/76/
# Wat Tambor
# 200 https://swapi.co/api/people/77/
# San Hill
# 200 https://swapi.co/api/people/78/
# Shaak Ti
# 200 https://swapi.co/api/people/79/
# Grievous
# 200 https://swapi.co/api/people/80/
# Tarfful
# 200 https://swapi.co/api/people/81/
# Raymus Antilles
# 200 https://swapi.co/api/people/82/
# Sly Moore
# 200 https://swapi.co/api/people/83/
# Tion Medon
# 200 https://swapi.co/api/people/84/
# Finn
# 200 https://swapi.co/api/people/85/
# Rey
# 200 https://swapi.co/api/people/86/
# Poe Dameron
# 200 https://swapi.co/api/people/87/
# BB8
# 200 https://swapi.co/api/people/88/
# Captain Phasma
# 404 https://swapi.co/api/people/89/
# 404 https://swapi.co/api/people/90/
# 404 https://swapi.co/api/people/91/
# 404 https://swapi.co/api/people/92/
# 404 https://swapi.co/api/people/93/
# 404 https://swapi.co/api/people/94/
