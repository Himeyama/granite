import os
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import sys
from granite.port import check_tcp_connectivity
import tkinter
from tkinter import messagebox
from granite.database import create_granite_table, insert_data, read_data, remove_data


# ポート番号
port: int = 50032

# token_path: str = "token.txt"
dir: str = ""
if os.path.isdir("_internal"):
    dir = "_internal/"

if check_tcp_connectivity("127.0.0.1", port):
    print("ポート番号が使用されています。\n" \
          f"{port} ポートを使用してるアプリケーションを終了してください。")
    root: tkinter.Tk = tkinter.Tk()
    root.withdraw()
    root.iconbitmap(f"{dir}icon.ico")
    messagebox.showerror('起動エラー',
        "ポート番号が使用されています。\n" \
        f"{port} ポートを使用してるアプリケーションを終了してください。")
    
    ret: bool = messagebox.askyesno('アプリ', 'アプリを終了しますか?')
    if ret:
        os.system('taskkill /F /IM granite.exe')

    sys.exit(False)

create_granite_table()

app: FastAPI = FastAPI()

class DataModel(BaseModel):
    data: str

class UuidModel(BaseModel):
    uuid: str

@app.post("/save")
async def save_data(item: DataModel):
    data: str = item.data
    insert_data(data)
    return {"data": data}

@app.get("/load")
async def load_data():
    data: list[str] = []
    for row in read_data():
        data.append({"uuid": row[0], "data": row[1], "date": row[2]})
    return data

@app.post("/delete")
async def delete_data(item: UuidModel):
    remove_data(item.uuid)
    return {
        "uuid": item.uuid
    }

# 標準出力を捨てる
sys.stdout = open(os.devnull, 'w')

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=port)
    except Exception as ex:
        print(ex)
