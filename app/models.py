# app/models.py
# Definisi semua model database menggunakan SQLAlchemy.

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    """Model untuk pengguna (Admin, Wali Kelas, BK, Petugas)."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    role = db.Column(db.String(20), nullable=False)
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.id'), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Kelas(db.Model):
    """Model untuk data kelas."""
    id = db.Column(db.Integer, primary_key=True)
    nama_kelas = db.Column(db.String(50), unique=True, nullable=False)
    wali_kelas_nama = db.Column(db.String(100))
    siswas = db.relationship('Siswa', backref='kelas', lazy='dynamic')
    wali_kelas_user = db.relationship('User', backref='kelas_asuhan', uselist=False)

class Siswa(db.Model):
    """Model untuk data siswa."""
    id = db.Column(db.Integer, primary_key=True)
    nis = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    nomor_orang_tua = db.Column(db.String(20), nullable=True)
    foto_path = db.Column(db.String(200))
    kelas_id = db.Column(db.Integer, db.ForeignKey('kelas.id'), nullable=False)

class Absensi(db.Model):
    """Model untuk mencatat setiap record kehadiran."""
    id = db.Column(db.Integer, primary_key=True)
    siswa_id = db.Column(db.Integer, db.ForeignKey('siswa.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Menambahkan status 'Terlambat'
    status = db.Column(db.String(20), default='Hadir', nullable=False) # Hadir, Terlambat, Izin, Sakit, Alpha
    keterangan = db.Column(db.String(255), nullable=True)
    siswa = db.relationship('Siswa', backref='absensi_records')

class Pengaturan(db.Model):
    """Model untuk menyimpan pengaturan aplikasi secara dinamis (key-value)."""
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Pengaturan {self.key}>'
