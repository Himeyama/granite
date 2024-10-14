import datetime
import sqlite3
import uuid


def create_granite_table():
    # データベースに接続（この時点でファイルがなければ自動的に作成される）
    conn = sqlite3.connect("granite.db")
    # カーソルオブジェクトを作成
    cursor = conn.cursor()
    # テーブルを作成するSQL文
    create_table_query = """
    CREATE TABLE IF NOT EXISTS granite (
        uuid TEXT PRIMARY KEY,
        data TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """
    # SQL文を実行してテーブルを作成
    cursor.execute(create_table_query)
    # 変更を保存
    conn.commit()
    # カーソルと接続を閉じる
    cursor.close()
    conn.close()


# データを書き込む関数
def insert_data(data):
    # データベースに接続
    conn = sqlite3.connect("granite.db")
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO granite (uuid, data, date) VALUES (?, ?, ?)
    """
    # UUIDを生成し、現在の日付を取得
    new_uuid = str(uuid.uuid4())
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # データを挿入
    cursor.execute(insert_query, (new_uuid, data, current_date))
    conn.commit()
    # カーソルと接続を閉じる
    cursor.close()
    conn.close()


def read_data():
    # データベースに接続
    conn = sqlite3.connect("granite.db")
    cursor = conn.cursor()
    # データを取得するSQL文
    select_query = "SELECT * FROM granite"
    # SQL文を実行
    cursor.execute(select_query)
    # 取得したデータをすべてフェッチ
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows


def remove_data(uuid: str):
    # データベースに接続
    conn = sqlite3.connect("granite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM granite WHERE uuid = ?", (uuid,))
    # 変更を保存
    conn.commit()
    # カーソルと接続を閉じる
    cur.close()
    conn.close()
