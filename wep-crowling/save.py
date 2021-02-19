import csv


def save_to_file():
    file = open('movies.csv', mode='w')
    writer = csv.writer(file)
    writer.writrow(['title', 'theater', 'time', 'seat'])
