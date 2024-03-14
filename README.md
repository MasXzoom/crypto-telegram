# Bot Pemantau Harga Mata Uang Kripto

Bot Telegram ini dirancang untuk memantau harga mata uang kripto secara real-time dan mengirim notifikasi ke pengguna melalui Telegram ketika terjadi perubahan harga yang signifikan atau drastis. Bot ini menggunakan API CoinGecko untuk mengambil data harga mata uang kripto dan mengirimkan update secara periodik berdasarkan konfigurasi yang ditentukan.

## Fitur Utama

- **Pemantauan Harga Real-time**: Mendukung pemantauan harga untuk berbagai mata uang kripto.
- **Notifikasi Otomatis**: Mengirim notifikasi ketika harga berubah melebihi threshold yang ditentukan.
- **Penyimpanan Data Lokal**: Menyimpan data harga terakhir ke dalam file untuk mempertahankan state antar sesi.
- **Konfigurasi Mudah**: Menggunakan file `.env` untuk konfigurasi mudah token bot, chat ID, dan simbol mata uang kripto.

## Persyaratan Sistem

- Python 3.7 atau lebih tinggi
- Modul `python-telegram-bot`
- Modul `requests`
- Akses internet untuk menghubungi API CoinGecko dan Telegram Bot API

## Cara Konfigurasi

1. Clone repositori ini.
2. Buat file `.env` pada direktori yang sama dengan skrip bot dengan isi sebagai berikut:

    ```
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    CHAT_ID=your_telegram_chat_id
    CRYPTO_SYMBOLS=btc,eth,sol  # Contoh simbol mata uang kripto
    ```

3. Ganti `your_telegram_bot_token` dengan token bot Telegram Anda, `your_telegram_chat_id` dengan chat ID Anda, dan `btc,eth,sol` dengan daftar simbol mata uang kripto yang ingin Anda pantau.

## Cara Menjalankan

```
pip install -r requirements.txt
```

Setelah konfigurasi selesai, jalankan bot dengan perintah berikut dari terminal: python3 bot.py

Bot akan mulai memantau harga mata uang kripto yang ditentukan dan mengirim notifikasi melalui Telegram sesuai dengan konfigurasi.

## Kontribusi

Kontribusi terhadap proyek ini sangat dihargai. Jika Anda memiliki saran atau perbaikan, silakan buat issue atau pull request.
