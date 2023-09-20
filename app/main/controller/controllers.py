from app.main.model.models import Film
from werkzeug import exceptions
from flask import jsonify, request
from app import db

def index():
    try:
        films = Film.query.all()
        data = [f.json for f in films]
        return jsonify({"films": data})
    except:
        raise exceptions.InternalServerError("We are working on it")
    
def show(id):
    try:
        film = Film.query.filter_by(id=id).first()
        return jsonify({"data": film.json}), 200
    except:
        raise exceptions.NotFound("you get it")

def create():
    try:
        name, genre, release_date = request.json.values()
        new_film = Film(name=name, genre=genre, release_date=release_date)
            
        db.session.add(new_film)
        db.session.commit()

        return jsonify({"data": new_film.json}), 201
    except:
        raise exceptions.BadRequest(f"We cannot process your request, name, genre and release_date are required!")
    
def update(id):
        data = request.json
        film = Film.query.filter_by(id=id).first()

        for (attribute, value) in data.items():
            if hasattr(film, attribute):
                setattr(film, attribute, value)

        db.session.commit()

        return jsonify({ "data": film.json })

def delete(id):
        film = Film.query.filter_by(id=id).first()
        db.session.delete(film)
        db.session.commit()
        return f"Film deleted", 204

