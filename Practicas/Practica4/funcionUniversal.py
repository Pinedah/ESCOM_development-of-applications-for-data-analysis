#! python3

import pandas as pd  # Para trabajar con la mayoría de los formatos
import json          # Para exportar a JSON
import xml.etree.ElementTree as ET  # Para exportar a XML
import h5py          # Para exportar a HDF5
import logging

# TODO: convertir a cada formato
"""
        tsv -> pandas
        hdf5 -> h5py
        excel -> openpyxl
        xml -> xml
        json -> json
"""

def convertDataSet(filename, inExtension, outExtension):
    match inExtension.lower():
        case "tsv":

    pass


def main():
    filename = str(input("enter the filename: "))
    ext = filename.split(',')[1]
    name = filename.split(',')[0]

    if convertDataSet(filename, inEx, outEx):
        print("Dataset converted successfully")
    else:
        print("convertedn't")


if __name__ == "__main__":
    main()