from app.main import db
from app.main.model.music import Music
from app.main.common.response_builder import success


def save_new_music(data: Music):
    save_changes(data)
    return success('Music successfully created.'), 201


def get_all_musics():
    return Music.query.all()


def get_a_music(id):
    return Music.query.filter_by(id=id).first()


def delete_music(data: Music):
    db.session.delete(data)
    db.session.commit()
    return success('Music successfully deleted.')


def save_changes(data: Music) -> None:
    db.session.add(data)
    db.session.commit()
