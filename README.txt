Проект web-страницы для EyePoint
Больше информации https://ximc.ru/issues/37198

Запуск сервера (для тестов):
python server.py

Сборка и запуск контейнера
sudo docker build . -t ep-web
sudo docker run --publish 80:8080 --restart=always -d ep-web

Либо для пересборки контейнера попробуй скрипт
rebuild-docker.sh
