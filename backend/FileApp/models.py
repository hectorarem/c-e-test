import os
from zipfile import ZipFile
from django.db import models
from .validators import validate_file_size

class File(models.Model):
    created_at = models.DateTimeField('creado el', auto_now_add=True)
    updated_at = models.DateTimeField('actualizado el', auto_now=True)
    file = models.FileField('fichero', upload_to='upload/', validators=[validate_file_size])
    uploaded_by = models.ForeignKey('auth.User', related_name='user', on_delete=models.DO_NOTHING)

    # TODO considerar hacer publico o no el fichero
    # public = models.BooleanField('es público', default=True)

    class Meta:
        verbose_name = 'file cargado'
        verbose_name_plural = 'files cargados'
        ordering = ('-created_at',)

    def __str__(self):
        return self.created_at.__str__()

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        return super().delete()

    @property
    def file_full_name(self):
        return self.file.name.split('/')[-1]

    @property
    def file_name(self):
        return self.file.name.split('/')[-1].split('.')[0]

    @property
    def file_extension(self):
        return self.file.name.split('/')[-1].split('.')[1]

    @property
    def file_size(self):
        size = self.file.size
        if size > 1073741824: #hay que validar que no llegue aqui 😂
            return str("%.2f" % (size / 1073741824)) + " GB"
        elif size >= 1048576:
            return str("%.2f" % (size / 1048576)) + " MB"
        elif size >= 1024:
            return str("%.2f" % (size / 1024)) + " KB"
        else:
            return str(self.file.size) + " B"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file_extension != 'zip':
            ZipFile(self.file.path + '.zip', mode='w').write(self.file.path, self.file_full_name)
            old_file = self.file.path
            self.file.name = self.file.name + ".zip"
            os.remove(old_file)
            super().save()


