# 1

# import threading
#
#
# def find_even_numbers():
#     ans = [i for i in range(30, 51) if i % 2 == 0]
#     print(ans)
#
#
# def find_odd_numbers():
#     ans = [i for i in range(30, 51) if i % 2 != 0]
#     print(ans)
#
#
# t1 = threading.Thread(target=find_even_numbers)
# t2 = threading.Thread(target=find_odd_numbers)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

# 2

import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
    'https://www.pexels.com/video/a-cloud-of-paint-underwater-7565439/',
    'https://www.pexels.com/video/a-cloud-of-yellow-paint-underwater-7565431/',
    'https://www.pexels.com/video/a-magnificent-view-of-the-waterfalls-6981411/',

]


def download_mp3(url):
    r = requests.get(url)

    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f'{filename} downloaded')


with ThreadPoolExecutor() as executor:
    executor.map(download_mp3, urls)
