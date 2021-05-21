from datetime import datetime

from .. import db


class Music(db.Model):
    """ Music Model for storing music related details """
    __tablename__ = "music"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song = db.Column(db.String(255), nullable=False)
    singer = db.Column(db.String(255), nullable=False)
    last_modify_date = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Music '{}'>".format(self.song)


