from moviesbd import MoviesDB
from transformdb import TransformDB
from postgresdb import PostgresDB

FINAL_DBS = ['film_work_person', 'film_work_genre', 'film_work', 'person', 'genre']
PERSONS_ROLE = []
GENRE_NAME = []
FILM_WORK = []


def run():
    movies_db = MoviesDB('db.sqlite')
    transform_bd = TransformDB()
    postgres_db = PostgresDB()

    movie_table = movies_db.get_movie_table()
    for row_movies in movie_table:
        film_work_id = row_movies[0]
        for director_name in movies_db.make_director_to_list(row_movies[5]):
            PERSONS_ROLE.append(transform_bd.PersonRole(film_work_id, director_name, "director"))
        for director_name in movies_db.make_actors_names_to_list(row_movies[6]):
            PERSONS_ROLE.append(transform_bd.PersonRole(film_work_id, director_name, "actor"))
        for director_name in movies_db.make_writers_names_to_list(row_movies[7],
                                                                  movies_db.make_writers_to_list(row_movies[8])):
            PERSONS_ROLE.append(transform_bd.PersonRole(film_work_id, director_name, "writer"))
        for genre in row_movies[2].split(', '):
            GENRE_NAME.append(transform_bd.GenreName(film_work_id, genre))

        FILM_WORK.append(
            transform_bd.FilmWork(film_work_id, movies_db.get_text(row_movies[3]),
                                  movies_db.get_text(row_movies[4]),
                                  movies_db.make_imdb_rating_float(row_movies[1])))

    transform_bd.transfer_bd_to_csv(PERSONS_ROLE, GENRE_NAME, FILM_WORK)

    for db in FINAL_DBS:
        postgres_db.copy_db_from_csv(db)


if __name__ == '__main__':
    run()