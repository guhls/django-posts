import shutil  # save img locally

import requests  # request img from web


def get_img(url, file_name):
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(f'posts/temp/{file_name}', 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', file_name)
    else:
        print('Image Couldn\'t be retrieved')

    return f'posts/temp/{file_name}'


if __name__ == '__main__':
    # get_img()
    ...
