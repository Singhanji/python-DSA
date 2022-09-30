from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.get('/')
def get_all_pages():
    
    return render_template("index.html")

"""
@bookmarks.get('/me')
def me():
    return {"user": "me"}"""