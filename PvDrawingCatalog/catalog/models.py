from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.


class AssemblyDrawing(MPTTModel):
    """
    модель для хранения сборочногих эдениц
        assembly_number -> чертежный номер сборочгонго чертиже
        assembly_name -> наименование сборочной еденици
        num_of_changes_assembly -> номер текущего изменения сборочного чертижа
        num_of_changes_specification -> номер текущего изменения спецификации
        file_assembly -> для хранения файла сборочного чертижа
        file_specification -> для хранения файла спецефикации
        num_of_notice -> номер извещения об изменении
        parent -> родитель (для хранения структуры сборок которие входять в сборки)
    """
    assembly_number = models.CharField(max_length=20, verbose_name='Номер сборки')
    assembly_name = models.CharField(max_length=100, verbose_name='Название сборки')
    num_of_changes_assembly = models.SmallIntegerField(blank=True, null=True, verbose_name='№ изменения СБ')
    num_of_changes_specification = models.SmallIntegerField(blank=True, null=True,
                                                            verbose_name='№ изменения спецификации')
    file_assembly = models.FileField(verbose_name='Путь к файлу СБ', blank=True)
    file_specification = models.FileField(verbose_name='Путь к файлу спецификации', blank=True)
    num_of_notice = models.CharField(max_length=30, verbose_name='номер звещения', blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='assembly')

    def __str__(self):
        return '%s - %s' % (self.assembly_number, self.assembly_name)

    class Meta:
        verbose_name = 'Сборка'
        verbose_name_plural = 'Сборки'


class Detail(MPTTModel):
    """
    Модель для хранения деталей
        detail_number -> чертежный номер деталей
        detail_name -> название детали
        num_of_changes -> номер текущего изменения детали
        file_detail -> для хранения файла детали
        num_of_notice -> номер извещения об изменении
        parent -> родитель (для хранения структуры вхождения детали в сборку)
    """
    detail_number = models.CharField(max_length=20, verbose_name='чертеж №')
    detail_name = models.CharField(max_length=100, verbose_name='Название чертижа')
    num_of_changes = models.SmallIntegerField(blank=True, null=True, verbose_name='№ изменения')
    file_detail = models.FileField(verbose_name='Путь к файлу детали', blank=True)
    num_of_notice = models.CharField(max_length=30, verbose_name='номер звещения', blank=True)
    parent = TreeForeignKey(AssemblyDrawing, on_delete=models.CASCADE, null=True, blank=True, related_name='detail')

    def __str__(self):
        return '%s - %s' % (self.detail_number, self.detail_name)

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Book(models.Model):

    assembly = models.ManyToManyField(AssemblyDrawing)
    book_name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.book_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Product(models.Model):

    product_name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return '%s' % self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
