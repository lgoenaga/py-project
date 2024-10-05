import uvicorn
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return ['item1', 'item2', 'item3']

@app.get('/data')
def get_datos():
    return [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}, {'name': 'John Smith', 'age': 40}]

@app.get('/pagina1', response_class=HTMLResponse)
def get_pagina1():
    return '''
        <html>
            <head>
                <title>Página 1</title>
            </head>
            <body>
                <h1>Esta es la página 1</h1>
                <p>Este es un párrafo de la página 1</p>
                <p>Este es otro párrafo de la página 1</p>
                <a href="/pagina2">Ir a la página 2</a>
            </body>
        </html>
    '''


def run():
    uvicorn.run("main:app", port=8000, log_level="info", reload=False)
    r = store.get_categories()
    for category in r:
        print(category['name'])

if __name__ == '__main__':
    run()