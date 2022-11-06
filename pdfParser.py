import requests
import img2pdf


def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    img_list = []

    for i in range(1, 49):
        url = f"https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        img = requests.get(url, headers=headers)
        responce = img.content

        with open(f"data/{i}.jpg", "wb") as f:
            f.write(responce)
            img_list.append(f"data/{i}.jpg")
            print(f"Download of {i} files is ready")

    print("#" * 20)
    print(img_list)

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("Pdf file created")


def main():
    get_data()


if __name__ == '__main__':
    main()
