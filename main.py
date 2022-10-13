from PIL import Image
import glob
import os


class Convertor:
    def convert(file_dir=None, save_dir=None, file_name=None, file_start_res=None, file_end_res=None):
        if (file_dir is None):
            file_dir = os.getcwd()
        if (save_dir is None):
            save_dir = os.getcwd()
        if (file_name is None):
            file_name = '/*'
        if (file_start_res is None):
            file_start_res = 'jpg'
        if (file_end_res is None):
            file_end_res = 'png'
        mass = []
        for img in glob.glob(file_dir + file_name + '.' + file_start_res):
            file_mid_name = os.path.basename(
                img.removesuffix('.' + file_start_res))
            Image.open(img).save(os.path.join(
                save_dir, file_mid_name + '.' + file_end_res))
            mass.append(os.path.basename(
                str(glob.glob(save_dir + '/' + file_mid_name + '.' + file_end_res)[0])))
        return mass

    def convert_for_test(self, file_dir=os.getcwd(), save_dir=os.getcwd(), file_name='/*', file_start_res='jpg', file_end_res='png'):
        mass = []
        for img in glob.glob(file_dir + file_name + '.' + file_start_res):
            file_mid_name = os.path.basename(
                img.removesuffix('.' + file_start_res))
            Image.open(img).save(os.path.join(
                save_dir, file_mid_name + '.' + file_end_res))
            mass.append(os.path.basename(
                str(glob.glob(save_dir + '/' + file_mid_name + '.' + file_end_res)[0])))
        return mass


_file_dir = None
_save_dir = None
_file_name = None
_file_start_res = None
_file_end_res = None

print('Вы хотите конвертировать изображения в текущей директории? (y/n)')
a = str(input())
if (a == 'n'):
    _file_dir = str(input())
print('Вы хотите сохранить изображения в текущей директории? (y/n)')
a = str(input())
if (a == 'n'):
    _save_dir = str(input())
print('Вы хотите конвертировать изображения с форматом "jpg"? (y/n)')
a = str(input())
if (a == 'n'):
    _file_name = str(input())
print('Вы хотите конвертировать все изображения с этим форматом в текущей директории? (y/n)')
a = str(input())
if (a == 'n'):
    _file_start_res = str(input())
print('Вы хотите конвертировать изображения в формат "png"? (y/n)')
a = str(input())
if (a == 'n'):
    _file_end_res = str(input())

Convertor.convert(file_dir=_file_dir, save_dir=_save_dir, file_name=_file_name,
                  file_start_res=_file_start_res, file_end_res=_file_end_res)
