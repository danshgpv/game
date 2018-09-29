import arcade
import os

SPRITE_SCALING = 1.1

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

MOVEMENT_SPEED = 6


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        self.texture_left = arcade.load_texture("images/char01.png", mirrored=True, scale=SPRITE_SCALING)
        self.texture_right = arcade.load_texture("images/char01.png", scale=SPRITE_SCALING)

        # By default, face right.
        self.texture = self.texture_right

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.texture_left
        if self.change_x > 0:
            self.texture = self.texture_right

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.all_sprites_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Set the background color
        # arcade.set_background_color(arcade.color.AMAZON)

        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.score = 0
        self.player_sprite = arcade.AnimatedWalkingSprite()

        self.background = arcade.load_texture("images/background.jpg")

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = Player()
        # self.player_sprite.center_x = 50
        # self.player_sprite.center_y = 50
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT - 600
        self.all_sprites_list.append(self.player_sprite)

        character_scale = 1.1

        # Standing
        self.player_sprite.stand_left_textures = []
        self.player_sprite.stand_left_textures.append(arcade.load_texture("images/char01.png", scale=SPRITE_SCALING, mirrored=True))
        self.player_sprite.stand_left_textures.append(arcade.load_texture("images/char02.png", scale=SPRITE_SCALING, mirrored=True))


        # Walk
        self.player_sprite.walk_right_textures = []
        self.player_sprite.walk_right_textures.append(arcade.load_texture("images/char01.png", scale=SPRITE_SCALING))
        self.player_sprite.walk_right_textures.append(arcade.load_texture("images/char02.png", scale=SPRITE_SCALING))

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Draw all the sprites.
        self.all_sprites_list.draw()

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()