FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["dv.bin", "model1.bin", "q4_predict_flask.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=localhost:9696", "q4_predict_flask:app"]