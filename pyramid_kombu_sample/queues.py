from kombu import Exchange, Queue

exchange = Exchange('simple_exchange', type='direct')
queue = Queue('simple_queue', exchange)
