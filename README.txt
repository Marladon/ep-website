Проект web-страницы для EyePoint
Больше информации
https://ximc.ru/issues/37198
https://ximc.ru/issues/38120
https://ximc.ru/issues/36703

Запуск сервера (для тестов):
python server.py

Сборка и запуск контейнера
sudo docker build . -t ep-web
sudo docker run --publish 80:8080 --restart=always -d ep-web

Либо для пересборки контейнера попробуй скрипт
scripts/rebuild-docker.sh

Иконки флагов взяты с
https://github.com/HatScripts/circle-flags.git
Другие иконки взяты с
https://www.iconsdb.com/white-icons/
