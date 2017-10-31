import Database
import datetime

def select_producer(key=None, value=None):
    if key == None:
        return db.data['producers']

    producer_array = []

    for producer in db.data['producers']:
        if producer[key] == value:
            producer_array.append(producer)

    return producer_array

def create_producer(name,date):
    if len(select_producer('name', name)) > 0:
        raise Exception('Error: producer with name \'{0}\' already exists'.format(name))

    db.data['producers'].append({
        'id': db.data['config']['pid_current'],
        'name': name,
        'date': date,
    })

    db.data['config']['pid_current'] += 1

def update_producer(id, key, value):
    for producer in db.data['producers']:
        if producer['id'] == id:
            producer[key] = value
            break


def delete_producer(id):
    for producer in db.data['producers']:
        if producer['id'] == id:
            for film in db.data['films']:
                if film['producer'] == producer['name']:
                    db.data['films'].remove(film)
            db.data['producers'].remove(producer)
            break

def print_producer(producers):
    for producer in producers:
        print('[{0}] {1} {2} '.format(producer['id'], producer['name'], producer['date']))

def select_film(key=None, value=None):
    if key == None:
        return db.data['films']

    film_array = []

    for film in db.data['films']:
        if film[key] == value:
            film_array.append(film)

    return film_array

def create_film(film_name, producer, country):
    if len(select_film('film_name', film_name)) > 0:
        raise Exception('Error: film with name \'{0}\' already exists'.format(film_name))

    db.data['films'].append({
        'id': db.data['config']['fid_current'],
        'film_name': film_name,
        'producer': producer,
        'country': country,
    })

    db.data['config']['fid_current'] += 1

def update_film(id, key, value):
    for film in db.data['films']:
        if film['id'] == id:
            film[key] = value
            break

def delete_film(id):
    for film in db.data['films']:
        if film['id'] == id:
            db.data['films'].remove(film)
            break

def print_film(films):
    for film in films:
        print('[{0}] {1} {2} {3}'.format(film['id'], film['film_name'], film['producer'], film['country']))

def filter_film():
    film_result = []

    for film in db.data['films']:
        if film['country'] == 'Ukraine':
            if film_result != film['producer']:
                if film['producer'] not in film_result:
                    film_result.append(film['producer'])
    return film_result

db = Database.database()


if db.data['config']['initMe']:
   create_producer('Tarantino', datetime.date(1982, 2, 11))
   create_producer('Skripka',   datetime.date(1963, 8, 23))
   create_producer('Shaskovich',datetime.date(1973, 11, 14))

   create_film('School', 'Tarantino', 'USA')
   create_film('Legend', 'Skripka', 'Ukraine')
   create_film('Shark', 'Skripka', 'Ukraine')
   create_film('Walking dead', 'Shaskovich', 'Italy')

   db.data['config']['initMe'] = False

