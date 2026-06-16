FROM python:3

ARG FRED_API_TOKEN

ENV FRED_API_TOKEN=${FRED_API_TOKEN}

COPY app /app
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

#CMD echo "Completed!"

# Keep alive
CMD ["python3", "-m", "app.main"]


