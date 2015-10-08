from django.db import models

# Create your models here.


class Rater(models.Model):
    # id is automatic

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    X = 'X'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (X, 'Did not answer'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return self.title


class Rating(models.Model):
    stars = models.PositiveSmallIntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '@{} gives {} {}*'.format(self.rater, self.movie, self.stars)


def load_ml_data():
    import csv
    import json
    import re

    users = []

    with open('ml-1m/users.dat') as f:

        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'moviedb.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

    print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))
