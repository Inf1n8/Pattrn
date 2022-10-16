import os
from pony.orm import Database, PrimaryKey, Required, sql_debug, db_session
import uuid
from http import HTTPStatus
from apis.env import *
#pg_conn_string = os.environ.get('COCKROACH_URL')
pg_conn_string = COCKROACH_URL
db = Database()


class UserTable(db.Entity):
    _table_ = 'UserTable'
    id = PrimaryKey(uuid.UUID, auto=True)
    email = Required(str, unique=True)
    password = Required(str)
    fhir_id = Required(int)


db.bind(
    'postgres', f'{pg_conn_string}&sslrootcert={os.getcwd()}/apis/root.crt')
db.generate_mapping(create_tables=True)


@db_session
def check_login_data(email, password):
    record = UserTable.get(email=email, password=password)
    if record is None:
        return {'message': 'Unauthorized Request'}, HTTPStatus.UNAUTHORIZED
    else:
        return {'message': 'Authentication Successful', 'id': str(record.id)}, HTTPStatus.ACCEPTED


@db_session
def get_fhir_id(id):
    record = UserTable.get(id=id)
    return record.fhir_id


@db_session
def post_login_data(email, password, fhir_id):
    result = UserTable(email=email, password=password, fhir_id=fhir_id)
    result.flush()
    return result.id


#post_login_data("Daasaiata@google.com", "nice")
#check_login_data("Daasaiata@google.com", "nice")
