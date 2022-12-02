FROM python:3.10-slim
RUN pip install requests
WORKDIR /opt
COPY src/index.py .
ENTRYPOINT ["python","/opt/index.py"]