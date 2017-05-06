from random import randint


class Scene(object):
    def enter(self):
        print " This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene_map
        current_scene.enter()


class Death(Scene):
    def enter(self):
        quip = [
            "You died. You are kind of terrible at this.",
            "Your mom would be so proud. Not!",
            "So, so bad.",
            "My five year old dowes better than that!"
        ]

        def enter(self):
            print Death.quips[randint(0, len(self.quips)-1)]
            exit(1)

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
