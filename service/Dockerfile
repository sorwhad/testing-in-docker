FROM python:3.8

RUN mkdir /workspace

COPY requirements.txt /workspace

RUN pip install -r /workspace/requirements.txt

COPY . /workspace/project

WORKDIR "/workspace/project"

CMD ["python3", "app.py"]