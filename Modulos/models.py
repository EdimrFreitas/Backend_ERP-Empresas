from api_back_end import db


class Crm(db.Model):
    username = db.Column(db.String(16), nullable=False, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    create_time = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.username
