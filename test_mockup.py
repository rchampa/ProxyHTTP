#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import json


logging.basicConfig(filename='middleware.log', level=logging.DEBUG)
logging.debug('Middleware is called')

def main():
    data = sys.stdin.readlines()
    # this is a json string in one line so we are interested in that one line
    # print(json.dumps(data))
    payload = data[0]
    logging.debug(payload)

    payload_dict = json.loads(payload)

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
                        "nombreProducto": "LCI Pós Santander 1 Ano proposta",
                        "reqProducto": "5",
                        "iLiquidezProducto": "1",
                        "tipoActivo": "0002",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0001",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "9999",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "0.0",
                        "rent5Meses": "0.0",
                        "leadingValue": "0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "100",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
                        "idPregunta3Test": "01",
                        "emergente": "S",
                        "roa": "0.4",
                        "benchmark": "%CDI",
                        "rent24Meses": "0",
                        "rent12MBench": "1",
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
                    "saldo": 0.1,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Letra Financeira Pré 2 anos",
                        "reqProducto": "6",
                        "iLiquidezProducto": "6",
                        "tipoActivo": "0006",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0001",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "BUY",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "1.0",
                        "rent5Meses": "0.0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "50",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
                        "idPregunta3Test": "01",
                        "emergente": "S",
                        "roa": "0.2",
                        "benchmark": "%CDI",
                        "rent24Meses": "0",
                        "rent12MBench": "0",
                        "rent24MBench": "0",
                        "fmi": "S",
                        "importeMinimo": "250000",
                        "tipoAdvisory2": "RFPR",
                        "tipoAdvisory2Desc": "Renda Fixa - Pré",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "LFPRESANT2"
                    },
                    "saldoPcrt": 10
                },
                {
                    "saldo": 0.05,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Santander FI IMA-B 5 Top Renda Fixa Longo Prazo",
                        "reqProducto": "51",
                        "iLiquidezProducto": "1",
                        "tipoActivo": "0004",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0005",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "BUY",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "13.43",
                        "rent5Meses": "7.25",
                        "leadingValue": "0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "20",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
                        "idPregunta3Test": "05",
                        "emergente": "S",
                        "roa": "0.22",
                        "benchmark": "%CDI",
                        "rent12MBench": "105.34",
                        "fmi": "N",
                        "focusList": "FUND_RF",
                        "importeMinimo": "50000",
                        "rating": "0",
                        "tipoAdvisory2": "RFIF",
                        "tipoAdvisory2Desc": "Renda Fixa - Inflação",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "COT_1325"
                    },
                    "saldoPcrt": 5
                },
                {
                    "saldo": 0.2,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Santander FIC FI Vintage II Renda Fixa Crédito Privado",
                        "reqProducto": "19",
                        "iLiquidezProducto": "2",
                        "tipoActivo": "0002",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0005",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "BUY",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "12.82",
                        "rent5Meses": "6.82",
                        "leadingValue": "0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "100",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
                        "idPregunta3Test": "05",
                        "emergente": "S",
                        "roa": "0.22",
                        "benchmark": "%CDI",
                        "rent24Meses": "24.96",
                        "rent12MBench": "100.55",
                        "rent24MBench": "101.64",
                        "fmi": "N",
                        "focusList": "FUND_DI",
                        "importeMinimo": "50000",
                        "rating": "0",
                        "tipoAdvisory2": "RFDI",
                        "tipoAdvisory2Desc": "DI",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "COT_1170"
                    },
                    "saldoPcrt": 20
                },
                {
                    "saldo": 0.3,
                    "producto": {
                        "entProducto": "0002",
                        "isinProducto": "0",
                        "nombreProducto": "Santander FIC FI Yield Premium Referenciado DI Crédito Privado",
                        "reqProducto": "8",
                        "iLiquidezProducto": "2",
                        "tipoActivo": "0002",
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0005",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "BUY",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "12.71",
                        "rent5Meses": "6.69",
                        "leadingValue": "0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "100",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
                        "idPregunta3Test": "05",
                        "emergente": "S",
                        "roa": "0.37",
                        "benchmark": "%CDI",
                        "rent24Meses": "24.47",
                        "rent12MBench": "99.68",
                        "rent24MBench": "99.65",
                        "fmi": "N",
                        "focusList": "FUND_DI",
                        "importeMinimo": "100000",
                        "rating": "0",
                        "tipoAdvisory2": "RFDI",
                        "tipoAdvisory2Desc": "DI",
                        "tipoAdvisory1": "FJ",
                        "idProducto": "0859SCSB"
                    },
                    "saldoPcrt": 30
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
                        "zonaGeografica": "0001",
                        "divisaProducto": "BRL",
                        "tipoProducto": "0010",
                        "productosRefer": "N",
                        "complejoBasico": "SIMP",
                        "recomendado": "BUY",
                        "recomEmisor": "REBL",
                        "comercializable": "S",
                        "rent12Meses": "11.99",
                        "rent5Meses": "6.55",
                        "leadingValue": "0",
                        "rentEsperada": "12.0",
                        "productoEmision": "N",
                        "maxConcentracion": "100",
                        "fechaCreacion": "12/01/2016",
                        "fechaModificacion": "12/01/2016",
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