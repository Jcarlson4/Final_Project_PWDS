' ' ' python
# Creation of sets
master_set = set()
monthly_set = set()


# Adding into our sets. 

master_set.add("parent1@gmail.com")
master_set.add("parent2@gmail.com")
master_set.add("parent3@gmail.com")
master_set.add("parent4@gmail.com")

monthly_set.add("parent1@gmail.com")
monthly_set.add("parent4@gmail.com")
monthly_set.add("parent5@gmail.com")


# Removing duplicates from our set to create a new master list

new_master_list = master_set.union(monthly_set)

print(f"Here is our new master list: {new_master_list}")
' ' ' python