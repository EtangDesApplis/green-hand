FROM python:3.8.0-alpine
WORKDIR /home/worker
RUN pip install flask flask_cors
COPY main.py /home/worker/main.py
EXPOSE 5000
CMD ["python", "main.py"]
