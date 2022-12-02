FROM python:3.9.12
RUN pip install prometheus_client kubernetes
WORKDIR /opt
COPY count_pods.py .
EXPOSE 9100/tcp
CMD ["python", "/opt/count_pods.py", "run"]