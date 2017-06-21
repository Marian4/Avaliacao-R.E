from connect import Connection
from User import User

connection = Connection.session()

new_user = User("Marcos", "marcossilva", "12345")
connection.add(new_user)
connection.commit()
