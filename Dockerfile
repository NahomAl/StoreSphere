FROM alpine:latest


WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN apk add --no-cache python3 py3-pip
RUN pip install pipenv --break-system-packages && pipenv install
RUN pipenv run pip install psycopg2-binary 


COPY . /app/
RUN chmod +x wait-for-it.sh