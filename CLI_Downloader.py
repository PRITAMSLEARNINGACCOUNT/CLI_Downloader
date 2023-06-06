import requests
from tqdm import tqdm
import math
url = input("Enter Your URL??\n")
response = requests.get(url, stream=True)
total_size_in_bytes = float(response.headers["Content-Length"])
total_size = float("{:.2f}".format(
    float(response.headers["Content-Length"])*math.pow(10, -9)))
print(f"The Size Of Your Given File Is {total_size} GB")

splitted_url = url.split("/")
chunk_size = 128
with open(f"{splitted_url[-1]}", "wb") as fuck:
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
    for i in response.iter_content(chunk_size):
        fuck.write(i)
        progress_bar.update(chunk_size)
progress_bar.close()
print("The File Has Been Downloaded Successfully.")
