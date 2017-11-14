class Vector():
	def __init__(self, *args):
		self.coords = list(args)

	def __repr__(self):
		template = '{}({})' # chcemy osiągnąć NazwaKlasy(argumenty, oddzielone, przecinkami)
		name = self.__class__.__name__
		args = ', '.join(repr(x) for x in self)
		return template.format(name, args)

	def __add__(self, other):
		tmp = [x + y for x, y in zip(self, other)]
		return Vector(*tmp)

	def __iadd__(self, other):
		for i, v in enumerate(other):
			self[i] += v
		return self

	def __radd__(self, other):
		return self + other

	def __len__(self):
		return len(self.coords)

	def __eq__(self, other):
		for x, y in zip(self, other):
			if not x == y:
				return False
		return True

	def __getitem__(self, idx):
		return self.coords[idx]

	def __setitem__(self, idx, value):
		self.coords[idx] = value
