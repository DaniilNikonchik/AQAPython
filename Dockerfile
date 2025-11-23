# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем Playwright и его браузеры
RUN python -m playwright install

# Запускаем тесты
CMD ["pytest", "--alluredir=allure-results"]
