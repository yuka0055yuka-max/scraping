https://yuka0055yuka-max.github.io/scraping/　←こちらで公開されてます
学習用スクレイピング PWAツール
日本語版
プロジェクト概要
このプロジェクトは、Python（Flask）バックエンドとシンプルなフロントエンドを組み合わせたPWA（プログレッシブWebアプリ）です。

robots.txt によるアクセス制御

禁止サイトはパスワード認証でのみ強制スクレイピング

HTML本文／script／meta／title から多層的に情報を抽出

類義語展開・正規表現・ノイズ除去を用いた精密検索

対話的にURL・キーワードを入力し、結果をJSONで返却

学習・実験・検証用途に最適化された設計となっています。

主な機能
対象URLとキーワードを入力する対話型UI

robots.txt の許可チェックとパスワードによるバイパス

Playwrightによる動的ページの取得

BeautifulSoupによるHTMLからのテキスト抽出

類義語を含む部分一致検索＆ヒット件数表示

結果をBOM付きUTF-8 JSON形式で保存

オフライン対応・ホーム画面追加可能なPWA

動作環境・要件
Python 3.7以上

Flask, flask-cors, python-dotenv, playwright, beautifulsoup4

Playwrightブラウザ（playwright install）

モダンブラウザ（Chrome, Edge, Firefox など）

インストール手順
リポジトリをクローンまたはダウンロード

bash
git clone https://github.com/あなたのユーザー名/リポジトリ名.git
cd リポジトリ名
仮想環境の作成・有効化

bash
python -m venv venv
# Windows Powershell
.\venv\Scripts\Activate.ps1
必要パッケージのインストール

bash
pip install flask flask-cors python-dotenv playwright beautifulsoup4
playwright install
環境変数ファイル .env をプロジェクト直下に作成

コード
SCRAPE_PASSWORD=your_secret_password
.gitignore に以下が含まれていることを確認

gitignore
.env
__pycache__/
*.py[cod]
playwright-report/
.vscode/
実行方法
bash
python backend.py
ブラウザで http://localhost:5000 を開く

URL・キーワード・（禁止時は）パスワードを入力し「スクレイプ実行」

JSON形式の結果を画面に表示

ブラウザのインストールボタンでPWAとしてホーム画面に追加可能

プロジェクト構成
コード
myproject/
├─ backend.py             # Flask APIサーバー
├─ scraper_logic.py       # スクレイピング／検索ロジック
├─ .env                   # 環境変数（コミット除外）
└─ static/
   ├─ index.html          # フロントエンドHTML
   ├─ app.js              # UI制御＆API呼び出し
   ├─ manifest.json       # PWAマニフェスト
   └─ service-worker.js   # オフラインキャッシュ設定
クレジット
開発者: YUME


## ライセンス

このプロジェクトは [Apache License 2.0](LICENSE) の下でライセンスされています。

## License



English Version
Learning Scraping PWA Tool
Project Overview
This project is a Progressive Web App combining a Python (Flask) backend with a lightweight frontend. It features:

Access control via robots.txt

Password-protected override for disallowed sites

Multi-layered extraction from HTML body, <script>, <meta>, and <title>

Precise search using synonyms, regex, and noise filtering

Interactive input of URL and keywords, returning JSON results

Optimized for learning, experimentation, and verification.

Key Features
Interactive UI for entering target URL and keywords

robots.txt check with optional password bypass

Dynamic page retrieval via Playwright

Text extraction from HTML using BeautifulSoup

Synonym-expanded partial match search & hit-count display

Results saved as BOM-prefixed UTF-8 JSON

Offline-ready and installable PWA

Requirements
Python 3.7+

Flask, flask-cors, python-dotenv, playwright, beautifulsoup4

Playwright browsers (playwright install)

Modern web browser (Chrome, Edge, Firefox, etc.)

Installation
Clone or download the repository

bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create and activate a virtual environment

bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
Install dependencies

bash
pip install flask flask-cors python-dotenv playwright beautifulsoup4
playwright install
Create a .env file at the project root:

コード
SCRAPE_PASSWORD=your_secret_password
Ensure .gitignore contains the following:

gitignore
.env
__pycache__/
*.py[cod]
playwright-report/
.vscode/
Usage
bash
python backend.py
Open your browser at http://localhost:5000

Enter URL, keywords, and (if disallowed) password

View JSON results in the page

Click the install button to add the app as a PWA
Project Structure
コード
myproject/
├─ backend.py             # Flask API server
├─ scraper_logic.py       # Scraping & search logic
├─ .env                   # Environment variables (excluded)
└─ static/
   ├─ index.html          # Frontend HTML
   ├─ app.js              # UI logic & API calls
   ├─ manifest.json       # PWA manifest
   └─ service-worker.js   # Offline caching
Credits
Developer: YUME
## License
This project is licensed under the [Apache License 2.0](LICENSE).

