FROM python:3.10-alpine
RUN pip install pymysql jinja2
WORKDIR /opt
COPY gen_page.py .
COPY index.j2 .
CMD ["python", "/opt/gen_page.py" ,"run"]
