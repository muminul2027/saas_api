#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___

#CODE SECTION->

#Official Python From Docker
FROM python:3.14.3

#SetUp Directory inside Container
WORKDIR /saas_api_folder

#COPY to Docker Dir
COPY . /saas_api_folder

#Install Dependencies
RUN pip install --upgrade pip
RUN pip install --r requirements.txt

#OPEN/EXPOSE PORT
EXPOSE 8000
#RUN Uvicorn with FastAPI
CMD ["uvicorn","app.main:web_app","--host","0.0.0.0","--port","8000"]