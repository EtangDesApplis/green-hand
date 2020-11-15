FROM python:3.8.0-alpine
WORKDIR /home/worker
RUN pip install flask flask_cors
COPY main.py /home/worker/main.py
EXPOSE 5000
RUN echo "python3 -u /back/janitord.py /tmp case 300 &" > start.sh && \
    echo "python3 -u /back/main.py" >> start.sh
CMD ["sh", "start.sh"]
