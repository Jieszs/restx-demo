from marshmallow import validate, fields

from app.main import ma, db
from app.main.common.error import ValidateException
from app.main.common.response_builder import validation_error
from app.main.model.music import Music


class MusicSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    song = fields.String(
        validate=validate.Length(min=1, max=10, error='song长度最小为1,最长为10'))  # song长度最小为1,最长为10

    def handle_error(self, exc, data, **kwargs):
        msg = list(exc.messages.values())[0][0]
        error = validation_error(False, msg)
        raise ValidateException(data=error)

    class Meta:
        model = Music
        sqla_session = db.session
        load_instance = True
