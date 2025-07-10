Aplikasi Absensi Wajah Real-Time

Aplikasi web modern berbasis Python Flask untuk sistem absensi sekolah. Menggunakan teknologi pengenalan wajah secara real-time untuk mencatat kehadiran siswa secara otomatis, dilengkapi dengan dashboard admin yang interaktif, manajemen data yang lengkap, dan sistem pelaporan yang canggih.

(Disarankan untuk mengganti URL ini dengan screenshot dashboard aplikasi Anda)
Fitur Utama

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

Teknologi yang Digunakan

    Backend: Python, Flask

    Computer Vision: OpenCV, dlib, face_recognition

    Database: SQLAlchemy, Flask-Migrate (dengan SQLite sebagai default)

    Frontend: HTML, Bootstrap 5, CSS, JavaScript, Chart.js

    Deployment: Siap dijalankan dengan Gunicorn untuk lingkungan produksi.

Panduan Instalasi & Setup

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

(Ganti username/nama-repo dengan URL repository GitHub Anda)
3. Buat Virtual Environment

Sangat disarankan untuk menggunakan virtual environment agar tidak mengganggu instalasi Python global Anda.

# Membuat environment baru bernama 'venv'
python -m venv venv

# Mengaktifkan environment
# Di Windows:
venv\Scripts\activate
# Di macOS / Linux:
source venv/bin/activate

4. Install Ketergantungan

Install semua library Python yang dibutuhkan dari file requirements.txt dengan satu perintah:

pip install -r requirements.txt

5. Konfigurasi Environment (.env)

Buat file baru bernama .env di direktori utama proyek. Salin konten di bawah ini ke dalam file tersebut dan sesuaikan nilainya.

# Ganti dengan string acak yang sangat kuat untuk keamanan sesi
SECRET_KEY='kunci-rahasia-anda-yang-sulit-ditebak'

# Path ke database SQLite (tidak perlu diubah untuk setup lokal)
DATABASE_URI='sqlite:///app.db'

# (Opsional) URL Webhook dari n8n untuk notifikasi
N8N_WEBHOOK_URL='https://url-n8n-anda/webhook/...'

6. Setup Database

Jalankan perintah berikut secara berurutan untuk membuat database dan semua tabelnya.

# 1. Inisialisasi folder migrasi (hanya dijalankan sekali untuk proyek baru)
flask db init

# 2. Buat file migrasi pertama berdasarkan model yang ada
flask db migrate -m "Initial database migration"

# 3. Terapkan migrasi tersebut untuk membuat tabel di database
flask db upgrade

Catatan: Jika Anda mengubah model di app/models.py di kemudian hari, cukup jalankan langkah 2 dan 3 lagi untuk memperbarui database.
7. Buat User Admin Pertama

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
8. Jalankan Aplikasi

Sekarang aplikasi Anda siap dijalankan!

python run.py

Buka browser Anda dan akses alamat http://127.0.0.1:5000.
Kredit

Dibuat dengan ❤️ oleh Rifqy Iza Fahrizal
