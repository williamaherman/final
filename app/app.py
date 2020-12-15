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
app.config['MYSQL_DATABASE_DB'] = 'InventoryData'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def inventory():
    user = {'username': 'Inventory Viewer'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory')
    result = cursor.fetchall()
    return render_template('layout.html', user=user, addresses=result)


@app.route('/listview/<int:inventory_id>', methods=['GET'])
def show_inventory(inventory_id):
    user = {'username': 'Final Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory WHERE id=%s', inventory_id)
    result = cursor.fetchall()
    return render_template('listview.html', user=user, address=result[0])

@app.route('/edit/<int:inventory_id>', methods=['GET'])
def edit_inventory(inventory_id):
    user = {'username': 'Addresses Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory WHERE id=%s', inventory_id)
    result = cursor.fetchall()
    return render_template('edit.html', user=user, address=result[0])


@app.route('/edit/<int:inventory_id>', methods=['POST'])
def update_inventory(inventory_id):
    cursor = mysql.get_db().cursor()
    sql = "UPDATE Inventory SET product_name = %s, product_description=%s, made_in=%s, price=%s, color=%s WHERE id = %s"
    req = request.form
    val = (
        req.get('product_name'), req.get('product_description'), req.get('made_in'), req.get('price'), req.get('color'),
        inventory_id)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/new', methods=['GET'])
def create_inventory_form():
    user = {'username': 'sa'}
    return render_template('new.html', user=user)


@app.route('/new', methods=['POST'])
def create_inventory():
    cursor = mysql.get_db().cursor()
    sql = "INSERT INTO Inventory (product_name, product_description, made_in, price, color) VALUES (%s,%s,%s,%s,%s)"
    req = request.form
    val = (req.get('product_name'), req.get('product_description'), req.get('made_in'), req.get('price'), req.get('color'))
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:inventory_id>', methods=['POST'])
def delete_inventory(inventory_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM Inventory WHERE id = %s"
    val = (inventory_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/inventory', methods=['GET'])
def list_inventory():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/inventory/<int:inventory_id>', methods=['GET'])
def view_inventory(inventory_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM Inventory WHERE id=%s', inventory_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/inventory/<int:inventory_id>', methods=['PUT'])
def change_inventory(inventory_id):
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "UPDATE Inventory product_name = %s, product_description=%s, made_in=%s, price=%s, color=%s WHERE id = %s"
    val = (content['product_name'], content['product_description'], content['made_in'], content['price'], content['color'])
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/inventory', methods=['POST'])
def new_inventory():
    cursor = mysql.get_db().cursor()
    content = request.json
    sql = "INSERT INTO Inventory (product_name, product_description, made_in, price, color) VALUES (%s,%s,%s,%s,%s)"
    val = (content['product_name'], content['product_description'], content['made_in'], content['price'], content['color'])
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/inventory/<int:inventory_id>', methods=['DELETE'])
def remove_inventory(inventory_id):
    cursor = mysql.get_db().cursor()
    sql = "DELETE FROM Inventory WHERE id = %s"
    val = (inventory_id,)
    cursor.execute(sql, val)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

