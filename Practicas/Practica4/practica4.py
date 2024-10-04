#! python3

import pandas as pd  # Para trabajar con la mayoría de los formatos
import json          # Para exportar a JSON
import xml.etree.ElementTree as ET  # Para exportar a XML
import h5py          # Para exportar a HDF5
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
# logging.disable(logging.CRITICAL)

def main():

    # TODO: convertir a cada formato
    """
        tsv -> pandas
        hdf5 -> h5py
        excel -> openpyxl
        xml -> xml
        json -> json
    """

    file = input("Ingresa el nombre del archivo a convertir (CSV): ")

    dataframe = pd.read_csv(f'dataSets/{file}.csv')

    dataframe.to_json(f'ds{file}/{file}.json', orient='records')
    logging.info("JSON convertido")

    dataframe.to_hdf(f'ds{file}/{file}.h5', key='dataframe', mode='w', format='table')
    logging.info("HDF5 convertido")

    dataframe.to_excel(f'ds{file}/{file}.xlsx', index=None, header=True)
    logging.info("Excel convertido")

    dataframe.to_csv(f'ds{file}/{file}.tsv', sep='\t', index=False)
    logging.info("TSV convertido")

    # Crear el elemento raíz
    root = ET.Element('root')
    # Iterar sobre cada fila del DataFrame y construir la estructura XML
    for _, row in dataframe.iterrows():
        entry = ET.SubElement(root, 'entry')  # Crear un subelemento para cada fila
        for col in dataframe.columns:
            child = ET.SubElement(entry, col)  # Crear un subelemento para cada columna
            child.text = str(row[col])  # Asignar el valor de la celda como texto del elemento
    tree = ET.ElementTree(root)
    tree.write(f'ds{file}/{file}.xml')  
    logging.info("XML convertido")


if __name__ == '__main__':
    main()