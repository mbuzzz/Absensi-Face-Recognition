<div align="center">
<img src="https://placehold.co/150x150/4e73df/FFFFFF?text=Logo" alt="Logo Aplikasi" width="120">
<h1>Aplikasi Absensi Wajah Real-Time</h1>
<p>
Aplikasi web modern berbasis Python Flask untuk sistem absensi sekolah yang cerdas dan otomatis.
</p>
<p>
<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
<img src="https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask" alt="Flask Version">
<img src="https://img.shields.io/badge/OpenCV-4.x-blue?style=for-the-badge&logo=opencv" alt="OpenCV Version">
<img src="https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap" alt="Bootstrap Version">
</p>
</div>

Aplikasi ini menggunakan teknologi pengenalan wajah secara real-time untuk mencatat kehadiran siswa secara otomatis, dilengkapi dengan dashboard admin yang interaktif, manajemen data yang lengkap, dan sistem pelaporan yang canggih.
✨ Fitur Utama

    Live Absensi: Kamera real-time untuk proses absensi dengan deteksi multi-wajah dan umpan balik visual saat absensi berhasil.

    Dashboard Dinamis: Grafik dan rekapitulasi kehadiran harian serta tren mingguan menggunakan Chart.js.

    Manajemen Data Lengkap (CRUD):

        Manajemen Siswa & Foto untuk Training.

        Manajemen Kelas & Wali Kelas.

        Manajemen Pengguna dengan 4 level hak akses (Admin, Wali Kelas, BK, Petugas).

    Laporan Canggih:

        Edit kehadiran harian untuk mengubah status siswa (Izin, Sakit, Alpha).

        Log kehadiran dengan filter per kelas dan rentang waktu (harian, mingguan, bulanan).

        Ekspor laporan yang telah difilter ke format file Excel.

    Sistem Absensi Cerdas:

        Otomatis menandai siswa "Terlambat" berdasarkan jam yang bisa diatur.

        Otomatis menandai siswa "Alpha" jika tidak ada kabar hingga jam yang ditentukan.

    Pengaturan Aplikasi: Kustomisasi nama aplikasi, nama sekolah, logo, dan jam-jam penting melalui panel admin.

    Integrasi Notifikasi: Siap terhubung dengan n8n untuk notifikasi ke Telegram, WhatsApp (via WAHA), atau platform lainnya.

🛠️ Teknologi yang Digunakan

    Backend: Python, Flask

    Computer Vision: OpenCV, dlib, face_recognition

    Database: SQLAlchemy, Flask-Migrate (dengan SQLite sebagai default)

    Frontend: HTML, Bootstrap 5, CSS, JavaScript, Chart.js

    Deployment: Siap dijalankan dengan Gunicorn untuk lingkungan produksi.

🚀 Panduan Instalasi & Setup

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda.
1. Prasyarat

Pastikan perangkat Anda telah terinstal:

    Git

    Python 3.8 atau lebih baru.

    C++ Compiler & CMake: Ini sangat penting untuk menginstal library dlib.

        Windows: Install Visual Studio dengan paket "Desktop development with C++".

        macOS: Jalankan brew install cmake.

        Linux (Debian/Ubuntu): Jalankan sudo apt-get install build-essential cmake.

2. Clone Repository

Buka terminal atau command prompt, lalu clone repository ini:

git clone https://github.com/mbuzzz/Absensi-Face-Recognition.git
cd Absensi-Face-Recognition

3. Buat Virtual Environment

Sangat disarankan untuk menggunakan virtual environment agar tidak mengganggu instalasi Python global Anda.

# Membuat environment baru bernama 'venv'
python -m venv venv

4. Aktifkan Virtual Environment

# Di Windows (Command Prompt):
venv\Scripts\activate

# Di macOS / Linux:
source venv/bin/activate

    ⚠️ Catatan untuk Pengguna Windows PowerShell
    Jika Anda menggunakan PowerShell dan mendapatkan error seperti ...cannot be loaded because running scripts is disabled on this system, jalankan perintah berikut terlebih dahulu untuk mengizinkan eksekusi skrip hanya untuk sesi terminal saat ini. Ini adalah langkah yang aman.

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

    Setelah itu, jalankan kembali perintah venv\Scripts\activate.

5. Install Ketergantungan

Setelah virtual environment aktif, install semua library yang dibutuhkan dengan satu perintah:

pip install -r requirements.txt

6. Konfigurasi Environment (.env)

Buat file baru bernama .env di direktori utama proyek. Salin konten di bawah ini ke dalam file tersebut dan sesuaikan nilainya.

# Ganti dengan string acak yang sangat kuat untuk keamanan sesi
SECRET_KEY='kunci-rahasia-anda-yang-sulit-ditebak'

# Path ke database SQLite (tidak perlu diubah untuk setup lokal)
DATABASE_URI='sqlite:///app.db'

# (Opsional) URL Webhook dari n8n untuk notifikasi
N8N_WEBHOOK_URL='https://url-n8n-anda/webhook/...'

7. Setup Database

Jalankan perintah berikut secara berurutan untuk membuat database dan semua tabelnya.

# 1. Inisialisasi folder migrasi (hanya dijalankan sekali untuk proyek baru)
flask db init

# 2. Buat file migrasi pertama berdasarkan model yang ada
flask db migrate -m "Initial database migration"

# 3. Terapkan migrasi tersebut untuk membuat tabel di database
flask db upgrade

Catatan: Jika Anda mengubah model di app/models.py di kemudian hari, cukup jalankan langkah 2 dan 3 lagi untuk memperbarui database.
8. Buat User Admin Pertama

Untuk bisa login dan mengelola aplikasi, Anda harus membuat satu akun Admin terlebih dahulu. Ini dilakukan melalui shell interaktif Flask.

Langkah 1: Buka Flask Shell

Di terminal Anda (pastikan virtual environment masih aktif), jalankan perintah berikut:

flask shell

Anda akan melihat prompt >>> muncul, yang menandakan Anda sudah masuk ke dalam shell Python.

Langkah 2: Jalankan Kode Python

Salin dan tempel (copy-paste) seluruh blok kode di bawah ini ke dalam shell, lalu tekan Enter. Kode ini akan memeriksa apakah user admin sudah ada. Jika belum, ia akan membuatnya.

from app import db
from app.models import User

# Cek apakah user 'admin' sudah ada
user = User.query.filter_by(username='admin').first()

if not user:
    # Jika belum ada, buat user baru
    u = User(username='admin', email='admin@sekolah.com', role='Admin')
    u.set_password('admin') # Ganti dengan password yang aman
    db.session.add(u)
    db.session.commit()
    print("User admin berhasil dibuat!")
else:
    # Jika sudah ada, beri tahu pengguna
    print("User admin sudah ada di database.")

Langkah 3: Keluar dari Shell

Setelah melihat pesan konfirmasi, ketik exit() dan tekan Enter untuk keluar.
9. Jalankan Aplikasi

Sekarang aplikasi Anda siap dijalankan!

python run.py

Buka browser Anda dan akses alamat http://127.0.0.1:5000.
Kredit

Dibuat dengan ❤️ oleh Rifqy Iza Fahrizal dan Yanuar.
