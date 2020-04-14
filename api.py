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
    'O êxito parece doce a quem não o alcança. - Emily Dickson',
    'A persistência realiza o impossível. - Proverbio Chinês',
    'Persistência é a irmã gêmea da excelência. Uma é a mãe da qualidade, a outra é a mãe do tempo. - Marabel Morgan',
    'Tem gente que tá perto e nem sente perto do que a gente sente - Vitor Kley',
    'Eu escolho um homem que não duvide de minha coragem, que não me acredite inocente, que tenha a coragem de me tratar como uma mulher. - Anais Nin'
];

def mensages():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%H:%M")
    print(data_e_hora_em_texto)
    if data_e_hora_em_texto == '20:00':
        api.update_status('BOT motivacional: '+ random.choice(phrase))

def main():
    while True:
        mensages()
        time.sleep(60)

if __name__ == "__main__":
    main()
