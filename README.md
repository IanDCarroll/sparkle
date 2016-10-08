# sparkle
Python module for CL text prettification

This is a basic module so that you don't have to remember the ANSI color codes. Yes, I know you can just google them, but with this you just call the color instead.

```
from twilight import sparkle

print sparkle.red + 'This text is colored red' + sparkle.reset
print sparkle.blue + 'This text is colored blue' + sparkle.reset
```

It's important to remember to add sparkle.reset to the end of your text or there is a chance in some cases that your CLI will be that color until you write a script to change it back! (It might be less of a big deal than that though.)

That being said, make your CLI output cheerful, clever and friendly with twilight.sparkle!
