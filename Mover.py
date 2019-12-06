import struct
from os import *

from pendulum import *
from shutil import *
from piexif import *
import piexif


start_path = 'H:/Медиа (фото, видео, др.)'
sorted_path = 'H:/Медиа (фото, видео, др.)/Фото по годам'
c = 0

for i in walk(start_path):
    for j in i[-1]:
        if j.endswith('.JPG') or j.endswith('.jpg'):
            c += 1
            change_date_photo = from_timestamp(int(str(stat(f'{i[0]}/{j}').st_mtime).split('.')[0])).__format__('MMMM YYYY')
            try:
                if load(f'{i[0]}/{j}')['Exif'] and 'прованс' not in i[0].lower():
                    y, m, d = [int(i.strip("b'")) for i in str(load(f'{i[0]}/{j}')['Exif'][36867].split()[0]).split(':')]
                    date_photo = date(y, m, d).__format__('MMMM YYYY')

                    if not path.exists(f'{sorted_path}/{date_photo.split()[1]}'):
                        mkdir(f'{sorted_path}/{date_photo.split()[1]}')
                    if not path.exists(f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}'):
                        mkdir(f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}')
                    if not path.exists(f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}/{j}'):
                        copy(f'{i[0]}/{j}', f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}/{j}')

                    if c % 100 == 0:
                        print(c)
            except piexif._exceptions.InvalidImageDataError:
                print('Type error')
            except struct.error:
                print('Struct error')
            else:
                if not load(f'{i[0]}/{j}')['Exif']:
                    if not path.exists(f'{sorted_path}/{change_date_photo.split()[1]}'):
                        mkdir(f'{sorted_path}/{change_date_photo.split()[1]}')
                    if not path.exists(f'{sorted_path}/{change_date_photo.split()[1]}/{change_date_photo.split()[0]}'):
                        mkdir(f'{sorted_path}/{change_date_photo.split()[1]}/{change_date_photo.split()[0]}')
                    copy(f'{i[0]}/{j}', f'{sorted_path}/{change_date_photo.split()[1]}/{change_date_photo.split()[0]}/{j}')

                    if c % 100 == 0:
                        print(c)
