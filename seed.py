from app import db
from app.main.model.models import Film

db.drop_all() # do not run this on a production database
db.create_all()

entry1 = Film(name="Eternal Sunshine of the spotless mind", genre="Drama", release_date="2004")
entry2 = Film(name="Mullholland Dr", genre="Thriller", release_date="2001")
entry3 = Film(name="Howl's Moving Castle", genre="Adventure", release_date="2004")
entry4 = Film(name="City of God", genre="Thriller", release_date="2002")
entry5 = Film(name="La Haine", genre="Drama", release_date="1995")
entry6 = Film(name="Punch Drunk Love", genre="Drama", release_date="2002")

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6])
db.session.commit()