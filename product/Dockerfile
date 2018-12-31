FROM python:3
WORKDIR /usr/src/app
ENV FLASK_APP=api.py
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD /usr/src/app/boot.sh && python api.py
