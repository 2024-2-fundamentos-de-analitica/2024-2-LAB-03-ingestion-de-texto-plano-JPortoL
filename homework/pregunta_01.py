"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re


def limpiar_encabezado(dir):
    with(open(dir, "r")) as file:
        lineas = file.readlines()

    linea1 = re.split(r'(?=[A-Z])', lineas[0].strip())
    linea2 = re.split(r'(?=[p])', lineas[1].strip())

    linea1 = [
    re.sub(r'\s+', '_', item.strip().lower())  
    for item in linea1 if item 
    ]

    linea2 = [
    re.sub(r'\s+', '_', item.strip().lower()) 
    for item in linea2 if item 
    ]

    encabezados = [
      linea1[0],
      linea1[1] + '_' + linea2[0],
      linea1[2] + '_' + linea2[1],
      linea1[3],
    ]

    #coñoetumadreculemondalargacolejoaaaaa
    return encabezados

def limpiar_cuerpo(dir):
    with(open(dir, "r")) as file:
        lineas = file.readlines()
    
    filas = []
    fila_actual = []
    palabras = ""
    for linea in lineas[4:]:
        if re.match(r"^\s+\d+", linea):
            if fila_actual:
                fila_actual.append(palabras[1:])
                filas.append(fila_actual)
            fila_actual = []
            partes = re.split(r'\s+', linea.strip())
            cluster = int(partes[0])
            cantidad = int(partes[1])
            porcentaje = float(partes[2].replace(',', '.'))
            fila_actual = [cluster, cantidad, porcentaje]
            palabras =  re.sub(r'\s{2,}', '', " ".join(partes[3:])).replace('%', '').replace('.', '')
        else:
            palabras += " " + re.sub(r'\s{2,}', ' ', linea.strip()).replace('%', '').replace('.', '')

    # if fila_actual:
    #     fila_actual.append(palabras[1:])
    #     filas.append(fila_actual)
    # for fila in filas:
    #     print(fila, "\n \n")

    # eldiavlolocoestoestamuyheavy
    return filas

            
            

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    encabezados = limpiar_encabezado('files/input/clusters_report.txt')
    filas = limpiar_cuerpo('files/input/clusters_report.txt')
    df = pd.DataFrame(filas, columns=encabezados)
    # print(df.principales_palabras_clave.to_list()[1], "\n \n")
    return df

if __name__ == '__main__':
    print(pregunta_01())