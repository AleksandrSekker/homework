class Human:
    species = 'Homosapiens'
    def __init__(self, name):
        self.name = name
    def say(self, msg):
        return "{name} >>> {message}".format(name=self.name, message=msg)
    @classmethod
    def get_species(cls):
        return cls.species
    @staticmethod
    def grunt():
        return 'Static'
