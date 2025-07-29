from scene_loader import Scene
import numpy as np

if __name__ == "__main__":

    width, height = 400, 400
    canvas = np.ones((height, width, 3), dtype=np.uint8) * 255  # white canvas
    scene = Scene("step3_example.xml")
    #scene = Scene("step4_example.json")
    scene.load_from_file()
    scene.render(canvas)
    Scene.show_scene(canvas)
