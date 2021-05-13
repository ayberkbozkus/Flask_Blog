from test import dbs, Human

dbs.create_all()
human1 = Human('Arin',25)
human2 = Human('Mahmut',32)
human3 = Human('Fatma',27)

### CREATE
dbs.session.add_all([human1, human2, human3])
dbs.session.commit()

print(human1.id)
print(human2.id)

### READ

all_humans = Human.query.all()
print(all_humans)