venv и разное ПО для него
====
# venv

### Виртуальное окружение
1) Создание вирт окруж

```bash
python -m venv venv
```
2) Активация 
Для PowerShell и linux (вторая строка)
```bash
./venv/Scripts/activate
или
(linux) source venv/Scripts/activate
```
Выключить - 
```bash
deactivate 
```

3) Установка и экспорт зависимостей

```
pip install -r requirements.txt

pip freeze > requirements.txt 
```
4) Удалить venv  (если файлы просто удалить вывалится ошибки)
```bash
rm -r venv  
```

# Poetry

[Poetry: from zero to hero / Хабр](https://habr.com/ru/articles/740376/)

[Poetry — прекрасная альтернатива pip (шпаргалка) / Хабр](https://habr.com/ru/articles/593529/)