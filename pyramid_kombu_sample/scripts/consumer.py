from kombu.mixins import ConsumerMixin
from kombu.log import get_logger

from pyramid_kombu_sample.queues import queue

logger = get_logger(__name__)


class Worker(ConsumerMixin):
    """Worker based on this example:
    http://docs.celeryproject.org/projects/kombu/en/latest/userguide/examples.html
    """

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=[queue], callbacks=[self.process_task])]

    def process_task(self, body, message):
        logger.info('Got message: %s', body)
        message.ack()

if __name__ == '__main__':
    from kombu import Connection
    from kombu.utils.debug import setup_logging
    # setup root logger
    setup_logging(loglevel='INFO', loggers=[''])

    with Connection('redis://localhost:6379/') as conn:
        try:
            worker = Worker(conn)
            worker.run()
        except KeyboardInterrupt:
            print('bye bye')
