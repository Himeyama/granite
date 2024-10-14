# Granite
小さなサーバーを立ち上げ、小さなデータを記録します。

## インストール方法
https://github.com/Himeyama/Granite/releases よりインストーラーをダウンロードし、インストールを行います。

PC 起動時にアプリ (サーバー) が起動します。

> [!NOTE]
> `Win` + `R` のファイル名を指定して実行で `shell:startup` を実行するとショートカットがあります。

## 開発環境
以下、開発者向けの説明です。

- Windows 11
- Python 3.8.10 (pyenv install 3.8)
- Poetry (pip install poetry)

```bash
poetry shell # 仮想環境立ち上げ
poetry install # 依存パッケージインストール
```

## 実行

```bash
poetry run task main # サーバー起動
```

## 実行ファイル作成
PyInstaller で実行ファイルを作成します。

```bash
poetry run task build # PyInstaller で実行ファイル作成
```

## インストーラー作成
nsis でインストーラーを作成します。

```bash
poetry run task pack
```

## API 実行
[FastAPI - Swagger UI](http://localhost:50032/docs)
