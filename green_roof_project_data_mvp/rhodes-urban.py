import openeo
import os

# Step 1: Connect to the openEO backend of Copernicus Data Space
connection = openeo.connect("https://openeo.dataspace.copernicus.eu")

# Step 2: Authenticate via OpenID Connect
connection.authenticate_oidc()

# Step 3: Define input parameters for the urban area of Rhodes (approximate bounding box for the city of Rhodes)
urban_bbox = {
    "west": 28.210,   # Approximate longitude for the western part of Rhodes city
    "south": 36.425,  # Approximate latitude for the southern part of Rhodes city
    "east": 28.250,   # Approximate longitude for the eastern part of Rhodes city
    "north": 36.465   # Approximate latitude for the northern part of Rhodes city
}

# Step 4: Load Land Surface Temperature (LST) data from Sentinel-3 SLSTR for the year 2023
datacube = connection.load_collection(
    "SENTINEL3_SLSTR_L2_LST",  # Correct collection for Land Surface Temperature (LST)
    spatial_extent=urban_bbox,
    temporal_extent=["2023-01-01", "2023-12-31"],  # Entire years of 2022,2023 and 2024 end of Ausgust to ensure data availability
    bands=["LST"]  # LST band for Land Surface Temperature
)

# Print datacube information to check if data is loaded correctly
print("Datacube info:", datacube)

# Step 5: Reduce the datacube over time to get the average LST for the time period
mean_temperature = datacube.mean_time()

# Print information about the mean temperature cube
print("Mean temperature datacube:", mean_temperature)

# Step 6: Define the output file path in the current working directory
current_directory = os.getcwd()
output_file_path = os.path.join(current_directory, "Rhodes_Urban_LST.tif")

# Step 7: Execute the process and save the result as a GeoTIFF file in the working directory
job = mean_temperature.execute_batch(outputformat="GTiff", outputfile=output_file_path)

# Step 8: Describe the job to check its status
job_info = job.describe_job()
print(f"Job Information: {job_info}")

# Print the file path for confirmation
print(f"Land Surface Temperature data for Rhodes city has been saved to: {output_file_path}")
