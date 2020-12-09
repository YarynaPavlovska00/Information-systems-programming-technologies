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
    docker build -t bobas/lab4-examples:django .
    docker images
    dokcer push bobas/lab4-examples:django
    ```
    [Імедж](https://hub.docker.com/layers/129330797/pavlovska/information_systems_programming_technologies/django/images/sha256-774e96e224aa0328b5fd8b70b71a40f2553116b226428ea6dab59039a236a222?context=explore)