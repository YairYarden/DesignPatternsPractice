from scene_loader import Scene
import numpy as np
import cv2

if __name__ == "__main__":
    if __name__ == "__main__":
        print('Start')

        width, height = 400, 400
        canvas = np.ones((height, width, 3), dtype=np.uint8) * 255  # white canvas

        scene = Scene()
        scene.load_from_file("step1_example.xml")
        scene.render(canvas)
        Scene.show_scene(canvas)

        print('Finish')