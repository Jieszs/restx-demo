from typing import Dict, Tuple

from flask import request
from flask_restx import Resource

from .schemas.music import MusicSchema
from .. import db
from ..common.pagination import paginate
from ..model.music import Music
from ..service.music_service import save_new_music, get_a_music, delete_music
from ..util.decorator import token_required
from ..util.dto import MusicDto
from app.main.common.response_builder import success, message

api = MusicDto.api
_music = MusicDto.music
parser = api.parser()
parser.add_argument('Authorization', location='headers')


@api.route('/')
@api.expect(parser)
class MusicList(Resource):
    @api.doc('list_of_music')
    @api.param('page', '页码')
    @api.param('per_page', '页数')
    def get(self):
        """List all musics"""
        schema = MusicSchema(many=True)
        query = Music.query
        return paginate(query, schema)

    @api.expect(_music, validate=True)
    @token_required
    @api.response(201, 'Music successfully created.')
    @api.doc('create a new Music')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Music """
        schema = MusicSchema()
        music = schema.load(request.json)
        return save_new_music(music)


@api.route('/<id>')
@api.param('id', 'The music identifier')
@api.response(404, 'music not found.')
class OneMusic(Resource):
    @api.doc('get a music')
    def get(self, id):
        """get a music given its identifier"""
        music = get_a_music(id)
        schema = MusicSchema()

        if not music:
            return message(False, 'music not found.'), 404
        else:
            return schema.dump(music)

    @api.doc('delete a music')
    def delete(self, id):
        """get a music given its identifier"""
        music = get_a_music(id)
        if not music:
            return message(False, 'music not found.'), 404
        else:
            return delete_music(music)

    @api.doc('update a music')
    @api.response(200, 'Music successfully updated.')
    @api.expect(_music, validate=True)
    def put(self, id):
        """get a music given its identifier"""
        schema = MusicSchema(partial=True)
        music = get_a_music(id)
        if not music:
            return message(False, 'music not found.'), 404
        else:
            music = schema.load(request.json, instance=music)
            db.session.commit()
        return success('Music successfully updated.')
