FROM python:3.8

RUN apt-get update

RUN mkdir -p /workspace
RUN useradd ubuntu -m -s /bin/bash 

COPY requirements.txt /workspace/requirements.txt
RUN chown -R ubuntu /workspace

RUN pip install -r /workspace/requirements.txt

COPY . /workspace/project
RUN chown -R ubuntu /workspace/project
RUN chmod +x /workspace/project/run.sh

USER ubuntu
WORKDIR /workspace/project

CMD ["/workspace/project/run.sh"]