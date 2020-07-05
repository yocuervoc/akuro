import requests 
def get_data_cat():

    URL = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1"
    r = requests.get(url = URL)
    data = r.json() 
    print(data["text"])


get_data_cat()