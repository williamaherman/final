from flask import Flask, render_template, request, redirect, Response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import simplejson as json

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'Inventory'
mysql.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)