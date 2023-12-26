from statistics import Statistics
from auto import Auto
from konto import Konto


def test_auszahlen():
    k=Konto('101A',100,'Peter') #facem obiectul

    k.auszahlen(10)
    assert k.betrag==90

"""def test_count_color():
    s=Statistics()
    autos=[Auto('m1','m2',1000,'red'),
           Auto('m1','m2',1000,'blue'),
           Auto('m1','m2',1000,'red')
           ]

    color='red'"""


