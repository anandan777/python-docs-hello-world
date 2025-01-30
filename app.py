from flask import Flask, Response, redirect

app = Flask(__name__)

@app.route('/cdn-images/stock/y/yf17vwj-7-l.jpg')
def fake_image():
    js_code = "alert('Image is not available! Redirecting...'); window.location.href='/cdn-images/stock/y/yf17vwj-7-l-real.jpg';"
    return Response(js_code, mimetype='application/javascript')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
