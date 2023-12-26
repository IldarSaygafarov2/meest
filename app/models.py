from django.db import models


class UserRequest(models.Model):
    track_number = models.CharField(verbose_name="Трек номер", max_length=50)
    fullname = models.CharField(verbose_name="Полное имя", max_length=100)
    passport_series = models.CharField(verbose_name="Серия пасопрта", max_length=3)
    passport_number = models.CharField(verbose_name="Номер паспорта", max_length=12)
    pinfl = models.CharField(verbose_name="ПИНФЛ", max_length=14)
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.track_number}: {self.fullname}'

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']
