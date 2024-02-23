from abc import ABC, abstractmethod


class Test(ABC):

    @property
    @abstractmethod
    def critical(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def teardown(self):
        pass
