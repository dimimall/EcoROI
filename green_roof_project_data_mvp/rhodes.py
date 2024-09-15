import openeo
import os

# Step 1: Connect to the openEO backend of Copernicus Data Space
connection = openeo.connect("https://openeo.dataspace.copernicus.eu")

# Step 2: Authenticate via OpenID Connect
connection.authenticate_oidc()

# Step 3: Define input parameters for Rhodes Island
bbox = {
    "west": 27.7,   # Longitude of the westernmost point
    "south": 35.8,  # Latitude of the southernmost point
    "east": 28.4,   # Longitude of the easternmost point
    "north": 36.5   # Latitude of the northernmost point
}

# Step 4: Load Land Surface Temperature (LST) data from Sentinel-3 SLSTR
datacube = connection.load_collection(
    "SENTINEL3_SLSTR_L2_LST",  # Correct collection for Land Surface Temperature (LST)
    spatial_extent=bbox,
    temporal_extent=["2023-01-01", "2023-12-31"],  # Select a time period
    bands=["LST"]  # LST band for Land Surface Temperature
)

# Print datacube information to check if data is loaded correctly
print(datacube)

# Step 5: Reduce the datacube over time to get the average LST for the time period
mean_temperature = datacube.mean_time()

# Step 6: Define the output file path in the current working directory
current_directory = os.getcwd()
output_file_path = os.path.join(current_directory, "Rhodes_Island_LST.tif")

# Step 7: Execute the process and save the result as a GeoTIFF file in the working directory
job = mean_temperature.execute_batch(outputformat="GTiff", outputfile=output_file_path)

# Step 8: Describe the job to check its status
job_info = job.describe_job()
print(f"Job Information: {job_info}")

# Print the file path for confirmation
print(f"Land Surface Temperature data has been saved to: {output_file_path}")
