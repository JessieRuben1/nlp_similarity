FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip3 install spacy
CMD ["python", "./watch_next.py"]