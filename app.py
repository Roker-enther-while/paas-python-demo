import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo PaaS - Cloud Computing</title>
        <meta charset="utf-8">
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1 style="color: #184C78;">Triển Khai Ứng Dụng Thành Công Trên Nền Tảng PaaS (Render.com)</h1>
        <p><b>Học phần:</b> Điện toán đám mây</p>
        <p><b>Mô hình:</b> Platform as a Service (PaaS)</p>
        <p style="color: green;"><i>Trạng thái: Ứng dụng Python Flask đang chạy trực tuyến!</i></p>
    </body>
    </html>
    """

@app.route("/api/health")
def health():
    return jsonify({
        "status": "UP",
        "model": "Platform as a Service (PaaS)",
        "platform": "Render.com",
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
