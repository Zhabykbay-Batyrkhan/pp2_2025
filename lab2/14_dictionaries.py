myfamily = {
  "child1" : {
    "name" : "Aisana",
    "year" : 2015
  },
  "child2" : {
    "Me" : "Batyrkhan",
    "year" : 2007
  },
  "child3" : {
    "name" : "Bakdaulet",
    "year" : 2006
  },
  "child4" : {
    "name" : "Nurila",
    "year" : 2001
  },
  "child5" : {
    "name" : "Nurzhanat",
    "year" : 2000
  }
}

for child, details in myfamily.items():
    print(f"{child}: {details}")