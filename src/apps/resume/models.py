from django.db import models as m


class Technology(m.Model):
    name = m.TextField(unique=True)
    description = m.TextField(null=True, blank=True)

    def __str__(self):
        return f"#{self.pk}: {self.name!r}"


class Project(m.Model):
    started_at = m.DateField(null=True, blank=True)
    finished_at = m.DateField(null=True, blank=True)
    summary = m.TextField(null=True, blank=True)
    technologies = m.ManyToManyField(Technology, related_name="projects")


class Responsibility(m.Model):
    project = m.ForeignKey(Project, on_delete=m.CASCADE, related_name="responsibilities")
    summary = m.TextField()
