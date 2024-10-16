import os
import django
import io

# Устанавливаем переменную окружения, чтобы указать на файл настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial_project.settings')

# Инициализируем Django
django.setup()

from snippets.serializers import SnippetSerializer

serializer = SnippetSerializer()
print(repr(serializer))
