from flask import Flask
from flask import Blueprint, render_template
from .models import Veiculos

# Cria um Blueprint para as rotas

bp = Blueprint('main', __name__)

# Define a rota para a página inicial

@bp.route('/')
def index():
    return render_template ('index.html')

@bp.route('/base')
def base():
    return render_template('base.html')

@bp.route('/formularios')
def formularios():
    return render_template('formularios.html')

@bp.route('/veiculos')
def veiculos():
    return render_template('veiculos.html')