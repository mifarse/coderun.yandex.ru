# Решение задач с coderun.yandex.ru
Всем привет! В этом репозитории я собираю свои решения по задачам на языке
python.

<p align="left">
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Минимальная настройка репозитория
Чтобы работать с этим репозиторием просто создайте ✨ codespace ✨

В общем на этом все. Я настроил `devcontainer.json`, так что в бразуере для вас 
откроется IDE с предустановленным python и pytest.

## Структура репозитория
Код разделен по папкам. Одна папка - одна задача. В папке содержатся файлы:
- `main.py` - код задачи. Этот файл можно запускать и дебажить как мы обычно 
привыкли.
- `test_XX.py` - тест задачи. В тесте импортируется ф-я `main()` и патчится 
stdin и stdout.
- `README.md` - условие задачи.

## Попрактиковаться
Вы можете изменять код в созданном codespace как хотите. Можете стереть 
содержимое функции `main()` и написать по-своему. В вашем распоряжении есть все 
инструменты для отладки и тестирования.
### Запуск тестов
Для запуска тестов используйте вкладку 🧪 (тестирование) или руками выполняйте
консольную команду:

```bash
pytest <папка-задачи> -v
```
