from flask_restful import Resource

saved_user = {1: "hola", 2: "chau"}


class UserAPI(Resource):
    def get(self, id):
        print(type(id))
        return {"message": saved_user[id]}

class UserAPICreationList(Resource):
    def post(self):
        some_json = request.get_json()
        return {"message": "Created"}, 201
    def get(self):
        return {"allUsers": saved_user}