from flask import Blueprint
from flask import render_template
from flask import request
from flask import session,redirect,url_for


mainbp = Blueprint('main', __name__)
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')