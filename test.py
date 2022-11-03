from source.logger import Logger 
from source.settings import Settings


# test = Logger(True)
# test.log("Test", "It seems that's work")
# test.warn("Test", "Just a warn test")
# test.fail("Test", "Just a fail test")
# test.succeed("Test", "Yaaaaa ! Logger work")
# del(test)

a = Settings()
a.update({"dev" : True})
