class package(object):
  def __init__(self, id: int=0, weight: float=0.0, cost:      float=0.0):
    """
    Class used to define the package's id, weight and cost, the principal elements to define our object
    """
    self._id = id
    self._weight = weight
    self._cost = cost

  @property
  def id(self) -> int:
    """
    Returns package's id
    """
    return self._id

  @id.setter
  def id(self, id: int):
    """
    The id of the package
    """
    self._id = id

  @property
  def weight(self) -> float:
    """
    Returns the weight of the object
    """
    return self._weight

  @weight.setter
  def weight(self, weight: float):
    """
    The weight of the package
    """
    self._weight = weight

  @property
  def cost(self) -> float:
    """
    Returns the cost of the package by grams
    """
    return self._cost

  @cost.setter
  def cost(self, cost: float):
    """
    The cost by grams
    """
    self._cost = cost

  def calculate(self) -> float:
    """
    Method used to calculate the total cost, taking the weight and cost by grams
    """
    return self._weight*self._cost

class standardpackage(package):
  def __init__(self, id: int=0, weight: float=0.0, cost:  float=0.0, days: int=0, extra: float=0.0):
    """
    New class which is a sub-class of package. We define a new init using the father class parameters and defining the days and the extra that is used in case the package
    needs more than 2 days to arrive
    """
    package.__init__(self, id, weight, cost)
    self._days = days
    self.extra = extra

  @property
  def days(self) -> int:
    """
    Returns the days needed for the package to arrive
    """
    return self._days

  @days.setter
  def days(self, days: int):
    """
    Days for the package to arrive
    """
    self._days = days

  @property
  def extra(self) -> float:
    """
    Returns the extra that is put for each day after 2 days. The first 2 days do not count
    """
    return self._extra

  @extra.setter
  def extra(self, extra: float):
    """
    Extra money that the person will pay
    """
    self._extra = extra

  def calculate(self) -> float:
    if self.days > 2:
      return (self._weight*self._cost)+((self.days-2)*self.extra)
    if self.days <=2:
      return self._weight*self._cost

class overweightpackage(package):
  def __init__(self, id: int=0, weight: float=0.0, cost: float=0.0):
    package.__init__(self, id, weight, cost)

  def calculate(self) -> float:
    """
    We use weight to see if the package is over the weight limit. 
    """
    print ("Limite de peso permitido: 100 Kg. \nUna vez pasado, se cobran 30 por cada Kg")
    if self.weight >=100:
      return (self._weight*self._cost)+((self.weight-100)*30)
    if self.weight < 100:
      return self._weight*self._cost

apa = overweightpackage(id=345678, weight=200, cost= 120)
epa = standardpackage(id= 524352, weight=80, cost= 120, days= 3, extra= 50)
print(epa.calculate())
    