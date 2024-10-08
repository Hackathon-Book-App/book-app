from re import A
from fastapi import FastAPI

from app import App


app=FastAPI()

@app.get("/user")
def user_auth(user_name: str = "raoul"):

    #cumva sa primeasca username si parola si sa verifice in baza de date daca exista userul, daca e buna parola si sa intoarca o validare ca e buna sau nu
    #sau daca nu exista sa intoarca ca nu, sa il promtuiasca ca nu are cont si daca vrea sa creeze si atunci sa creeze cu username si parola data
    #sa returneze si subscriptia de care beneficiaza

    return {"username": user_name}

@app.get("/app")
def app_query(object):

    results=App(object)
    return {"recommendation": results['answer']}