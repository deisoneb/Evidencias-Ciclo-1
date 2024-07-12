from imdb import Cinemagoer

# Crear una instancia de la clase Cinemagoer
ia = Cinemagoer()

# Función para obtener información de una película
def search_movies(title):
    try:
        results = ia.search_movie(title)
        return results
    except Exception as e:
        print(f"An error occurred while searching: {str(e)}")
        return []

def get_movie_details(movie_id):
    try:
        movie = ia.get_movie(movie_id)
        info = {
            'title': movie.get('title', 'N/A'),
            'year': movie.get('year', 'N/A'),
            'rating': movie.get('rating', 'N/A'),
            'votes': movie.get('votes', 'N/A'),
            'plot': movie.get('plot outline', 'N/A'),
            'cast': [actor['name'] for actor in movie.get('cast', [])[:5]] if movie.get('cast') else 'N/A',
            'directors': [director['name'] for director in movie.get('directors', [])] if movie.get('directors') else 'N/A',
            'genres': movie.get('genres', 'N/A'),
        }
        return info
    except Exception as e:
        print(f"An error occurred while fetching movie details: {str(e)}")
        return None

def display_movie_info(movie_info):
    if movie_info:
        print("\nMovie Details:")
        print(f"Title: {movie_info['title']} ({movie_info['year']})")
        print(f"Rating: {movie_info['rating']} (based on {movie_info['votes']} votes)")
        print(f"Plot: {movie_info['plot']}")
        print(f"Cast: {', '.join(movie_info['cast'])}")
        print(f"Directors: {', '.join(movie_info['directors'])}")
        print(f"Genres: {', '.join(movie_info['genres'])}")
    else:
        print("Movie information not available.")

def main():
    while True:
        search_title = input("\nEnter a movie title to search (or 'quit' to exit): ")
        if search_title.lower() == 'quit':
            break

        search_results = search_movies(search_title)
        if not search_results:
            print("No movies found with that title.")
            continue

        print("\nSearch Results:")
        for i, movie in enumerate(search_results[:10], 1):
            print(f"{i}. {movie.get('title')} ({movie.get('year', 'N/A')})")

        while True:
            choice = input("\nEnter the number of the movie for more details (or '0' to search again): ")
            if choice == '0':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(search_results):
                    selected_movie = search_results[choice - 1]
                    movie_info = get_movie_details(selected_movie.movieID)
                    display_movie_info(movie_info)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print("Thank you for using the Movie Search tool!")

if __name__ == "__main__":
    main()