# Yandex_Afisha
Учебный проект dvmn

Показывает интересные места по всему миру с помощью яндекс афиши, основан на этом [Фронтенде для сайта](https://github.com/devmanorg/where-to-go-frontend).     
<img width="1228" alt="image" src="https://github.com/SGKespace/sale_of_fish_bot/assets/55636018/6cd4d26f-0769-412c-b2fd-a765c6f35478">


[Посмотреть как все работает](http://80.249.150.113:8080 )


## Требования к окружению 
Уставновить [Python 3+](https://www.python.org/downloads/)    
Скачайте репозиторий.
Установите, создайте и активируйте виртуальное окружение:
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```
Установите библиотеки командой: 
```
pip3 install -r requirements.txt  
``` 
     
## Переменные окружения     
Создайте файл ".env" (в него надо прописать ваши настройки)   
`DEBUG` - режим отладки      
`SECRET_KEY` - секретный ключ    
`ALLOWED_HOSTS` - Список хостов/доменов, для которых может работать текущий сайт.    
     
Пример .env файла    
```
SECRET_KEY=123qwe123
DEBUG=false
ALLOWED_HOSTS=webargs,konch,ped
```
## Запуск кода  
```
python3 manage.py runserver
```
## Добавление мест с помощью кода
```
python3 manage.py load_place http://адрес/файла.json
```
[Данные, которые можете загрузить](https://github.com/devmanorg/where-to-go-places).    
     
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

## Отказ от ответственности:
Автор программы не несет никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Эта программа была написана для обучения автора и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
