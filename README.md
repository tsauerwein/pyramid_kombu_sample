Pyramid example project for Kombu
===================================

This is a very simple Pyramid project showing the integration with
[Kombu](http://docs.celeryproject.org/projects/kombu/) using Redis.

This application provides a web-service, which pushes a message into a Redis
queue. A consumer script reads from this queue. That's all.

Start the web-application
-------------------------

    pserve development.ini --reload

Start the consumer script
-------------------------

    python pyramid_kombu_sample/scripts/consumer.py
    Connected to redis://localhost:6379//

Send a message to the queue
---------------------------

    $ curl http://localhost:6543
    {"project": "ok"}

The consumer script should output:

    $ python pyramid_kombu_sample/scripts/consumer.py
    Connected to redis://localhost:6379//
    Got message: {'msg': 'test'}

To check what is sent to Redis use `redis-cli` and the `MONITOR` command:

    $ redis-cli
    127.0.0.1:6379> MONITOR
    OK
    1459970119.603485 [0 127.0.0.1:43211] "INFO"
    ...
