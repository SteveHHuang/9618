# Additional notes for paper4 practical

> **这是我通过历年真题mark scheme中总结的一些必要的注意事项，这样可以让你尽可能不会因为格式问题而丢分**

i. Attribute declaration直接**参考pseudocode**的声明方式

ii. 涉及文件操作的代码**一律加上** exception handling
    ```python
    try:
        <...>
    except IOError:
        print("File not found or cannot be accessed.")
    ```

iii. 如果题干要求定义一个全局变量：必须在 `main` 的前面写 `global 变量名`

iv. 如果要定义一个 `global` 的数组：注释加在 `global 数组名` 后面

v. 不要在 `main` 中给一个没有给定初始值的变量赋一个初始值

vi. 对一个没有初始数据的数组**：直接在 `main` 中赋一个空数组

vii. 无论什么时候定义一个数组都要**加注释**