from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class Intro(FlaskForm):
    height = IntegerField(
        "Высота", validators=[NumberRange(min=4, max=20, message="От 4х до 20-ти")]
    )
    width = IntegerField(
        "Ширина", validators=[NumberRange(min=4, max=20, message="От 4х до 20-ти")]
    )
    submit = SubmitField("Начать игру")


class Quest(FlaskForm):
    direction = SelectField(
        "Выберите направление",
        coerce=str,
        choices=[
            "Север",
            "Юг",
            "Запад",
            "Восток",
        ],
        validators=[DataRequired()],
    )
    steps = IntegerField(
        "Количество шагов",
        validators=[NumberRange(min=1, max=5, message="От одного до 3х шагов за раз")],
    )
    submit = SubmitField("Пройти")
