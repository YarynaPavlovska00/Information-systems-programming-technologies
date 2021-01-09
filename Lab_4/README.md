## Lab_4: Робота з Docker
1. Для ознайомляння що таке Docker звернулася до [документації](https://docs.docker.com/);
2. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запустила перевірку версії, виведення допомоги та тестовий імедж:
    ```bash
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    - перенаправила вивід цих команд у файл `my_work.log` та закомітила його до репозиторію.
3. Як можна бачити Docker працює з Імеджами та Контейнерами. Імедж це свого роду операційна система з попередньо інстальованим ПЗ. Контейнер це запущений Імедж. Ідея роботи Docker дещо схожа на віртуальні машини. Перш за все створила імедж з якого буде запускатись контейнер. Для цього існує Dockerfile який описує контент імеджу.
4. Для знайомства з Docker створила імедж із Django сайтом зробленим у попередній роботі.
    - Використала команду щоб завантажити базовий імедж з репозиторію:
    ```bash
    docker pull python:3.8-slim
    docker images
    docker inspect python:3.8-slim
    ```
    - Створила файл з іменем `Dockerfile` скопіювала туди вміст такого ж файлу з цього репозиторію;
    - Ознайомилась із коментарями та постаралася зрозуміти структуру написання Dockerfile;
    - Замінила посилання на власний Git репозиторій із веб-сайтом та закомітила даний Dockerfile*
5. Створила власний репозиторій на Docker Hub. Для цього залогінилася у власний аккаунт на Docker Hub після чого створила репозиторій [Репозиторій](https://hub.docker.com/repository/docker/pavlovska/information_systems_programming_technologies).
6. Виконала білд (build) Docker імеджа та завантажила його до репозиторію: 
    ```bash
    docker build -t pavlovska/information_systems_programming_technologies:django .
    docker images
    docker push pavlovska/information_systems_programming_technologies:django
    ```
    [Імедж](https://hub.docker.com/layers/129330797/pavlovska/information_systems_programming_technologies/django/images/sha256-774e96e224aa0328b5fd8b70b71a40f2553116b226428ea6dab59039a236a222?context=explore)
    
7. Для запуску веб-сайту виконала команду:
    ```bash
    docker run -it --name=django --rm -p 8000:8000 pavlovska/information_systems_programming_technologies:django
    ``` 
    - перейшла на адресу `http://127.0.0.1:8000` та переконалася що веб-сайт працює;
8. Cтворила Dockerfile.site. Виконала білд (build) Docker імеджа з моніторингом та завантажила його до репозиторію.
    ```bash
        sudo docker build -t pavlovska/information_systems_programming_technologies:monitoring --file Dockerfile.site . 
        sudo docker images
        sudo docker push pavlovska/information_systems_programming_technologies:monitoring
    ``` 
   Запустила обидва імеджі.
   ```bash
        sudo docker run -it --rm -p 8000:8000 pavlovska/information_systems_programming_technologies:django
        sudo docker run --net=host --rm -it --volume /home/yaryna/Git/Information-systems-programming-technologies/Lab_4:/app pavlovska/information_systems_programming_technologies:monitoring
   ``` 

9. Після успішного виконання роботи відредагувала _README.md_ у цьому репозиторію та створила pull request.
//
