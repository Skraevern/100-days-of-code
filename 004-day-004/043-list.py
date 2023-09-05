states_of_america = ["Delaware", "Pennsylvania", "Aapaoskd", "Hawaii"]
print(states_of_america[0]) # Delaware
print(states_of_america[-1]) # Hawaii

states_of_america[2] = "New Jersey"
print(states_of_america) # ['Delaware', 'Pennsylvania', 'New Jersey', 'Hawaii']

states_of_america.append("Georgia")
print(states_of_america) # ['Delaware', 'Pennsylvania', 'New Jersey', 'Hawaii', 'Georgia']

states_of_america.extend(["Minnesota", "California"])
print(states_of_america) # ['Delaware', 'Pennsylvania', 'New Jersey', 'Hawaii', 'Georgia', 'Minnesota', 'California']