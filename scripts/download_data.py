import requests
import zipfile
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

URLS = {
    "ne_10m_admin_0_countries": "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip",
    "ne_10m_lakes": "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_lakes.zip"
}

def download_and_extract(url_name, url):
    print(f"📥 Baixando {url_name}...")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    
    zip_path = DATA_DIR / f"{url_name}.zip"
    zip_path.write_bytes(resp.content)
    print("✅ ZIP baixado")
    
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(DATA_DIR)
    print(f"✅ {url_name} extraído")
    zip_path.unlink()  # Remove ZIP após extrair

if __name__ == "__main__":
    for name, url in URLS.items():
        download_and_extract(name, url)
    print("🎉 Dados Natural Earth prontos em data/!")
    print("Rode: pytest -v")
EOF
