import requests
import json
#from django.conf import settings

#base_dir = settings.BASE_DIR

from pathlib import Path
base_dir = Path(".")

response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code==200:
    data = response.json()
    data_dir = base_dir / "data"
    data_dir.mkdir(parents=True,exist_ok=True)
    data_file = data_dir / "post.json"
    with data_file.open("w") as fp:
        json.dump(data,fp)