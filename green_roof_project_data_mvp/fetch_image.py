import openeo
import rasterio
import numpy as np
import matplotlib.pyplot as plt

#OpenEO backend for Copernicus Data Space
connection = openeo.connect("https://openeo.dataspace.copernicus.eu")
connection.authenticate_oidc()


bbox = {
    "west": 28.210,  # Longitude for the western part of Rhodes
    "south": 36.425,  # Latitude for the southern part of Rhodes
    "east": 28.250,  # Longitude for the eastern part of Rhodes
    "north": 36.465   # Latitude for the northern part of Rhodes
}

#Date range (e.g., Summer 2023)
time_range = ["2023-07-01", "2023-07-31"]

# Load the Sentinel-2 L2A data collection (True Color RGB bands)
datacube = connection.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=bbox,
    temporal_extent=time_range,
    bands=["B04", "B03", "B02"]  # Red, Green, Blue bands
)

# Reduce by time (mean composite for the time period)
mean_composite = datacube.reduce_dimension(dimension="t", reducer="mean")

# Export the data as a GeoTIFF file
output_file = "sentinel2_rhodes_summer_2023.tif"
mean_composite.download(outputfile=output_file)

# Open the downloaded GeoTIFF
with rasterio.open(output_file) as dataset:
    red = dataset.read(1)  # Band 04 (Red)
    green = dataset.read(2)  # Band 03 (Green)
    blue = dataset.read(3)  # Band 02 (Blue)

# Normalize the bands (to bring them to the range 0-1 for better display)
def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

# Normalize each band
red_norm = normalize(red)
green_norm = normalize(green)
blue_norm = normalize(blue)


rgb_image = np.dstack((red_norm, green_norm, blue_norm))

# Plot
plt.figure(figsize=(10, 10))
plt.imshow(rgb_image)
plt.title('Enhanced True-Color Image of Rhodes (July 2023)')
plt.axis('off')  # Hide the axis for better visualization
plt.show()
