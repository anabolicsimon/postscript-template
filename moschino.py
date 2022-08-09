# -*- coding: UTF-8 -*-

import requests
import random
import configparser
config= configparser.ConfigParser()
config.read('secrets.ini')

id_app = config['secrets']['id_applicazione'] # ID applicazione Facebook
id_page = config['secrets']['id_pagina'] # ID pagina facebook

# token accesso applicazione

access_token = config['secrets']['token_accesso']


def moschino():

  #lista link immagini da cui pescare
  image_url = []

  # lista messaggi da cui pescare
  list_msg = []

  # url chiamata facebook server
  post_url = 'https://graph.facebook.com/{}/photos'.format(id_page)

  # logica valore precedente cosi da non postare
  # 2 volte consecutive la stessa immagine
  previous_value = None

  # scelta random da lista immagini
  img_url = random.choice(image_url)

  # logica per determinare valore precedente
  if img_url != previous_value:
    payload = {
      'message': random.choice(list_msg),  # testo post
      'url': img_url,                      # link immagine
      'access_token': access_token         # token accesso app
    }
    # assegno img selezionata come valore precedente
    previous_value = img_url

    # posto la richiesta al server facebook
    try:
      r = requests.post(post_url, data=payload)
      print(r.text)
      #conferma successo
      print('Post pubblicato.')
    except:
      print("C'è stato un errore nel pubblicare questo post..")