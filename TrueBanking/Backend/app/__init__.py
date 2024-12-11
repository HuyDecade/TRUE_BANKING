from flask import Flask
from .routes import init_routes

def create_app():
    app = Flask(__name__)

    # Cấu hình ứng dụng nếu cần
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Đăng ký các route
    init_routes(app)

    return app
