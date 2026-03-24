import math
def m_litra(gallonat):
    litrat= gallonat*3.785
    return litrat

while True:
    n_gallonat= float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa):"))
    if n_gallonat < 0:
        print("Ohjelma päättyy.")
        break
    vastaus= m_litra(n_gallonat)
    print(f"{n_gallonat:.2f} gallonaa on {vastaus:.3f} litraa.")