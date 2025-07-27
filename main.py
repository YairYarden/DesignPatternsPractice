from scene_loader import Scene

if __name__ == "__main__":
    if __name__ == "__main__":
        print('Start')

        scene = Scene()
        scene.load_from_file("step1_example.xml")
        scene.render()

        print('Finish')