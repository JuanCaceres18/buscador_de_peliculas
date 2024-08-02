from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Leer archivo .csv
movies = pd.read_csv("movies.csv")
print(movies.head())


@app.route("/")
def index():
    movies_list = {}

    for index, row in movies.iterrows():
        movies_list[row["title"]] = [row["imdbRating"], row["movie_poster"]]
        print(movies_list)

    return render_template("index.html", movies_list = movies_list)

@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    # Obtengo lo introducido en el input
    consulta_busqueda = request.args.get("busqueda")

    resultados_busqueda = movies[movies["title"].str.contains(consulta_busqueda, case=False, na=False)]

    movies_list = {}
    for index, row in resultados_busqueda.iterrows():
        movies_list[row["title"]] = [row["imdbRating"], row["movie_poster"]]
        print(movies_list)

    return render_template("index.html", movies_list=movies_list)



if __name__ == "__main__":
    app.run(debug=True)