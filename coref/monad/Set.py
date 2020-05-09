from pymonad.Monad import *
from pymonad.Monoid import *

class Set(set, Monad, Monoid):
	"""
	Represents a non-deterministic calculation or a calculation with more than one possible result.
	Based on Python's built-in 'set' type, 'Set' supports most basic set operations
	"""

	def __init__(self, *values):
		""" Takes any number of values (including none) and puts them in the Set monad. """
		super(Set, self).__init__(values)

	def __eq__(self, other):
		if not isinstance(other, List):
			raise TypeError("Can't compare Set with non-Set type.")
		return super(Set, self).__eq__(other)

	def __ne__(self, other):
		if not isinstance(other, Set):
			return True
		return super(Set, self).__ne__(other)

	@classmethod
	def unit(cls, value):
		return Set(value)

	def getValue(self):
		"""
		Returns the set.
		This method is mainly to maintain compatibility with other monads,
		it's not strictly necessary, you can simply operate on the 'Set' like
		any other sets in Python.

		"""
		return self

	def fmap(self, function):
		""" Applies 'function' to every element in a Set, returning a new Set. """
		return Set(*list(map(function, self)))

	def amap(self, functorValue):
		""" Applies the function(s) stored in the functor to the contents of the 'functorValue' Set. """
		result = set()
		for func in self.getValue():
			result.add(func * functorValue)
		return Set(*result)

	def bind(self, function):
		"""
		Applies 'function' to the result of a previous Set operation.
		'function' should accept a single non-Set argument and return a new Set.
		"""
		result = set()
		for subList in (map(function, self)):
			result.add(subList)
		return Set(*result)

	def __or__(self, function):
		return super(Set, self).__rshift__(function)

	def __rmul__(self, function):
		return self.fmap(function)

	@staticmethod
	def mzero():
		""" Returns the identity element (an empty Set) of the Set monoid.  """
		return Set()

	def mplus(self, other):
		"""
		Combines two Set monoid values into a single Set monoid by concatenating the
		two sets together.

		"""
		return Set(*(super(Set, self).union(other)))

	def __add__(self, other):
		""" Overrides Python's native set __add__ operator to call 'mplus'.  """
		return self.mplus(other)
