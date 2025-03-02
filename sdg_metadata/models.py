from django.db import models


class SDGMetadata(models.Model):
    project_name = models.CharField(max_length=255)
    github_url = models.URLField()
    description = models.TextField()
    sdg_targets = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
