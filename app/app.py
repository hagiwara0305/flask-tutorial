from flask import Flask
import mysql.connector

#DB接続情報
def conn_db():
      conn = mysql.connector.connect(
              host = 'localhost',      #localhostでもOK
              user = 'root',
              passwd = 'root',
              db = 'test'
      )
      return conn

sql = ' select * from test_table'

try:
    conn = conn_db()              #ここでDBに接続
    cursor = conn.cursor()       #カーソルを取得
    cursor.execute(sql)             #selectを投げる
    rows = cursor.fetchall()      #selectの結果を全件タプルに格納

    cursor.close()                #接続を閉じる
    conn.close()

    print_str = ''
    for t_rows in rows:
        print_str += str(t_rows[0]) + ' ' + t_rows[1] + '<br>'    #selectの結果を1行ずつ表示
except(mysql.connector.errors.ProgrammingError) as e:
    print('エラーだぜ')
    print(e)


# ここからルーティング処理


app = Flask(__name__)

@app.route('/')
def hello():
    return print_str

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')