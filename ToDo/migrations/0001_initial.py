from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=64, unique=True)),
                ("repository", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="ToDo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField(blank=True, null=True)),
                ("create", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]