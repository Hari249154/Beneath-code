# player_movement.py — 3D Character Movement (Game Animation)

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

class Player:
    def __init__(self, name):
        self.name = name
        self.position = Vector3(0, 0, 0)
        self.speed = 5.0
        self.is_jumping = False
        self.animation_state = "idle"

    def move(self, direction):
        if direction == "forward":
            self.position.z += self.speed
        elif direction == "backward":
            self.position.z -= self.speed
        elif direction == "left":
            self.position.x -= self.speed
        elif direction == "right":
            self.position.x += self.speed
        self.animation_state = "walking"
        print(f"{self.name} moved {direction} → {self.position}")

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.position.y += 10
            self.animation_state = "jumping"
            print(f"{self.name} jumped! Height: {self.position.y}")
        else:
            print(f"{self.name} is already in the air!")

    def land(self):
        self.position.y = 0
        self.is_jumping = False
        self.animation_state = "idle"
        print(f"{self.name} landed. Back to ground.")

# — Demo —
hero = Player("Hero")
hero.move("forward")
hero.move("right")
hero.jump()
hero.land()
hero.move("left")
print("THIS IS A REAL CHANGE")