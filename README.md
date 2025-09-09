# 📚 API de Gestión de Libros

Una API REST completa para gestionar una colección de libros, desarrollada con Flask y SQLAlchemy.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)

📦 **Repositorio**: [github.com/Mozta/clase-api-libros](https://github.com/Mozta/clase-api-libros)

## 🚀 Características

- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Base de datos SQLite con SQLAlchemy
- ✅ Validación de datos de entrada
- ✅ Manejo robusto de errores
- ✅ Documentación OpenAPI/Swagger
- ✅ Respuestas JSON consistentes

## 📋 Requisitos

- Python 3.7+
- Flask
- Flask-SQLAlchemy

## 🛠️ Instalación

1. Clona el repositorio:

```bash
git clone git@github.com:Mozta/clase-api-libros.git
cd clase-api-libros
```

2. (Opcional) Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install flask flask-sqlalchemy
```

4. Ejecuta la aplicación:

```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

## 📖 Endpoints

### General

- `GET /` - Página de bienvenida

### Libros

- `GET /libros` - Obtener todos los libros
- `GET /libros/{id}` - Obtener un libro específico
- `POST /libros` - Crear un nuevo libro
- `PUT /libros/{id}` - Actualizar un libro existente
- `DELETE /libros/{id}` - Eliminar un libro

## 🔍 Documentación Swagger

La documentación completa de la API está disponible en el archivo `books.yaml` (formato OpenAPI 3.0.3).

Para visualizar la documentación de forma interactiva:

1. **Opción 1 - Online**: Sube el archivo `books.yaml` a [Swagger Editor](https://editor.swagger.io/)

2. **Opción 2 - Local**: Usa cualquier visualizador de OpenAPI local

## 📝 Ejemplos de uso

### Obtener todos los libros

```bash
curl -X GET http://localhost:5000/libros
```

### Crear un nuevo libro

```bash
curl -X POST http://localhost:5000/libros \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "1984",
    "autor": "George Orwell",
    "editorial": "Secker & Warburg",
    "edicion": 1949
  }'
```

### Obtener un libro específico

```bash
curl -X GET http://localhost:5000/libros/1
```

### Actualizar un libro

```bash
curl -X PUT http://localhost:5000/libros/1 \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Nineteen Eighty-Four",
    "edicion": 1984
  }'
```

### Eliminar un libro

```bash
curl -X DELETE http://localhost:5000/libros/1
```

## 📊 Estructura de datos

### Libro (respuesta)

```json
{
  "id": 1,
  "titulo": "El Quijote",
  "autor": "Miguel de Cervantes",
  "editorial": "Francisco de Robles",
  "edicion": 1605
}
```

### Crear libro (entrada)

```json
{
  "titulo": "1984",
  "autor": "George Orwell",
  "editorial": "Secker & Warburg",
  "edicion": 1949
}
```

_Todos los campos son requeridos_

### Actualizar libro (entrada)

```json
{
  "titulo": "Nuevo título",
  "edicion": 2023
}
```

_Todos los campos son opcionales_

## ⚠️ Códigos de respuesta

- `200` - Operación exitosa
- `201` - Recurso creado exitosamente
- `400` - Error en la solicitud (datos inválidos)
- `404` - Recurso no encontrado
- `500` - Error interno del servidor

## 🗂️ Estructura del proyecto

```
.
├── app.py              # Aplicación Flask principal
├── models.py           # Modelos de SQLAlchemy
├── books.yaml          # Especificación OpenAPI
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos a ignorar en Git
├── LICENSE             # Licencia MIT
├── README.md           # Documentación
└── libros.db           # Base de datos SQLite (se crea automáticamente)
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 🔧 Desarrollo

### Agregar nuevos campos al modelo

1. Modifica la clase `Libro` en `models.py`
2. Actualiza el método `__init__` y `to_dict()`
3. Actualiza los endpoints en `app.py`
4. Actualiza la documentación en `books.yaml`

### Validaciones personalizadas

Las validaciones se encuentran en los endpoints de `app.py`. Puedes agregar más validaciones según sea necesario.

## 📄 Licencia

MIT License
