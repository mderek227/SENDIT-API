"""Temporary data store"""

Parcels = []

def add_parcel(pick_up, destination, parcel_name, price, user_id):
    """create a parcel delivery order and update the data store"""
    parcel = {
        'parcel_id' : len(Parcels) + 1,
        'pick_up': pick_up,
        'destination':destination,
        'parcel_name':parcel_name,
        'price':price,
        'user_id':user_id,
        'status':'transit'
        }
    Parcels.append(Parcel)
    return Parcels
        