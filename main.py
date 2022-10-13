from PIL import Image
import glob
import os

out_dir = ''
cnt = 0
for img in glob.glob('C:\\Users\\Turka\\Desktop\\New Folder\\/*.bmp'):
    Image.open(img).save(os.path.join(out_dir, str(cnt) + '.png'))
    cnt += 1
