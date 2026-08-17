# Additional notes for paper4 practical

> **这是我通过历年真题mark scheme中总结的一些必要的注意事项，这样可以让你的答案尽可能避免由于格式问题而丢分**

i. Attribute declaration直接**参考pseudocode**的声明方式
```python
class Character:
	def _init_(self,cn,colour,ss,fly, invisible):
		self.CharacterName=cn # PUBLIC CharacterName: STRING
		self.Colour=colour # PUBLIC Colour: STRING
		self.SuperStrength=ss # PUBLIC SuperStrength: STRING
		self.Fly=fly # PUBLIC Fly: STRING
		self.Invisible=invisible # PUBLIC Invisible: STRING
```

ii. 涉及文件操作的问题**一律加上** exception handling
```python
    try:
        #Contents
    except IOError:
        print("File not found or cannot be read.")
```

iii. 第一次要求在main program中写代码的时候在第一行加上`#main`
```python
#main 

CharArray=ReadData()
OutputCharacters(CharArray)
```
iii. 如果题干要求定义一个全局变量：必须在 `main` 的前面写 `global 变量名`

iv. 无论什么时候定义一个数组都要**加注释**

v. 定义一个 `global` 数组时，注释加在 `global <数组名>` 后面

vi. 不要在 `main program` 中给一个没有给定初始值的变量赋一个初始值，此时直接在 `main` 中赋一个空数组就好

```python
global DataArray # DECLARE DataArray: ARRAY[0:14] OF STRING 

#main 

DataArray=[]

```
