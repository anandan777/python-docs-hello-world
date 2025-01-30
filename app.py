from flask import Flask, Response

app = Flask(__name__)

@app.route('/cdn-images/stock/y/yf17vwj-7-l.jpg')
def fake_image():
    html_content = """
    <html>
        <body>
            <script>
                alert('Image is not available! Redirecting...');
                window.location.href = '/cdn-images/stock/y/yf17vwj-7-l-real.jpg';
            </script>
            <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==" style="display:none;">
        </body>
    </html>
    """
    return Response(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
