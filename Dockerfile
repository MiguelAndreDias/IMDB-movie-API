FROM python:3.7.6

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD python ./imdb_api.py