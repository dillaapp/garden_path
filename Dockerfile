FROM pypy:latest AS builder

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

FROM pypy:latest

WORKDIR /app

COPY --from=builder /app /app

CMD python garden.py
