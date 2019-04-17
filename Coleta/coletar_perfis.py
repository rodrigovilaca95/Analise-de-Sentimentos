# acessar https://apps.twitter.com para criar uma nova aplicacao
# cada aplicacao tem suas proprias chaves

import tweepy
import re
import time

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('5LHtyQsZgpl5RoMOFNvVFxwXF', 'EUIeyCPjd8eCr3VUrxHRM5VDwhM1OIuLDX2Rh9lgseBzuyqn42')

# define o token de acesso
# para criar basta clicar em "Create my access token"
# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token('941337744298708992-Mk6kAJNrD1TlEAdvqLgjvlSlXBnyvmz',
    'IJL43DRbijX1TaeK5b4LXpVlMJILIClITEO1SgnTwUFZu')

# cria um objeto api
api = tweepy.API(auth)

# obtem tweets de um dado usuario
def obter_tweets(usuario, limite=10):
  resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
  tweets = [] # lista de tweets inicialmente vazia
  for r in resultados:
    # utiliza expressao regular para remover a URL do tweet
    # http pega o inicio da url
    # \S+ pega os caracteres nao brancos (o final da URL) 
    tweet = re.sub(r'http\S+', '', r.full_text)
    tweets.append(tweet.replace('\n', ' ')) # adiciona na lista
  return tweets # retorna a lista de tweets


ids = []
i = 0
for page in tweepy.Cursor(api.followers_ids, screen_name="unb_oficial").pages():
    ids.extend(page)
    print ("carregando pagina ", i, "/n" )
    i=i+1
    time.sleep(60)

with open('ids.txt', 'w') as f:
    for item in ids:
        f.write("%s\n" % item)


# escreve os tweets em um arquivo 'tweets.txt'
#tweets = obter_tweets(usuario='jairbolsonaro', limite=100)
#with open('tweets.txt', 'w') as f:
#  f.write('\n'.join(tweets))