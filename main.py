# -*- coding: UTF-8 -*-

from run_threaded import run_threaded
import schedule
import time

# importa task da file (from <nome_file> import <nome_funzione>)
from basic import basic

# lettura segreti applicazione
import configparser
config= configparser.ConfigParser()
config.read('secrets.ini')

id_app = config['secrets']['id_applicazione'] # ID applicazione Facebook
id_page = config['secrets']['id_pagina'] # ID pagina facebook
access_token = config['secrets']['token_accesso'] # token accesso applicazione


# programma random tra x-minuti e y-minuti
schedule.every(15).minutes.do(run_threaded, task)
schedule.every(15).minutes.do(run_threaded, basic)

# programma ogni ora al minuto :50 -> specifica nome feed
#schedule.every().hour.at(":50").do(run_threaded, task)

# programma ogni 2 ore al minuto :28 -> specifica nome feed
#schedule.every(2).hours.at(":28").do(run_threaded, task)

# rimuovi i cancelletti per

while 1:
  schedule.run_pending()
  time.sleep(1)
