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
        SELECT * FROM mocks WHERE id_mock=1
        """)

    data = cursor.fetchone()
    logging.debug("sqlite3")
    logging.debug(data)
    # u'canción'.encode('utf8')=="canción" => True


    data = sys.stdin.readlines()
    # this is a json string in one line so we are interested in that one line
    # print(json.dumps(data))
    # logging.debug(data)
    # application/json;charset=UTF-8
    payload = data[0]
    logging.debug(payload)

    payload_dict = json.loads(payload)
    logging.debug("request")
    request = payload_dict['request']
    logging.debug(request)
    logging.debug("request-path")
    logging.debug(request['path'])

    if request['path'] != "/posicionIntegrada/datosPosicionAgrupados/0002/N603638/10648812898":
        logging.debug("This is not a mock")
        # print(json.dumps(payload_dict))
        return

    body_mock = {
        "investmentProposalGrouping": [
            {
                "agrupacionDesc": "Carteira de Ricardo com Perfil",
                "agrupacionId": "555511987",
                "agrupacionTipo": "CUSTCP",
                "agrupacionSaldo": 3.05,
                "agrupacionPcrt": 0.00014727422522060096,
                "investmentProposalGrouping": [
                    {
                        "agrupacionDesc": "Alternativo",
                        "agrupacionId": "IN",
                        "agrupacionSaldo": 3.05,
                        "agrupacionPcrt": 0.00014727422522060096,
                        "investmentProposalGrouping": [
                            {
                                "agrupacionDesc": "Alternativo",
                                "agrupacionId": "IN",
                                "agrupacionSaldo": 3.05,
                                "agrupacionPcrt": 0.00014727422522060096,
                                "distribucion": [
                                    {
                                        "producto": {
                                            "idProducto": "TESOURARIA",
                                            "nombreProducto": "Tesouraria",
                                            "idCartera": "555511987",
                                            "descCartera": "Carteira de Custodia com Perfil",
                                            "tipoCartera": "CUSTCP",
                                            "perfilCartera": "CONS",
                                            "tipoActivo": "0001",
                                            "descTipoActivo": "ALTERNATIVO",
                                            "divisaProducto": "BRL",
                                            "tipoCambio": 1,
                                            "fechaSaldo": "2015-11-10",
                                            "reqProducto": 0,
                                            "iLiquidezProducto": 1,
                                            "comGestion": 1.1,
                                            "comDistribucion": 0.6,
                                            "cotizacion": 9.12,
                                            "tipoAdvisory2": "ALTR",
                                            "tipoProducto": "0012",
                                            "entProducto": "0002",
                                            "isinProducto": "0",
                                            "zonaGeografica": "0001",
                                            "productosRefer": "N",
                                            "complejoBasico": "SIMP",
                                            "recomendado": "9999",
                                            "recomEmisor": "REBL",
                                            "comercializable": "N",
                                            "rent12Meses": 0,
                                            "rent5Anio": 0,
                                            "leadingValue": 0,
                                            "rentEsperada": 12,
                                            "productoEmision": "N",
                                            "maxConcentracion": 100,
                                            "fechaCreacion": "2016-01-12",
                                            "fechaModificacion": "2016-01-12",
                                            "idPregunta3Test": "12",
                                            "emergente": "S",
                                            "fmi": "N",
                                            "focusList": "ACOES",
                                            "importeMinimo": 1000,
                                            "tipoAdvisory2Desc": "Alternativo",
                                            "tipoAdvisory1": "IN",
                                            "impMinimoAdicional": 5000,
                                            "iliquidezProducto": 1
                                        },
                                        "saldo": 3.05,
                                        "saldoPcrt": 0.00014727422522060096
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "totalPosicionGlobal": 2070966.59,
        "totalInversion": 2070966.59,
        "totalFinanciacion": 0,
        "fechaSaldo": "2015-11-10"
    }

    payload_dict['response']['status'] = 200
    payload_dict['response']['body'] = json.dumps(body_mock)
    payload_dict['response']['body'] += "\n"

    # esta linea es la que realmente hace de proxy
    print(json.dumps(payload_dict))


if __name__ == "__main__":
    main()
