#! python3

import pandas as pd  # Para trabajar con la mayoría de los formatos
import json          # Para exportar a JSON
import xml.etree.ElementTree as ET  # Para exportar a XML
import h5py          # Para exportar a HDF5
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
# logging.disable(logging.CRITICAL)


frame = pd.read_csv('dataSets/MBA.csv')

frame.to_json('dsMBA/MBA.json', orient='records')
logging.info("JSON")

frame.to_hdf('dsMBA/MBA.h5', key='frame', mode='w', format='table')
logging.info("hdf")

#frame.to_xml('dsMBA/MBA.json', orient='records')
frame.to_excel('dsMBA/MBA.xlsx', index=None, header=True)
logging.info("excel")

frame.to_csv('dsMBA/MBA.tsv', sep='\t', index=False)
logging.info("tsv")

# Crear el elemento raíz
root = ET.Element('root')

# Iterar sobre cada fila del DataFrame y construir la estructura XML
for _, row in frame.iterrows():
    entry = ET.SubElement(root, 'entry')  # Crear un subelemento para cada fila
    for col in frame.columns:
        child = ET.SubElement(entry, col)  # Crear un subelemento para cada columna
        child.text = str(row[col])  # Asignar el valor de la celda como texto del elemento

tree = ET.ElementTree(root)
tree.write('MBA.xml')  # Guardar el archivo con el nombre 'dataset_converted.xml'