from PIL import Image
import glob
import os


class Convertor:
    def convert(self, file_dir=os.getcwd(), save_dir=os.getcwd(), file_name='/*', file_start_res='jpg', file_end_res='png'):
        mass = []
        for img in glob.glob(file_dir + file_name + '.' + file_start_res):
            file_mid_name = os.path.basename(
                img.removesuffix('.' + file_start_res))
            Image.open(img).save(os.path.join(
                save_dir, file_mid_name + '.' + file_end_res))
            mass.append(os.path.basename(
                str(glob.glob(save_dir + '/' + file_mid_name + '.' + file_end_res)[0])))
        return mass
