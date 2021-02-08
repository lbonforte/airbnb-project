import pyodbc
import unittest

server = ''
database = 'Airbnb'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class ListingsTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Listings', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                          SELECT COLUMN_NAME
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Listings';
                                          """).fetchall()
        self.assertIn('Listings_ID'and 'Host_ID' and 'Location_ID' and 'Last_Scraped' and 'Name' and 'Description' and
                      'Latitude' and 'Longitude' and 'Price' and 'Property_Type' and 'Room_Type' and 'Accommodates' and
                      'Bedrooms' and 'Bathrooms' and 'Availability_30' and 'Availability_60' and 'Availability_90' and
                      'Availability_365', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        listing_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Listing_ID';
                                              """).fetchone()

        host_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Host_ID';
                                              """).fetchone()

        location_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Location_ID';
                                              """).fetchone()

        last_scraped_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Last_Scraped';
                                              """).fetchone()

        name_data_type = cursor.execute("""
                                          SELECT DATA_TYPE
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Name';
                                          """).fetchone()

        description_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Description';
                                              """).fetchone()

        latitude_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Latitude';
                                              """).fetchone()

        longitude_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Longitude';
                                              """).fetchone()

        price_data_type = cursor.execute("""
                                          SELECT DATA_TYPE
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Price';
                                          """).fetchone()

        property_type_data_type = cursor.execute("""
                                                  SELECT DATA_TYPE
                                                  FROM INFORMATION_SCHEMA.COLUMNS
                                                  WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Property_Type';
                                                  """).fetchone()

        room_type_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Room_Type';
                                              """).fetchone()

        accomodates_data_type = cursor.execute("""
                                                  SELECT DATA_TYPE
                                                  FROM INFORMATION_SCHEMA.COLUMNS
                                                  WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Accommodates';
                                                  """).fetchone()

        bedrooms_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Bedrooms';
                                              """).fetchone()

        bathrooms_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Bathrooms';
                                              """).fetchone()

        availability_30_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Availability_30';
                                                      """).fetchone()

        availability_60_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Availability_60';
                                                      """).fetchone()

        availability_90_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'availability_90';
                                                      """).fetchone()

        availability_365_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Availability_365';
                                                      """).fetchone()

        self.assertEqual(listing_id_data_type[0], 'int')
        self.assertEqual(host_id_data_type[0], 'int')
        self.assertEqual(location_id_data_type[0], 'int')
        self.assertEqual(last_scraped_data_type[0], 'date')
        self.assertEqual(name_data_type[0], 'varchar')
        self.assertEqual(description_data_type[0], 'varchar')
        self.assertEqual(latitude_data_type[0], 'float')
        self.assertEqual(longitude_data_type[0], 'float')
        self.assertEqual(price_data_type[0], 'money')
        self.assertEqual(property_type_data_type[0], 'varchar')
        self.assertEqual(room_type_data_type[0], 'varchar')
        self.assertEqual(accomodates_data_type[0], 'int')
        self.assertEqual(bedrooms_data_type[0], 'int')
        self.assertEqual(bathrooms_data_type[0], 'varchar')
        self.assertEqual(availability_30_data_type[0], 'int')
        self.assertEqual(availability_60_data_type[0], 'int')
        self.assertEqual(availability_90_data_type[0], 'int')
        self.assertEqual(availability_365_data_type[0], 'int')

    def test_listing_id_is_primary_key(self):
        listing_id_pk = cursor.execute("""
                                      SELECT tc.CONSTRAINT_TYPE
                                      FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                      INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                      WHERE tc.TABLE_NAME = 'Listings' AND kcu.COLUMN_NAME = 'Listing_ID';
                                      """).fetchone()
        self.assertEqual(listing_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                      SELECT IS_NULLABLE
                                      FROM INFORMATION_SCHEMA.COLUMNS
                                      WHERE TABLE_NAME = 'Listings' AND COLUMN_NAME = 'Listing_ID'
                                      """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Listing_ID)
                                    FROM Listings
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Listing_ID))
                                    FROM Listings
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])

    def test_host_id_is_foreign_key(self):
        host_id_pk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Listings' AND kcu.COLUMN_NAME = 'Host_ID';
                                    """).fetchone()
        self.assertEqual(host_id_pk[0], 'FOREIGN KEY')

    def test_location_id_is_foreign_key(self):
        location_id_fk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Listings' AND kcu.COLUMN_NAME = 'Location_ID';
                                    """).fetchone()
        self.assertEqual(location_id_fk[0], 'FOREIGN KEY')

    def test_host_id_fk_primary_table(self):
        fk_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Host_ID' AND tab.name = 'Listings'
                                            """).fetchone()
        self.assertEqual(fk_primary_table[0], 'Hosts')

    def test_location_id_fk_primary_table(self):
        fk_id_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Location_ID' AND tab.name = 'Listings'
                                            """).fetchone()
        self.assertEqual(fk_id_primary_table[0], 'Locations')


class AmenitiesTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Amenities', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                        SELECT COLUMN_NAME
                                        FROM INFORMATION_SCHEMA.COLUMNS
                                        WHERE TABLE_NAME = 'Amenities';
                                        """).fetchall()
        self.assertIn('Amenity_ID' and 'Amenity_name', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        amenity_id_data_type = cursor.execute("""
                                            SELECT DATA_TYPE
                                            FROM INFORMATION_SCHEMA.COLUMNS
                                            WHERE TABLE_NAME = 'Amenities' AND COLUMN_NAME = 'Amenity_ID';
                                            """).fetchone()

        amenity_name_data_type = cursor.execute("""
                                            SELECT DATA_TYPE
                                            FROM INFORMATION_SCHEMA.COLUMNS
                                            WHERE TABLE_NAME = 'Amenities' AND COLUMN_NAME = 'Amenity_name';
                                            """).fetchone()

        self.assertEqual(amenity_id_data_type[0], 'int')
        self.assertEqual(amenity_name_data_type[0], 'varchar')

    def test_amenity_id_is_primary_key(self):
        amenity_id_pk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Amenities' AND kcu.COLUMN_NAME = 'Amenity_ID';
                                    """).fetchone()
        self.assertEqual(amenity_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                    SELECT IS_NULLABLE
                                    FROM INFORMATION_SCHEMA.COLUMNS
                                    WHERE TABLE_NAME = 'Amenities' AND COLUMN_NAME = 'Amenity_ID'
                                    """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Amenity_ID)
                                    FROM Amenities
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Amenity_ID))
                                    FROM Amenities
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])


class ListingAmenitiesTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Listing_Amenities', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                        SELECT COLUMN_NAME
                                        FROM INFORMATION_SCHEMA.COLUMNS
                                        WHERE TABLE_NAME = 'Listing_Amenities';
                                        """).fetchall()
        self.assertIn('Listing_ID' and 'Amenity_ID', [tuple[0] for tuple in column_names])


    def test_column_data_types(self):
        listing_id_data_type = cursor.execute("""
                                            SELECT DATA_TYPE
                                            FROM INFORMATION_SCHEMA.COLUMNS
                                            WHERE TABLE_NAME = 'Listing_Amenities' AND COLUMN_NAME = 'Listing_ID';
                                            """).fetchone()

        amenity_id_data_type = cursor.execute("""
                                            SELECT DATA_TYPE
                                            FROM INFORMATION_SCHEMA.COLUMNS
                                            WHERE TABLE_NAME = 'Listing_Amenities' AND COLUMN_NAME = 'Amenity_ID';
                                            """).fetchone()

        self.assertEqual(listing_id_data_type[0], 'int')
        self.assertEqual(amenity_id_data_type[0], 'int')

    def test_listing_id_is_foreign_key(self):
        listing_id_pk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Listing_Amenities' AND kcu.COLUMN_NAME = 'Listing_ID';
                                    """).fetchone()
        self.assertEqual(listing_id_pk[0], 'FOREIGN KEY')


    def test_amenity_id_is_foreign_key(self):
        amenity_id_fk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Listing_Amenities' AND kcu.COLUMN_NAME = 'Amenity_ID';
                                    """).fetchone()
        self.assertEqual(amenity_id_fk[0], 'FOREIGN KEY')

    def test_listing_id_fk_primary_table(self):
        fk_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Listing_ID' AND tab.name = 'Listing_Amenities'
                                            """).fetchone()
        self.assertEqual(fk_primary_table[0], 'Listings')

    def test_amenity_id_fk_primary_table(self):
        fk_id_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Amenity_ID' AND tab.name = 'Listing_Amenities'
                                            """).fetchone()
        self.assertEqual(fk_id_primary_table[0], 'Amenities')


class HostsTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Hosts', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                          SELECT COLUMN_NAME
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Hosts';
                                          """).fetchall()
        self.assertIn('Host_ID'and 'Host_Name' and 'Host_Since' and 'Host_Location' and 'Host_Response_Time' and
                      'Host_Response_Rate' and 'Host_Acceptance_Rate' and 'Host_Is_Superhost' and 'Host_Listings_Count'
                      and 'Host_Total_Listings_Count', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        host_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_ID';
                                              """).fetchone()

        host_name_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Name';
                                              """).fetchone()

        host_since_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Since';
                                              """).fetchone()

        host_location_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Location';
                                              """).fetchone()

        host_response_time_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Response_Time';
                                                      """).fetchone()

        host_response_rate_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Response_Rate';
                                                      """).fetchone()

        host_acceptance_rate_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Acceptance_Rate';
                                                      """).fetchone()

        host_is_superhost_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Is_Superhost';
                                                      """).fetchone()

        host_listings_count_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Listings_Count';
                                                      """).fetchone()

        host_total_listings_count_data_type = cursor.execute("""
                                                      SELECT DATA_TYPE
                                                      FROM INFORMATION_SCHEMA.COLUMNS
                                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_Total_Listings_Count';
                                                      """).fetchone()

        self.assertEqual(host_id_data_type[0], 'int')
        self.assertEqual(host_name_data_type[0], 'varchar')
        self.assertEqual(host_since_data_type[0], 'date')
        self.assertEqual(host_location_data_type[0], 'varchar')
        self.assertEqual(host_response_time_data_type[0], 'varchar')
        self.assertEqual(host_response_rate_data_type[0], 'decimal')
        self.assertEqual(host_acceptance_rate_data_type[0], 'decimal')
        self.assertEqual(host_is_superhost_data_type[0], 'varchar')
        self.assertEqual(host_listings_count_data_type[0], 'int')
        self.assertEqual(host_total_listings_count_data_type[0], 'int')


    def test_host_id_is_primary_key(self):
        host_id_pk = cursor.execute("""
                                      SELECT tc.CONSTRAINT_TYPE
                                      FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                      INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                      WHERE tc.TABLE_NAME = 'Hosts' AND kcu.COLUMN_NAME = 'Host_ID';
                                      """).fetchone()
        self.assertEqual(host_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                      SELECT IS_NULLABLE
                                      FROM INFORMATION_SCHEMA.COLUMNS
                                      WHERE TABLE_NAME = 'Hosts' AND COLUMN_NAME = 'Host_ID'
                                      """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Host_ID)
                                    FROM Hosts
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Host_ID))
                                    FROM Hosts
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])


class LocationsTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Locations', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                          SELECT COLUMN_NAME
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Locations';
                                          """).fetchall()
        self.assertIn('Location_ID' and 'neighbourhood' and 'Area', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        location_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Locations' AND COLUMN_NAME = 'Location_ID';
                                              """).fetchone()

        neighbourhood_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Locations' AND COLUMN_NAME = 'neighbourhood';
                                              """).fetchone()

        area_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Locations' AND COLUMN_NAME = 'Area';
                                              """).fetchone()

        self.assertEqual(location_id_data_type[0], 'int')
        self.assertEqual(neighbourhood_data_type[0], 'varchar')
        self.assertEqual(area_data_type[0], 'varchar')

    def test_location_id_is_primary_key(self):
        location_id_pk = cursor.execute("""
                                      SELECT tc.CONSTRAINT_TYPE
                                      FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                      INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                      WHERE tc.TABLE_NAME = 'Locations' AND kcu.COLUMN_NAME = 'Location_ID';
                                      """).fetchone()

        self.assertEqual(location_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                      SELECT IS_NULLABLE
                                      FROM INFORMATION_SCHEMA.COLUMNS
                                      WHERE TABLE_NAME = 'Locations' AND COLUMN_NAME = 'Location_ID'
                                      """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Location_ID)
                                    FROM Locations
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Location_ID))
                                    FROM Locations
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])


class ReviewersTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Reviewers', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                          SELECT COLUMN_NAME
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Reviewers';
                                          """).fetchall()
        self.assertIn('Reviewer_ID' and 'Name', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        reviewer_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviewers' AND COLUMN_NAME = 'Reviewer_ID';
                                              """).fetchone()

        name_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviewers' AND COLUMN_NAME = 'Name';
                                              """).fetchone()
        self.assertEqual(reviewer_id_data_type[0], 'int')
        self.assertEqual(name_data_type[0], 'varchar')


    def test_reviewer_id_is_primary_key(self):
        reviewer_id_pk = cursor.execute("""
                                      SELECT tc.CONSTRAINT_TYPE
                                      FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                      INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                      WHERE tc.TABLE_NAME = 'Reviewers' AND kcu.COLUMN_NAME = 'Reviewer_ID';
                                      """).fetchone()

        self.assertEqual(reviewer_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                      SELECT IS_NULLABLE
                                      FROM INFORMATION_SCHEMA.COLUMNS
                                      WHERE TABLE_NAME = 'Reviewers' AND COLUMN_NAME = 'Reviewer_ID'
                                      """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Reviewer_ID)
                                    FROM Reviewers
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Reviewer_ID))
                                    FROM Reviewers
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])


class ReviewsTableTest(unittest.TestCase):

    def test_table_exists(self):
        tables = cursor.execute("""
                                SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                """).fetchall()
        self.assertIn('Reviews', [tuple[0] for tuple in tables])

    def test_columns_exist(self):
        column_names = cursor.execute("""
                                          SELECT COLUMN_NAME
                                          FROM INFORMATION_SCHEMA.COLUMNS
                                          WHERE TABLE_NAME = 'Reviews';
                                          """).fetchall()
        self.assertIn('Review_ID' and 'Reviewer_ID' and 'Location_ID' and 'Comments', [tuple[0] for tuple in column_names])

    def test_column_data_types(self):
        review_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviews' AND COLUMN_NAME = 'Review_ID';
                                              """).fetchone()

        reviewer_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviews' AND COLUMN_NAME = 'Reviewer_ID';
                                              """).fetchone()

        location_id_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviews' AND COLUMN_NAME = 'Location_ID';
                                              """).fetchone()

        comments_data_type = cursor.execute("""
                                              SELECT DATA_TYPE
                                              FROM INFORMATION_SCHEMA.COLUMNS
                                              WHERE TABLE_NAME = 'Reviews' AND COLUMN_NAME = 'Comments';
                                              """).fetchone()

        self.assertEqual(review_id_data_type[0], 'int')
        self.assertEqual(reviewer_id_data_type[0], 'int')
        self.assertEqual(location_id_data_type[0], 'int')
        self.assertEqual(comments_data_type[0], 'varchar')

    def test_review_id_is_primary_key(self):
        review_id_pk = cursor.execute("""
                                      SELECT tc.CONSTRAINT_TYPE
                                      FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                      INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                      WHERE tc.TABLE_NAME = 'Reviews' AND kcu.COLUMN_NAME = 'Review_ID';
                                      """).fetchone()
        self.assertEqual(review_id_pk[0], 'PRIMARY KEY')

    def test_primary_key_not_null(self):
        pk_is_null = cursor.execute("""
                                      SELECT IS_NULLABLE
                                      FROM INFORMATION_SCHEMA.COLUMNS
                                      WHERE TABLE_NAME = 'Reviews' AND COLUMN_NAME = 'Review_ID'
                                      """).fetchone()
        self.assertEqual(pk_is_null[0], 'NO')

    def test_primary_key_is_unique(self):

        pk_row_count = cursor.execute("""
                                    SELECT COUNT(Review_ID)
                                    FROM Reviews
                                    """).fetchone()

        pk_distinct_values_count = cursor.execute("""
                                    SELECT COUNT(DISTINCT(Review_ID))
                                    FROM Reviews
                                    """).fetchone()

        self.assertEqual(pk_row_count[0], pk_distinct_values_count[0])

    def test_reviewer_id_is_foreign_key(self):
        host_id_pk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Reviews' AND kcu.COLUMN_NAME = 'Reviewer_ID';
                                    """).fetchone()
        self.assertEqual(host_id_pk[0], 'FOREIGN KEY')

    def test_location_id_is_foreign_key(self):
        location_id_fk = cursor.execute("""
                                    SELECT tc.CONSTRAINT_TYPE
                                    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu
                                    INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON kcu.CONSTRAINT_NAME = tc.CONSTRAINT_NAME
                                    WHERE tc.TABLE_NAME = 'Reviews' AND kcu.COLUMN_NAME = 'Location_ID';
                                    """).fetchone()
        self.assertEqual(location_id_fk[0], 'FOREIGN KEY')

    def test_reviewer_id_fk_primary_table(self):
        fk_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Reviewer_ID' AND tab.name = 'Reviews'
                                            """).fetchone()
        self.assertEqual(fk_primary_table[0], 'Reviewers')

    def test_location_id_fk_primary_table(self):
        fk_id_primary_table = cursor.execute("""
                                            SELECT pk_tab.name
                                            FROM sys.tables tab
                                                INNER JOIN sys.columns col
                                                    ON col.object_id = tab.object_id
                                                LEFT OUTER JOIN sys.foreign_key_columns fk_cols
                                                    ON fk_cols.parent_object_id = tab.object_id
                                                    AND fk_cols.parent_column_id = col.column_id
                                                LEFT OUTER JOIN sys.foreign_keys fk
                                                    ON fk.object_id = fk_cols.constraint_object_id
                                                LEFT OUTER JOIN sys.tables pk_tab
                                                    ON pk_tab.object_id = fk_cols.referenced_object_id
                                                LEFT OUTER JOIN sys.columns pk_col
                                                    ON pk_col.column_id = fk_cols.referenced_column_id
                                                    AND pk_col.object_id = fk_cols.referenced_object_id
                                            WHERE col.name = 'Location_ID' AND tab.name = 'Reviews'
                                            """).fetchone()
        self.assertEqual(fk_id_primary_table[0], 'Locations')

