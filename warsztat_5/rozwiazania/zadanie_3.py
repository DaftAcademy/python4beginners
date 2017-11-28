# Fibonacci generator
#
# Napisz generator ciągu Fibonacciego: fibonnacci(elements_limit).
# Generator ma zwracać kolejne wyrazy ciągu Fibonacciego: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
# 
# Args:
#    `elements_limit` - określa ilość zwróconych liczb. Jeśli `elements_limit` nie zostanie podane to generator ma być nieograniczony. Załóż, że jeżeli `elements_limit` będzie podane to zawsze będzie to int >= 0.



def fibonnacci(elements_limit=None):
	limit_set = False
	count = 0
	if elements_limit is not None:
		limit_set = True
	fib = _inf_fib()
	while True:
		if limit_set:
			if count < elements_limit:
				count += 1
				yield next(fib)
			else:
				break
		else:
			yield next(fib)


def _inf_fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a, b = b, c
