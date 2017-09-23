from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.files import File
from PIL import Image

from django.core.files.images import ImageFile


class User(AbstractUser):
    cover_image = models.ImageField(upload_to='user/%Y/%m', default='default.png', verbose_name='头像')

    def save(self, *args, **kwargs):
        try:
            image = self.cover_image.file.name
        except:
            image = None
        super(User, self).save()
        # 将文件保存成150 * 150
        try:
            new = None
            if image:
                name = self.cover_image.file.name
                if not name == image:
                    out = Image.open(name)
                    width, height = out.size
                    dif = abs((width - height) / 2)
                    if width > height:
                        right = dif + height
                        new = out.crop((dif, 0, right, height))
                    else:
                        down = dif + width
                        new = out.crop((0, dif, width, down))
                # new.thumbnail((100, 100))
                img = new.resize((250, 250), Image.ANTIALIAS)
                img.save(name)
        except:
            pass