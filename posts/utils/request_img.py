import shutil  # save img locally
from pathlib import Path

import requests  # request img from web

root_path = Path(__file__).parent.parent.parent


def get_img(url, file_name):
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(f'{root_path}/temp/{file_name}', 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ', file_name)

        return f'{root_path}/temp/{file_name}'
    else:
        print('Image Couldn\'t be retrieved')


if __name__ == '__main__':
    # get_img()
    ...
