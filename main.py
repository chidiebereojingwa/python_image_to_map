
import folium
from PIL import Image
from io import BytesIO
import base64

def create_map_with_overlay_images(image_paths, map_center=(0, 0), zoom_start=12, output_map_path="map.html"):
    # Create a Folium map centered at the specified location
    map_object = folium.Map(location=map_center, zoom_start=zoom_start)

    for image_path in image_paths:
        # Load the image using Pillow
        image = Image.open(image_path)

        # Convert the image to a data URL format
        data_url = BytesIO()
        image.save(data_url, format='png')
        data_url = 'data:image/png;base64,' + base64.b64encode(data_url.getvalue()).decode()

        # Add the image as an overlay to the map
        folium.raster_layers.ImageOverlay(
            image=data_url,
            bounds=[[map_center[0] - 0.001, map_center[1] - 0.001], [map_center[0] + 0.001, map_center[1] + 0.001]],
            opacity=1,
            interactive=True,
            cross_origin=False,
            zindex=1
        ).add_to(map_object)

    # Save the map to an HTML file
    map_object.save(output_map_path)

if __name__ == "__main__":
    image_paths = ["DJI_0177.JPG", "image2.jpg", "image3.jpg"]  # Replace with the actual paths to your images
    latitude = 46.778642
    longitude = -92.431184
    map_center = (latitude, longitude)  # Replace with the latitude and longitude of the map center
    zoom_start = 12  # Initial zoom level of the map
    output_map_path = "map.html"  # Replace with the desired output path for the map

    create_map_with_overlay_images(image_paths, map_center, zoom_start, output_map_path)
