import pyjokes;

joke = pyjokes.get_joke()
print(joke)

# printing multiline string
print(''' Hello,
      How are you?
      All Fine?
      Don't worry''')

print("Hello {}".format("Vedant"))
print("Hello %s %d" %("vedant", 21))

import time

for i in range(3):
    print("Processing...", end="\r", flush=True)
    time.sleep(1)