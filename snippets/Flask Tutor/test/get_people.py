from data import data_manager

manager = data_manager.DataManager()
people = manager.get_people()

for person in people:
    print(person.get_name())