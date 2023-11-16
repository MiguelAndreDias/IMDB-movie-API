from flask import Flask, jsonify, request
from pymongo import MongoClient
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Connect to your MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['IMDB']
collection = db['JustMovies']

def apply_sorting(movies, sort_by):
    if sort_by == 'rating_asc':
        return movies.sort('averageRating', 1)
    elif sort_by == 'rating_desc':
        return movies.sort('averageRating', -1)
    elif sort_by == 'title_asc':
        return movies.sort('primaryTitle', 1)
    elif sort_by == 'title_desc':
        return movies.sort('primaryTitle', -1)
    else:
        return movies

def build_filter_query():
    filter_query = {'titleType': 'movie'}
    genres = request.args.get('genres', default=None, type=str)
    min_rating = request.args.get('minRating', default=None, type=float)
    max_rating = request.args.get('maxRating', default=None, type=float)
    start_year = request.args.get('startYear', default=None, type=int)
    title_name = request.args.get('titleName', default=None, type=str)

    if genres:
        filter_query['genres'] = {'$regex': genres, '$options': 'i'}
    if min_rating is not None:
        filter_query['averageRating'] = {'$gte': min_rating}
    if max_rating is not None:
        filter_query['averageRating'] = {'$lte': max_rating}
    if start_year is not None:
        filter_query['startYear'] = start_year
    if title_name is not None:
        filter_query['primaryTitle'] = {'$regex': title_name, '$options': 'i'}

    return filter_query

# Define the /movies endpoint
@app.route('/movies', methods=['GET', 'POST'])
def get_movies():
    """
    file: colors.yml
    """
    if request.method == "GET":
        # Extract query parameters
        sort_by = request.args.get('sortBy', default=None, type=str)
        page = request.args.get('page', default=1, type=int)

        # Build the filter query based on parameters
        filter_query = build_filter_query()

        # Fetch movies based on the query, excluding those with no rating
        movies = collection.find(filter_query, {'_id': 0})

        # Apply sorting based on 'sort_by' parameter
        movies = apply_sorting(movies, sort_by)

        # Calculate pagination limits
        items_per_page = 20
        skip_count = (page - 1) * items_per_page
        movies = movies.skip(skip_count).limit(items_per_page)

        # Convert to list for JSON serialization
        movies = list(movies)
        if movies:
            return jsonify(movies)
        else:
            return jsonify({'error': 'List of movies not found'}), 404

    elif request.method == 'POST':
        # Add a new movie to the database
        new_movie_data = request.json
        collection.insert_one(new_movie_data)
        return jsonify({'message': 'Movie added successfully'}), 201
    else:
        return jsonify({'error': 'List of movies not found'}), 404

# Define the /movies/{ID} endpoint
@app.route('/movies/<string:tconst>', methods=['GET'])
def get_movie(tconst):
    movie = collection.find_one({'tconst': tconst, 'titleType': 'movie'}, {'_id': 0})

    if movie:
        return jsonify(movie)
    else:
        return jsonify({'error': 'Movie not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
