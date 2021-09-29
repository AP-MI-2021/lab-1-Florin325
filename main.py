'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n==0 or n==1:
    return False
  for d in range(2, n//2):
    if n%d==0:
      return False

  return True

  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
   prod=1
   for el in range(0, len(lst)):
     prod = prod*lst[el]
   return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x!=y:
      if x>y:
          x=x-y
      else:
          y=y-x
  return x

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  r=x%y
  while r!=0 :
      x=y
      y=r
      r=x%y
  return y
  
  
def main():
  print ('''
    1. Nr_prim
    2. Produs
    3. Cmmdc v1
    4. Cmmdc v2 ''')
  while True:
     x=int(input('comanda='))
     if x==1:
         n=int(input('Numar='))
         print(is_prime(n))
     if x==2:
        n=int(input('Lungimea listei'))
        lst = []
        for i in range(0,n):
            element=int(input())
            lst.append(element)
        print(get_product(lst))
     if x==3:
         n=int(input('n='))
         m=int(input('m='))
         print(get_cmmdc_v1(n,m))
     if x==4:
         n = int(input('n='))
         m = int(input('m='))
         print(get_cmmdc_v2(n, m))





if __name__ == '__main__':
    main()
