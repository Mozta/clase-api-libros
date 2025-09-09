from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    autor = db.Column(db.String(80), nullable=False)
    editorial = db.Column(db.String(80))
    edicion = db.Column(db.Integer)
    
    def __init__(self, titulo, autor, editorial=None, edicion=None):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.edicion = edicion
    
    def to_dict(self):
        """Convierte el objeto a diccionario para serialización JSON"""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "editorial": self.editorial,
            "edicion": self.edicion
        }
    
    def __repr__(self):
        return f'<Libro {self.titulo} por {self.autor}>'