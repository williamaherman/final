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
app.config['MYSQL_DATABASE_DB'] = 'taxablesData'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def taxables():
    user = {'username': 'William'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM taxables')
    result = cursor.fetchall()
    return render_template('taxables.html', user=user, taxables=result)


@app.route('/view/<int:taxable_id>', methods=['GET'])
def show_taxable(taxable_id):
    user = {'username': 'William'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM taxables WHERE id=%s', taxable_id)
    result = cursor.fetchall()
    return render_template('view.html', user=user, taxable=result[0])

@app.route('/edit/<int:taxable_id>', methods=['GET'])
def edit_taxable(taxable_id):
    user = {'username': 'William'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM taxables WHERE id=%s', taxable_id)
    result = cursor.fetchall()
    return render_template('edit.html', user=user, taxable=result[0])


@app.route('/edit/<int:taxable_id>', methods=['POST'])
def update_taxable(taxable_id):
    cursor = mysql.get_db().cursor()
    sql = "UPDATE taxables SET Index= %s, Item=%s, Cost=%s, Tax=%s, Total=%s WHERE id = %s"
    req = request.form
    val = (
        req.get('Index'), req.get('Item'), req.get('Cost'), req.get('Tax'), req.get('Total'),
        taxable_id)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/new', methods=['GET'])
def new_taxable_form():
    user = {'username': 'William'}
    return render_template('new.html', user=user)


@app.route('/new', methods=['POST'])
def create_taxable():
    cursor = mysql.get_db().cursor()
    sql = "INSERT INTO taxables (Index, Item, Tax, Total) VALUES (%s,%s,%s,%s,%s)"
    req = request.form
    val = (req.get('Index'), req.get('Item'), req.get('Cost'), req.get('Tax'), req.get('Total'))
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:taxable_id>', methods=['POST'])
def delete_taxable(taxable_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM taxables WHERE id = %s"
    val = (taxable_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/taxables', methods=['GET'])
def list_taxable():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM taxables')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/taxables/<int:taxables_id>', methods=['GET'])
def view_taxables(taxables_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM taxables WHERE id=%s', taxables_id)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/taxables/<int:taxables_id>', methods=['PUT'])
def change_taxables(taxables_id):
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "UPDATE taxables SET Index= %s, Item=%s, Cost=%s, Tax=%s, Total=%s WHERE id = %s"
    val = (content['Index'], content['Item'], content['Cost'], content['Tax'], content['Total'])
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/taxables', methods=['POST'])
def new_taxables():
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "INSERT INTO taxables (Index, Item, Cost, Tax, Total) VALUES (%s,%s,%s,%s,%s)"
    val = (content['Index'], content['Item'], content['Cost'], content['Tax'], content['Total'])
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/taxables/<int:taxables_id>', methods=['DELETE'])
def remove_taxables(taxables_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM taxables WHERE id = %s"
    val = (taxables_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

