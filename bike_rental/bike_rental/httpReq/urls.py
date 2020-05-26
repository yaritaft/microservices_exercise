from .. import api
from .user import UserAPI, UserAPICreationList

api.add_resource(
    UserAPICreationList, '/users', endpoint = 'user-list-creation'
)
api.add_resource(
    UserAPI, '/users/<int:id>', endpoint = 'user'
)
