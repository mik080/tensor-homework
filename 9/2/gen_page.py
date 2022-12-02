#!/usr/bin/env python3
import pymysql, os, time
from jinja2 import Environment, FileSystemLoader, select_autoescape



connection_mysql = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_USER_PASSWORD'],
    db='homework',
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8',
    autocommit=True
)
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)




if __name__ == '__main__':
    while True:
        with connection_mysql.cursor() as cursor:
            sql="SELECT * FROM articles ORDER BY RAND() LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            template = env.get_template('index.j2')

            html_page = template.render(title=result['title'], text=result['text'])

            with open('index.html', 'w', encoding="utf8") as file:
                file.write(html_page)
        if not os.path.exists("www"):
            os.makedirs("www")

        os.popen("mv index.html www/")
        time.sleep(120)