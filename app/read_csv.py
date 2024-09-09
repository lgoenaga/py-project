import csv

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)
        data = []
        for row in reader:
            population = zip(headers, row)
            dcit_population = dict(population)
            data.append(dcit_population)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    