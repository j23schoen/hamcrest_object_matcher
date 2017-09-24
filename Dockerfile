FROM alpine
RUN apk add --update python3
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
CMD ["pytest", "test/test_app.py"]
