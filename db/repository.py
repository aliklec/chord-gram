import abc
from model.chord import *

# abstract class
# don't want domain code to worry about database specifics
# don't want to have to rewrite code if database changes
# instead can just change this repository class
class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_songs(self):
        raise NotImplementedError

    @abc.abstractmethod
    def load_chords(self):
        raise NotImplementedError