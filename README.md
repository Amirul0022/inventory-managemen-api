# 📦 Gudang API - Sistem Manajemen Inventori

Sistem backend RESTful API modular untuk manajemen data barang dan transaksi (masuk/keluar) gudang. Proyek ini dibangun menggunakan **FastAPI** dan dilengkapi dengan arsitektur kontrak data (Pydantic), sistem autentikasi, serta *automated testing* (Pytest).

## 🚀 Fitur Utama
* **Manajemen Barang (CRUD):** Tambah, lihat daftar, lihat detail, dan hapus barang.
* **Manajemen Transaksi:** Pencatatan barang masuk (IN) dan barang keluar (OUT).
* **Validasi Aturan Bisnis:** Penolakan transaksi keluar (OUT) jika stok tidak mencukupi, dan validasi tipe data menggunakan Pydantic.
* **Keamanan API:** Proteksi *endpoint* manipulasi data menggunakan autentikasi *Header* `X-API-Key`.
* **Automated Testing:** Dilengkapi dengan 15 skenario *unit test* komprehensif (Cakupan 100% *Passed*).

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** Python 3
* **Framework:** FastAPI
* **Validasi Data:** Pydantic V2
* **Server:** Uvicorn
* **Testing:** Pytest

## 📂 Struktur Direktori
```text
gudang_api/
├── dependencies/       # Logika injeksi dependensi (Autentikasi API Key)
├── routers/            # Endpoint API (items.py, transactions.py)
├── schemas/            # Kontrak data Pydantic (item.py, transaction.py)
├── tests/              # Kumpulan automated unit test (test_main.py)
└── main.py             # Entry point aplikasi FastAPI
