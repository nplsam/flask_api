from flask import jsonify, request
from werkzeug import exceptions
from app import app, db
from app.main.model.models import Film
from app.main.controller.controllers import index, show, create, update, delete

@app.route("/")
def welcome():
    return jsonify({
        "message": "Welcome!",
        "description": "Films API",
          "endpoints": [
            "GET /"
            " GET /<id>"
            " POST /"
            " PATCH /<id>"
            " DELETE /<id>"
        ]
    })

@app.route("/films", methods=["GET", "POST"])
def create_film():
    if request.method == "POST": return create()
    if request.method == "GET": return index()
      
# angle bracket makes it dynamic in python instead of the characters/:id seen in javascript (line 28)
@app.route("/films/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show_film(id):
    if request.method == "GET":
        return show(id)
    
    if request.method == "PATCH":
        return update(id)
    
    if request.method == "DELETE":
        return delete(id)

# a way to error handle using werkzeug
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500

@app.errorhandler(exceptions.BadRequest)
def handler_400(err):
    return jsonify({"error": f"Oops {err}"}), 400
    