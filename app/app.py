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
app.config['MYSQL_DATABASE_DB'] = 'addressesData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def addresses():
    user = {'username': 'Addresses Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory')
    result = cursor.fetchall()
    return render_template('addresses.html', user=user, addresses=result)


@app.route('/view/<int:address_id>', methods=['GET'])
def show_address(address_id):
    user = {'username': 'Addresses Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('view.html', user=user, address=result[0])


@app.route('/edit/<int:address_id>', methods=['GET'])
def edit_address(address_id):
    user = {'username': 'Addresses Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    return render_template('edit.html', user=user, address=result[0])


@app.route('/edit/<int:address_id>', methods=['POST'])
def update_address(address_id):
    cursor = mysql.get_db().cursor()
    sql = "UPDATE addresses SET first_name = %s, last_name=%s, street=%s, city=%s, state=%s, zip=%s WHERE id = %s"
    req = request.form
    val = (
        req.get('first_name'), req.get('last_name'), req.get('street'), req.get('city'), req.get('state'),
        req.get('zip'),
        address_id)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/create', methods=['GET'])
def create_address_form():
    user = {'username': 'Addresses Project'}
    return render_template('create.html', user=user)


@app.route('/create', methods=['POST'])
def create_address():
    cursor = mysql.get_db().cursor()
    sql = "INSERT INTO addresses (first_name,last_name,street,city,state,zip) VALUES (%s,%s,%s,%s,%s,%s)"
    req = request.form
    val = (
        req.get('first_name'), req.get('last_name'), req.get('street'), req.get('city'), req.get('state'),
        req.get('zip'))
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:address_id>', methods=['POST'])
def delete_address(address_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM addresses WHERE id = %s"
    val = (address_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


# api

@app.route('/api/v1/addresses', methods=['GET'])
def list_addresses():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['GET'])
def view_address(address_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM addresses WHERE id=%s', address_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['PUT'])
def change_address(address_id):
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "UPDATE addresses SET first_name = %s, last_name=%s, street=%s, city=%s, state=%s, zip=%s WHERE id = %s"
    val = (
        content['first_name'], content['last_name'], content['street'], content['city'], content['state'],
        content['zip'],
        address_id)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses', methods=['POST'])
def new_address():
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "INSERT INTO addresses (first_name,last_name,street,city,state,zip) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (
        content['first_name'], content['last_name'], content['street'], content['city'], content['state'],
        content['zip'])
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/addresses/<int:address_id>', methods=['DELETE'])
def remove_address(address_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM addresses WHERE id = %s"
    val = (address_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)