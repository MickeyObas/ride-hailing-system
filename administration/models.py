from django.db import models


class AdminLog(models.Model):
    admin_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='+')
    target_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='+')
    action = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)


class SupportTicket(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    message = models.TextField()
    status = models.CharField(max_length=140)
    priority = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    