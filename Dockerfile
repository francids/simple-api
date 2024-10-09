# FROM python:3.10.15-alpine3.20
FROM python
WORKDIR /app
COPY requirements.txt start.sh ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x start.sh
EXPOSE 8000
CMD ["./start.sh"]
