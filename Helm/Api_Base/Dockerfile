FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY ./entrypoint.sh .
COPY ./requirements.txt .
COPY ./app ./app
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "6008"]
# CMD ["python", "/app/main.py"]