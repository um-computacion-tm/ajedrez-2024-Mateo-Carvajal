FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Mateo-Carvajal

WORKDIR /ajedrez-2024-Mateo-Carvajal

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python3 -m game.cli"]

# sudo docker buildx build -t ajedrez-2024-mateo-carvajal . --no-cache
# sudo docker run -i ajedrez-2024-mateo-carvajal

