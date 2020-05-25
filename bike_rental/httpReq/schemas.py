from marshmallow import Schema, fields, pprint

class UserSchema(Schema):
    name = fields.Str()
    fullname = fields.Str()
    nickname = fields.Str()
