# {} or dict() to create dictionary
meals = {"breakfast" : "toast", "lunch" : "salad", "dinner" : "enchiladas"}
print(meals["breakfast"])
#(meals[KEY])

print("breakfast" in meals)
print("2nd breakfast" in meals)
#True/false if key value is present

meals["2nd breakfast"] = "more toast"
meals["breakfast"] = "yoghurt"
print(meals)
#create or update value for keys

del(meals["lunch"])
#delete a key and value

print(meals.keys())
print(meals.values())
#print keys only, or values only.

countries = {
    "uk" : {
        "capital" : "London",
        "population" : "10000"
    },
    "germany" :  {
        "capital" : "Berlin",
        "population" : "20000"
    }
}
print(countries["germany"]["population"])
print(countries["uk"]["capital"])
#nested dictionaries, store multiple keys under an existing key
#best practice, use seperate lines for each key:value pair