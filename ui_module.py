from abc import ABC, abstractmethod


class UInterface(ABC):

  @abstractmethod
  def setWindowSize(self, width, height):
    pass

  @abstractmethod
  def setTextField(self):
    pass

  @abstractmethod
  def setLineCounter(self):
    pass

  @abstractmethod
  def setMenu(self):
    pass