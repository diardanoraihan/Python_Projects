import requests
from bs4 import BeautifulSoup

# URL target
# url = "https://chse.kemenparekraf.go.id/id/detail-tersertifikasi/11863-taman-langit-pangalengan-360"




def get_data_adm(url):
  """
  Description:
    Scrape chse kemenparekraf to get information about the destination object, address, province, and more.
  
  Return:
    a dictionary containing location of the destination object
  """
  # objek_wisata = []
  # alamat = []
  # provinsi = []
  # kab_kota = []
  # kecamatan = []
  # desa = []

  # Mengambil konten halaman
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to retrieve page. Status code: {response.status_code}")
      exit()

  # Parsing HTML menggunakan BeautifulSoup
  soup = BeautifulSoup(response.text, "html.parser")

  # Ekstraksi informasi
  try:
      # Nama Objek Wisata
      objek_wisata = soup.find("h1", class_="h2").text.strip()
      
      # Alamat
      alamat = soup.find("span", class_="d-block").text.strip()

      # Tabel informasi lainnya
      data_table = soup.find_all("dd", class_="col-6")
      provinsi = data_table[1].string
      kab_kota = data_table[2].string
      kecamatan = data_table[3].string
      desa = data_table[4].string

  except Exception as e:
      print(f"An error occurred: {e}")
      
  data = {
  'objek_wisata': objek_wisata,
  'alamat': alamat,
  'provinsi': provinsi,
  'kab_kota': kab_kota,
  'kecamatan': kecamatan,
  'desa': desa
  }
  
  return data


def dms_to_decimal(coord):
  """
  Mengonversi koordinat DMS (Degree, Minute, Second) menjadi desimal.
  
  Parameter:
  - coord: str, koordinat dalam format "7°13'52.9"S" atau "107°31'33.2"E"
  
  Return:
  - float, koordinat dalam format desimal
  """
  # Pisahkan komponen
  parts = coord[:-1]  # Hilangkan huruf terakhir (S, N, W, E)
  direction = coord[-1]  # Ambil huruf terakhir (S, N, W, E)

  # Ekstrak derajat, menit, detik
  d, m, s = [float(x.replace("°", "").replace("'", "").replace('"', "")) for x in parts.replace("°", " ").replace("'", " ").replace('"', "").split()]

  # Hitung desimal
  decimal = d + (m / 60) + (s / 3600)

  # Buat negatif jika arah Selatan (S) atau Barat (W)
  if direction in ['S', 'W']:
      decimal = -decimal

  return decimal

def get_data_coord(url):
  
  # webpage = '''
  # <div jstcache="24" class="place-name" jsan="7.place-name">7°13'52.9"S 107°31'33.2"E</div>
  # '''
  
  # Mengambil konten halaman
  response = requests.get(url)
  if response.status_code != 200:
      print(f"Failed to retrieve page. Status code: {response.status_code}")
      exit()

  # Parsing HTML menggunakan BeautifulSoup
  soup = BeautifulSoup(response.text, "html.parser")

  coord = soup.find('div', class_ = 'place-name').text
  
  lat, long = coord.split()[0], coord.split()[1]
  
  data = {
  'latitude': lat,
  'longitude': long
  }
  
  return data

dms_to_decimal("7°13'52.9"S")