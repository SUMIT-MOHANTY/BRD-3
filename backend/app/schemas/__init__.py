from marshmallow import Schema, fields, validate, ValidationError

class RegisterSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=128))
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=64))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=64))

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
