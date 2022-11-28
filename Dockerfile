FROM python:3.10
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000