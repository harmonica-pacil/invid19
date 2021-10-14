### invid19

## 🌏 Situs Web 🌎

Proyek ini dapat diakses di [invid19.herokuapp.com](https://invid19.herokuapp.com/).

## 👨‍💻 Pengembang Aplikasi 👩‍💻

Proyek ini dibuat oleh kelompok A10 yang beranggotakan sebagai berikut.

- Taufik Pragusga (2006595980)
- Almira Eka Putri Maharani (2006597784)
- Nahda Amalia (2006597935)
- Jason Widodo (2006596415)
- Muhammad Irham Luthfi (2006473964)
- Rickyanto Wangsa Mulya (2006597765)
- Muhammad Haddad (2006596195)

## 📃 Ringkasan 📃

COVID-19 adalah penyakit yang disebabkan oleh virus severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). Penyakit ini mengakibatkan pandemi yang besar sehingga hampir seluruh bagian negara memiliki kewalahan dalam mengatasi penyebaran virus ini. Penanganan pandemi COVID-19 memerlukan gotong royong semua pihak, salah satunya adalah dengan memiliki pemahaman terkait informasi COVID-19 untuk menjaga diri.

Informasi yang valid merupakan suatu hal yang krusial dalam melawan COVID-19. Oleh karenanya, aplikasi ini dibuat dengan tujuan untuk memberikan informasi seputar covid-19. Pada aplikasi ini terdapat beberapa halaman, seperti artikel, diskusi, berita, info vaksinasi, dan data covid.

## 📋 Daftar Modul 📋

Berikut ini adalah daftar modul yang akan diimplementasikan.

- User <br>
  Modul User digunakan untuk mengidentifikasi pengguna aplikasi. Pada modul ini nantinya akan dibuat model untuk datanya yang akan berisi nama lengkap, email, password, bio, tanggal lahir, dan foto profil. Selain itu, akan dibuat juga halaman untuk signup, signin, dan halaman profil untuk menampilkan data user yang sudah login.
- Diskusi <br>
  Pada modul diskusi, user yang sudah login dapat melihat daftar dari halaman diskusi yang berisi diskusi yang telah dibuat dan dapat memulai sebuah diskusi. Jika user belum login hanya dapat melihat daftar halaman diskusi yang berisi diskusi yang telah dibuat.
- Comment/Reply (Berhubungan dengan modul diskusi) <br>
  Pada modul Comment/Reply jika user sudah login user dapat melihat 1 halaman diskusi beserta komentar-komentarnya dan dapat mereply diskusi yang sedang dilihat maupun mereply komentar lain. Jika belum login maka hanya dapat melihat 1 halaman diskusi beserta komentar-komentarnya.
- Artikel <br>
  Pada modul artikel, tersedia halaman untuk menampilkan artikel-artikel terkait kesehatan yang bertujuan untuk memberikan informasi dan edukasi kesehatan, terutama terkait Covid-19, kepada user. Daftar artikel hanya dapat dibuat dan diedit oleh user admin.
- Berita <br>
  Pada modul berita tersedia halaman yang menampilkan berita-berita terbaru. Berita ini hanya dapat dibuat dan diedit oleh user admin. Bagi mereka yang belum login hanya bisa melihat headline berita.
- Vaksinasi <br>
  Pada modul vaksinasi, tersedia halaman berisi informasi vaksinasi, seperti lokasi, jenis vaksin, tanggal, kuota, dan jam vaksinasi. Tersedia form untuk membuat informasi vaksinasi yang hanya dapat diakses oleh admin. Bagi user yang belum login tidak dapat melihat kuota dam jam vaksinasi
- Data Covid-19 <br>
  Pada modul ini, tersedia halaman berisi data Covid-19 di Indonesia. Informasi yang ditampilkan berupa angka kasus positif dan negatif, angka sembuh, angka meninggal, dan lain-lain. Modul ini bertujuan untuk memberikan informasi terkait kondisi Indonesia di masa pandemi ini. Hanya user admin yang dapat menambahkan data dan mengedit data.

## 👥 Persona 👥

- Guest User:
  Hanya bisa melihat konten-konten yang ada pada aplikasinya. User yang belum login tidak bisa mengakses halaman profile serta halaman untuk membuat artikel, berita, diskusi, vaksinasi, dan data covid-19. Bagi user yang belum login, halaman artikel dan berita hanya akan menampilkan list dari headline artikel dan berita yang tersedia.
- Registered User:
  Dapat mengakses seluruh halaman dan dapat membuat komentar pada diskusi yang ada. User yang sudah login pun dapat mengakses isi berita dan artikel yang ada pada web.
- Admin:
  Dapat mengisi konten pada aplikasi, seperti berita, artikel, vaksinasi, dan data covid-19.

## 📑 Referensi 📑

Berikut ini adalah sumber referensi yang digunakan dalam pembuatan proyek ini.

- [django-template-heroku](https://github.com/laymonage/django-template-heroku)
