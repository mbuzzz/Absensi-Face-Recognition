# config.py
# Menyimpan semua konfigurasi untuk aplikasi Flask.

import os
from dotenv import load_dotenv

# Menentukan direktori dasar proyek
basedir = os.path.abspath(os.path.dirname(__file__))
# Memuat variabel dari file .env
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    Kelas konfigurasi utama.
    Mengambil nilai dari environment variables atau menggunakan nilai default.
    """
    # Kunci rahasia untuk melindungi form dan session dari serangan CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Konfigurasi database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Menonaktifkan fitur modifikasi dari Flask-SQLAlchemy yang tidak digunakan
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # URL Webhook untuk integrasi dengan n8n
    N8N_WEBHOOK_URL = os.environ.get('N8N_WEBHOOK_URL')

    # Konfigurasi untuk upload file
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads/siswa_photos')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
