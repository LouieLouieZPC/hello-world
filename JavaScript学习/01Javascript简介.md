# 01Javascript简介

1. 本文的[参考文档](https://zh.javascript.info/hello-world#xian-dai-de-biao-ji-markup)

2. [Plunker (plnkr.co)](https://plnkr.co/edit/?p=preview&preview)可以用来模拟运行html代码

## 一、“script” 标签

我们几乎可以使用 `<script>` 标签将 JavaScript 程序插入到 HTML 文档的任何位置。

比如：

```html
<!DOCTYPE HTML>
<html>

<body>

  <p>script 标签之前...</p>

  <script>
    alert('Hello, world!');
  </script>

  <p>...script 标签之后</p>

</body>

</html>
```



## 二、外部脚本

如果你有大量的 JavaScript 代码，我们可以将它放入一个单独的文件。

脚本文件可以通过 `src` 特性（attribute）添加到 HTML 文件中。

```javascript
<script src="/path/to/script.js"></script>
```

`/path/to/script.js` 是脚本文件从网站根目录开始的**绝对路径**。当然也可以提供当前页面的相对路径。例如，`src ="script.js"`，就像 `src="./script.js"`，表示当前文件夹中的 `"script.js"` 文件。也可以提供一个完整的 URL 地址，例如`src``="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js"`

要附加多个脚本，请使用多个标签：

```javascript
<script src="/js/script1.js"></script>
<script src="/js/script2.js"></script>
…
```

> 一般来说，只有最简单的脚本才嵌入到 HTML 中。更复杂的脚本存放在单独的文件中。
>
> 使用独立文件的好处是浏览器会下载它，然后将它保存到浏览器的 [缓存](https://en.wikipedia.org/wiki/Web_cache) 中。
>
> 之后，其他页面想要相同的脚本就会从缓存中获取，而不是下载它。所以文件实际上只会下载一次。
>
> 这可以节省流量，并使得页面（加载）更快。



## 三、练习

使用外部的脚本显示一个提示语：

HTML 代码：

```html
<!DOCTYPE html>
<html>

<body>

  <script src="alert.js"></script>

</body>

</html>
```

同一个文件夹中的 `alert.js` 文件：

```javascript
alert("I'm JavaScript!");
```



