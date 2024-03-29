import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.github.com/repos/DataTalksClub/nyc-tlc-data/releases/tags/green'
    response = requests.get(url)

    assets = response.json().get('assets', [])

    # List all files
    download_urls = []
    for asset in assets:
        file_name = asset.get('name')
        download_url = asset.get('browser_download_url')

        year = file_name.split('_')[2][:4]
        month = file_name.split('_')[2][5:7]

        #take only data for the last quarter of 2020
        if year == '2020' and month in ['10', '11','12']:
            download_urls.append(download_url)



    #data field definition of the data
    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float
            }
    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dframes = []
    for url in download_urls:
        df = pd.read_csv(url \
                        , sep=',' \
                        , compression='gzip' \
                        , dtype=taxi_dtypes \
                        , parse_dates=parse_dates)
  
    dframes.append(df)
    
    #merge all the dataframes in the list into 1 massive dataframe
    taxi_df = pd.concat(dframes)

    return taxi_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
