[![Build Status](https://travis-ci.com/mderek227/SENDIT-API.svg?branch=api)](https://travis-ci.com/mderek227/SENDIT-API)
[![Coverage Status](https://coveralls.io/repos/github/mderek227/SENDIT-API/badge.svg?branch=develop)](https://coveralls.io/github/mderek227/SENDIT-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/c352b1b61ea4b3b4a0ba/maintainability)](https://codeclimate.com/github/mderek227/SENDIT-API/maintainability)
# SendIT API
SendIT courier enables user to deliver parcels to different places. SendIT charges subscribers according to the weight category of the parcel

## Features
- `Create a parcel delivery order` User should be able to create a parcel delivery order
- `Get all parcel delivery orders` User should be able to fetch all delivery orders
- `Get a specific parcel delivery order` User should be able to fetch a delivery order by its id
- `Cancel a parcel delivery order` User should be able to cancel a delivery order by its id 
- `Get all parcel delivers by userid` User should be able to fetch all delivery orders by a userid



## API Endpoints
|  EndPoint  |  Functionality  |
| ------------- | ------------- |
| GET /parcels  | Fetch all parcel delivery orders  |
| GET /parcels/\<parcel_id\>  | Fetch a specific parcel delivery order  |
| GET /users/\<user_id\>/parcels | Fetch all parcel delivery orders by a specific user |
| PUT /parcels/\<parcel_id\>/cancel | Cancel the specific parcel delivery order |
| POST /parcels | Create a parcel delivery order |
  