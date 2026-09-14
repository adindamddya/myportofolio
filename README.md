Nama : Adinda Madya Aliyah

NPM : 2506656362

Kelas : PBP CLatihan Branching


Nama : Adinda Madya Aliyah

NPM : 2506656362

Kelas : PBP C

### Tugas 2

1. Jelaskan bagaimana alur data dari URL hingga ditampilkan ke browser.

   Ketika pengguna membuka halaman Education, request akan masuk ke URL configuration pada project dan diteruskan ke `main/urls.py`. Setelah itu, request diarahkan ke view `show_education`. View tersebut mengambil data dari model `Education` menggunakan `Education.objects.all()`, kemudian memasukkan data tersebut ke dalam context. Context kemudian dikirim ke template `education.html`. Di dalam template, Django Template Language digunakan untuk melakukan perulangan dan menampilkan data pendidikan. Setelah proses rendering selesai, halaman tersebut dikirim kembali dan ditampilkan pada browser.

2. Jelaskan mengapa data bagian portofolio baru sebaiknya disimpan dalam model dibandingkan langsung di template HTML.

   Data pendidikan lebih baik disimpan di dalam model karena lebih mudah untuk dikelola dan diperbarui. Jika data ditulis langsung di template HTML, setiap perubahan atau penambahan data harus dilakukan pada kode HTML. Dengan menyimpan data di model, data dapat ditambah, diubah, atau dihapus melalui database tanpa perlu mengubah struktur template. Hal ini juga membuat website lebih mudah dikembangkan jika jumlah data pendidikan semakin banyak.

3. Jelaskan perbedaan `makemigrations` dan `migrate`.

   `makemigrations` digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada model. Sedangkan `migrate` digunakan untuk menerapkan perubahan tersebut ke database. Contohnya, setelah membuat model `Education`, saya menjalankan `makemigrations` untuk menghasilkan file `0002_education.py`. Setelah itu, saya menjalankan `migrate` untuk membuat perubahan tersebut diterapkan pada database.

### AI Disclosure

Saya menggunakan ChatGPT sebagai salah satu referensi selama pengerjaan Tugas 2, terutama untuk memahami konsep MVT, mengecek beberapa error pada implementasi, dan membantu melakukan review terhadap unit test. Implementasi dan pengujian tetap dilakukan pada project yang saya kerjakan.

### Riwayat Bantuan AI

- Memahami penerapan MVT pada section Education.
- Membantu mengecek error pada model, URL, dan unit test.
- Melakukan review terhadap hasil implementasi dan checklist tugas.