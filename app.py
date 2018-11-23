from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Network, Server
from forms import NetworkForm
from forms import ServerForm

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///networks.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('networks'))


@app.route("/new_network", methods=('GET', 'POST'))
def new_network():
    '''
    Create new network
    '''
    form = NetworkForm()
    form.servers.choices = [(s.name, s.name + " - " + s.description) for s in Server.query.order_by('name')]

    if form.validate_on_submit():
        my_network = Network()
        form.populate_obj(my_network)
        my_network.servers = ",".join(my_network.servers)

        db.session.add(my_network)
        try:
            db.session.commit()
            # User info
            flash('Network created correctly', 'success')
            return redirect(url_for('networks'))
        except:
            db.session.rollback()
            flash('Error generating network.', 'danger')

    return render_template('web/new_network.html', form=form)

@app.route("/new_server", methods=('GET', 'POST'))
def new_server():
    '''
    Create new server
    '''
    form = ServerForm()
    if form.validate_on_submit():
        my_server = Server()
        form.populate_obj(my_server)
        db.session.add(my_server)
        try:
            db.session.commit()
            # User info
            flash('Server created correctly', 'success')
            return redirect(url_for('servers'))
        except:
            db.session.rollback()
            flash('Error generating server.', 'danger')

    return render_template('web/new_server.html', form=form)



@app.route("/edit_network/<id>", methods=('GET', 'POST'))
def edit_network(id):
    '''
    Edit network

    :param id: Id from network
    '''
    my_network = Network.query.filter_by(id=id).first()
    form = NetworkForm(obj=my_network)

    form.servers.choices = [(s.name, s.name + " - " + s.description) for s in Server.query.order_by('name')]
    if not form.is_submitted() :
        form.servers.data = [(s) for s in my_network.servers.split(",")]

    if form.validate_on_submit():
        try:
            # Update network
            form.populate_obj(my_network)
            my_network.servers = ",".join(my_network.servers)
            db.session.add(my_network)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update network.', 'danger')
    return render_template(
        'web/edit_network.html',
        form=form)

@app.route("/edit_server/<id>", methods=('GET', 'POST'))
def edit_server(id):
    '''
    Edit server

    :param id: Id from server
    '''
    my_server = Server.query.filter_by(id=id).first()
    form = ServerForm(obj=my_server)

    if form.validate_on_submit():
        try:
            # Update network
            form.populate_obj(my_server)
            db.session.add(my_server)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update network.', 'danger')

    return render_template(
        'web/edit_server.html',
        form=form)


@app.route("/networks")
def networks():
    '''
    Show alls networks
    '''
    networks = Network.query.order_by(Network.name).all()
    return render_template('web/networks.html', networks=networks)

@app.route("/servers")
def servers():
    '''
    Show alls networks
    '''
    servers = Server.query.order_by(Server.name).all()
    return render_template('web/servers.html', servers=servers)


@app.route("/search")
def search():
    '''
    Search
    '''
    name_search = request.args.get('name')
    all_networks = Network.query.filter(
        Network.name.contains(name_search)
        ).order_by(Network.name).all()
    return render_template('web/networks.html', networks=all_networks)


@app.route("/networks/delete", methods=('POST',))
def networks_delete():
    '''
    Delete network
    '''
    try:
        mi_networko = Network.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_networko)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  network.', 'danger')

    return redirect(url_for('networks'))

@app.route("/servers/delete", methods=('POST',))
def servers_delete():
    '''
    Delete network
    '''
    try:
        mi_servero = Server.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_servero)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  network.', 'danger')

    return redirect(url_for('servers'))


@app.route("/network.json")
def networkjson():
    import json
    import pickle
    networks = Network.query.order_by(Network.name).all()
    output = []
    for network in networks:
        output.append({'name': network.name, 'cidr': network.cidr, 'servers': network.servers, 'vlanid': network.vlanid, 'options': network.options})
    salida = json.dumps(output, indent=4, sort_keys=True)
    return  render_template('web/network.json', networks=salida)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
