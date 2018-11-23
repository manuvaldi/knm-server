from models import db, Network, Server
from faker import Factory
from random import randint

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake networks
for num in range(10):
    name = "net-"+fake.sentence(nb_words=2,  variable_nb_words=False, ext_word_list=None).replace(' ','-').replace('.','').lower()
    cidr = fake.ipv4_private(network=True, address_class='a')
    servers = "server1,server2"
    vlanid = randint(1000, 1500)
    options = "DI"
    # Save in database
    mi_network = Network(name=name, cidr=cidr, servers=servers, vlanid=vlanid, options=options)
    db.session.add(mi_network)

mi_server = Server(name='server1', description='descserver')
db.session.add(mi_server)
db.session.commit()
