![alt text](https://secure.meetupstatic.com/photos/event/8/8/6/5/highres_490894917.jpeg)

[![PyPI](https://img.shields.io/pypi/v/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
![Python Versions](https://img.shields.io/badge/Python-3.7-green.svg)
![Ubuntu](https://img.shields.io/badge/Ubuntu-18.04-blue.svg)
[![PyPI - License](https://img.shields.io/pypi/l/virtualenv?style=flat-square)](https://opensource.org/licenses/MIT)


# Meetup Analytics & Python 1 de Julio: Web scraping en tiempos de cuarentena

El siguiente repositorio contiene el código fuente oficial de la charla ***Web scraping en tiempos de cuarentena***, dictada el día 01-07-2020 para la comunidad. La información oficial del evento se encuentra en el siguiente [link](https://www.meetup.com/Analytics-y-Python/events/271358503/).

## Herramientas utilizadas

El proyecto general se montó en el OS Linux con distro Ubuntu v18.04, en una VM levantada en Google Cloud Platform (g1-small (1 vCPU, 1.7 GB memory)).

Para llevar a cabo los scrapers se utilizó Python v3.8, y creación de un ambiente virtual usando [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

En el caso de simular el navegador web para realizar el scraping interactivo se utilizó selenium, con [Chromium](https://chromedriver.chromium.org/).

Para el procesamiento de imágenes se utilizó la API de [Tesseract]() en Python.

## Descripción del contenido

La configuración del ambiente virtual para la replicabilidad de los resultados exhibidos se encuentra en el archivo [requirements.txt]()

## Autoría

* **Moebius Analítica** - [Webpage](https://www.moebius-analitica.cl/)
