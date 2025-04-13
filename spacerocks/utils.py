from pygame.image import load
# so this file created to keep all reusable methods!


def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

# load method = reads images
# with_alpha convert // simple convert =
        # convert the image to a format that better fits the screen to speed up the drawing process.
