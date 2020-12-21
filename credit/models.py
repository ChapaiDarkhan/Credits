from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Program(models.Model):
    min_credits_sum = models.IntegerField(null=True)
    max_credits_sum = models.IntegerField(null=True)
    age_min = models.IntegerField(null=True)
    age_max = models.IntegerField(null=True)


class Borrower(models.Model):
    iin = models.IntegerField(unique=True)
    birthday = models.DateField(null=True, blank=True)


class Bid(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    data = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    sum = models.IntegerField(null=True)
    status = models.CharField(null=True, blank=True, max_length=50)


class Blacklist(models.Model):
    iin = models.CharField(max_length=13, db_index=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Credit'
        verbose_name_plural = 'Blacklist'

    def __str__(self):
        return str(self.iin)


# def check_credit_status(self):
#     if self.age >= 18:
#         if not self.black_book:
#             self.status = "одобрено"
#         else:
#             self.status = "Заемщик в черном списке"
#             self.save()
#     else:
#         self.status = "Заемщик не подходит по возрасту"
