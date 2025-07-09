# app/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.fields import DateField, TimeField
from app.models import User, Kelas
from datetime import date

# --- Factory untuk Query ---
def kelas_query():
    """Fungsi factory untuk mendapatkan daftar kelas untuk form."""
    return Kelas.query.order_by(Kelas.nama_kelas).all()

# --- Form Otentikasi ---
class LoginForm(FlaskForm):
    """Form untuk login pengguna."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Ingat Saya')
    submit = SubmitField('Login')

# --- Form CRUD Siswa ---
class SiswaForm(FlaskForm):
    """Form untuk menambah data siswa."""
    nis = StringField('NIS (Nomor Induk Siswa)', validators=[DataRequired()])
    nama = StringField('Nama Lengkap', validators=[DataRequired()])
    nomor_orang_tua = StringField('Nomor Telepon Orang Tua/Wali')
    kelas = QuerySelectField('Kelas', query_factory=kelas_query, get_label='nama_kelas', allow_blank=False, validators=[DataRequired()])
    foto = FileField('Foto Wajah Siswa (.jpg, .png)', validators=[
        FileRequired(message="File foto wajib diisi!"),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Hanya file gambar (.jpg, .jpeg, .png) yang diizinkan!')
    ])
    submit = SubmitField('Simpan Data')

class SiswaEditForm(FlaskForm):
    """Form untuk mengedit data siswa (foto opsional)."""
    nis = StringField('NIS (Nomor Induk Siswa)', validators=[DataRequired()])
    nama = StringField('Nama Lengkap', validators=[DataRequired()])
    nomor_orang_tua = StringField('Nomor Telepon Orang Tua/Wali')
    kelas = QuerySelectField('Kelas', query_factory=kelas_query, get_label='nama_kelas', allow_blank=False, validators=[DataRequired()])
    foto = FileField('Ganti Foto Wajah (Opsional)', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Hanya file gambar (.jpg, .jpeg, .png) yang diizinkan!')
    ])
    submit = SubmitField('Update Data')

# --- Form CRUD Kelas ---
class KelasForm(FlaskForm):
    """Form untuk menambah atau mengedit data kelas."""
    nama_kelas = StringField('Nama Kelas', validators=[DataRequired()], render_kw={"placeholder": "Contoh: XII TKJ 1"})
    wali_kelas_nama = StringField('Nama Wali Kelas (untuk tampilan)', validators=[DataRequired()], render_kw={"placeholder": "Contoh: Bpk. Budi Santoso, S.Kom"})
    submit = SubmitField('Simpan')

# --- Form CRUD User ---
class UserForm(FlaskForm):
    """Form untuk menambah pengguna."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Peran', choices=[
        ('Admin', 'Admin'), 
        ('Wali Kelas', 'Wali Kelas'), 
        ('BK', 'BK'), 
        ('Petugas', 'Petugas')
    ], validators=[DataRequired()])
    kelas_asuhan = QuerySelectField('Kelas Asuhan (khusus Wali Kelas)', query_factory=kelas_query, get_label='nama_kelas', allow_blank=True, blank_text='-- Tidak Ada --')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Ulangi Password', validators=[DataRequired(), EqualTo('password', message='Password harus sama!')])
    submit = SubmitField('Simpan Pengguna')

class UserEditForm(FlaskForm):
    """Form untuk mengedit pengguna."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Peran', choices=[
        ('Admin', 'Admin'), 
        ('Wali Kelas', 'Wali Kelas'), 
        ('BK', 'BK'), 
        ('Petugas', 'Petugas')
    ], validators=[DataRequired()])
    kelas_asuhan = QuerySelectField('Kelas Asuhan (khusus Wali Kelas)', query_factory=kelas_query, get_label='nama_kelas', allow_blank=True, blank_text='-- Tidak Ada --')
    password = PasswordField('Password Baru (opsional)')
    password2 = PasswordField('Ulangi Password Baru', validators=[Optional(), EqualTo('password', message='Password harus sama!')])
    submit = SubmitField('Update Pengguna')

# --- Form Pengaturan ---
class PengaturanForm(FlaskForm):
    """Form untuk pengaturan umum aplikasi."""
    nama_aplikasi = StringField('Nama Aplikasi', validators=[DataRequired()])
    nama_sekolah = StringField('Nama Sekolah', validators=[DataRequired()])
    logo_aplikasi = FileField('Upload Logo Baru (Opsional)', validators=[
        Optional(),
        FileAllowed(['png', 'jpg', 'jpeg', 'svg'], 'Hanya file gambar yang diizinkan!')
    ])
    waktu_terlambat = TimeField('Batas Waktu Dianggap Terlambat', format='%H:%M', validators=[DataRequired()])
    waktu_alpha = TimeField('Batas Waktu Dianggap Alpha', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Simpan Pengaturan')

# --- Form Laporan & Kehadiran ---
class LaporanFilterForm(FlaskForm):
    """Form untuk memfilter laporan log kehadiran dengan rentang tanggal."""
    kelas = QuerySelectField('Filter Kelas', query_factory=kelas_query, get_label='nama_kelas', allow_blank=True, blank_text='-- Semua Kelas --')
    tanggal_mulai = DateField('Dari Tanggal', format='%Y-%m-%d', default=date.today, validators=[DataRequired()])
    tanggal_akhir = DateField('Sampai Tanggal', format='%Y-%m-%d', default=date.today, validators=[DataRequired()])
    submit = SubmitField('Tampilkan Log')
    export = SubmitField('Export ke Excel')

class KehadiranHarianFilterForm(FlaskForm):
    """Form untuk filter halaman edit kehadiran harian."""
    kelas = QuerySelectField('Filter Kelas', query_factory=kelas_query, get_label='nama_kelas', allow_blank=True, blank_text='-- Semua Kelas --')
    tanggal = DateField('Pilih Tanggal', format='%Y-%m-%d', default=date.today, validators=[DataRequired()])
    submit = SubmitField('Tampilkan')

class KehadiranUpdateForm(FlaskForm):
    """Form untuk mengupdate status kehadiran per siswa."""
    status = SelectField('Status', choices=[
        ('Hadir', 'Hadir'),
        ('Terlambat', 'Terlambat'),
        ('Izin', 'Izin'),
        ('Sakit', 'Sakit'),
        ('Alpha', 'Alpha')
    ], validators=[DataRequired()])
    keterangan = TextAreaField('Keterangan', render_kw={"rows": 1, "placeholder": "Keterangan..."})
    submit = SubmitField('Update')
