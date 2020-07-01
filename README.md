![alt text](https://secure.meetupstatic.com/photos/event/8/8/6/5/highres_490894917.jpeg)

[![PyPI](https://img.shields.io/pypi/v/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
![Python Versions](https://img.shields.io/badge/Python-3.8-blue.svg)
[![PyPI - License](https://img.shields.io/pypi/l/virtualenv?style=flat-square)](https://opensource.org/licenses/MIT)


# Meetup Analytics & Python 1 de Julio: Web scraping en tiempos de cuarentena

El siguiente repositorio contiene el código fuente oficial de la charla ***Web scraping en tiempos de cuarentena***, dictada el día 01-07-2020 para la comunidad. La información oficial del evento se encuentra en el siguiente [link](https://www.meetup.com/Analytics-y-Python/events/271358503/).

## Herramientas utilizadas

Para llevar a cabo los scrapers se utilizó Python 3.8, y creación de un ambiente virtual usando [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).



docker run --rm -d -p {port}:{port}/tcp apisunat:latest
````

La imagen fue construida con las últimas versiones estables de cada software.

## Tests

En construcción ...

## Implementación

La API provee el endpoint '/info' mediante el método GET, el cual requiere el parámetro 'ruc' y retorna un JSON con la info asociada a la empresa.

Internamente la API ejecuta la función `scraper.scraper` que retorna un diccionario con la info extraída de la web.

Además, la api provee el endpoint '/health' mediante el método get, para verificar el estado del servicio.

Ambos endpoints requieren autenticación mediante token, para lo que se requiere incorporar al request el header 'Authorization' con el valor 'Token {token}'.

Ejemplo de requests:

````
curl -v GET \
    http://{host}:{port}/health \
    -H 'Authorization: Token {token}'
````

````
curl -v GET \
    http://{host}:{port}/info?ruc=20503644968 \
    -H 'content-type: application/json' \
    -H 'Authorization: Token {token}'
````

## Construido con

* [Tesseract]() - 
* [Chromium]() - 
* [Falcon](https://github.com/falconry/falcon) - Web framework
* [falcon-auth](https://github.com/loanzen/falcon-auth) - Backend de autenticación
* [Gunicorn](https://github.com/benoitc/gunicorn) - Servidor WSGI HTTP
* [Nginx](https://nginx.org/en/) - Reverse proxy
* [Docker](https://docs.docker.com/engine/) - Creación de contenedores

## Autores

* **Juan Pablo Rojas** - [Github](https://github.com/jp-rojas)
* **Joaquín Ureta** - [Github](https://github.com/juakonap)
