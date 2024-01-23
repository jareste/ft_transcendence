from channels.generic.websocket import WebsocketConsumer

from .models import Usermine


class loginConnection(WebsocketConsumer):
    
    def connect(self):
        print("hola estem aqui")
        self.user = self.scope['query_string'].decode('UTF-8').split('&')[0].split('=')[1]

        self.accept()


    def disconnect(self, code):

        userBD = Usermine.objects.get(id=self.user);

        userBD.online = False
        userBD.save()
                
    
    def receive(self, text_data):
        return
        
