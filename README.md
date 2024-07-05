# Map My World

Map My World is a backend application built with FastAPI and SQLAlchemy for exploring and reviewing different locations and categories worldwide.

## Features

- Location Management: Add and manage locations with latitude and longitude.
- Category Management: Define and manage categories for different types of places.
- Exploration Recommender: Recommends unreviewed location-category combinations based on specified criteria.
- Robust API: Provides endpoints for CRUD operations on locations and categories

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- SQLite (for local development)

## Instalación

    1. Clona el repositorio:    
        git clone https://github.com/your/repository.git
        cd repository

    2. Set up virtual environment (optional but recommended):
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    3. Install dependencies:
        pip install -r requirements.txt

    4. Set up the database::
        # Assuming you have SQLAlchemy configured in your app
        python app/db/init_db.py

## Configuration
    Update app/config.py with your specific configurations (database connection, etc.).

##Usage
    1. Clona el repositorio:
    
        
        

## Uso
    Para iniciar el servidor, ejecuta el siguiente comando:

    mvn spring-boot:run    

    o por medio de Docker: 
    
        - docker build -t api-justo:1.1 .
        - docker images
        - docker run -p 8080:8080 idImagen

    El servidor estará disponible en http://localhost:8080.

## Rutas y Endpoints
    Aquí se describen las rutas y endpoints del API:

    /api/products: Obtiene los productos
    api/purchase/prices: obtiene los productos seleccionados indicando, precio y descuento aplicado. 

## Contribución
    Si quieres contribuir al proyecto, sigue estos pasos:

        1. Haz un fork del repositorio.
        2. Crea una nueva rama (git checkout -b feature)
        3. Haz tus cambios y confirma (git commit -am 'Agrega una nueva función')
        4. Empuja a la rama (git push origin feature)
        5. Crea una nueva solicitud de extracción.

## Contacto
    Para cualquier pregunta o comentario, no dudes en contactarme a través de betobustamante.ef@gmail.com o visita mi perfil en [https://github.com/betobustamante].
