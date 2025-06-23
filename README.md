# LLMTwins-Line
這是一份程式碼，本用作於對科技城合作案的相關測試  
主要功能:通過對LINE API的訪問，達成對本地端程式碼的回應，架構如下:
![image](https://github.com/user-attachments/assets/8477b576-bdce-4c41-adfb-41480c8d887a)
本專案中的資料結構為:
```
.
|-- RAG-TEST
|   |-- __pycache__
|   |   `-- ai.cpython-311.pyc
|   |-- ai.py
|   |-- .env
|   `-- server.py
|-- README.md
`-- requirements.txt

```
其中sever.py會引入在ai.py中有設定的有關Gemini v1.5 Pro 的相關Prompt回覆，並去RAG相關網頁(在設定中為[本網頁](https://www.nlight.tw/pages/facts))
## 如何使用
首先創建虛擬環境並執行
```cmd
python -m venv venv
.\venv\Scripts\activate
```
再來安裝相對應的套件:
```python
pip install requirements.txt
```
編輯相對應的環境變數(.env):
```
CHANNEL_ACCESS_TOKEN = your_token
CHANNEL_SECRET = your_key
GOOGLE_API_KEY = your_api_key
```
最後啟動即可，必須使用ngrok或其他方式使localhost被public出來:
```
uvicorn server:app --reload
```
