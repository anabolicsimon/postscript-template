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


def basic():

  #lista link immagini da cui pescare
  image_url = ['https://i.imgur.com/v0UL4nL.jpg', 'https://i.imgur.com/78ZNaFi.jpg', 'https://i.imgur.com/Uz97DMK.jpg', 'https://i.imgur.com/b1DGtxO.jpg', 'https://i.imgur.com/EQbObRO.jpg', 'https://i.imgur.com/XepJFlL.jpg', 'https://i.imgur.com/nYuBDEW.jpg', 'https://i.imgur.com/FjjHlvU.jpg', 'https://i.imgur.com/vtrCSwv.jpg', 'https://i.imgur.com/5sM3yMV.jpg', 'https://i.imgur.com/PFdJ7j9.jpg', 'https://i.imgur.com/9oIB3yX.jpg', 'https://i.imgur.com/PpL3hEh.jpg', 'https://i.imgur.com/Dp7nuby.jpg', 'https://i.imgur.com/nIFzni6.jpg']

  # lista messaggi da cui pescare
  list_msg = ['SANDRINI CALZATURE E ABBIGLIAMENTO\nti aspetta online e in negozio!\n\n- spedizione gratuita 🆓\n- consegna express ⏩\n- resi semplici 😌', 'TANTE NOVITÀ ESTATE 2022\nCalzature e abbigliamento al passo con i tempi\n\n- spedizione gratuita 🆓\n- consegna express ⏩\n- resi semplici 😌', 'CALZATURE E ABBIGLIAMENTO\nAL PASSO CON I TEMPI\n\nSandrini donna: https://is.gd/sandrinidonna22\nSandrini kids: https://is.gd/sandrinikids22\nSandrini uomo: https://is.gd/sandriniuomo22', 'SCOPRI LE NOVITÀ\nSALDI ESTATE22!\n\nSandrini donna: https://is.gd/sandrinidonna22\nSandrini kids: https://is.gd/sandrinikids22\nSandrini uomo: https://is.gd/sandriniuomo22']

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