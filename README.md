# user_image_api
User Image System

# For run this application

1- Server PostgreSQL and Server RabbitMQ https://github.com/wasosky313/infrastructure

2- git clone https://github.com/wasosky313/user_image_api.git

3- cd user_image_api

4- docker build -t api .

5- docker run -e DB_HOST='your host database address' -e MQ_CONNECTION='your host RabbitMQ address' --net=host -t api

For Example docker run -e DB_HOST='192.168.1.104' -e MQ_CONNECTION='192.168.1.104' --net=host -t api 
