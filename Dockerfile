FROM python:3
MAINTAINER juaneml <juaneml@correo.ugr.es>
WORKDIR src/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD cd src && gunicorn proyecto-dep-app:__hug_wsgi__ --log-file -
