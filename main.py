from table_creation import *
from table_config import *

Locations_table = TableCreate('Locations', Locations)

reviewers_table = TableCreate('Reviewers', Reviewers)

hosts_table = TableCreate('Hosts', Hosts)

reviews_table = TableCreate('Reviews', Reviews)

listings_table = TableCreate('Listings', Listings)

amenity_table = TableCreate('Amenities', Amenities)

list_amen_junction = TableCreate('Listing_Amenities', List_amen_junction)
