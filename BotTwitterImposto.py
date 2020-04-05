import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
import ListaImpostos
from datetime import datetime
import importlib

# Lembrar de entrar com o valor de N certo
n = 25

# Authenticate to Twitter
auth = tweepy.OAuthHandler("SEU HANDLER")
auth.set_access_token("SEU TOKEN")

# Create API object
api = tweepy.API(auth)


# Funcao que carrega os impostos

def LogaTwitter():
    print("Logando no Twitter")
    auth.set_access_token("SEU TOKEN")


def PrintaTempo():
    print(datetime.now())


def PrintaImposto():
    print(ListaImpostos.Impostos[n])


def PostImposto():
    global n

    if n <= 365:
        importlib.reload(ListaImpostos)
        api.update_status(ListaImpostos.Impostos[n])
        n += 1
        return n
    # else:
    #    api.update_status(
    #       "Terminamos um ano inteiro, tweetando um imposto por dia, obrigado a todos")
    #   scheduler.shutdown(wait=False)



api.update_status(ListaImpostos.Impostos[24])
print(ListaImpostos.Impostos[24])
print(datetime.now())

job_defaults = {
    'coalesce': True,
}

# Faz o Agendamento das Postagens
scheduler = BlockingScheduler()
scheduler.add_job(LogaTwitter, 'cron', hour=11, minute=40, misfire_grace_time=300, coalesce=True, replace_existing=True)
scheduler.add_job(PrintaTempo, 'cron', hour=12, misfire_grace_time=300, coalesce=True, replace_existing=True)
scheduler.add_job(PrintaImposto, 'cron', hour=12, misfire_grace_time=300, coalesce=True, replace_existing=True)
scheduler.add_job(PostImposto, 'cron', hour=12, misfire_grace_time=300, coalesce=True, replace_existing=True)
scheduler.start()
