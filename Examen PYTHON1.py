#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 16:28:40 2022

@author: alioubadraconde
"""

"""
Created on Tue Feb  1 15:14:49 2022

@author: alioubadraconde
"""

#a) Implémenter la fonction polynomiale ci-dessous:

def polynome(n) :
    #fonction polynome
    polynome = n*n*n-1.5*n*n-6*n+5
    return polynome
print(polynome(5))


## b) Implémenter la fonction factorielle (Approche récursive ou classique) :

 #factorielle 


while True :
    n = int(input("Saisir la valeur de n : "))
    if n >= 0 :
        break
if n == 0 :
    print("Factorielle de 0 est 1")
else :
    F = 1
    for i in range (2, n+1) : 
        F = F * i
        print("factorielle de ",n," est : " , F)


#### c-) La suite de fibonacci 
# 1ere méthode :
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
    print(fibonacci(i))


#2éme méthode :
    nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant

# 2-) Création de fonction comportant des modules de gestions des exceptions
def factorielle(x) :
    if type (x) == str :
        print ("Saisie incorrecte. Entrer des valeurs entieres positives")
        if type(x) == complex :
            print ("Saisie incorrecte. Entrer des valeurs entieres positives")
            if x < 0 :
                print ("Saisie incorrecte. Entrer des valeurs entieres positives")
                if x > 10**5 :
                    print ("Saisie trop grande. Entrer des valeurs entieres positives")
                    if x < 5:
                        print ("Nombre trop petit. Entrer des valeurs plus grandes")
        

#3. Question Bonus : Implémentation de la formule Pricer d’option avec Python

def d1 (S,X,r,kho,T):
    d1 = (np.log(S/X)+(r +(kho*kho)*T))/(kho*np.sqrt(T))
    return d1
def d2 (d1,kho,T):
    d2 = d1 - (kho*np.sqrt(T))
    return d2
def c (S,N,X,d1,d2,r,kho,T):
    c = (S*N*d1)-(X*np.exp(-(r*T))*N*d2)
    return c
def p (S,N,X,d1,d2,r,kho,T):
    p = (X*np.exp(-(r*T))N(-d2))-(S*N*(-d1))
    return c


        


