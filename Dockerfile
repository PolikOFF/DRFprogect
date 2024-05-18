FROM python:3

WORKDIR /app

COPY /pyproject.toml .

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]
