from django.db import models
from django.urls import reverse


c_choices = (
    ('МГУ', 'МГУ'),
    ('ВШЭ', 'ВШЭ'),
    ('Финашка', 'Финашка'),
    ('Плешка', 'Плешка'),
)


class AbcModel(models.Model):
    fam = models.CharField(
        verbose_name="Фамилия ученика",
        default="Мураткин",
        max_length=255,
    )
    a = models.CharField(
        verbose_name="Образовательная программа",
        max_length=255,
    )
    b = models.IntegerField(
        verbose_name="Курс",
        default=2, help_text="Курс студента на момент заполнения",
    )
    c = models.CharField(
        verbose_name="ВУЗ",
        choices=c_choices,
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения", auto_now=True
    )

    def __str__(self):
        return f"self.id:{self.id}; self.fam:{self.fam}"

    class Meta:
        verbose_name = "A_B_C_Таблица"
        verbose_name_plural = "A_B_C_Таблицы"
        ordering = ("-pk", )
    
class Item(models.Model):
    item_title = models.CharField(verbose_name='Заголовок (title)', max_length=255, default="Заголовок")
    item_nav = models.CharField(verbose_name='Название ссылки', max_length=255, default="Название ссылки")
    item_nav_position = models.IntegerField(verbose_name='Приоритет ссылки в навигации (0 - исключить)', default=1, help_text="большее - число правее, 0 - исключить из навигации")
    item_content = models.TextField(verbose_name='Основное содержание страницы',
                                   default="Проверка сайта")
    item_current_date = models.DateTimeField(verbose_name="Дата Записи", auto_now=True)

    class Meta:
        verbose_name = 'Содержание текущей страницы'
        verbose_name_plural = 'Содержание всех страниц'
        ordering = ('-item_nav_position',) # Сортировка по убыванию позиции в навигации

    def __str__(self):  # Используйте __str__ вместо str
        return f"pk: {self.pk};  item_title: {self.item_title}"

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})
