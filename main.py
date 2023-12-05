import requests


def main():
    url = 'https://www.hdwallpapers.in/download/colorful_glowing_shape_lines_4k_8k_hd_abstract-HD.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'
    }
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        with open('img.jpg', 'wb') as picture:
            for chunk in response.iter_content(chunk_size=10000):
                if chunk:
                    picture.write(chunk)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image. Status code:", response.status_code)


if __name__ == '__main__':
    main()
