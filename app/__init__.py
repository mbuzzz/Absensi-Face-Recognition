# app/__init__.py
# File inisialisasi (app factory) untuk aplikasi Flask.

from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
import logging
from logging.handlers import RotatingFileHandler

# Inisialisasi ekstensi Flask
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'
login.login_message = 'Silakan login untuk mengakses halaman ini.'
login.login_message_category = 'info'

def create_app(config_class=Config):
    """
    App Factory: Fungsi untuk membuat dan mengkonfigurasi instance aplikasi Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Registrasi Blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from datetime import datetime
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow}
        
    # Menjalankan fungsi setup satu kali saat aplikasi dibuat.
    with app.app_context():
        from app.routes import refresh_data
        refresh_data()

    # --- KONFIGURASI LOGGING UNTUK PRODUKSI ---
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        # RotatingFileHandler memastikan file log tidak terlalu besar.
        file_handler = RotatingFileHandler('logs/absensi_app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Aplikasi Absensi Dimulai')

    # --- MENAMBAHKAN HALAMAN ERROR KUSTOM ---
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback() # Batalkan transaksi database yang mungkin error
        app.logger.error(f"Internal Server Error: {error}")
        return render_template('500.html'), 500
        
    return app
