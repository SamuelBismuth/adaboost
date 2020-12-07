FROM python:3.9

WORKDIR /adaboost

COPY src src
COPY data data

CMD [ "python", "src/adaboost.py" ]