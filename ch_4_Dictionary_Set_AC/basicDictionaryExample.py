# key -> key can be any thing except list and Dictionary
# Reason why because we can change the value of list and dictionay 
# and it's values are not fixed so....
# But , there is not restriction on values
info = {
    "key":"value",
    "name":"apana college",
    "subjects":["python","c","java"],
    "age":35,
    "is_aduly":True,
    "marks":94.7,
    12:12
}

print(info)
print(type(info))  # <class 'dict'>

#used to store key - value pairs
#Dictionary - unordered , mutable and don't allow duplicate keys
# Dictionary are Mutable , it means it is changeble