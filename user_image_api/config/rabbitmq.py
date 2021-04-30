import pika
from pika.exceptions import AMQPConnectionError

from user_image_api.config import MQ_CONNECTION
from user_image_api.exception.base import RabbitMQConnect

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_CONNECTION))
    channel = connection.channel()
    channel.queue_declare(queue='user_image_api_logg')
except AMQPConnectionError:
    raise RabbitMQConnect()
