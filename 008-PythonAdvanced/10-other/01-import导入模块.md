## `import`导入模块

## 1. 目的

在上学期我们已经学习过多模块开发，因为我们本学期要学习较大的项目，而大项目往往都是由多个人一起开发完成的，所以会出现分模块开发，即让A同事完成`xxx.py`，B同时完成`yyy.py`。。。而最后则需要将他们这些`.py`文件合并，一个大项目就这样完成了

## 2. `import`搜索路径

![](assets/QQ20171023-213011@2x.png)

### 路径搜索

* 从上面列出的目录里依次查找要导入的模块文件
* 空字符串`''` 表示当前路径
* 列表中的路径的先后顺序代表了`Python解释器`在搜索模块时的先后顺序，如果在前一个路径中找到了需要的模块，则停止搜索

## 3. 程序执行时添加新的模块路径

### 3.1 需求

Python解释器默认导入模块的路径在上面已经学习过，通过打印`sys.path`能够知道

但是在一个程序运行时，如果需要另外一个特殊的路径但它 却不在`sys.path`标识的那些中，此时

我们可以手动添加一个路径，此时OK了

### 3.2 方式

添加一个搜索路径的方式1（在末尾添加）

```python
sys.path.append('/home/itcast/xxx')
```

添加一个搜索路径的方式2（保证优先搜索）

```python
sys.path.insert(0, '/home/itcast/xxx')
```

### 3.3 测试

```python
In [37]: sys.path.insert(0,"/home/python/xxxx")
In [38]: sys.path
Out[38]: 
['/home/python/xxxx',
 '',
 '/usr/bin',
 '/usr/lib/python35.zip',
 '/usr/lib/python3.5',
 '/usr/lib/python3.5/plat-x86_64-linux-gnu',
 '/usr/lib/python3.5/lib-dynload',
 '/usr/local/lib/python3.5/dist-packages',
 '/usr/lib/python3/dist-packages',
 '/usr/lib/python3/dist-packages/IPython/extensions',
 '/home/python/.ipython']

```

## 4. 重新导入模块

模块被导入后，`import module`不能重新导入模块，重新导入需用`reload`

### 4.1 测试1

编写一个代码`reload_test.py`如下：

![](assets/QQ20171023-213646@2x.png)

使用终端打开`python`或者`ipython`，跳转到`reload_test.py`所在的路径，然后执行如下代码：

![](assets/QQ20171023-213753@2x.png)

可以看到`---1---`所以也就说明了在`reaload_test.py`中的`test函数`被执行了



在不退出上图终端的情况下，修改`reload_test.py`中的`test函数`，如下：

![](assets/QQ20171023-214117@2x.png)



既然`reaload_test.py`中的`test函数`已经被修改了，根据常理来说，只需要重新`import`导入一次，然后调用`test函数`应该能够看到修改之后的变化`---2---`

但是，请看如下图所示代码，好像结果与我们想的大相径庭

![image-20190304112934090](assets/image-20190304112934090.png)

### 4.2 测试2

如果在程序运行中，需要重新再次导入模块，需要使用`reload`

![image-20190304112951686](assets/image-20190304112951686.png)



运行效果：

![image-20190304113542348](assets/image-20190304113542348.png)

![image-20190304113604528](assets/image-20190304113604528.png)

![image-20190304113835734](assets/image-20190304113835734.png)



## 5. 多模块开发时的注意点

### 5.1 说明

下面的代码模拟了一个实际开发过程，将接收数据的功能封装到了`recv_msg.py`，将处理数据的功能封装到了`handle_msg.py`中，将`recv_msg.py`、`handle_msg.py`中都需要用到的变量定义在`common.py`中，而`main.py`负责完成整体的调用

### 5.2 代码

`common.py模块`

```python
RECV_DATA_LIST = list()
HANDLE_FLAG = False
```


`recv_msg.py模块`

```python
from common import RECV_DATA_LIST
# from common import HANDLE_FLAG
import common


def recv_msg():
	"""模拟接收到数据，然后添加到common模块中的列表中"""
	print("--->recv_msg")
	for i in range(5):
		RECV_DATA_LIST.append(i)


def test_recv_data():
	"""测试接收到的数据"""
	print("--->test_recv_data")
	print(RECV_DATA_LIST)


def recv_msg_next():
	"""已经处理完成后，再接收另外的其他数据"""
	print("--->recv_msg_next")
	# if HANDLE_FLAG:
	if common.HANDLE_FLAG:
		print("------发现之前的数据已经处理完成，这里进行接收其他的数据(模拟过程...)----")
	else:
		print("------发现之前的数据未处理完，等待中....------")

```


`handle_msg.py模块`
```python
from common import RECV_DATA_LIST
# from common import HANDLE_FLAG
import common

def handle_data():
	"""模拟处理recv_msg模块接收的数据"""
	print("--->handle_data")
	for i in RECV_DATA_LIST:
		print(i)

	# 既然处理完成了，那么将变量HANDLE_FLAG设置为True，意味着处理完成
	# global HANDLE_FLAG
	# HANDLE_FLAG = True
	common.HANDLE_FLAG = True

def test_handle_data():
	"""测试处理是否完成，变量是否设置为True"""
	print("--->test_handle_data")
	# if HANDLE_FLAG:
	if common.HANDLE_FLAG:
		print("=====已经处理完成====")
	else:
		print("=====未处理完成====")



```


`main.py模块`
```python
from recv_msg import *
from handle_msg import *


def main():
	# 1. 接收数据
	recv_msg()
	# 2. 测试是否接收完毕
	test_recv_data()
	# 3. 判断如果处理完成，则接收其它数据
	recv_msg_next()
	# 4. 处理数据
	handle_data()
	# 5. 测试是否处理完毕
	test_handle_data()
	# 6. 判断如果处理完成，则接收其它数据
	recv_msg_next()


if __name__ == "__main__":
	main()

```

整体代码结构如下：

![image-20190304115333144](assets/image-20190304115333144.png)

运行方式1(使用`from … import …`)，效果如下

![image-20190304115904246](assets/image-20190304115904246.png)

![image-20190304115523899](assets/image-20190304115523899.png)

运行方式2(使用`import ...`)，效果如下：

![image-20190304115740025](assets/image-20190304115740025.png)

![image-20190304115751844](assets/image-20190304115751844.png)

### 5.3 `from...import…`与`import ...`的区别

`from...import...`的大体效果如下

![](assets/QQ20171024-080610@2x.png)

小总结：

> from…import…相当于在本.py文件中，定义一个变量，这个变量指向了另外一个.py文件中的那个数据
>
> 如果在本.py中直接使用赋值运算符修改，其实是修改的它的引用，而另外一个.py文件中的数据并没有被修改



`import...`的大体效果如下

![](assets/QQ20171024-081134@2x.png)

小总结:

> import的方式，也可以理解为在本.py文件中，定义了一个变量，这个变量此时是直接指向另外一个.py文件（此时可以将这个.py文件理解为一个特殊的对象），因为此种方法修改另外.py文件中的数据的方式是`模块名.变量名`，所以此时就直接可以修改另外一个.py文件中的数据了