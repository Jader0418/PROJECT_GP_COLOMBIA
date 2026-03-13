# =========================================================
# IMPORTACIONES
# =========================================================

# IMPORTAR SQLMODEL PARA CREAR MODELOS DE BASE DE DATOS
from sqlmodel import SQLModel, Field

# IMPORTAR TIPOS OPCIONALES
from typing import Optional

# IMPORTAR TIPO FECHA
from datetime import date


# =========================================================
# MODELO DE COMPETIDOR
# REPRESENTA UN PILOTO INSCRITO EN EL CAMPEONATO
# =========================================================

class Competitor(SQLModel, table=True):

    # ID UNICO DEL COMPETIDOR
    id: Optional[int] = Field(default=None, primary_key=True)


    # NOMBRE COMPLETO DEL PILOTO
    full_name: str


    # TIPO DE DOCUMENTO
    # EJEMPLO: CC / CE / PASSPORT
    document_type: str


    # NUMERO DE DOCUMENTO
    document_number: str


    # FECHA DE NACIMIENTO
    birth_date: date


    # CIUDAD DE RESIDENCIA
    city: str


    # TELEFONO DE CONTACTO
    phone: str


    # CORREO ELECTRONICO
    email: str


    # NOMBRE DEL EQUIPO O ESCUDERIA
    team: Optional[str] = None


    # EXPERIENCIA EN CARRERAS
    # VALORES: SI / NO
    experience: str


    # MARCA DE LA MOTOCICLETA
    motorcycle_brand: str


    # MODELO DE LA MOTOCICLETA
    motorcycle_model: str


    # CILINDRAJE DEL MOTOR
    engine_cc: int


    # NUMERO DEL COMPETIDOR
    competitor_number: int


    # ACEPTACION DE TERMINOS
    terms_accepted: bool