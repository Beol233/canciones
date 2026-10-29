from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.usuario import Usuario
from flask_app.models.cancion import Cancion

# Mostrar todos los usuarios
@app.route('/')
@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.get_all()
    return render_template('usuarios.html', usuarios=usuarios)

# Crear usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'email': request.form['email'],
        'password': request.form['password']
    }

    Usuario.save(data)
    return redirect('/usuarios')

# Mostrar un usuario
@app.route('/usuarios/<int:id>')
def mostrar_usuario(id):
    data = {'id': id}

    usuario = Usuario.get_one(data)

    if usuario is None:
        return redirect('/usuarios')

    favoritos = Cancion.favoritos_usuario(data)
    canciones = Cancion.get_all()

    return render_template(
        'mostrar_usuario.html',
        usuario=usuario,
        favoritos=favoritos,
        canciones=canciones
    )

# Agregar canción favorita desde la página del usuario
@app.route('/usuarios/<int:id>/agregar_favorito', methods=['POST'])
def agregar_favorito_usuario(id):
    data = {
        'usuarios_id': id,
        'canciones_id': request.form['canciones_id']
    }

    Cancion.agregar_favorito(data)
    return redirect(f'/usuarios/{id}')
