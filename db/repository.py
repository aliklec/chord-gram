import abc
from model.chordmaker import *

# abstract class
# don't want domain code to worry about database specifics
# don't want to have to rewrite code if you changed database
# instead you could just change this repository class
class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_chord(self):
        raise NotImplementedError

