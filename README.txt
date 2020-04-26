Проект web-страницы для EyePoint
Больше информации
https://ximc.ru/issues/37198
https://ximc.ru/issues/38120
https://ximc.ru/issues/36703

Для корректной работы сервера директория с файлами на скачивание должна существовать
Папки для каждого продукта на продажу должны быть в view/static/download. При использовании контейнера эта папка
монтируется с помощью docker volume. Для тестового запуска, во время разработки (без контейнера) эту папку можно
просто создать

Запуск сервера (для тестов):
python server.py

Сборка и запуск контейнера
sudo docker build . -t epw
sudo docker run --publish 80:8080 --restart=always -d --mount source=download,target=/app/view/static/download epw
Обрати внимание: docker диск 'download' должен существовать. В этом разделе должны быть файлы для скачивания с
сайта


Для пересборки контейнера можно использовать скрипт
scripts/rebuild-docker.sh

Иконки флагов взяты с
https://github.com/HatScripts/circle-flags.git
Другие иконки взяты с
https://www.iconsdb.com/white-icons/
