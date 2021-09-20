from flask import Flask
import mysql.connector

# hostのipだけmysqlに入って「ifconfig」を売って調べる
conn = mysql.connector.connect(user='root', password='root', host='172.20.0.2', database='testdb')
cur = conn.cursor()

cur.execute("select * from test;")

printstr = ""
for row in cur.fetchall():
    printstr += str(row[0]) + row[1] + "<br>"

cur.close
conn.close

# ここからflask-app

app = Flask(__name__)

@app.route('/')
def hello_world():
    return printstr

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)