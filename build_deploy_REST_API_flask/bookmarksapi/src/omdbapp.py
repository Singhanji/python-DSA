from distutils.log import debug
from flask import Flask, render_template
import urllib.request, json
from flask import Blueprint
import os

omdbapp = Blueprint("omdbapp",__name__,url_prefix="/api/v1/omdbapp")

@omdbapp.get('/')
def get_all_movies():
    if os.getenv('OMDB_API_KEY') is None:
        return "Failed to authenticate API"

    url = "http://www.omdbapi.com/?apikey="+ os.environ['OMDB_API_KEY'] + "&" + "t=titanic"

    response = urllib.request.urlopen(url)
    data = response.read()

    return json.loads(data)

@omdbapp.route("/movies")
def get_movies_list():
    url = "http://www.omdbapi.com/?apikey=[afd1d86e]&".format(os.environ.get("OMDB_API_KEY"))

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)
    print(movies)

    return {"results": movies}
"""
if __name__ == '__main__':
    omdbapp.run(debug=True) """