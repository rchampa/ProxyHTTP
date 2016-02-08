__author__ = 'Ricardo'
from flask_restful import Resource, reqparse, fields, marshal
from restful.format_response import formatOutput
from flaskapp import db,Mock
from datetime import datetime

mock_fields = {
    'id_mock': fields.Integer,
    'ip': fields.String,
    'port': fields.Integer,
    'method': fields.Integer,
    'url': fields.String,
    'body': fields.String,
    'activado': fields.Boolean,
    'creado_en': fields.DateTime(dt_format='iso8601'),
    'actualizado_en': fields.DateTime(dt_format='iso8601')
}

class MocksAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('ip', type=str, required = True, help = 'Falta la ip', location = 'json')
        self.reqparse.add_argument('port', type=int, location = 'json')
        self.reqparse.add_argument('method', type=int, required = True, help = 'Falta el method', location = 'json')
        self.reqparse.add_argument('url', type=str, required = True, help = 'Falta la url', location = 'json')
        self.reqparse.add_argument('body', type=str, required = True, help = 'Falta el objeto json', location = 'json')
        super(MocksAPI, self).__init__()


    def get(self):
        lista_mocks = Mock.query.all()
        content = list(map(lambda t: marshal(t, mock_fields), lista_mocks))
        return formatOutput(1000,content)

    def post(self):
        args = self.reqparse.parse_args()
        ip = args['ip']
        port = args['port']
        method = args['method']
        url = args['url']
        body = args['body']

        if port is None:
            port = 80

        creado_en = datetime.utcnow()
        nuevo_mock = Mock(ip, port, method, url, body, creado_en)
        db.session.add(nuevo_mock)
        db.session.commit()
        return formatOutput(1001)


# class AdminLoginAPI(Resource):
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument('email', type = str, required = True, help = 'No email provided', location = 'json')
#         self.reqparse.add_argument('password', type = str, required = True, help = 'No password provided', location = 'json')
#         super(AdminLoginAPI, self).__init__()
#
#     def post(self):
#         from flaskapp import Admin
#         args = self.reqparse.parse_args()
#         email = args['email']
#         admin = Admin.query.filter_by(email=email).first()
#
#         if admin is None:
#             return formatOutput(1001)
#
#         password = args['password']
#         ok = check_password_hash(admin.password,password)
#         if ok:
#             if admin.activado:
#                 return formatOutput(1002)
#             else:
#                 return formatOutput(1003)
#         else:
#             return formatOutput(1001)