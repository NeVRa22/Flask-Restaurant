from app import application
from flask import jsonify, Response, session, request, abort
from app.models import *
from app import *
import uuid
import datetime
from marshmallow import Schema, fields
from flask_restful import Resource, Api
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import json


#  Restful way of creating APIs through Flask Restful
class SignUpAPI(MethodResource, Resource, Schema):
    @app.route('/set.name', methods=['GET', 'POST'])
    def SignUpAPI(self):
        username = request.json.get('username')
        password = request.json.get('password')
        models.db.level = request.json.get('level')
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': user.username})


api.add_resource(SignUpAPI, '/signup')
docs.register(SignUpAPI)


class LoginAPI(MethodResource, Resource):
    @auth.route('/login', methods=['GET', 'POST'])
    def LoginAPI(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))


api.add_resource(LoginAPI, '/login')
docs.register(LoginAPI)


class LogoutAPI(MethodResource, Resource):
    @app.route('/logout')
    def logout():
        session.pop('login', None)
        return 'logged out successfully'


api.add_resource(LogoutAPI, '/logout')
docs.register(LogoutAPI)


class AddVendorAPI(MethodResource, Resource):
    @app.route('/add_vendor', methods=['Get', 'Post'])
    def add_vendor(self):
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))


api.add_resource(AddVendorAPI, '/add_vendor')
docs.register(AddVendorAPI)


class GetVendorsAPI(MethodResource, Resource):
    @app.route('/list_vendors')
    def list_vendors(self,Vendors):
        Vendors = Vendors
        Vendors = Vendors.query.all()


api.add_resource(GetVendorsAPI, '/list_vendors')
docs.register(GetVendorsAPI)


class AddItemAPI(MethodResource, Resource):
    @app.route('/item_name', methods=['GET', 'POST'])
    def item_name(self):
        item_name = request.json.get('item_name')
        return jsonify({'item_name': item_name})

    db.session.add(item_name)
    db.session.commit()


api.add_resource(AddItemAPI, '/add_item')
docs.register(AddItemAPI)


class ListItemsAPI(MethodResource, Resource):
    @app.route('/list_items')
    def list_items():
        item_name = item_name.query.all()


api.add_resource(ListItemsAPI, '/list_items')
docs.register(ListItemsAPI)


class CreateItemOrderAPI(MethodResource, Resource):
    @app.route('/create_items_order', methods=['GET', 'POST'])
    def ItemOrder():
        if request.method == "POST":
            purchased_item = request.form.get('purchased_item')
            item_name = item_name.query.filter_by(name=item_name).first()
        if request.method == "GET":
            item_name = item_name.query.filter_by(item_name=None)


api.add_resource(CreateItemOrderAPI, '/create_items_order')
docs.register(CreateItemOrderAPI)


class PlaceOrderAPI(MethodResource, Resource):
    @app.route('/place_order', methods=['GET', 'POST'])
    def place_order():
        if request.method == "POST":
            purchased_item = request.form.get('purchased_item')
            item_name = item_name.query.filter_by(name=item_name).first()

        if request.method == "GET":
            item_name = item_name.query.filter_by(item_name=None)


api.add_resource(PlaceOrderAPI, '/place_order')
docs.register(PlaceOrderAPI)


class ListOrdersByCustomerAPI(MethodResource, Resource):
    @app.route('/list_orders')
    def list_orders():
        list_orders = list_orders.query.all()


api.add_resource(ListOrdersByCustomerAPI, '/list_orders')
docs.register(ListOrdersByCustomerAPI)


class ListAllOrdersAPI(MethodResource, Resource):
    p@app.route('/list_orders')
    def list_orders():
        list_orders = list_orders.query.all()


api.add_resource(ListAllOrdersAPI, '/list_all_orders')
docs.register(ListAllOrdersAPI)
