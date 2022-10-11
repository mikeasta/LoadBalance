# Запуск
В первую очередь, в файле config.py задаем число серверов и стартовый порт для серверов.
Порты будут назначены на один правее от заданного стартового порта:
Стартовый порт = 7000 - значит сервер №1 запустится на порту 7001
Далее:
1. Запускаем сервера-исполнителей. В терминале 1 прописываем:
```
python workers.py 
```
2. Запускаем сервер-распределитель. В терминале 2 прописываем:
```
python server.py
```
3. Запускаем интерфейс для тестирования. В терминале 3 прописываем:
```
locust
```