info = {
    "key":"value",
    "name":"apana college",
    "subjects":["python","c","java"],
    "age":35,
    "is_aduly":True,
    "marks":94.7,
    12:12
}

# get all values of Dictionary 
print(info)
#get specific key value of dictionary object
print(info["key"])
print(info["subjects"])
print(info["is_aduly"])
print(info[12])
# Override the dictionary object
info["key"]="New Value"
info["key"]="New Value 9" # it will override 
info["key1"]="New Value 1"
print(info)
#12:00