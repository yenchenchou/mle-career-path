FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# RUN chmod +x entrypoint.sh
# CMD [ "./entrypoint.sh" ]