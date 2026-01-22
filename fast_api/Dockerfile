FROM python:3.7.3-slim
WORKDIR /fast_api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn","fast_api.app:app","--host","0.0.0.0","--port","8000","--reload"]
