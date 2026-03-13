from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session
from database import create_db_and_tables, get_session
import models

app = FastAPI(

    title="GP COLOMBIA API",
    description="Sistema de registro para campeonatos de motociclismo en Colombia",
    version="0.0.1"
)

@app.on_event("startup")
def on_startup():
    # CREAR TABLAS EN LA BASE DE DATOS
    create_db_and_tables()

#CONFIGURAR LOS ARCHIVOS ESTATICOS COMO HTML Y CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# CONFIGURAR TEMPLATES HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def show_index(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/register")
def register_competitor(

    request: Request,

    # DATOS PERSONALES
    full_name: str = Form(...),
    document_type: str = Form(...),
    document_number: str = Form(...),
    birth_date: str = Form(...),
    city: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),

    # DATOS DE EQUIPO
    team: str = Form(None),
    experience: str = Form(...),

    # DATOS DE MOTO
    motorcycle_brand: str = Form(...),
    motorcycle_model: str = Form(...),
    engine_cc: int = Form(...),
    competitor_number: int = Form(...),

    # TERMINOS
    terms: bool = Form(...),

    # SESION DE BASE DE DATOS
    session: Session = Depends(get_session)

):

    competitor = models.Competitor(

        full_name=full_name,
        document_type=document_type,
        document_number=document_number,
        birth_date=birth_date,
        city=city,
        phone=phone,
        email=email,
        team=team,
        experience=experience,
        motorcycle_brand=motorcycle_brand,
        motorcycle_model=motorcycle_model,
        engine_cc=engine_cc,
        competitor_number=competitor_number,
        terms_accepted=terms
    )

    # GUARDAR EN BASE DE DATOS

    session.add(competitor)
    session.commit()
    session.refresh(competitor)

    return {
        "message": "COMPETIDOR REGISTRADO CORRECTAMENTE",
        "competitor_id": competitor.id
    }