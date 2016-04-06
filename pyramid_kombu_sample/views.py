from pyramid.view import view_config
from kombu.pools import producers

from pyramid_kombu_sample.queues import exchange, queue


@view_config(route_name='home', renderer='json')
def home(request):
    message = {'msg': 'test'}

    connection = request.registry.queue_connection
    with producers[connection].acquire(block=True) as producer:
        producer.publish(message, exchange=exchange, declare=[exchange, queue])

    return {'status': 'ok'}
