# API Restaurant Menu

<h3>Запуск проекта:</h3>

1. Клонируйте репозиторий;
2. Создайте в корне проекта и заполните файл .env по примеру файла .env.example:

    ```
    SECRET_KEY=
    DEBUG=
    
    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=
    ```
3. Установите docker или проверьте его наличие командой, также перейдите в файл проекта:

   ```
   docker --version
   ```
   ```
   cd api_drf_restaurant
   ```
4. Запустите проект командой:

   ```
   docker compose up -d --build
   ```

5. Если необходимо загрузить фикстуру, то используйте команду:
   ```
   docker exec -it <id контейнера> python3 manage.py loaddata <название файла>.json 
   ```

6. Документация доступна по ссылкам:
    ```
    http://127.0.0.1:8000/api/schema/swagger-ui/
    ```
   или
    ```
    http://127.0.0.1:8000/api/schema/redoc/
    ```