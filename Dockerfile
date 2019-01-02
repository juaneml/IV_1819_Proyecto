FROM python:3
LABEL maintainer="juaneml@correo.ugr.es"
WORKDIR src/
COPY . src/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD cd src && gunicorn proyecto-dep-app:__hug_wsgi__
