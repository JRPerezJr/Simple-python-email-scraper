FROM python:3.9-alpine

WORKDIR /usr/src/python_email_scraper

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./email_scraper.py" ]