FROM python:3
WORKDIR /usr/src/app
ENV FLASK_APP=api.py
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn
COPY . .
CMD /usr/src/app/boot.sh
