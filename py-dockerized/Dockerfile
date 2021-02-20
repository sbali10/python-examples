FROM python:alpine
 
LABEL Name=my_test_flaskapp Version=0.0.1
EXPOSE 5000
 
WORKDIR /app
ADD . /app
 
# Using pip:
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "/app/main.py"]