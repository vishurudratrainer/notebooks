from sqlalchemy import create_engine,or_,and_
from sqlalchemy import text
enginee =create_engine("sqlite:///my.db")
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

with enginee.connect() as con:
    selectQuery =text("select * from emp")
    results =con.execute(selectQuery)
    r =results.mappings().all()
    print(r)

Base =declarative_base()

class Emp(Base):
    __tablename__="emp"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    def __str__(self):
        return "id {} name {} age {}".format(self.id,self.name,self.age)

Base.metadata.create_all(enginee)


from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=enginee)
session=Session()
#emp1=Emp(id=1,name="Raj",age=22)
#session.add(emp1)
#session.commit()

#for emp in session.query(Emp).all():
 #  print(emp)

#data=[Emp(id=4,name="Vishwa",age=55),Emp(id=35,name="Raju",age=14)]
#session.add_all(data)
#session.commit()
#res=session.query(Emp).filter(or_(Emp.id==1,Emp.id==2)).all()
#for emp in res:
 #   print(emp)
#res=session.query(Emp).filter(Emp.id==1,Emp.id==2).all()

res=session.query(Emp).filter(Emp.name.like("R%")).all()
for emp in res:
    print(emp)