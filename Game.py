"""
Final Cisc 108 Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Jumping for Money"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.08
TILE_SCALING = 0.1
COIN_SCALING = 0.25

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 25

LEFT_VIEWPORT_MARGIN = 150
RIGHT_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.bonus_list = None
        self.dont_touch_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        arcade.set_background_color(arcade.csscolor.DARK_MAGENTA)



    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0


        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bonus_list = arcade.SpriteList()
        self.dont_touch_list= arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("images/jumpingman.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 600
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(128, 1250, 256):
            wall = arcade.Sprite("images/start.png",0.1)
            wall.center_x = 600
            wall.center_y = 50
            self.wall_list.append(wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites




        coordinate_list = [[random.randint(0,SCREEN_WIDTH), 500],[random.randint(0,SCREEN_WIDTH), 700],[random.randint(0,SCREEN_WIDTH), 900],[random.randint(0,SCREEN_WIDTH), 1100],[random.randint(0,SCREEN_WIDTH), 1300],[random.randint(0,SCREEN_WIDTH), 1500],[random.randint(0,SCREEN_WIDTH), 1700],[random.randint(0,SCREEN_WIDTH), 1900],[random.randint(0,SCREEN_WIDTH), 2100],[random.randint(0,SCREEN_WIDTH), 2300],[random.randint(0,SCREEN_WIDTH), 2500],[random.randint(0,SCREEN_WIDTH), 2700],[random.randint(0,SCREEN_WIDTH), 2900],[random.randint(0,SCREEN_WIDTH), 3100],[random.randint(0,SCREEN_WIDTH), 3300],[random.randint(0,SCREEN_WIDTH), 3500],[random.randint(0,SCREEN_WIDTH), 3700],[random.randint(0,SCREEN_WIDTH), 3900],[random.randint(0,SCREEN_WIDTH), 4100],[random.randint(0,SCREEN_WIDTH), 4300],[random.randint(0,SCREEN_WIDTH), 4500],[random.randint(0,SCREEN_WIDTH), 4700],[random.randint(0,SCREEN_WIDTH), 4900],[random.randint(0,SCREEN_WIDTH), 3000],[random.randint(0,SCREEN_WIDTH), 5100],[random.randint(0,SCREEN_WIDTH), 5300],[random.randint(0,SCREEN_WIDTH), 5500],[random.randint(0,SCREEN_WIDTH), 5700],[random.randint(0,SCREEN_WIDTH), 5900],[random.randint(0,SCREEN_WIDTH), 6100],[random.randint(0,SCREEN_WIDTH), 6300],[random.randint(0,SCREEN_WIDTH), 6500],[random.randint(0,SCREEN_WIDTH), 6700],[random.randint(0,SCREEN_WIDTH), 6900],[random.randint(0,SCREEN_WIDTH), 7100],[random.randint(0,SCREEN_WIDTH), 7300],[random.randint(0,SCREEN_WIDTH), 7500],[random.randint(0,SCREEN_WIDTH), 7700],[random.randint(0,SCREEN_WIDTH), 7900],[random.randint(0,SCREEN_WIDTH), 8100],[random.randint(0,SCREEN_WIDTH), 8300],[random.randint(0,SCREEN_WIDTH), 8500],[random.randint(0,SCREEN_WIDTH), 8700],[random.randint(0,SCREEN_WIDTH), 8900],[random.randint(0,SCREEN_WIDTH), 9100],[random.randint(0,SCREEN_WIDTH), 9300],[random.randint(0,SCREEN_WIDTH), 9500],[random.randint(0,SCREEN_WIDTH), 9700],[random.randint(0,SCREEN_WIDTH), 9900],[random.randint(0,SCREEN_WIDTH), 10100],[random.randint(0,SCREEN_WIDTH), 10300],[random.randint(0,SCREEN_WIDTH), 10500],[random.randint(0,SCREEN_WIDTH), 10700],[random.randint(0,SCREEN_WIDTH), 10900]]





        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite("images/trampoline.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

            # Use a loop to place some coins for our character to pick up
            for x in range(128, 1250, 256):
                coin = arcade.Sprite("images/Coins.png", COIN_SCALING)
                coin.center_x = random.randint(-200,1400)
                coin.center_y = random.randint(160, 12000)
                self.coin_list.append(coin)

         # pick up some bonuses
        coordinate_bonus_list = [[random.randint(0,SCREEN_HEIGHT),1500], [random.randint(0,SCREEN_HEIGHT),3000], [random.randint(0,SCREEN_HEIGHT),4500]]
        for coordinate in coordinate_bonus_list:

            bonus = arcade.Sprite("images/bonus.png", TILE_SCALING)
            bonus.position = coordinate
            self.bonus_list.append(bonus)

            coordinate_dont_touch_list = [[-1000,-5000],[0,-5000],[1000,-5000],[2000,-5000],[3000,-5000]]
            for coordinate in coordinate_dont_touch_list:
                dont_touch = arcade.Sprite("images/flame.png", 3)
                dont_touch.position = coordinate
                self.dont_touch_list.append(dont_touch)

            # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        # Draw our sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.bonus_list.draw()
        self.dont_touch_list.draw()


        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.BLACK, 18)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Add one to the score
            self.score += random.randint(3,10)

        bonus_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.bonus_list)
        for bonus in bonus_hit_list:
            bonus.remove_from_sprite_lists()
            self.score += 100

        # Did the player touch something they should not?
        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.dont_touch_list):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = 600
            self.player_sprite.center_y = 100
            self.score = 0

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()