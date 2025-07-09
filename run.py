# run.py
# File utama untuk menjalankan aplikasi Flask.

from app import create_app, db
from app.models import User, Siswa, Kelas, Absensi

# Membuat instance aplikasi menggunakan app factory
app = create_app()

@app.shell_context_processor
def make_shell_context():
    """
    Menyediakan konteks untuk 'flask shell'.
    Memudahkan proses debugging dengan mengimpor model database secara otomatis.
    """
    return {'db': db, 'User': User, 'Siswa': Siswa, 'Kelas': Kelas, 'Absensi': Absensi}

if __name__ == '__main__':
    # Menjalankan aplikasi dalam mode debug.
    # Jangan gunakan mode debug di lingkungan produksi.
    app.run(debug=True)
