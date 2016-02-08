__author__ = 'Ricardo'

def formatOutput(code, content={}):

    messages =  {
                    1000:"Lista de mockups",
                    1001:"Nuevo mockup registrado",



                    100000:""



                }

    return {
            'code': code,
            'message': messages[code],
            'content':content
            }