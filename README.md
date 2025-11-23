# Автоматические UI тесты для сайта effective-mobile.ru

## Требования:
- Python 3.10
- Docker (если вы хотите запускать тесты в контейнере)

## Установка зависимостей:
1. Клонируйте проект:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Инициализируйте Playwright:
   ```bash
   python -m playwright install

## Запуск тестов:
1. Запуск тестов локально:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
2. Запуск тестов через Docker:
   * Построить контейнер:
     ```bash
     docker build -t playwright-tests .
   * Запустить контейнер:
     ```bash
     docker run --rm playwright-tests

## Структура проекта:
   * /tests: директория с тестами
   * /pages: Паттерн Page Object для страницы
   * Dockerfile: для сборки и запуска тестов в Docker
   * requirements.txt: зависимости проекта
   * README.md: инструкция по установке и запуску

