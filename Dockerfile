# docker buildx build --platform linux/amd64 --build-arg MONGODB_CONNECTION_STRING="<CONNECTION_STRING" -t komendan/weather --push .


FROM python:3.12.1-slim

ARG MONGODB_CONNECTION_STRING

WORKDIR /usr/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501

ENV MONGODB_CONNECTION_STRING=$MONGODB_CONNECTION_STRING

CMD ["sh", "-c", "streamlit run --server.port 8501 /usr/app/app.py"]
