import requests
from .schemas import UserSchema, pprint

def send_user(one_user):
    schema = UserSchema()
    result = schema.dump(one_user)
    pprint(result, indent=2)


# TODO, endpoint to receive data with app in flask.
# TODO SDK to communicate two microservices
# TODO CHECK IF user_app is ok, using repository and http or if I need another
# layer of abstraction.
# TODO git repository + env vars + dockerize + flake8 + README + Docstrings
