# IMDB-movie-API

This API is built using Python and Flask, and it utilizes a MongoDB database to store IMDb movie data. The API provides three main endpoints: GET MOVIES, GET MOVIES/ID, and POST MOVIES.

##Endpoints
###1. GET MOVIES
Retrieve a list of movies from the database. This endpoint supports sorting and filtering options.

####Parameters:
rating_asc: Sort movies by ascending rating.
rating_desc: Sort movies by descending rating.
minRating: Filter movies by minimum rating.
maxRating: Filter movies by maximum rating.
genres: Filter movies by specified movie genres.
startYear: Filter movies released in a specified year.
titleName: Filter movies by title.

Example Usage:

   ```bash
   GET /movies?rating_asc=true&genres=action&minRating=7.5&startYear=2000&titleName=example


2. GET MOVIES/{id}
Retrieve information about a specific movie using its tconst value.

Parameters:
id: The tconst value of the movie.
Example Usage:
http
Copy code
GET /movies/tt1234567
3. POST MOVIES
Add a new movie to the database.

Request Body:
json
Copy code
{
  "tconst": "tt1234567",
  "title": "Example Movie",
  "genres": ["Action", "Drama"],
  "rating": 8.5,
  "releaseYear": 2022
}
Example Usage:
http
Copy code
POST /movies
Getting Started
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/movie-database-api.git
cd movie-database-api
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Set up MongoDB:

Create a MongoDB database and update the connection details in config.py.
Run the application:

bash
Copy code
python app.py
The API will be accessible at http://localhost:5000.

Contributing
Feel free to contribute to the development of this API by submitting issues or pull requests. Your feedback and suggestions are highly appreciated!

License
This project is licensed under the MIT License.
