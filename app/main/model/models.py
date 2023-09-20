from app import db, app 

app.app_context().push()

class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Film(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {"id": self.id, "name": self.name, "genre": self.genre, "release_date": self.release_date}