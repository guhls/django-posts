from pathlib import Path

import requests  # request img from web
from django.core import files
from django.core.files.temp import NamedTemporaryFile

root_path = Path(__file__).parent.parent.parent


def get_img(url, file_name):
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        image_temp_file = NamedTemporaryFile(delete=True)

        # Write the in-memory file to the temporary file
        # Read the streamed image in sections
        for block in res.iter_content(1024 * 8):

            # If no more file then stop
            if not block:
                break
            # Write image block to temporary file
            image_temp_file.write(block)

        file_name = f'{file_name}'  # Choose a unique name for the file
        image_temp_file.flush()
        temp_file = files.File(image_temp_file, name=file_name)

        print('Image sucessfully Downloaded: ', file_name)

        return temp_file
    else:
        print('Image Couldn\'t be retrieved')


if __name__ == '__main__':
    # get_img()
    ...
