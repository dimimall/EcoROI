import openeo
import numpy as np
import matplotlib.pyplot as plt
import rasterio

# Step 1: Connect to openEO backend and authenticate
connection = openeo.connect("https://openeo.dataspace.copernicus.eu")
connection.authenticate_oidc()

# Step 2: Define the bounding box for Rhodes Island (in WGS84 coordinates)
bbox = {
    "west": 28.210,  # Longitude for the western part of Rhodes
    "south": 36.425,  # Latitude for the southern part of Rhodes
    "east": 28.250,  # Longitude for the eastern part of Rhodes
    "north": 36.465   # Latitude for the northern part of Rhodes
}

# Step 3: Define the time range for winter
time_range = ["2023-12-01", "2024-02-28"]

# Step 4: Load Sentinel-3 LST (Land Surface Temperature) collection for the winter period
datacube = connection.load_collection(
    "SENTINEL3_SLSTR_L2_LST",  # Land Surface Temperature collection
    spatial_extent=bbox,
    temporal_extent=time_range,
    bands=["LST"]  # Use the LST band for Land Surface Temperature
)

# Step 5: Reduce the datacube by taking the average temperature over time (for the winter period)
mean_temperature_winter = datacube.mean_time()

# Step 6: Download the result as a GeoTIFF file
output_filename = "winter_temperature.tif"
mean_temperature_winter.download(outputfile=output_filename)

# Step 7: Load and process the actual temperature data from the downloaded GeoTIFF file
with rasterio.open(output_filename) as dataset:
    temperature_data = dataset.read(1)  # Read the first band (temperature in Kelvin)
    actual_temperature_celsius = temperature_data - 273.15  # Convert from Kelvin to Celsius

# Step 8: Calculate the average actual temperature for the winter period
average_actual_temperature = np.nanmean(actual_temperature_celsius)
print(f"Average Actual Winter Temperature: {average_actual_temperature:.2f} °C")

# Step 9: Define the target temperature for winter (-2°C)
target_temperature = -2.0  # Target temperature in Celsius

# Step 10: Visualize the comparison between actual and targeted temperature
fig, ax = plt.subplots()

# Plot actual temperature
ax.bar(["Actual Winter Temperature"], [average_actual_temperature], color="blue", label="Actual Temperature")

# Plot target temperature
ax.bar(["Targeted Winter Temperature"], [target_temperature], color="red", label="Target Temperature")

# Set graph title and labels
ax.set_title("Comparison Between Targeted and Actual Winter Temperature")
ax.set_ylabel("Temperature (°C)")

# Add a legend
ax.legend()

# Show the plot
plt.show()
