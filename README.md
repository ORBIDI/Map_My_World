# Map My World

Map My World is a backend application built with FastAPI and SQLAlchemy for exploring and reviewing different locations and categories worldwide.

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Rutas y Endpoints](#rutas-y-endpoints)
4. [Ejemplos](#ejemplos)
5. [Contribución](#contribución)
6. [Licencia](#licencia)
7. [Contacto](#contacto)

## Instalación

    1. Clona el repositorio:
    
    git clone https://github.com/Justo-Supermercado/api-justo.git

    2. Instala las dependencias:

        - mvn clean install
        

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
