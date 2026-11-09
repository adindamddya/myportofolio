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


### Tugas 5

1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

   Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan aktivitas selama waktu tertentu. Pada fitur pencarian dengan AJAX, debouncing penting agar request ke server tidak dikirim setiap kali pengguna mengetik satu karakter. Dengan begitu, jumlah request dapat dikurangi sehingga penggunaan server menjadi lebih efisien dan pencarian tetap responsif.

2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

   `await` digunakan untuk menunggu hasil dari operasi asynchronous seperti `fetch()` sebelum kode berikutnya dijalankan. Dengan menggunakan `await`, program dapat menunggu sampai response dari server diterima sehingga data dapat diproses dengan benar. Jika tidak menggunakan `await`, `fetch()` akan mengembalikan sebuah Promise dan kode berikutnya dapat berjalan sebelum data selesai diterima. Hal ini dapat menyebabkan data belum tersedia ketika ingin digunakan.

3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

   XSS (Cross-Site Scripting) adalah serangan yang terjadi ketika kode berbahaya, seperti JavaScript, dimasukkan ke dalam halaman web dan kemudian dijalankan oleh browser pengguna. Data yang ditampilkan melalui AJAX/JavaScript perlu lebih diperhatikan karena data tersebut biasanya dimasukkan secara dinamis ke dalam HTML. Jika data tidak di-escape, input seperti tag HTML atau JavaScript dapat dianggap sebagai kode oleh browser. Oleh karena itu, data teks harus di-escape sebelum dimasukkan ke HTML dan input juga perlu dibersihkan di sisi server.


### Tugas 6

1. **Jelaskan apa itu RESTful API dan mengapa mengembalikan data dalam format JSON saja belum tentu menjadikan API tersebut RESTful! Selain itu, jelaskan perbedaan penggunaan HTTP method PUT dan PATCH!**

   REST (Representational State Transfer) adalah gaya arsitektur perangkat lunak yang menggunakan protokol komunikasi standar (umumnya HTTP) untuk interaksi antarsistem, dengan memandang setiap entitas sebagai sumber daya (*resource*) yang diidentifikasi oleh URI (Uniform Resource Identifier). Suatu API tidak otomatis menjadi RESTful hanya karena mengembalikan respons berformat JSON. Agar dapat dikategorikan sebagai RESTful, API harus mematuhi prinsip-prinsip dasar REST, seperti arsitektur *client-server* yang terpisah, *statelessness* (setiap request harus mengandung seluruh informasi yang dibutuhkan server), *cacheability*, antarmuka yang seragam (*uniform interface* menggunakan HTTP method standar seperti GET, POST, PUT, PATCH, DELETE sesuai semantiknya), serta representasi status kode HTTP yang tepat (misalnya 200 OK, 201 Created, 204 No Content, 400 Bad Request, 403 Forbidden, 404 Not Found). Jika sebuah endpoint hanya mengembalikan JSON namun misalnya menggunakan method POST untuk semua operasi (membaca, menghapus, mengubah), atau tidak memiliki URI berbasis resource yang konsisten, API tersebut belum dapat dikatakan RESTful.

   Perbedaan utama antara **PUT** dan **PATCH**:
   - **PUT** bersifat penggantian penuh (*full update / replacement*). Klien harus mengirimkan seluruh representasi entitas data yang baru. Jika ada field yang tidak dikirimkan dalam payload PUT, field tersebut biasanya akan dikosongkan atau diisi dengan nilai default.
   - **PATCH** bersifat pembaruan parsial (*partial update*). Klien hanya perlu mengirimkan field-field tertentu yang ingin diubah tanpa harus mengirimkan seluruh atribut resource. Field lain yang tidak disertakan dalam payload request tidak akan diubah atau dihapus oleh server.

2. **Jelaskan peran `Serializer` dalam Django REST Framework (DRF) dibandingkan dengan membuat serialization secara manual menggunakan `JsonResponse` seperti pada tugas sebelumnya! Apa keuntungannya terkait validasi input?**

   Pada tugas sebelumnya, pembuatan respons JSON dilakukan secara manual dengan membangun dictionary Python melalui perulangan queryset lalu mengembalikannya menggunakan `JsonResponse()`. Cara manual ini memiliki banyak keterbatasan dan membutuhkan penulisan kode berulang. 
   
   `Serializer` (khususnya `ModelSerializer`) pada DRF memiliki peran penting dua arah:
   - **Serialisasi (Output)**: Mengubah object model Django yang kompleks beserta relasinya (seperti ManyToMany pada `starred_by`) menjadi tipe data Python primitif yang dapat dirender ke JSON, XML, atau format lainnya secara otomatis dan konsisten.
   - **Deserialisasi & Validasi (Input)**: Menerima data payload dari request klien, memvalidasi struktur serta tipe datanya, dan mengubahnya kembali menjadi objek Python/model yang siap disimpan ke database.

   Keuntungan utama `Serializer` terkait validasi input meliputi:
   - **Validasi Terstruktur dan Otomatis**: Serializer secara otomatis menerapkan aturan validasi berdasarkan skema model (seperti tipe data, batasan panjang teks, atau nullability).
   - **Custom Validation Method**: Pengembang dapat dengan mudah menambahkan validasi khusus pada level field (seperti method `validate_school()` untuk membersihkan input dengan `strip_tags()` dan mencegah input kosong) maupun validasi lintas field pada method `validate()`.
   - **Pencegahan Data Tampering**: Serializer membatasi field mana saja yang boleh ditulis oleh klien melalui deklarasi `fields` dan `read_only_fields`. Field hasil kalkulasi (seperti `star_count`, `is_starred`, dan `starred_by_names`) yang menggunakan `SerializerMethodField` bersifat read-only sehingga tidak dapat dipalsukan atau diisi sembarangan oleh request klien.
   - **Standardisasi Pesan Error**: Jika validasi gagal (`serializer.is_valid()`), Serializer secara otomatis menghasilkan dictionary error yang rapi dengan rincian per field dan kode status HTTP 400 Bad Request.

3. **Jelaskan perbedaan antara autentikasi (authentication) dan otorisasi (authorization) dalam konteks REST API! Mengapa pemeriksaan izin (permission check) harus selalu dilakukan di sisi server (backend), bukan hanya mengandalkan penyembunyian elemen di antarmuka (frontend)?**

   - **Autentikasi (Authentication)** menjawab pertanyaan *"Siapa kamu?"* (*identity verification*). Ini adalah proses untuk memverifikasi identitas pengguna yang melakukan request, misalnya melalui session cookie, token JWT, atau kredensial login. Jika autentikasi berhasil, DRF mengisi objek `request.user` dengan data pengguna yang bersangkutan.
   - **Otorisasi (Authorization)** menjawab pertanyaan *"Apa yang boleh kamu lakukan?"* (*access control / permissions*). Setelah identitas diketahui, otorisasi menentukan apakah pengguna tersebut memiliki izin atau hak akses untuk melakukan aksi tertentu pada resource yang diminta (misalnya apakah pengunjung boleh membaca, apakah Editor boleh mengedit melalui PUT/PATCH, atau hanya Superuser yang boleh menambah dan menghapus data).

   Pemeriksaan izin **wajib dilakukan di sisi server (backend)** karena:
   - Tampilan di sisi klien (frontend), seperti menyembunyikan tombol Edit atau Delete menggunakan JavaScript/CSS, hanyalah bentuk pengalaman pengguna (*User Experience / UX*) dan sama sekali bukan mekanisme keamanan.
   - Siapa pun dapat memanipulasi kode frontend di DevTools browser, memodifikasi DOM, atau mengirimkan request HTTP langsung ke endpoint API menggunakan alat seperti cURL, Postman, Fetch API console, atau script Python tanpa melalui tombol di UI.
   - Jika backend tidak melakukan verifikasi hak akses pada setiap request yang masuk, pengguna tanpa hak (atau penyerang) dapat dengan mudah mengubah atau menghapus data sensitif. Oleh karena itu, aturan keamanan utama adalah *never trust the client* dan seluruh otorisasi harus ditegakkan secara ketat di backend melalui permission class.

4. **Mengapa perlindungan CSRF tetap dibutuhkan ketika menggunakan `SessionAuthentication` pada API DRF, padahal API umumnya dianggap stateless? Mengapa pemanggilan `force_authenticate` pada test case tidak menguji pemeriksaan CSRF, dan bagaimana cara mengujinya secara tepat?**

   - **Perlindungan CSRF dengan `SessionAuthentication`**: Meskipun REST API pada umumnya dirancang stateless (misalnya saat menggunakan token Bearer/JWT di mana browser tidak melampirkan kredensial secara otomatis), penggunaan `SessionAuthentication` pada DRF memanfaatkan mekanisme session cookie bawaan browser (`sessionid`). Karena browser secara otomatis menyertakan cookie session pada setiap request yang dikirim ke origin yang sama, aplikasi menjadi rentan terhadap serangan Cross-Site Request Forgery (CSRF)—di mana situs web berbahaya dapat memicu request pengubahan data (POST, PUT, PATCH, DELETE) atas nama pengguna yang sedang terautentikasi. Oleh karena itu, DRF mewajibkan validasi token CSRF (melalui header `X-CSRFToken` atau cookie `csrftoken`) untuk setiap request non-safe method yang menggunakan autentikasi session.
   - **Mengapa `force_authenticate` tidak menguji CSRF**: Method `force_authenticate(user=...)` pada `APIClient` adalah jalan pintas khusus pengujian DRF yang langsung menempelkan objek `user` ke `request.user` di memori dan secara sengaja melewati (*bypass*) seluruh alur autentikasi dan middleware Django, termasuk `CsrfViewMiddleware`. Akibatnya, request uji yang menggunakan `force_authenticate` tidak akan pernah memicu atau memverifikasi mekanisme proteksi CSRF.
   - **Cara menguji CSRF secara tepat**: Pengujian CSRF harus dilakukan dengan mengaktifkan pemeriksaan CSRF secara eksplisit menggunakan `APIClient(enforce_csrf_checks=True)` dan melakukan autentikasi menggunakan `client.login(username=..., password=...)`. Dengan cara ini, request non-safe method tanpa token CSRF akan ditolak dengan respons status `403 Forbidden`, sedangkan request yang menyertakan header token CSRF yang valid (`HTTP_X_CSRFTOKEN=token`) akan berhasil diproses (`200 OK` atau `201 Created`).

### AI Disclosure

Dalam pengerjaan Tugas 6, saya menggunakan bantuan AI asisten (Google Antigravity / Gemini) untuk:
- Memahami implementasi Django REST Framework (DRF) secara mendalam, termasuk penggunaan `ModelSerializer`, `SerializerMethodField`, validasi data kustom, serta pembuatan custom `BasePermission` (`IsPortfolioOwnerOrEditorOrReadOnly`).
- Merancang arsitektur API view berbasis fungsi dengan decorator `@api_view`, `@authentication_classes([SessionAuthentication])`, dan `@permission_classes`.
- Menghubungkan frontend AJAX ke endpoint REST API DRF dengan penanganan CSRF token, escaping konten, modal popover add/edit, dan pesan error toast interaktif.
- Menyusun rangkaian unit test komprehensif menggunakan `APITestCase` dan `APIClient(enforce_csrf_checks=True)` untuk menguji keempat peran pengguna dan proteksi CSRF.
Seluruh kode diuji secara lokal, dipastikan seluruh test suite lulus, dan dideploy langsung ke PWS serta GitHub.
