from flask import Flask, jsonify, request
from models import db, Libro

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///libros.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    return "Welcome to my API"

# ENDPOINTS

@app.get("/libros")
def get_libros():
    libros = Libro.query.all()
    return jsonify([libro.to_dict() for libro in libros])

@app.get("/libros/<int:id>")
def get_libro(id):
    libro = Libro.query.get(id)
    if not libro:
        return jsonify({"error": "No encontrado"}), 404
    
    return jsonify(libro.to_dict())

@app.post("/libros")
def add_libro():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    # Validar campos requeridos
    required_fields = ["titulo", "autor", "editorial", "edicion"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo requerido: {field}"}), 400
    
    # Validar tipos de datos
    try:
        edicion = int(data.get("edicion"))
    except (ValueError, TypeError):
        return jsonify({"error": "El campo 'edicion' debe ser un número entero"}), 400
    
    try:
        nuevo = Libro(
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            editorial=data.get("editorial"),
            edicion=edicion
        )
        db.session.add(nuevo)
        db.session.commit()
        
        # Serializar el objeto para la respuesta
        return jsonify(nuevo.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear el libro"}), 500

@app.put("/libros/<int:id>")
def update_libro(id):
    libro = Libro.query.get(id)
    if not libro:
        return jsonify({"error": "No encontrado"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    try:
        # Actualizar campos si están presentes
        if "titulo" in data:
            libro.titulo = data["titulo"]
        if "autor" in data:
            libro.autor = data["autor"]
        if "editorial" in data:
            libro.editorial = data["editorial"]
        if "edicion" in data:
            libro.edicion = int(data["edicion"])
        
        db.session.commit()
        return jsonify(libro.to_dict())
        
    except (ValueError, TypeError):
        return jsonify({"error": "El campo 'edicion' debe ser un número entero"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar el libro"}), 500

@app.delete("/libros/<int:id>")
def delete_libro(id):
    libro = Libro.query.get(id)
    if not libro:
        return jsonify({"error": "No encontrado"}), 404
    
    try:
        db.session.delete(libro)
        db.session.commit()
        return jsonify({"message": "Libro eliminado exitosamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al eliminar el libro"}), 500

if __name__ == "__main__":
    app.run(debug=True)