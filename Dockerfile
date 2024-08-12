FROM python:3.9

EXPOSE 5000

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

## just to keep container open - comment out when using Flask
#CMD tail -f /dev/null

# to run Flask app
CMD python app.py
