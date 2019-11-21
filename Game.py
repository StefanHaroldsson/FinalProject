import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_FLY = 0.2
fly = arcade.Sprite("fly.jpg", SPRITE_SCALING_FLY)

SPRITE_SCALING_PLAYER = 0.2
player = arcade.Sprite("pngtree-cute-green-cartoon-frog-png-image_951640.jpg", SPRITE_SCALING_FLY)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("pngtree-cute-green-cartoon-frog-png-image_951640.jpg", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50  # Starting position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the flies
        for i in range(0,100):
            # Create the fly
            # Coin image from kenney.nl
            fly = arcade.Sprite("fly.jpg", SPRITE_SCALING_FLY)

            # Position the coin
            fly.center_x = random.randrange(SCREEN_WIDTH)
            fly.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the flies to the lists
            self.fly_list.append(fly)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.fly_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        # Generate a list of all  flies that collided with the player.
        flies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fly_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for fly in flies_hit_list:
            fly.kill()
            self.score += 1


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()