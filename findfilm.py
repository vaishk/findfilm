from flask import Flask, request, render_template, session, redirect
import numpy as np
import requests 
import json
import random
import pandas as pd
from pandas import DataFrame as df
from IPython.display import Image, HTML


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)


@app.route('/')
def index():
	data = json.loads(requests.get("http://kvaishali.com/assets/data/films2.json").text)
	choice = random.sample(range(2, 952), 10)
	film_list = []
	for num in choice:
		film_id = (data[num]["Title"])
		film_json = json.loads(requests.get("http://www.omdbapi.com/?i="+film_id+"&apikey=2e272849").text)
		plot = film_json["Plot"]
		title = film_json["Title"]
		poster = film_json["Poster"]
		director = film_json["Director"] 
		film_list.append([title, plot, director, poster])
	return render_template('index.html', film_list=film_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

