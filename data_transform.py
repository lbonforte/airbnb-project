import csv
import ast
import pandas as pd
import pyodbc
import sqlalchemy


class Airbnb:

    def __init__(self, listing_file, review_file, server_info):
        self.server = server_info['server']
        self.database = server_info['database']
        self.username = server_info['username']
        self.password = server_info['password']
        self.listings_data = []
        self.reviews_data = []
        data = open(listing_file, encoding='utf-8')
        listing = csv.reader(data, delimiter=",")
        for line in listing:
            self.listings_data.append(line)
        data2 = open(review_file, encoding='utf-8')
        reviews = csv.reader(data2, delimiter=',')
        for line in reviews:
            self.reviews_data.append(line)
        self.transform_amenity()
        self.transform_locations()
        self.transform_reviewers()
        self.transform_hosts()
        self.transform_reviews()
        self.transform_listings()

    def transform_amenity(self):
        print('Creating Amenity Table')
        amenity_data = []
        amenity_index = self.listings_data[0].index('amenities')
        for listing in self.listings_data[1:]:
            amenity_data.append(listing[amenity_index])
        self.amenities_df = self._pull_table('Amenities')
        self.amenities_df = self.amenities_df.set_index('Amenity_ID')
        amenities = []
        for amenity_list in amenity_data:
            amenity_list = ast.literal_eval(amenity_list)
            for amenity in amenity_list:
                if amenity not in self.amenities_df.Amenity_name:
                    if amenity not in amenities:
                        amenities.append(amenity)

        amenities_df = pd.DataFrame(data={'Amenity_name': amenities})
        amenities_df.index.name = 'Amenity_ID'
        self.amenities_df = self.amenities_df.append(amenities_df, ignore_index=True)
        self.amenities_df.index.name = 'Amenity_ID'
        self._push_amenities()

    def _pull_table(self, table_name):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = cnxn.cursor()
        sql = 'SELECT * FROM Amenities;'
        data = pd.read_sql(sql, cnxn)
        cursor.close()
        return data

    def _push_amenities(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = cnxn.cursor()
        self.amenities_df.to_sql('tester', con=cnxn, if_exists='append', chunksize=1000)

    def transform_locations(self):
        print('Creating Locations Table')
        locations_data = []
        neighbourhood_index = self.listings_data[0].index('neighbourhood')
        area_index = self.listings_data[0].index('neighbourhood_cleansed')

        for listing in self.listings_data[1:]:
            data = [listing[neighbourhood_index], listing[area_index]]
            if data not in locations_data:
                locations_data.append(data)

        n = []
        a = []
        i = []
        for ind in range(len(locations_data)):
            i.append(ind)
            n.append(locations_data[ind][0])
            a.append(locations_data[ind][1])
        self.listing_location_ids = []
        for i in range(len(n)):
            self.listing_location_ids.append([n[i], a[i]])
        self.locations_df = pd.DataFrame({'Location_ID': i, 'neighbourhood': n, 'Area': a})

    def transform_reviewers(self):
        print('Creating Reviewers Table')
        reviewers_data = []
        reviewer_ID_index = self.reviews_data[0].index('reviewer_id')
        name_index = self.reviews_data[0].index('reviewer_name')
        count = 0
        for review in self.reviews_data[1:50000]:
            data = [review[reviewer_ID_index], review[name_index]]
            if data not in reviewers_data:
                reviewers_data.append(data)
            count += 1
        self.reviewers_df = pd.DataFrame(reviewers_data)

    def transform_hosts(self):
        print('Creating Hosts Table')
        hosts_data = []
        host_id_index = self.listings_data[0].index('host_id')
        host_name = self.listings_data[0].index('host_name')
        host_since = self.listings_data[0].index('host_since')
        host_response_time = self.listings_data[0].index('host_response_time')
        host_acceptance_rate = self.listings_data[0].index('host_acceptance_rate')
        host_is_superhost = self.listings_data[0].index('host_is_superhost')
        host_listings_count = self.listings_data[0].index('host_listings_count')
        for listing in self.listings_data[1:]:
            data = [listing[host_id_index], listing[host_name], listing[host_since], listing[host_response_time],
                    listing[host_acceptance_rate], listing[host_is_superhost], listing[host_listings_count]]
            if data not in hosts_data:
                hosts_data.append(data)
        self.hosts_df = pd.DataFrame({'Host_ID': hosts_data[0], 'Host_Name': hosts_data[1],
                                      'Host_Since': hosts_data[2],'Host_Location': hosts_data[3],
                                      'Host_Response_time': hosts_data[4],'Host_Acceptance_Rate': hosts_data[5],
                                      'Host_Is_Superhost': hosts_data[6],'Host_Listings_Count': hosts_data[7],
                                      })
        self.hosts_df = pd.DataFrame(hosts_data)

    def transform_reviews(self):
        print('Creating Reviews Table')
        reviews_data = []
        review_id_index = self.reviews_data[0].index('id')
        reviewer_id_index = self.reviews_data[0].index('reviewer_id')
        comments_index = self.reviews_data[0].index('comments')
        listing_id_index = self.reviews_data[0].index('listing_id')
        for review in self.reviews_data[1:50000]:
            data = [review[review_id_index], review[reviewer_id_index], review[comments_index], review[listing_id_index]]
            reviews_data.append(data)

        self.hosts_df = pd.DataFrame(reviews_data)

    def transform_listings(self):
        print('Creating Listings Table')
        listings_data = []
        Listing_ID = self.listings_data[0].index('id')
        Host_ID = self.listings_data[0].index('host_id')
        neighbourhood = self.listings_data[0].index('neighbourhood')
        neighbourhood_cleansed = self.listings_data[0].index('neighbourhood_cleansed')
        Last_Scraped = self.listings_data[0].index('last_scraped')
        Name = self.listings_data[0].index('name')
        Description = self.listings_data[0].index('description')
        Latitude = self.listings_data[0].index('latitude')
        Longitude = self.listings_data[0].index('longitude')
        Price = self.listings_data[0].index('price')
        Property_Type = self.listings_data[0].index('property_type')
        Room_Type = self.listings_data[0].index('room_type')
        Accommodates = self.listings_data[0].index('accommodates')
        Bedrooms = self.listings_data[0].index('bedrooms')
        Bathrooms = self.listings_data[0].index('bathrooms')
        Availability_30 = self.listings_data[0].index('availability_30')
        Availability_60 = self.listings_data[0].index('availability_60')
        Availability_90 = self.listings_data[0].index('availability_90')
        Availability_365 = self.listings_data[0].index('availability_365')
        Minimum_Nights = self.listings_data[0].index('minimum_nights')
        Maximum_Nights = self.listings_data[0].index('maximum_nights')
        for listing in self.listings_data[1:]:
            location = [listing[neighbourhood], listing[neighbourhood_cleansed]]
            location_index = self.listing_location_ids.index(location)
            data = [listing[Listing_ID], listing[Host_ID], listing[Last_Scraped],
                    listing[Name] ,listing[Description], listing[Latitude],
                    listing[Longitude],listing[Description], listing[Latitude],listing[Longitude],
                    listing[Price], listing[Property_Type], listing[Room_Type],
                    listing[Accommodates], listing[Bedrooms], listing[Bathrooms],
                    listing[Availability_30], listing[Availability_60], listing[Availability_90],
                    listing[Availability_365], listing[Minimum_Nights], listing[Maximum_Nights]]
            listings_data.append(data)
        self.listings_df = pd.DataFrame(listings_data)
