from pymonad.Monad import *
from pymonad.Monoid import *

class Dict(dict, Monad, Monoid):
	"""
	Represents a non-deterministic calculation or a calculation with more than one possible result.
	Based on Python's built-in 'dict' type, 'Dict' supports most basic dict operations such as
	indexing,  etc.
	"""

	def __init__(self, **values):
		""" Takes any number of values (including none) and puts them in the Dict monad. """
		super(Dict, self).__init__(values)

	def __eq__(self, other):
		if not isinstance(other, Dict):
			raise TypeError("Can't compare Dict with non-Dict type.")
		return super(Dict, self).__eq__(other)

	def __ne__(self, other):
		if not isinstance(other, Dict):
			return True
		return super(Dict, self).__ne__(other)

	#def __getitem__(self, key):
	#	print(key, self)
	#	return Dict(**super(Dict, self).__getitem__(key))

	def __str__(self):
		display = "Dict {  "
		for item in self:
			display += "{}:{}".format(str(item),str(self[item])) + ", "
		return display[:-2]+ "  }"

	@classmethod
	def unit(cls, value):
		return Dict(value)

	def getValue(self):
		"""
		Returns the dict.
		This method is mainly to maintain compatibility with other monads,
		it's not strictly necessary, you can simply operate on the 'Dict' like
		any other dict in Python.

		"""
		return self

	def fmap(self, function):
		""" Applies 'function' to every element in a Dict, returning a new Dict. """
		res = {}
		for k in self:
			res[k] = function(k, self[k])
		return Dict(**res)

	def amap(self, functorValue):
		""" Applies the function(s) stored in the functor to the contents of the 'functorValue' Dict. """
		result = {}
		for name in self.getValue():
			result[name] = self[key] * functorValue
		return Dict(**result)

	def bind(self, function):
		"""
		Applies 'function' to the result of a previous Dict operation.
		'function' should accept a single non-Dict argument and return a new Dict.
		"""
		return Dict(**function(self))

	def __or__(self, function):
		return super(Dict, self).__rshift__(function)

	def __rmul__(self, function):
		return self.fmap(function)

	@staticmethod
	def mzero():
		""" Returns the identity element (an empty Dict) of the Dict monoid.  """
		return Dict()

	def mplus(self, other):
		"""
		Combines two Dict monoid values into a single Dict monoid 

		"""
		super(Dict, self).update(other)
		return Dict(**self)

	def __add__(self, other):
		""" Overrides Python's native list __add__ operator to call 'mplus'.  """
		return self.mplus(other)

Values = Dict
