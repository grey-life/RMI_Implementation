import Pyro4

@Pyro4.expose

class GreetingMaker(object):
    def get_fortunate(self, name):
        greeting = 'Hello, '+name + "."
        fortune_message = '\nSomeone is looking upto you. Don\'t let that person down'
        return greeting + fortune_message

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingMaker)

print("Ready. Object uri = ", uri)
daemon.requestLoop()


