#Q24.  Create a Traffic Light Simulation

class TrafficLight:
    def __init__(self, color="Red"):
        self.color = color
        self.colors = ["Red", "Green", "Yellow"]

    def next_light(self):
        current_index = self.colors.index(self.color)
        next_index = (current_index + 1) % len(self.colors)
        self.color = self.colors[next_index]
        return self.color

# Create a TrafficLight object
light = TrafficLight()

# Change traffic lights
print(light.next_light())  # Green
print(light.next_light())  # Yellow
print(light.next_light())  # Red
