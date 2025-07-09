# app/face_logic.py
# Berisi semua logika yang terkait dengan pemrosesan wajah.

import face_recognition
import pickle
import os
from app.models import Siswa
from config import Config

def train_faces():
    """
    Melakukan training pada semua foto siswa yang ada di database dan menyimpannya ke 'encodings.pickle'.
    """
    print("Memulai proses training wajah...")
    from app import create_app
    app = create_app()
    with app.app_context():
        siswas = Siswa.query.filter(Siswa.foto_path.isnot(None)).all()

    if not siswas:
        if os.path.exists('encodings.pickle'): os.remove('encodings.pickle')
        return

    known_encodings = []
    known_ids = []

    for siswa in siswas:
        image_path = os.path.join(Config.UPLOAD_FOLDER, siswa.foto_path)
        if os.path.exists(image_path):
            try:
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_encodings.append(encodings[0])
                    known_ids.append(siswa.id)
                else:
                    print(f"Peringatan: Tidak ada wajah yang terdeteksi di {image_path}")
            except Exception as e:
                print(f"Error saat memproses gambar {image_path}: {e}")

    data = {"encodings": known_encodings, "ids": known_ids}
    with open('encodings.pickle', 'wb') as f:
        pickle.dump(data, f)
    print(f"Training selesai. Total {len(known_ids)} wajah berhasil di-train.")

def load_known_faces():
    """
    Memuat data encoding wajah dari file 'encodings.pickle'.
    """
    try:
        with open('encodings.pickle', 'rb') as f:
            data = pickle.load(f)
        return data['encodings'], data['ids']
    except FileNotFoundError:
        print("File 'encodings.pickle' tidak ditemukan. Lakukan training terlebih dahulu.")
        return [], []
