from data.data_manager import DataManager
from data.person import Person

new_person = Person()
new_person.set_id(3)
new_person.set_name("Michael")
new_person.set_surname("Jackson")
new_person.set_year(1900)

DataManager().add_person(new_person)