from os import *
from pendulum import *
from shutil import *


start_path = 'H:/Медиа (фото, видео, др.)'
sorted_path = 'H:/Медиа (фото, видео, др.)/Фото по годам'
c = 0

for i in walk(start_path):
    for j in i[-1]:
        if j.endswith('.JPG') or j.endswith('.PNG'):
            c += 1
            date_photo = from_timestamp(int(str(stat(f'{i[0]}/{j}').st_mtime).split('.')[0])).__format__('MMMM YYYY')
            if not path.exists(f'{sorted_path}/{date_photo.split()[1]}'):
                mkdir(f'{sorted_path}/{date_photo.split()[1]}')
            if not path.exists(f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}'):
                mkdir(f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}')
            copy(f'{i[0]}/{j}', f'{sorted_path}/{date_photo.split()[1]}/{date_photo.split()[0]}/{j}')
            if c % 10 == 0:
                print(c)