import pandas as pd
import matplotlib.pyplot as plt

# File paths
csv_path = "GrowLocations.csv"
map_path = "map7.png"
output_image_path = "Outputmap.png"

#StepLoad the dataset
df = pd.read_csv(csv_path)

#Rename the Latitude and Longitude columns
df = df.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})

#Filter invalid latitude and longitude values (outside UK bounds)
min_lat, max_lat = 50.681, 57.985
min_lon, max_lon = -10.592, 1.6848

df = df[(df['Latitude'] >= min_lat) & (df['Latitude'] <= max_lat) &
        (df['Longitude'] >= min_lon) & (df['Longitude'] <= max_lon)]

#Load the map image and plot the data
uk_map = plt.imread(map_path)

fig, ax = plt.subplots(figsize=(12, 12))
ax.imshow(uk_map, extent=[min_lon, max_lon, min_lat, max_lat], aspect='auto')

# Plot the sensor locations
ax.scatter(df['Longitude'], df['Latitude'], color='blue', s=20, label='GROW Sensor Locations')

# Add title, labels, and legend
plt.title("Plotting GROW Sensors on UK map")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()

# Save the plot and display it
plt.savefig(output_image_path, dpi=300, bbox_inches='tight')
plt.show()
