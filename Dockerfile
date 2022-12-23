FROM python:3.10-bullseye

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /src
COPY . /src

WORKDIR /src

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]