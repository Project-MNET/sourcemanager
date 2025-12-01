from .init_db import db

class KirjaViite(db.Model):
    __tablename__ = "Kirja_viite"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(50), unique = True, nullable = False)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return (
            f"Kirja_viite {self.id} | {self.key}, {self.author}, "
            f"{self.title}, {self.year}, {self.publisher}>"
            )

    def to_dict(self):
        return vars(self)

class ArtikkeliViite(db.Model):
    __tablename__ = "Artikkeli_viite"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    journal = db.Column(db.String(100))
    volume = db.Column(db.Integer)
    pages = db.Column(db.String(100))

    def __repr__(self):
        return (
            f"Artikkeli_viite {self.id} | {self.key}, {self.author}, "
            f"{self.title}, {self.year}, {self.journal}, {self.volume}, {self.pages}>"
            )

    def to_dict(self):
        return vars(self)

class KonferenssijulkaisuViite(db.Model):
    __tablename__ = "Konferenssijulkaisu_viite"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    booktitle = db.Column(db.String(100))

    def __repr__(self):
        return (
            f"Konferenssijulkaisu_viite {self.id} | {self.key}, {self.author}, "
            f"{self.title}, {self.year}, {self.booktitle}>"
            )

    def to_dict(self):
        return vars(self)
