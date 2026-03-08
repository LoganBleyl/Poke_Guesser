from PIL import Image
import io
import pygame

def create_silhouette(image_path):
    # Open the image
    image = Image.open(image_path).convert("RGBA")
    
    # Create a new image for the silhouette
    silhouette = Image.new("RGBA", image.size)
    
    # Get the pixel data
    pixels = image.load()
    silhouette_pixels = silhouette.load()
    
    # Create the silhouette by setting non-transparent pixels to black
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y][3] > 30:  # Check if the pixel is not transparent
                silhouette_pixels[x, y] = (0, 0, 0, 255)  # Set to black with full opacity
    
    buffer = io.BytesIO()
    silhouette.save(buffer, format="PNG")
    buffer.seek(0)
    surface = pygame.image.load(buffer)
    return surface.convert_alpha()