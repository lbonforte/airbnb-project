from table_creation import *
from table_config import *

Locations_table = Table_create('Locations', Locations)

reviewers_table = Table_create('Reviewers', Reviewers)

hosts_table = Table_create('Hosts', Hosts)

reviews_table = Table_create('Reviews', Reviews)

listings_table = Table_create('Listings', Listings)

amenity_table = Table_create('Amenities', Amenities)

list_amen_junction = Table_create('Listing_Amenities', List_amen_junction)
