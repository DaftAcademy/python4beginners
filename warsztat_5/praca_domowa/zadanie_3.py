# Fibonacci generator
#
# Napis generator ciągu Fibonacciego: fibonnacci(elements_limit).
# Generator ma zwracać kolejne wyrazy ciągu Fibonacciego: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
# 
# Args:
#    `elements_limit` - określa ilość zwróconych liczb. Jeśli `elements_limit` nie zostanie podane to generator ma być nieograniczony. Załóż, że jeżeli `elements_limit` będzie podane to zawsze będzie to int >= 0.

        
if __name__ == '__main__':
    assert list(fibonnacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert list(fibonnacci(1)) == [0]
    assert list(fibonnacci(0)) == []
    assert list(fibonnacci(2)) == [0, 1]
