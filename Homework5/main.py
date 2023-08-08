from person import Person
from person_mapper import PersonMapper

if __name__ == '__main__':
    person = Person("John", "AFRE", 17)
    print(person.get_name, person.get_last_name)
    mapper = PersonMapper()
    mapper.add_data(person)
    mapper.add_data(Person("Mike", "Yicke", 23))
    mapper.show_dictionary()
    mapper.delete_person(1)
    mapper.show_dictionary()
    person2 = mapper.to_person(2)
    print(person2.get_name,person2.get_last_name,person2.get_age)
