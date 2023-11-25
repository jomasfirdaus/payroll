from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from contract.models import *
from employee.models import *


class Salary(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True, related_name='salary')
    gross = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Gross Salary")
    tax = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    social = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name="Social Security")
    net = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_lock = models.BooleanField(default=False, null=True)
    is_confirm = models.BooleanField(default=False, null=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Salarycreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Salaryupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Salarydeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.employee} ({0.contract})'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Salary'
