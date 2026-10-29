
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.cancion import Cancion
from flask_app.models.usuario import Usuario

# Mostrar todas las canciones
@app.route('/canciones')
def canciones():
    canciones = Cancion.get_all()
    return render_template('canciones.html', canciones=canciones)

# Crear una canción
@app.route('/crear_cancion', methods=['POST'])
def crear_cancion():
    data = {
        'titulo': request.form['titulo'],
        'artista': request.form['artista']
    }

    Cancion.save(data)
    return redirect('/canciones')

# Mostrar una canción
@app.route('/canciones/<int:id>')
def mostrar_cancion(id):
    data = {'id': id}

    cancion = Cancion.get_one(data)

    if cancion is None:
        return redirect('/canciones')

    usuarios = Cancion.usuarios_favoritos(data)
    disponibles = Usuario.get_all()

    return render_template(
        'mostrar_cancion.html',
        cancion=cancion,
        usuarios=usuarios,
        disponibles=disponibles
    )

# Agregar usuario a favoritos
@app.route('/canciones/<int:id>/agregar_favorito', methods=['POST'])
def agregar_favorito_cancion(id):
    data = {
        'canciones_id': id,
        'usuarios_id': request.form['usuarios_id']
    }

    Cancion.agregar_favorito(data)
    return redirect(f'/canciones/{id}')
