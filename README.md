### Вывести все Twit (GET):
localhost:5000/twit

### Вывести Twit по номеру id (GET):
localhost:5000/twit/3

### Записать Twit (POST):
localhost:5000/twit
body:
{"body": "Hello World", "author": "@vireshnik"}

### Изменить выбранный Twit (PUT):
localhost:5000/twit/3
body:
{"body": "Hello my World!!!"}

### Удалить выбранный Twit (DELETE):
localhost:5000/twit/3
