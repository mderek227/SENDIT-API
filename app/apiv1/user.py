"""CONTAINS API ENDPOINTS"""
from flask import jsonify, request
from app.apiv1 import AppBp
from .modals import add_parcel, Parcels
from .errors import bad_request

@AppBp.route('/parcels', methods=['POST'])
def make_a_delivery_order():
    """Create a parcel delivery order"""
    order = request.get_json() or {}
    #check for an empty post and missing keys
    if not order:
        return bad_request("You entered nothing")
    for key in order:
        if len(order) < 5:
            return bad_request("You are missing a required field")

    #check for empty values in post and return missing field
    for key, value in order.items():
        if value == "":
            return bad_request("You are missing {} in your input".format(key))

    #create a delivery order
    add_parcel(order['pick_up'], order['destination'], order['parcel_name'],
               order['price'], order['user_id'])
    return jsonify("Delivery order created"), 201

@AppBp.route('/parcels', methods=['GET'])
def see_all_orders():
    """To view all available delivery orders"""
    if Parcels:
        return jsonify("Available Delivery Orders", Parcels), 200
    return jsonify("You dont have any delivery orders"), 200

@AppBp.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_order_by_id(parcel_id):
    """To view an available delivery order by its id"""
    try:
        if Parcels:
            order = [this_id for this_id in Parcels if this_id['parcel_id'] == parcel_id]
            return jsonify("The delivery order of id {}".format(parcel_id), order[0]), 200
        return jsonify("No delivery order made"), 200
    except IndexError:
        return jsonify("The delivery order of id {} doesnt exist".format(parcel_id)), 200

@AppBp.route('/users/<string:userid>/parcels', methods=['GET'])
def get_all_orders_by_userid(userid):
    """Fetch all delivery orders by user_id"""
    if not Parcels:
        return jsonify("You have not made any delivery orders"), 200
    user = [user for user in Parcels if user['user_id'] == userid]
    if len(user) != 0:
        return jsonify("The delivery order of {}".format(userid), user), 200
    return jsonify("The user {} doesnt have parcels and doesnt exist".format(userid))

@AppBp.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_delivery_order(parcel_id):
    """Cancel a parcel delivery order"""
    try:
        if Parcels:
            cancel = [this_order for this_order in Parcels if this_order['parcel_id'] == parcel_id]
            cancel[0]['status'] = 'Cancel'
            return jsonify('delivery order has been canceled'), 200
        return jsonify('You dont have delivery orders')
    except IndexError:
        return jsonify('Delivery order {} not found'.format(parcel_id)), 200        
