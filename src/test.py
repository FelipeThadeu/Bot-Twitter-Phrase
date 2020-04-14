# coding=UTF-8
import tweepy
import time
import random
from datetime import datetime

api = tweepy.API(auth)

phrase = [
    'Creia em si, mas não duvide sempre dos outros. - Machado de Assis', 
    'A coragem não é ausência do medo; é a persistência apesar do medo. - Desconhecido',
    'Estar decidido, acima de qualquer coisa, é o segredo do êxito. - Henry Ford', 
    'Só existe um êxito: a capacidade de levar a vida que se quer. - Cristopher Morlay',
    'O êxito parece doce a quem não o alcança. - Emily Dickson'
];

def mensages():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%H:%M")
    print(data_e_hora_em_texto)
    if data_e_hora_em_texto == '21:17':
        api.update_status(random.choice(phrase))

def main():
    while True:
        mensages()
        time.sleep(60)

if __name__ == "__main__":
    main()
