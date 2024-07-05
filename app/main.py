import logging
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from .database import database
from .routers import categories_router, locations_router, reviews_router, recommendations_router

# Configuración básica del logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Crear un logger
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Map My World API",
    description="API para gestionar ubicaciones y categorías, y proporcionar recomendaciones para la aplicación Map My World.",
    version="1.0.0"
)

database.Base.metadata.create_all(bind=database.engine)

app.include_router(categories_router)
app.include_router(locations_router)
app.include_router(reviews_router)
app.include_router(recommendations_router)

# Ejemplo de logging en el inicio de la aplicación
logger.info("Aplicación FastAPI iniciada")

# Habilitar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred."}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()}
    )
