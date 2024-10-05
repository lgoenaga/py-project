import util
import read_csv as rc
import pandas as pd

def run():
    file = 'data.csv'
    country = 'Afghanistan'
    '''
    #Lectura por CSV
    
    data = rc.read_csv(file)   
    print(f'Country : {country} {util.get_poblacion(data, country)}')
    util.get_chart(data, country)
    '''
    
    # Lectura por Panda
    df = pd.read_csv(file)
 
    df = df[df['Country/Territory'] == country]
    print(f'Country : {country} {util.get_poblation(df)}')
    util.get_bar_chart(df)

if __name__ == '__main__':
    run()
