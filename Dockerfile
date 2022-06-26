FROM python:3.10-slim

ENV HOME /code
WORKDIR $HOME
COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt
COPY project .
COPY tests .
COPY app.py .
COPY create_tables.py .
COPY fixtures.json .
COPY load_fixtures.py .
COPY start_app.sh .
#CMD flask run -h 0.0.0.0 -p:80

EXPOSE 80

CMD ["sh", "start_app.sh"]
