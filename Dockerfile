FROM python:3.7-slim-stretch
#FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install pip
# RUN pip install --upgrade pip
RUN python -m pip install --upgrade pip

RUN pip install statsmodels --upgrade
RUN pip install -r requirements.txt

EXPOSE 8501

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml

WORKDIR /app

ENTRYPOINT ["dtale-streamlit", "run", "abihydralitapp.py"]

#ENTRYPOINT ["dtale-streamlit", "run"]
#CMD ["abihydralitapp.py"]