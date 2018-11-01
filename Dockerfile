FROM python:3

WORKDIR /Users/jramachandra/Documents/python/src/containers

COPY containers/*	/var/www/tests/
RUN pip install --no-cache-dir -r /var/www/tests/requirements.txt
EXPOSE 5000

COPY . .

CMD [ "python", "containers/test.py" ]