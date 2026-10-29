from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Obtener todos los usuarios
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('canciones').query_db(query)

        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))

        return usuarios

    # Crear un nuevo usuario
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios
            (nombre, email, password, created_at, updated_at)
            VALUES (%(nombre)s, %(email)s, %(password)s, NOW(), NOW());
        """
        return connectToMySQL('canciones').query_db(query, data)

    # Obtener un usuario por su ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('canciones').query_db(query, data)

        if result:
            return cls(result[0])

        return None
