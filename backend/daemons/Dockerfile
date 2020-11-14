FROM python:3.8-alpine

RUN pip install pymongo

WORKDIR /app

COPY reminder.py /app/reminder.py
COPY scheduler.py /app/scheduler.py
COPY auditor.py /app/auditor.py

RUN echo "python -u /app/scheduler.py &" > start.sh && \
    echo "python -u /app/auditor.py &" >> start.sh && \
    echo "python -u /app/reminder.py" >> start.sh

CMD ["sh","start.sh"]