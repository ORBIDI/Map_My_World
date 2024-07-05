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

## Usage

    1. Run the application:    
        uvicorn app.main:app --reload
    2. Access the API documentation:    
        Use Swagger UI at http://localhost:8000/docs to test and interact with the API.
        
## Contribución
    Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contacto
    Para cualquier pregunta o comentario, no dudes en contactarme a través de betobustamante.ef@gmail.com o visita mi perfil en [https://github.com/ORBIDI/Map_My_World.git].
