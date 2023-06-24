import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="creator",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="todo",
            name="project",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="todoapp.project"),
        ),
        migrations.AddField(
            model_name="project",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]