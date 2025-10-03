# IPWAN-WiFi-Finder: Simple ICMP Sweep Tool

**IPWAN-WiFi-Finder** adalah sebuah skrip Python sederhana yang berfungsi sebagai alat bantu untuk fase **Reconnaissance** (pengintaian) dalam kegiatan *penetration testing*. Skrip ini mengotomatisasi proses **Ping Sweep** (atau ICMP Sweep) untuk secara cepat mengidentifikasi host yang aktif (*live hosts*) dalam sebuah rentang alamat IP.

Alat ini dirancang untuk efisiensi, memungkinkan seorang *pentester* untuk dengan cepat memetakan arsitektur jaringan target dengan mengganti proses ping manual yang memakan waktu.

## Latar Belakang & Tujuan 🎯

Dalam sebuah skenario *pentest*, langkah awal adalah memahami "medan perang" digital. Salah satu tugas pertama adalah mengetahui perangkat apa saja yang terhubung dan aktif di jaringan target. Skrip ini diciptakan untuk menjawab kebutuhan tersebut:

* **Pemetaan Jaringan**: Mengidentifikasi IP WAN dari perangkat Wi-Fi (atau perangkat lain) yang merespons permintaan ICMP.
* **Efisiensi Recon**: Menggunakan *multithreading* untuk menjalankan puluhan ping secara simultan, mempercepat proses pengumpulan informasi secara drastis.
* **Menentukan Target Potensial**: Dengan daftar IP yang aktif, seorang *pentester* dapat melanjutkan ke tahap selanjutnya seperti *port scanning*, *service enumeration*, dan *vulnerability analysis* pada target yang valid.

---

## Fitur Utama ✨

* **Eksekusi Paralel**: Ditenagai oleh `ThreadPoolExecutor` untuk memindai hingga 50 IP secara bersamaan.
* **Cross-Platform**: Berjalan mulus di **Windows, Linux, dan macOS** tanpa modifikasi.
* **Konfigurasi Fleksibel**: Cukup ubah dua variabel (`base_ip` dan `ip_range`) untuk mendefinisikan lingkup pemindaian.
* **Output Jelas**: Memberikan status yang mudah dibaca untuk setiap IP: `alive` (merespons) atau `unreachable` (tidak merespons).

---

## Persyaratan Sistem

* **Python 3.x**

Tidak ada dependensi eksternal yang perlu diinstal. Semua modul yang dibutuhkan sudah menjadi bagian dari pustaka standar Python.

---

## Panduan Penggunaan 🚀

1.  **Simpan Skrip**
    Salin kode di bawah ini dan simpan dalam sebuah file bernama `ping.py`.

2.  **Tentukan Lingkup (Scope)**
    Buka file `ping.py` dan sesuaikan variabel di bagian atas untuk mencocokkan rentang IP yang menjadi target pengujian Anda.

    ```python
    # === KONFIGURASI TARGET ===
    base_ip = "172.18.1."      # 3 oktet pertama dari subnet target
    ip_range = range(1, 255)   # Rentang untuk oktet terakhir (misal: 1-254)
    # ==========================
    ```

3.  **Luncurkan Pemindaian**
    Buka terminal atau Command Prompt, arahkan ke direktori tempat file `ping.py` berada, dan eksekusi perintah berikut:

    ```bash
    python ping.py
    ```

4.  **Analisis Hasil**
    Skrip akan menampilkan daftar alamat IP beserta statusnya secara *real-time*. Catat alamat IP yang berstatus `alive` untuk dianalisis lebih lanjut.

---
