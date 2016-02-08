#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import json

import sqlite3
fich = "/tmp/test.db"
NUM_CONSULTAS = 5

conn = sqlite3.connect(fich)
cursor = conn.cursor()

logging.basicConfig(filename='middleware.log', level=logging.DEBUG)
logging.debug('Middleware is called')

def main():
    cursor.execute("""
        SELECT * from mocks where id_mock=1
        """)

    data = cursor.fetchone()
    logging.debug("sqlite3")
    logging.debug(data)
    # u'canción'.encode('utf8')=="canción" => True


    data = sys.stdin.readlines()
    # this is a json string in one line so we are interested in that one line
    # print(json.dumps(data))
    # logging.debug(data)
    #application/json;charset=UTF-8
    payload = data[0]
    logging.debug(payload)


    payload_dict = json.loads(payload)

    if data['path'].encode('utf8')!="/posicionIntegrada/datosPosicionAgrupados/0002/N603638/10648812898":
        logging.debug("This is not a mock")
        print(json.dumps(payload_dict))
        return



    response = {
        "carteraModelo": {
            "carteraModeloId": "CON092015A",
            "entidad": "0002",
            "nombreCartera": "Carteira Ricardo Conservador AFFLUENT",
            "perfilCarteraId": "CONS",
            "modeloPlantilla": "N",
            "comosionRoa": 0,
            "distribucion": [
                {
                    "saldo": 0.2,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Ricardo mola mucho 1 Ano proposta",
                        "reqProducto": "5",
                        "iLiquidezProducto": "1",
                        "tipoActivo": "0002",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "rent24MBench": "1",
                        "fmi": "S",
                        "focusList": "RF_STD",
                        "importeMinimo": "0",
                        "rating": "0",
                        "tipoAdvisory2": "RFDI",
                        "tipoAdvisory2Desc": "DI",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "LCICDIPROPOSTA1"
                    },
                    "saldoPcrt": 20
                },
                {
                    "saldo": 0.15,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Santander FIC FI PB Ativo Renda Fixa Crédito Privado",
                        "reqProducto": "28",
                        "iLiquidezProducto": "2",
                        "tipoActivo": "0002",
                        "idPregunta3Test": "10",
                        "emergente": "S",
                        "roa": "0.6",
                        "benchmark": "%CDI",
                        "rent12MBench": "94.07",
                        "fmi": "N",
                        "focusList": "PREVI",
                        "importeMinimo": "500000",
                        "rating": "0",
                        "tipoAdvisory2": "RFDI",
                        "tipoAdvisory2Desc": "DI",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "1366"
                    },
                    "saldoPcrt": 15
                }
            ]
        },
        "paginacion": {
            "paginacion": 1,
            "numRegistros": 100,
            "esUltimaPagina": True,
            "numPaginas": 1
        }
    }


    payload_dict['response']['status'] = 200
    payload_dict['response']['body'] = json.dumps(response)
    payload_dict['response']['body'] += "\n"

    #esta linea es la que realmente hace de proxy
    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()