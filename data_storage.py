import csv

class DataStorage:
    def __init__(self, filename='tweets.csv'):
        self.filename = filename
        self.csv_file = open(self.filename, 'a')
        self.csv_writer = csv.writer(self.csv_file)

    def store_tweet(self, created_at, text):
        print(created_at, text)
        self.csv_writer.writerow([created_at, text.encode('utf-8')])

    def close(self):
        self.csv_file.close()
