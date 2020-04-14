# coding=UTF-8
import tweepy
import json
import requests
import time
import random
from datetime import datetime

r = requests.get('pensador-api.js')

print(r)

#auth = tweepy.OAuthHandler("BBVFsOS4tUzgUQlZGKmu7Ooq4", "2AvfUozkH3LczmjebKGaQqIBXVY80gwrP3U1e6dmwMRVOTxKiE")
#auth.set_access_token("226271460-YHzPPABOshvA60ApBrZZw6J4vSXyHcqoplO5oHsC", "HBZFUd28iCUCL2x7AB5rwMi2ayOlC2Qkiq0yk8jK6qY1V")

#api = tweepy.API(auth)

#print('')

#def mensages():
#    data_e_hora_atuais = datetime.now()
#    data_e_hora_em_texto = data_e_hora_atuais.strftime("%H:%M")
#    print(data_e_hora_em_texto)
#    if data_e_hora_em_texto == '21:17':
#        api.update_status(random.choice(phrase.id))

#def main():
#    while True:
#        mensages()
#        time.sleep(60)

#if __name__ == "__main__":
#    main()