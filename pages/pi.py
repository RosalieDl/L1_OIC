import streamlit as st
from mpmath import mp

def somme_pi(length: int):
    mp.dps = length + 1
    pi = mp.pi
    somme = 0
    for digit in str(pi)[2:]:
        somme += int(digit)
    return(somme)

print(somme_pi(20))
print(somme_pi(12*12))
