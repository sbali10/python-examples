import mod    #mod.py içeirsinde oluşturduğumuz modülü import ediyoruz

#result = help(mod)
#result = help(mod.func)   #moduülün functionı hakkındaki bilgilendirme
result = mod.number
result = mod.numbers
result = mod.person["name"]
result = mod.func(10)

p = mod.Person()
p.speak()

print(result)