from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from app.classes import Rooms


class Intro(FlaskForm):
    height = IntegerField("Высота", validators=[NumberRange(min=3, max=20, message="От 3х до 20-ти")])
    width = IntegerField("Ширина", validators=[NumberRange(min=3, max=20, message="От 3х до 20-ти")])
    room = SelectField("Выберите начальную комнату", coerce=str, choices=Rooms().names,
                       default="Подвал", validators=[DataRequired()])
    submit = SubmitField("Начать игру")


class Quest(FlaskForm):
    direction = SelectField('Выберите направление', coerce=str,
                            choices=[((1, 0), "Север"),
                                     ((-1, 0), "Юг"),
                                     ((0, -1), "Запад"),
                                     ((0, 1), "Восток")], validators=[DataRequired()])
    steps = IntegerField("Количество шагов", validators=[NumberRange(min=1, max=3,
                                                                     message="От одного до 3х шагов за раз")])
    submit = SubmitField("Пройти")
