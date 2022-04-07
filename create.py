from application import db

db.drop_all()
db.create_all()

# promotion1 = Promotions(name="UFC", owner="Dana White", based="Las Vegas, Nevada")
# db.session.add(promotion1)
# db.session.commit()

# promotion2 = Promotions(name="Bellator", owner="Scott Coker", based="Hollywood, California")
# db.session.add(promotion2)
# db.session.commit()

# promotion3 = Promotions(name="One Championship", owner="Chatri Sityodtong", based="Singapore")
# db.session.add(promotion3)
# db.session.commit()

# list_of_promotions = Promotions.query.all()
# print(list_of_promotions[].name)

# fighter1 = Fighters(name="Islam Makhachev", weightclass="Mens Lightweight", based="Dagestan, Russia", promotionsbr=promotion1)
# fighter2 = Fighters(name="MVP", weightclass="Mens Welterweight", based="London England", promotionsbr=promotion2)
# db.session.add(fighter1)
# db.session.add(fighter2)
# db.session.commit()

# print(testfighter1, testfighter2)