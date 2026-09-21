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


### Tugas 3

Pada Tugas 3, saya melakukan refactoring template HTML dengan menggunakan `base.html` sebagai root template. Saya juga menerapkan mekanisme form dan data delivery pada bagian Education. Fitur yang dibuat meliputi Create, Update, Delete, JSON Data Delivery, serta proses deserialization JSON sebelum data ditampilkan pada halaman Education. Selain itu, saya menambahkan fitur pencarian berdasarkan nama sekolah sebagai fitur tambahan.

1. **Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!**

   Saya menggunakan `ModelForm` karena form dapat dibuat berdasarkan model Django yang sudah ada. Dengan `ModelForm`, field dan proses validasi dapat mengikuti struktur model sehingga saya tidak perlu membuat setiap input dan proses penyimpanan data secara manual. Setelah form valid, data juga dapat langsung disimpan ke database menggunakan model yang terkait.

   `{% csrf_token %}` digunakan pada form dengan method `POST` untuk membantu melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token tersebut digunakan Django untuk memastikan bahwa request POST berasal dari form yang valid pada aplikasi.

2. **Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**

   JSON lebih sering digunakan karena struktur datanya sederhana, ringkas, dan mudah dibaca maupun diproses oleh program. Format JSON juga sesuai dengan struktur data yang umum digunakan dalam aplikasi web, sehingga memudahkan pertukaran data antara server dan client. Dibandingkan XML, JSON biasanya memiliki penulisan yang lebih sederhana sehingga lebih praktis untuk digunakan dalam pengembangan aplikasi web.

3. **Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?**

   Pada project saya, data Education terlebih dahulu diambil dari database menggunakan model `Education`. Data tersebut kemudian diproses menggunakan serialization untuk mengubah object Django menjadi format JSON yang dapat dikirim melalui HTTP response. Setelah itu, pada halaman Education, JSON tersebut diambil dan dilakukan deserialization sehingga data JSON kembali menjadi object Django yang dapat digunakan oleh template untuk menampilkan informasi Education.

#### AI Disclosure

Dalam pengerjaan Tugas 3, saya menggunakan AI untuk membantu memahami beberapa konsep Django dan ketika mengalami error saat mengerjakan project. AI membantu saya dalam memahami penggunaan ModelForm, template inheritance, serialization dan deserialization JSON, serta implementasi fitur Create, Update, Delete, dan JSON Data Delivery. Setelah itu, saya tetap mencoba menjalankan dan menguji kode sendiri, mengecek hasilnya di browser, dan memperbaiki bagian yang masih error.