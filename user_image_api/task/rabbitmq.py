
import json
import datetime

from user_image_api.config.rabbitmq import channel


def publish_message(user_id, user_name, image_id, endpoint):
    logged = {
        'user_id': user_id,
        'user_name': user_name,
        'image_id': image_id,
        'endpoint': endpoint,
        'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    channel.basic_publish(exchange='', routing_key='user_image_api_logg', body=json.dumps(logged))
    print(" [x] SENT MESSAGE TO QUEUE")

