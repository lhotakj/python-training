

# ----------------------------------------
# complicated way

def pozdrav_me(jmeno):
    return "Ahoj " + jmeno

def dekorator_pozdravu(fuknkce_pozdravu):
    def obal(jmeno):
        return "<b>%s</b>"%(fuknkce_pozdravu(jmeno))
    return obal

print(pozdrav_me('Jardo'))

vyvolej_pozdrav = dekorator_pozdravu(pozdrav_me)

print(vyvolej_pozdrav('Jardo'))

# ----------------------------------------
# decorator way

def dekorator_pozdravu(fuknkce_pozdravu):
    def obal(jmeno):
        return "<b>%s</b>"%(fuknkce_pozdravu(jmeno))
    return obal

@dekorator_pozdravu
def pozdrav_me(jmeno):
    return "Ahoj " + jmeno

print(pozdrav_me('Honzo'))
