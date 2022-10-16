from re import L
from marshmallow import Schema, fields


class AddressSchema(Schema):
    city = fields.Str()
    country = fields.Str()
    postalCode = fields.Str()
    state = fields.Str()


class PatientSchema(Schema):
    id = fields.Str(required=False)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    firstName = fields.Str()
    lastName = fields.Str()
    gender = fields.Str()
    birthDate = fields.Str()
    #address = fields.Nested(AddressSchema)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
