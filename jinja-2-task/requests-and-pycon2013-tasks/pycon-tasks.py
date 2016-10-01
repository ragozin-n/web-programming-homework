# ------- #
# 01_engine_usage Task 1
from sqlalchemy import create_engine
import os

if os.path.exists("some.db"):
    os.remove("some.db")
e = create_engine("sqlite:///some.db")
e.execute("""
    create table employee (
        emp_id integer primary key,
        emp_name varchar
    )
""")
e.execute("insert into employee (emp_name) values (:emp_name)", emp_name="dilbert")

# 01_engine_usage Task 2
e.execute("select * from employee")

# ------- #
# 02_metadata Task 1
from sqlalchemy import String, Integer, DateTime, ForeignKey
metadata = MetaData()
fancy_table = Table('network', metadata,
                    Column('network_id', Integer, primary_key=True),
                    Column('name', String(100), nullable=False),
                    Column('created_at', Datetime, nullable=False),
                    Column('owner_id', Integer, ForeignKey('user.id')),
                )

# 02_metadata Task 2
metadata.create_all(e)

# 02_metadata Task 3
metadata2 = MetaData()
user_reflected = Table('user', metadata2, autoload=True, autoload_with=e)

from sqlalchemy import inspect
inspector = inspect(e)
print(inspector.get_columns('network'))

# + bonus subtask
for column in inspector.get_columns('network'):
   print(column['name'])

# 02_metadata Task 4
result = []
for table_name in inspector.get_table_names():
   for column in inspector.get_columns(table_name):
       if column['name'] == 'story_id':
           result += table_name
print(set(result))

# ------- #
# 03_sql_expressions Task 1

metadata = MetaData()
user_table = Table('user', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('username', String(50)),
                    Column('fullname', String(50))
                   )
engine = create_engine("sqlite://some.db")
metadata.create_all(engine)

# 1 subtask
print(user_table.c.fullname == 'ed')

# 2 subtask
print(and_(user_table.c.fullname == 'ed',user_table.c.id > 5))

# 3 subtask
print(or_(user_table.c.username == 'ed'), and_(user_table.c.fullname == 'ed',user_table.c.id > 5))

# 03_sql_expressions Task 2
# 1 subtask
conn = engine.connect()
result = conn.execute(user_table.insert(), [{'username': 'dilbert', 'fullname': 'Dilbert Jones'}])

# 2 subtask
prin(result.inserted_primary_key)

# 3 subtask
select_some_values = select([user_table]).\
                    where(
                        or_(
                            user_table.c.username == 'wendy',
                            user_table.c.username == 'dilbert'
                        )
                    ).\
                    order_by(user_table.c.fullname)
conn.execute(select_some_values).fetchall()

# 03_sql_expressions Task 3
address_table = Table("address", metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', Integer, ForeignKey('user.id'),
                                                            nullable=False),
                        Column('email_address', String(100), nullable=False)
                      )
metadata.create_all(engine)
conn.execute(address_table.insert(), [
    {"user_id": 1, "email_address": "ed@ed.com"},
    {"user_id": 1, "email_address": "ed@gmail.com"},
    {"user_id": 2, "email_address": "jack@yahoo.com"},
    {"user_id": 3, "email_address": "wendy@gmail.com"},
])

select_query = select([user_table.c.fullname, address_table.c.email_address])
               .select_from(user_table.join(address_table))
               .where(user_table.c.username=='ed')
               .order_by(address_table.c.email_addres)
print(select_query)

# 03_sql_expressions Task 4
# 1 subtask
result = user_table.update()
                   .values(fullname = "Ed Jones")
                   .where(user_table.c.username=='ed')
conn.execute(result)

# 2 subtask
print(result.rowcount)

# 3 bonus subtask
bonus_query = user_table.update()
                        .values(fullname = user_table.c.fullname + user_email.as_scalar())
                        .where(user_table.c.username
                        .in_({'jack', 'wendy'}))
conn.execute(bonus_query)

# ------- #
# 04_orm Task 1
# 1 subtask
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Network(Base):
    __tablename__ = 'network'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    def __repr__(self):
        return "Network: %r" % (self.name)

# 2 subtask
# Already done in previous task: engine = create_engine('sqlite://some.db')
Base.metadata.create_all(engine)

# 3 subtask
from sqlalchemy.orm import Session
session = Session(bind = engine)
session.add(Network(name = 'net1'))
session.add(Network(name = 'net2'))
session.commit()

# 04_orm Task 2
# 1 subtask
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return "User: %r, %r" % (self.name, self.fullname)
session.add_all([
    User(name='wendy', fullname='Wendy Weathersmith'),
    User(name='mary', fullname='Mary Contrary'),
    User(name='fred', fullname='Fred Flinstone')
])

query = session.query(User.fullname).order_by(User.fullname)

# 2 subtask
query.all()

# 3 subtask
second_query = query.filter(User.name.in_(['mary', 'ed']))

# 4 subtask
second_query.all()
print(second_query[1])

# 04_orm Task 3
# 1 subtask
join_query = session.query(User.name, Address.email_address)
                    .join(Address)
                    .filter(Address.email_address.in_(['j25@yahoo.com']))
join_query.all()

# 2 bonus subtask
First, Second = aliased(User), aliased(User)
pairs_query = session.query(First.name, Second.name)
                     .outerjoin()
                     .filter(First.name != Second.name)
pairs_query.all()

# 04_orm Task 3 (Final Exam)
# 1 subtask
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    owner = Column(String(50), nullable=False)
    balance = Column(Numeric, default=0)
    def __repr__(self):
        return "Account: %r, %r" % (self.owner, self.balance)

# 2 subtask
class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Numeric, nullable=False)
    account_id = Column(Integer, ForeignKey(Account.__tablename__ + '.id'), nullable=False)
    # 3 subtask
    account = relationship('Account', backref="transactions")
    def __repr__(self):
        return "Transaction: %r" % (self.amount)

# 4 subtask
from sqlalchemy.orm import Session

session = Session(bind = engine)
a1 = Account(owner = "Jack Jones", balance = 5000)
a2 = Account(owner = "Ed Rendell", balance = 10000)
t1 = Transaction(amount = 500, account = a1)
t2 = Transaction(amount = 4500, account = a1)
t3 = Transaction(amount = 6000, account = a2)
t4 = Transaction(amount = 4000,  account = a2)
session.add_all([a1,a2,t1,t2,t3,t4])
session.commit()

# 5 subtask
for account in session.query(Account).all():
    owner = account.owner
    balance = account.balance
    spent_money = 0
    for account_transaction in account.transactions:
        spent_money += account_transaction.amount
    print("Account owner: " + str(owner) + '\t' +
          "Account balance: " + str(balance) + '\t' +  
          "Spent money: " + str(spent_money))
