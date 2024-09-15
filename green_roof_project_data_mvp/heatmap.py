import rasterio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from rasterio.warp import reproject, Resampling

# Load the satellite image (Sentinel-2 image of Rhodes)
with rasterio.open("sentinel2_rhodes_summer_2023.tif") as sat_dataset:
    satellite_image = sat_dataset.read([1, 2, 3])  # Reading RGB bands (True color)
    satellite_transform = sat_dataset.transform  # Get the transform for spatial alignment
    satellite_crs = sat_dataset.crs  # Get the coordinate reference system
    satellite_extent = sat_dataset.bounds  # Get the geographic bounds

# Load the temperature data (Sentinel-3 LST for Rhodes)
with rasterio.open("LST_2023_Winter.tif") as temp_dataset:
    temperature_data = temp_dataset.read(1)  # Read the first band (temperature in Kelvin)
    temperature_transform = temp_dataset.transform  # Get the transform for spatial alignment
    temperature_crs = temp_dataset.crs  # Get the coordinate reference system

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = np.where(temperature_data <= 0, np.nan, temperature_data - 273.15)

# Debugging: Print temperature data value range in Celsius
print(f"Temperature data value range (Celsius): {np.nanmin(temperature_celsius)}, {np.nanmax(temperature_celsius)}")

# Reproject temperature data to match the CRS and resolution of the Sentinel-2 image
reprojected_temp = np.empty(satellite_image.shape[1:], dtype=np.float32)

# Perform the reprojection if needed
if satellite_crs != temperature_crs:
    reproject(
        source=temperature_celsius,
        destination=reprojected_temp,
        src_transform=temperature_transform,
        src_crs=temperature_crs,
        dst_transform=satellite_transform,
        dst_crs=satellite_crs,
        resampling=Resampling.bilinear
    )
else:
    reprojected_temp = temperature_celsius  # No reprojection needed

# Debugging: Check if reprojected temperature data is within a reasonable range
print(f"Reprojected temperature value range (Celsius): {np.nanmin(reprojected_temp)}, {np.nanmax(reprojected_temp)}")

# Normalize the satellite RGB bands to [0, 1] for better visualization
def normalize(array):
    array_min, array_max = array.min(), array.max()
    return (array - array_min) / (array_max - array_min)

# Normalize each RGB band of the satellite image
red = normalize(satellite_image[0])  # Band 04 (Red)
green = normalize(satellite_image[1])  # Band 03 (Green)
blue = normalize(satellite_image[2])  # Band 02 (Blue)

# Stack the bands back into an RGB image
true_color_image = np.dstack((red, green, blue))

# Plot the true-color satellite image
fig, ax = plt.subplots(figsize=(12, 10))
ax.imshow(true_color_image)  # Display satellite image (RGB)
plt.title("True-Color Satellite Image of Rhodes")

# Ensure the temperature data is aligned with the satellite image
extent = [satellite_extent.left, satellite_extent.right, satellite_extent.bottom, satellite_extent.top]  # Match satellite bounds

# Adjust the color scale (vmin and vmax) for better contrast of temperature data
vmin, vmax = np.nanpercentile(reprojected_temp, [2, 98])  # Focus on the 2nd to 98th percentile of the data

# Overlay the reprojected temperature heatmap (in Celsius) with higher opacity to make it visible
norm = Normalize(vmin=vmin, vmax=vmax)
heatmap = ax.imshow(reprojected_temp, cmap='coolwarm', norm=norm, alpha=0.8, extent=extent)  # Set alpha to 0.8 for visibility

# Add colorbar for the heatmap
cbar = plt.colorbar(heatmap, ax=ax, orientation="vertical", fraction=0.02, pad=0.04)
cbar.set_label('Temperature (°C)')

# Set title and labels
plt.title("True-Color Satellite Image of Rhodes with LST Overlay (Winter 2023 in Celsius)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Show the plot
plt.show()
