from mysqlconnection import connectToMySQL

class User():
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results=connectToMySQL('users_schema').query_db(query)
        users=[]
        for each in results:
            users.append(cls(each))
        return users
    @classmethod
    def save(cls,data):
        query='INSERT INTO users (id, first_name , last_name , email , created_at, updated_at ) VALUES ( %(id)s,%(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );'
        return connectToMySQL('users_schema').query_db(query, data)