from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home():
    home = """
<h1>Sigma</h1>

<p>Apple</p>

<h1>Orange</h1>

<h3>Banana</h3>
"""
    return home