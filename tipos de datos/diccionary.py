"""dic = {
    "nombre": "Diego", 
    "apellido":"Saavedra", 
    "celular":"0992017564", 
    "edad":34 
    }

print(type(dic))
print(dic)

print(dic["celular"])
print(dic["edad"])

print(dic.get("apellido"))
dic["edad"]=35
print(dic)

print(len(dic))

dic["ciudad"] = "Loja"
print(dic)

dic.pop("ciudad")
print(dic)

dic.popitem()
print(dic)

del dic["nombre"]
print(dic)

dic2 = dic.copy()
print(dic2)
"""

perros = {
    "Tobby":{
        "name": "Tobby",
        "age": 7,
        "raza": "mestizo"
    },
    "Leo":{
        "name": "Leo",
        "age": 1,
        "raza": "mestizo"
    }
}

print(type(perros))
print(perros)

Tobby = {
    "name": "Tobby",
    "age": 7,
    "raza": "mestizo"
    }

Leo = {
    "name": "Leo",
    "age": 1,
    "raza": "mestizo"
    }

perros_v2 = {
    "Toby": Tobby,
    "Leo": Leo
}

print(type(perros_v2))
print(perros_v2)

Rocky = dict(
    name="Rocky",
    age =2,
    raza = "mestizo"
)

print(type(Rocky))
print(Rocky)