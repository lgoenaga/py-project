import util
import read_csv as rc

def run():
    file = './app/data.csv'
    data = rc.read_csv(file)
    country = 'Afghanistan'
    print(f'Country : {country} {util.get_poblacion(data, country)}')
    util.get_chart(data, country)

if __name__ == '__main__':
    run()
