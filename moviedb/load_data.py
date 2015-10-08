ml_dir = '../ml-1m'


def import_users():
    import csv
    import json

    users = []

    with open(ml_dir + '/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split(
                                    '::'),
                                delimiter='\t')
        for row in reader:
            user = {'fields': {'gender': row['Gender'],
                               'age': row['Age'],
                               'occupation': row['Occupation'],
                               'zipcode': row['Zip-code']},
                    'model': 'moviedb.Rater',
                    'pk': int(row['UserID'])
                    }
            users.append(user)

    with open('fixtures/users.json', 'w') as f:
        f.write(json.dumps(users))


def import_movies():
    import csv
    import json

    movies = []

    with open(ml_dir + '/movies.dat', encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['MovieID', 'MovieTitle'],
                                delimiter='\t',
                                )
        for row in reader:
            movie = {'fields': {'title': row['MovieTitle']},
                     'model': 'moviedb.Movie',
                     'pk': int(row['MovieID']),
                     }
            movies.append(movie)

    with open('fixtures/movies.json', 'w') as f:
        f.write(json.dumps(movies))


def import_ratings():
    import csv
    import json

    ratings = []

    with open(ml_dir + '/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames=['UserID', 'MovieID', 'Score'],
                                delimiter='\t'
                                )
        for row in reader:
            rating = {'fields': {'movie': row['MovieID'],
                                 'rater': row['UserID'],
                                 'stars': row['Score']},
                      'model': 'moviedb.Rating',
                      }

            ratings.append(rating)

    with open('fixtures/ratings.json', 'w') as f:
        f.write(json.dumps(ratings))


def import_all_data():
    import_users()
    import_movies()
    import_ratings()

import_all_data()
