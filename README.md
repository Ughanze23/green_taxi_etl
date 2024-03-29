# green_taxi_etl

For the homework, we'll be working with the green taxi dataset located here:

https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download

You may need to reference the link below to download via Python in Mage:

https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/

![image](https://github.com/Ughanze23/green_taxi_etl/assets/29339360/499f2f30-9645-4be1-a461-1e93cf89b614)


Below are the steps performed in this simple pipeline
# Actions
The goal will be to construct an ETL pipeline that loads the data, performs some transformations, and writes the data to a database (and Google Cloud!).

* Create a new pipeline, call it green_taxi_etl
  Add a data loader block and use Pandas to read data for the final quarter of 2020 (months 10, 11, 12).
* Add a transformer block and perform the following:
  Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
  Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
  Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
* Add three assertions:
  vendor_id is one of the existing values in the column (currently)
  passenger_count is greater than 0
  trip_distance is greater than 0
*Using a Postgres data exporter (SQL or Python), write the dataset to a table called green_taxi in a schema mage. Replace the table if it already exists.
  Write your data as Parquet files to a bucket in GCP, partioned by lpep_pickup_date. Use the pyarrow library!
  Schedule your pipeline to run daily at 5AM UTC.

