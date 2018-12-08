#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 11/09/18

from tg_io.staging.pin_port import SD_cs, SD_spi
from tg_modules.make_ios import dio

from adafruit import adafruit_sdcard

sdcard = adafruit_sdcard.SDCard(SD_spi, dio(SD_cs))
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")