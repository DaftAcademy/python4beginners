# Iterator Collatza
#
# Zadanie rozwiąż BEZ UŻYCIA GENERATORÓW.
# Napisz klasę CollatzSeq(start_value) wyliczającą kolejne liczby według wzoru:
#    https://pl.wikipedia.org/wiki/Problem_Collatza#Sformu.C5.82owanie_problemu_Collatza
# Powinno być możliwe iterowanie po CollatzSeq (po kolejnych liczbach z sekwencji).
# Wartość 1 powinna być zwrócona tylko raz, potem iteracja powinna zostać przerwana
# 
# Argumenty:
#     `start_value` - liczba od której zaczniemy wyliczać sekwencję. Podanie liczby innej niż 
#                            liczba naturalna powinno skutkować rzuceniem wyjątku ValueError


class CollatzSeq:
 	def __init__(self, start_value):
 		if not isinstance(start_value, int):
 			raise ValueError
 		if start_value < 1:
 			raise ValueError
 		self.start_value = start_value

 	def __iter__(self):
 		return CollatzSeqIterator(self)


class CollatzSeqIterator:
	def __init__(self, seq):
		self.val = seq.start_value
		self.initial_returned = False
		self.seq_finished = False


	def __iter__(self):
		return self

	def __next__(self):
		if self.seq_finished:
			raise StopIteration
		if not self.initial_returned:
			self.initial_returned = True
			if self.val == 1:
				self.seq_finished = True
			return self.val
		if self.val % 2:  # niepodzielne przez 2
			self.val = 3 * self.val + 1
		else:
			self.val //= 2  # // bo chcemy int a nie float.
		if self.val == 1:
			self.seq_finished = True
		return self.val
