# Introduction #

The previous EVIL project [Areis Bot](https://github.com/penvirus/areis_bot) tries to use a bot to replace LINE sticker service for those don't want to pay (e.g. me).  However, the project was unsuccessful due to cumbersome authentication.  LINE corporation does not encourage such hacking integration.

As an alternative, I took some screenshots on funny stickers and put them on my desktop.  Do the job in manually.  But that is too stupid.  I created the tool for helping download the stickers.

# Internal #

It is easy to find the source image URL.  They are all in the format ```https://stickershop.line-scdn.net/stickershop/v1/sticker/XXXX/YYYY/sticker.png```.  XXXX represents an unique sticker ID; YYYY represents a platform name.  For example, ```https://stickershop.line-scdn.net/stickershop/v1/sticker/404681/android/sticker.png``` is a valid image URL.

So, it may be intersting to construct the image URL randomly.  As sticker ID is just an integer, and the platform name is either "android" or "iphone" (could be more, I only find these two).

For instance, you can try to access these images.

* [https://stickershop.line-scdn.net/stickershop/v1/sticker/12345/android/sticker.png](https://stickershop.line-scdn.net/stickershop/v1/sticker/12345/android/sticker.png)
* [https://stickershop.line-scdn.net/stickershop/v1/sticker/12345678/iphone/sticker.png](https://stickershop.line-scdn.net/stickershop/v1/sticker/12345678/iphone/sticker.png)

# Usage #

```
$ python main.py [URL]...
```

For example,

```
$ python main.py https://store.line.me/stickershop/product/1008489
```
