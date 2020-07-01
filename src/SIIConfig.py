import sys
import time
import base64
import requests
from bs4 import BeautifulSoup


def info_sii(rut, dv):

    captcha_req = requests.post("https://zeus.sii.cl/cvc_cgi/stc/CViewCaptcha.cgi",data={'oper':'0'})
    if captcha_req.status_code != 200:
        raise Exception("Error de comunicacion con el SII")
    respuesta = captcha_req.json()
    txtCaptcha= respuesta['txtCaptcha']
    code = base64.b64decode(txtCaptcha)[36:40]
    consulta_sii = requests.post("https://zeus.sii.cl/cvc_cgi/stc/getstc",data={'RUT':rut,'DV':dv.upper(),'PRG':'STC','OPC':'NOR','txt_code':code,'txt_captcha':txtCaptcha})
    if captcha_req.status_code != 200:
        raise Exception("Error de comunicacion con el SII")
    datos = BeautifulSoup(consulta_sii.text,"html.parser")
    texto = consulta_sii.text

    if "No ha sido posible completar su solicitud" in consulta_sii.text or "El RUT consultado no figura con iniciaci" in consulta_sii.text:

        raise Exception("RUT sin inicio de actividades")
    razon_social= consulta_sii.text.split("n Social&nbsp;:")
    razon_social = razon_social[1].split("</div>")
    razon_social = razon_social[1][74:].strip()
    inicio_actividades =datos.find_all("span")
    inicio_actividades = consulta_sii.text.split("Fecha de Inicio de Actividades: ")
    if len(inicio_actividades)>1:    
        inicio_actividades = inicio_actividades[1][0:10]
    else:
        inicio_actividades = None
    es_pyme = consulta_sii.text.split("PRO-PYME: ")
    es_pyme = es_pyme[1][0:2]
    if es_pyme == "NO":
        es_pyme = False
    else:
        es_pyme = True
    #vemos si el RUT registra termino de giro
    if texto.find("T&eacute;rmino de giro")!= -1:
        termino_giro = True
        inicio_actividades = None
        #En este caso llevamos los datos correspondientes a nulo 
    else:
        termino_giro = False
    tablas = datos.find_all("table")
    try: 
        tabla_actividades = tablas[0]
        lista_actividades = tabla_actividades.find_all("tr")
        lista_actividades = lista_actividades[1:]
    except:
        lista_actividades = []
    actividades = []
    for item in lista_actividades:
        temporal = {}
        t = item.find_all("td")
        temporal['codigo'] = t[1].text.replace("\n","")
        temporal['actividad_economica'] = t[0].text.replace("\n","")
        actividades.append(temporal)
    salida = {}
    salida['RUT'] = rut+'-'+dv
    salida['razon_social']=razon_social.strip()
    if salida['razon_social'] == "": 
         #print consulta_sii.text.encode(out_enc)
         raise Exception("Razon Social en blanco") 
    salida['inicio_actividades'] = inicio_actividades
    salida['actividades_economicas'] = actividades
    salida['es_pyme'] = es_pyme
    salida['termino_giro'] = termino_giro
    return salida