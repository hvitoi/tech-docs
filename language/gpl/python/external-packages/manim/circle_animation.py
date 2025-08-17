from manim import *

# This creates a scene for the animation
class GrowingCircle(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)  # Set the color and transparency

        # Display the circle at the center
        self.play(Create(circle))

        # Animate the circle growing in size
        self.play(circle.animate.scale(2))

        # Wait for a moment before ending the scene
        self.wait(1)

# To render this animation, you can run:
# manim -pql circle_animation.py GrowingCircle
