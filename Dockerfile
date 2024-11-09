FROM python:3.12-slim

WORKDIR /app

COPY requirement.txt /app/

RUN pip install --upgrade pip && pip install -r requirement.txt

COPY . /app

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver"]
