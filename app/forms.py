from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField, IntegerField
from datetime import date
from wtforms.validators import DataRequired, Length, NumberRange


class Intro(FlaskForm):
    room = SelectField('Выберите начальную комнату', coerce=str, choices=[
        'Спальня',
        'Холл',
        'Кухня',
        'Подвал',
        'Коридор',
        'Оружейная',
    ], default='Подвал', validators=[DataRequired()])
    submit = SubmitField('Начать игру')


class Quest(FlaskForm):
    direction = SelectField('Выберите направление', coerce=str, choices=[
        (1, 'Север'),
        (2, 'Юг'),
        (3, 'Запад'),
        (4, 'Восток'),
    ], validators=[DataRequired()])
    steps = IntegerField('Количество шагов', validators=[NumberRange(min=1, max=3,
                                                                     message='От одного до 3х шагов за раз')])
    submit = SubmitField('Пройти')
