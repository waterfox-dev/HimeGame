from source.logger import Logger 

test = Logger(True)
test.log("Test", "It seems that's work")
test.warn("Test", "Just a warn test")
test.fail("Test", "Just a fail test")
test.succeed("Test", "Yaaaaa ! Logger work")
del(test)