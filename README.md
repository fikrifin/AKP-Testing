# AKP-Testing

jangan lupa instal dan gunakan virtual environment python ya

<h3>Detail Aplikasi</h3>
Bahasa Pemrograman   : Python
Framework            : Django
Database Enggine     : Postgresql
Javascrips Framework : Vue Js

<h3>Tutorial Penggunaan</h3>
<ul>1. Install Django serta Requirement.txt yang berisikan libarary python agar aplikasi dapat berjalan (python -m pip install -r requirements.txt).</ul>
<ul>2. Karena pada aplikasi ini menggunakan Postgresql sebagai database, pastikan postgress sudah terinstall, dan akses ke pgadmin.</ul>
<ul>3. Nama database yang di gunakan pada aplikasi ini adalah "database_akp" dapat di cek di setting.py yang ada di folder AKP.</ul>
<ul>4. Apabila ingin menggunakan nama sendiri silahkan sesuaikan data dari setting database yang ada di setting.py.</ul>
<ul>5. Jika sudah sesuai jangan lupa untuk migrasikan model dari tabel yang ada di models.py ke database dengan cara</ul>
  <li> a. pastikan terminal sudah berada di directory AKP (yang terdapat manage.py)</li>
  <li> b. ketikan python.exe manage.py makemigrations</li>
  <li> c. jika sudah, python.exe manage.py migrate</li>
  <li> d. cek pada database apakah sudah ada tabel yang sesuai</li>
<ul>6. Jika database sudah ada silahkan jalankan aplikasi dengan "python.exe manage.py runserver</ul>
<ul>7.  Buka http://127.0.0.1:8000/employee/list/ untuk masuk ke dashboard</ul>

<h3>Fitur</h3>
<ul>1. CRUD Data Divisi</ul>
<ul>2. CRUD Data Posisi</ul>
<ul>3. CRUD Data Karyawan</ul>

<h3>Kekurangan</h3>
<ul>- Pada aplikasi ini, saya tidak menambahkan field is_active karena model Employee yang saya gunakan tidak menarik data dari User Model Django.</ul>
<ul>- Pada Work Period belum mengkategorikan berdasarkan bulan dan tahun, saat ini masih dalam perhitungan bulan, namun masih bisa diperbaiki kedepannya.</ul>
