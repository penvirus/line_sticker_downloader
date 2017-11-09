# Introduction #

The previous EVIL project [Areis Bot](https://github.com/penvirus/areis_bot) tries to use a bot to replace LINE sticker service for those don't want to pay (e.g. me).  However, the project was unsuccessful due to cumbersome authentication.  LINE corporation does not encourage such hacking integration.

As an alternative, I took some screenshots on funny stickers and put them on my desktop.  Do the job in manually.  But that is too stupid.  I created the tool for helping download the stickers.

# Internal #

It is easy to find the source image URL.  They are all in the format ```https://stickershop.line-scdn.net/stickershop/v1/sticker/XXXX/YYYY/sticker.png```.  XXXX represents a sticker unique ID; YYYY represents a platform name.  For example, ```https://stickershop.line-scdn.net/stickershop/v1/sticker/404681/android/sticker.png``` is an image URL.

So, it may be intersting to construct the image URL randomly.  As sticker ID is just an integer, and valid platform is either "android" or "iphone".

For instance, you can try to access these image.

* [https://stickershop.line-scdn.net/stickershop/v1/sticker/66666/android/sticker.png](https://stickershop.line-scdn.net/stickershop/v1/sticker/66666/android/sticker.png)
* [https://stickershop.line-scdn.net/stickershop/v1/sticker/77777/iphone/sticker.png](https://stickershop.line-scdn.net/stickershop/v1/sticker/77777/iphone/sticker.png)

# Usage #

```
$ python main.py [URL]...
```

For example,

```
$ python main.py https://store.line.me/stickershop/product/1008489
```
