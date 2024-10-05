import read_csv as rc
import charts as ch
import pandas as pd

def get_poblacion(dict, country):
    data = dict
    encabezados = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']  
    result = {}
    for i in range(len(data)):
        if data[i]['Country/Territory'] == country:
            for j in range(len(encabezados)):
                result[encabezados[j]] = int(data[i][encabezados[j]])
            break
    if not result:
        return 'not found'
    else:
        return result

def get_poblation(dict):
    data = dict
    encabezados = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']  
    result = {}
    for i in range(len(data)):
        for j in range(len(encabezados)):
            result[encabezados[j]] = int(data[encabezados[j]][i])
        break
    if not result:
        return 'not found'
    else:
        return result
    
    
def get_chart(dict, country):
    data = dict
    result = get_poblacion(data, country)
    labels = list(result.keys())
    values = list(result.values())
    ch.generate_bar_chart(labels, values)
    return

def get_bar_chart(dict):
    data = dict
    result = get_poblation(data)
    labels = list(result.keys())
    values = list(result.values())
    ch.generate_bar_chart(labels, values)
    return

if __name__ == '__main__':
    # Con lectura por CSV
    '''
    data = rc.read_csv('data.csv')
    country = input('Ingrese el pais: ')
    print(f'Country : {country} {get_poblacion(data, country)}')
    get_chart(data, country)
    '''
    
    # Con lectura por Panda
    df = pd.read_csv('data.csv')
    print(f'Country : Afghanistan {get_poblation(df)}')
    get_bar_chart(df)

