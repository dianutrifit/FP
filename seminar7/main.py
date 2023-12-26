from die import Die, f
from frac import Frac
from auto import Auto
from statistics import Statistics

from konto import Konto
from tests import test_auszahlen


def main():


  f1=Frac(4,12)
  f1.reduce()
  print(f'{f1.n}/{f1.m}')

  s=Statistics()
  autos=[Auto('m1','m2',1000,'red'),
         Auto('m1','m2',1000,'blue'),
         Auto('m1','m2',1000,'red')
         ]

  print(f'#red autos= {s.count_color(autos,color)}')

  k=Konto(1234,4000,'Admin')
  k.einzahlen(200)
  print(k)


test_auszahlen()
main()
