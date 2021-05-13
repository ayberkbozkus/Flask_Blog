from test import db, Human

# db.create_all()
# human1 = Human('Arin',25)
# human2 = Human('Mahmut',32)
# human3 = Human('Fatma',27)

# ### CREATE
# db.session.add_all([human1, human2, human3])
# db.session.commit()

# print(human1.id)
# print(human2.id)

### READ

all_humans = Human.query.all()
print(all_humans)

### UPDATE

first_human = Human.query.get(1)
first_human.age = 100
db.session.add(first_human)
db.session.commit()

print(first_human)

### DELETE

sec_human = Human.query.get(2)
db.session.delete(sec_human)
db.session.commit()

print(Human.query.get(2))