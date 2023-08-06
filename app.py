from flask import Flask
from views import views
from delete_QR import execute_delete
import threading

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

delete_thread = threading.Thread(target=execute_delete, daemon=True)
delete_thread.start()

if __name__ == '__main__':
    app.run(debug=False)

