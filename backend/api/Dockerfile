FROM python:3.8.0-alpine
WORKDIR /home/worker
RUN pip install flask flask_cors
RUN pip install pymongo
RUN pip install Flask-PyMongo
COPY main.py /home/worker/main.py
EXPOSE 5000
CMD ["python", "-u", "main.py"]