import time
import pika
import os
def start(args, hkubeapi):

   connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get('RABBIT_SERVICE_HOST','localhost')))
   channel=connection.channel()

   channel.queue_declare(queue='hello')


   def callback(ch, method, properties, body):
      print(" [x] Received %r" % body)
      if (body == b'subpipeline'):
         ret = hkubeapi.start_stored_subpipeline('simple', {}, blocking=False)
      else:
         ret = hkubeapi.start_algorithm('green-alg', [{'body':body}], resultAsRaw=True, blocking=False)


   channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)


   channel.start_consuming()
   
   
