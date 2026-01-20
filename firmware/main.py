import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import RGB 

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

bus = busio.I2C(board.GP6, board.GP7)
driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.1,
    off_time=600,
    brightness=0.45
)

# star design
display.entries = [
    TextEntry(text='chaos', x=64, y=10, x_anchor="M"),
]
keyboard.extensions.append(display)

rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=4,
    val_default=120, 
    hue_default=210,
    sat_default=255,
)
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.GP29, board.GP28, board.GP27, board.GP26)
keyboard.row_pins = (board.GP4, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R,
        KC.A, KC.S, KC.D, KC.MUTE 
    ],
]

encoder_handler.pins = ((board.GP1, board.GP0, None),)
encoder_handler.map = [((KC.VOLU, KC.VOLD, None),)]

if __name__ == '__main__':
    keyboard.go()