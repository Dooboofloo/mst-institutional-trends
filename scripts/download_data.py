# ./scripts/download_data.py

from pathlib import Path
from urllib.request import Request, urlopen
import shutil

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

FILES = {
    "FallEnrollment.xlsx": "https://www.umsystem.edu/sites/default/files/media/documents/general/1_21.xlsx",
    "GraduationRates.xlsx": "https://www.umsystem.edu/sites/default/files/media/documents/general/1_32.xlsx",
    "RetentionRates.xlsx": "https://www.umsystem.edu/sites/default/files/media/documents/general/1_34.xlsx",
}

def download_file(url: str, destination: Path) -> None:
    request = Request(
        url,
        headers={"User-Agent": "mst-institutional-trends/1.0"}
    )

    with urlopen(request, timeout=30) as response:
        with destination.open("wb") as output:
            shutil.copyfileobj(response, output)


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True, parents=True)

    for filename, url in FILES.items():
        destination = DATA_DIR / filename
        print(f"Downloading {filename}...")
        download_file(url, destination)

    print(f"Data saved to {DATA_DIR}")

if __name__ == '__main__':
    main()