import openeo
import rasterio
import numpy as np
import json


connection = openeo.connect("https://openeo.dataspace.copernicus.eu")
connection.authenticate_oidc()

bbox = {
    "west": 28.210,   # Longitude for the western part of Rhodes city
    "south": 36.425,  # Latitude for the southern part of Rhodes city
    "east": 28.250,   # Longitude for the eastern part of Rhodes city
    "north": 36.465   # Latitude for the northern part of Rhodes city
}

# Define seasons and date ranges
seasonal_data = {
    "Winter": ["2023-01-01", "2023-03-31"],
    "Spring": ["2023-04-01", "2023-06-30"],
    "Summer": ["2023-07-01", "2023-09-30"],
    "Autumn": ["2023-10-01", "2023-12-31"]
}


def fetch_lst_data(year, season_dates, output_filename):
    # Load the collection
    datacube = connection.load_collection(
        "SENTINEL3_SLSTR_L2_LST",  # Land Surface Temperature collection
        spatial_extent=bbox,
        temporal_extent=season_dates,  # Specify the season's date range
        bands=["LST"]  # Fetch the LST band
    )
    
    # Reduce the datacube over time to get the average LST for the season
    mean_temperature = datacube.mean_time()
    
    # Download the GeoTIFF file (use a local path for the output file)
    mean_temperature.download(outputfile=output_filename)
    return output_filename

seasons = ["Winter", "Spring", "Summer", "Autumn"]
years = [2023, 2024]


seasonal_averages = {}


for year in years:
    seasonal_averages[year] = {}
    for season in seasons:
        season_dates = seasonal_data[season]  # Get the date range for the season
        output_file = f"LST_{year}_{season}.tif"  # Define the output file for each season
        fetch_lst_data(year, season_dates, output_file)  # Download the LST GeoTIFF file
        
        # Read the GeoTIFF file to calculate the average temperature
        with rasterio.open(output_file) as dataset:
            band1 = dataset.read(1)  # Read the first band (LST data)
            band1_celsius = np.where(band1 <= 0, np.nan, band1 - 273.15)  # Convert from Kelvin to Celsius
            avg_temp = np.nanmean(band1_celsius)  # Calculate the mean temperature in Celsius
            seasonal_averages[year][season] = avg_temp
            print(f"Mean Temperature for {year} {season}: {avg_temp:.2f} °C")


for year in seasonal_averages:
    for season in seasonal_averages[year]:
        seasonal_averages[year][season] = float(seasonal_averages[year][season])

# Save the data as JSON
output_data = {
    "seasons": seasons,
    "data": seasonal_averages
}

with open("temperature_data.json", "w") as json_file:
    json.dump(output_data, json_file)
