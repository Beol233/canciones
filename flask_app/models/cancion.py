from flask_app.config.mysqlconnection import connectToMySQL

class Cancion:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.artista = data['artista']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Obtener todas las canciones
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM canciones;"
        results = connectToMySQL('canciones').query_db(query)

        canciones = []
        for cancion in results:
            canciones.append(cls(cancion))

        return canciones

    # Crear una nueva canción
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO canciones
            (titulo, artista, created_at, updated_at)
            VALUES (%(titulo)s, %(artista)s, NOW(), NOW());
        """
        return connectToMySQL('canciones').query_db(query, data)

    # Obtener una canción por ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM canciones WHERE id = %(id)s;"
        result = connectToMySQL('canciones').query_db(query, data)

        if result:
            return cls(result[0])

        return None

    # Agregar canción a favoritos
    @classmethod
    def agregar_favorito(cls, data):
        query = """
            INSERT IGNORE INTO canciones_has_usuarios
            (canciones_id, usuarios_id)
            VALUES (%(canciones_id)s, %(usuarios_id)s);
        """
        return connectToMySQL('canciones').query_db(query, data)

    # Obtener canciones favoritas de un usuario
    @classmethod
    def favoritos_usuario(cls, data):
        query = """
            SELECT canciones.*
            FROM canciones
            JOIN canciones_has_usuarios
            ON canciones.id = canciones_has_usuarios.canciones_id
            WHERE canciones_has_usuarios.usuarios_id = %(id)s;
        """
        results = connectToMySQL('canciones').query_db(query, data)

        return [cls(cancion) for cancion in results]

    # Obtener usuarios que tienen una canción como favorita
    @classmethod
    def usuarios_favoritos(cls, data):
        query = """
            SELECT usuarios.nombre
            FROM usuarios
            JOIN canciones_has_usuarios
            ON usuarios.id = canciones_has_usuarios.usuarios_id
            WHERE canciones_has_usuarios.canciones_id = %(id)s;
        """
        return connectToMySQL('canciones').query_db(query, data)

    # Obtener usuarios que aún no tienen esta canción como favorita
    @classmethod
    def usuarios_disponibles(cls, data):
        query = """
            SELECT usuarios.id, usuarios.nombre
            FROM usuarios
            WHERE usuarios.id NOT IN (
                SELECT usuarios_id
                FROM canciones_has_usuarios
                WHERE canciones_id = %(id)s
            );
        """
        return connectToMySQL('canciones').query_db(query, data)
