FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . app
WORKDIR app
RUN mkdir -pv Results/Results_sc
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]
