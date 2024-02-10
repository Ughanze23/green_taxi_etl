if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

"""
Add a transformer block and perform the following:
Remove rows where the passenger count is equal to 0 and the trip distance is equal to zero.
Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
Add three assertions:
vendor_id is one of the existing values in the column (currently)
passenger_count is greater than 0
trip_distance is greater than 0 """
@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    data = data[data['passenger_count'] > 0] #exclude trips with no passengers
    data = data[data['trip_distance'] > 0]  #exclude trips with no distance
    data.columns = (data.columns.str.replace(" ","_").str.lower())
    #new column 
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Function to convert CamelCase to snake_case
    def camel_to_snake(name):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

    # Rename the columns
    data.columns = [camel_to_snake(col) for col in data.columns]
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'vendor_id' not in output.columns , "Column is missing from dataframe"

    assert output['passenger_count'].isin([0]).sum() == 0 , 'The output contains rides with 0 passengers'
    assert output['trip_distance'].isin([0]).sum() == 0 , 'The output contains rides with 0 trip_distance'
