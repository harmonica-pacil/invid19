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

COVID-19 adalah penyakit yang disebabkan oleh virus severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). Penyakit ini mengakibatkan pandemi hingga hampir seluruh bagian negara di dunia kewalahan dalam mengatasi penyebaran virus ini. Penanganan pandemi COVID-19 memerlukan gotong royong semua pihak, salah satunya adalah dengan memiliki pemahaman terkait informasi COVID-19 untuk menjaga diri. Dengan demikian, informasi yang valid merupakan suatu hal yang krusial dalam melawan COVID-19. Aplikasi ini dibuat dengan tujuan untuk memberikan informasi seputar COVID-19 dari segi kesehatan maupun dari perspektif kehidupan masyarakat yang terrdampak melalui fitur diskusi yang tersedia pada website ini. Pada aplikasi ini terdapat beberapa modul seperti artikel, diskusi, berita, info vaksinasi, dan data covid yang akan menunjang penguna untuk mendapatkan informasi terkini yang akurat serta saling berinteraksi.

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
- Ahmad <br>
  - Bio: <br> Budi adalah seorang driver berumur 60 tahun yang aktif bekerja di luar rumah hingga larut malam. Keseharian aktivitas hidupnya yang sibuk mencari nafkah tidak memungkinkan Budi untuk menyaring informasi di era arus informasi yang serba cepat. Oleh karenanya, Budi membutuhkan membutuhkan informasi terkini mengenai COVID-19 yang telah terfilter hingga memudahkan dalam memahami apa yang sedang terjadi COVID-19 baik dari segi pencegahan, vaksinasi, hingga berdiskusi secara langsung mengenai topik yang relevan dengan berbagai lini masyarakat mulai dari penyintas maupun tenaga kesahatan.
  - Goals: 
   1. Akses mudah terhadap informasi yang sudah terfilter terkait vaksin, berita COVID-19, sehingga tidak perlu mencari-cari lagi pada portal berita yang jangkauannya sangat luas serta general.
   2. Menjadi website yang mudah diakses dan dan user-friendly
  - Struggle:
   1. Era post-modernisme dengan arus berita yang sangat cepat membuat sulit menyaring berita yang tepat terkait COVID-19.
   2. Kesulitan harus membuka banyak website yang berbeda untuk mendapatkan informasi akurat serta fitur website yang ribet tidak mudah digunakan.

- Fatimah <br>
  - Bio: <br> Fatimah adalah seorang tenaga kesehatan berumur 26 tahun yang aktif bekerja menangani COVID-19 dalam divisi penyuluhan dan pendidikan. Aktivitas pekerjaannya yang berkaitan dalam penanganan dan pencegehan COVID-19 dengan mendidik masyarakat acapkali terhambat karena adanya hoax dan opini yang tidak tersaring beredar luas secara daring. Selain itu, usaha Fatimah dalam mengedukasi melalui berbagai _platform_ daring juga tidak lebih menarik dibandingkan mereka yang mementingkan _rating_ sehingga konten yang disebarkan seringkali tidak sampai pada demografi yang dimaksudkan. Oleh karenanya, Fatimah membutuhkan sebuh _platform_ yang menyediakan secara khusus informasi terkini mengenai COVID-19 sehingga seluruh berita, artikel, serta diskusi yang disediakan oleh Fatimah dapat disampaikan   secara langsung kepada mereka yang membutuhkan. Hal ini membuat Fatimah dimudahkan dalam memberikan penyuluhan berupa edukasi yang akan berdampak dalam pencegahan serta  penanganan COVID-19.
  - Goals: 
   1. Akses mudah terhadap untuk memberikan informasi yang sudah terfilter terkait vaksin, berita COVID-19, sehingga tidak perlu bersaing dalam berbagai portal berita maupun sosial media yang jangkauannya sangat luas serta general.
   2. Menjadi website yang mudah diakses dan dan user-friendly untuk memberikan edukasi terkait COVID-19
  - Struggle:
   1. Era post-modernisme dengan arus berita yang sangat cepat membuat sulit memberikan penyuluhan kepada masyarakat yang membutuhkan. Terkadang konten yang disebarkan tidak memiliki _views_ yang meningkat dibandingkan konten hoax dan opini tidak tersaring yang mudah sekali tersebar secara daring.
   2. Kesulitan harus membuka banyak platform yang berbeda untuk memberikan informasi akurat serta fitur website yang ribet tidak mudah digunakan.

## 📑 Referensi 📑

Berikut ini adalah sumber referensi yang digunakan dalam pembuatan proyek ini.

- [django-template-heroku](https://github.com/laymonage/django-template-heroku)
