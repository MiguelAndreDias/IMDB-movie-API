# IMDB-movie-API

This API is built using Python and Flask, and it utilizes a MongoDB database to store IMDb movie data. The API provides three main endpoints: GET MOVIES, GET MOVIES/ID, and POST MOVIES.

## Endpoints
### 1. GET MOVIES
Retrieve a list of movies from the database. This endpoint supports sorting and filtering options.

#### Parameters:

- rating_asc: Sort movies by ascending rating.
- rating_desc: Sort movies by descending rating.
- minRating: Filter movies by minimum rating.
- maxRating: Filter movies by maximum rating.
- genres: Filter movies by specified movie genres.
- startYear: Filter movies released in a specified year.
- titleName: Filter movies by title.

#### Pagination

To manage large datasets, this API employs a pagination method, limiting JSON results to 20 per page.

#### Example Usage:

Retrieves action movies released in the year 2000 with a minimum rating of 7.5, sorted in ascending order based on their ratings.

   ```bash
   GET http://127.0.0.1:5000/movies?sortBy=rating_asc&genres=action&minRating=7.5&startYear=2000
   ```

Retrieves the second page of movies with the "Dragon ball" title name in descending order of rating.

```bash
   GET http://127.0.0.1:5000/movies?sortBy=rating_desc&titleName=Dragon ball&page=2
```


### 2. GET MOVIES/{id}
Retrieve information about a specific movie using its tconst value.

#### Parameters:
- id: The tconst value of the movie.

#### Example Usage:

 ```bash
   GET http://127.0.0.1:5000/movies/tt7961060
   ```

Example JSON response:

 ```bash
   {
    "averageRating": 7.7,
    "genres": "Action,Adventure,Animation",
    "imdbLink": "https://www.imdb.com/title/tt7961060",
    "primaryTitle": "Dragon Ball Super: Broly",
    "runtimeMinutes": 100,
    "startYear": 2018,
    "tconst": "tt7961060",
    "titleType": "movie"
}
   ```


### 3. POST MOVIES
Add a new movie to the database.

Request Body:
 ```bash
{
    "averageRating": 7.7,
    "genres": "Comedy, Romance",
    "imdbLink": "https://www.imdb.com/title/ttxxxxxxx",
    "primaryTitle": "Example name",
    "runtimeMinutes": 100,
    "startYear": 2018,
    "tconst": "ttxxxxxxx",
    "titleType": "movie"
}
 ```

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
