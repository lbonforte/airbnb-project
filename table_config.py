import configparser
import ast

config = configparser.ConfigParser()
config.read('Table_config.ini')

Amenities = {}
Amenities['Amenity_ID'] = ast.literal_eval(config['Amenities'].get('Amenity_ID'))
Amenities['Amenity_name'] = ast.literal_eval(config['Amenities'].get('Amenity_name'))

List_amen_junction = {}
List_amen_junction['Listing_ID'] = ast.literal_eval(config['List_amen_junction'].get('Listing_ID'))
List_amen_junction['Amenity_ID'] = ast.literal_eval(config['List_amen_junction'].get('Amenity_ID'))

Locations = {}
Locations['Location_ID'] = ast.literal_eval(config['Locations'].get('Location_ID'))
Locations['neighbourhood'] = ast.literal_eval(config['Locations'].get('neighbourhood'))
Locations['Area'] = ast.literal_eval(config['Locations'].get('Area'))

Reviews = {}
Reviews['Review_ID'] = ast.literal_eval(config['Reviews'].get('Review_ID'))
Reviews['Reviewer_ID'] = ast.literal_eval(config['Reviews'].get('Reviewer_ID'))
Reviews['Location_ID'] = ast.literal_eval(config['Reviews'].get('Location_ID'))
Reviews['Comments'] = ast.literal_eval(config['Reviews'].get('Comments'))

Reviewers = {}
Reviewers['Reviewer_ID'] = ast.literal_eval(config['Reviewers'].get('Reviewer_ID'))
Reviewers['Name'] = ast.literal_eval(config['Reviewers'].get('Name'))

Hosts = {}
Hosts['Host_ID'] = ast.literal_eval(config['Hosts'].get('Host_ID'))
Hosts['Host_Name'] = ast.literal_eval(config['Hosts'].get('Host_Name'))
Hosts['Host_Since'] = ast.literal_eval(config['Hosts'].get('Host_Since'))
Hosts['Host_Location'] = ast.literal_eval(config['Hosts'].get('Host_Location'))
Hosts['Host_Response_Time'] = ast.literal_eval(config['Hosts'].get('Host_Response_Time'))
Hosts['Host_Response_Rate'] = ast.literal_eval(config['Hosts'].get('Host_Response_Rate'))
Hosts['Host_Acceptance_Rate'] = ast.literal_eval(config['Hosts'].get('Host_Acceptance_Rate'))
Hosts['Host_Is_Superhost'] = ast.literal_eval(config['Hosts'].get('Host_Is_Superhost'))
Hosts['Host_Listings_Count'] = ast.literal_eval(config['Hosts'].get('Host_Listings_Count'))
Hosts['Host_Total_Listings_Count'] = ast.literal_eval(config['Hosts'].get('Host_Total_Listings_Count'))

Listings = {}
Listings['Listing_ID'] = ast.literal_eval(config['Listings'].get('Listing_ID'))
Listings['Host_ID'] = ast.literal_eval(config['Listings'].get('Host_ID'))
Listings['Location_ID'] = ast.literal_eval(config['Listings'].get('Location_ID'))
Listings['Last_Scraped'] = ast.literal_eval(config['Listings'].get('Last_Scraped'))
Listings['Name'] = ast.literal_eval(config['Listings'].get('Name'))
Listings['Description'] = ast.literal_eval(config['Listings'].get('Description'))
Listings['Latitude'] = ast.literal_eval(config['Listings'].get('Latitude'))
Listings['Longitude'] = ast.literal_eval(config['Listings'].get('Longitude'))
Listings['Price'] = ast.literal_eval(config['Listings'].get('Price'))
Listings['Property_Type'] = ast.literal_eval(config['Listings'].get('Property_Type'))
Listings['Room_Type'] = ast.literal_eval(config['Listings'].get('Room_Type'))
Listings['Accommodates'] = ast.literal_eval(config['Listings'].get('Accommodates'))
Listings['Bedrooms'] = ast.literal_eval(config['Listings'].get('Bedrooms'))
Listings['Bathrooms'] = ast.literal_eval(config['Listings'].get('Bathrooms'))
Listings['Availability_30'] = ast.literal_eval(config['Listings'].get('Availability_30'))
Listings['Availability_60'] = ast.literal_eval(config['Listings'].get('Availability_60'))
Listings['Availability_90'] = ast.literal_eval(config['Listings'].get('Availability_90'))
Listings['Availability_365'] = ast.literal_eval(config['Listings'].get('Availability_365'))
