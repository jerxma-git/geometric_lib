# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c






# Code documentation
## Circle

<a href="../circle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `circle`

---

<a href="../circle.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(r)
```

Calculates the area of a circle 

**Args:**
 
 - <b>`r`</b> (number):  radius of the circle 



**Returns:**
 
 - <b>`number`</b>:  the area 


---

<a href="../circle.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(r)
```

Calculates the perimeter of a circle 



**Args:**
 
 - <b>`r`</b> (number):  radius of the circle 



**Returns:**
 
 - <b>`number`</b>:  the perimeter 


### Example usage
```
>>> from circle import area, perimeter
>>> area(1)
3.141592653589793
>>> area(3)
28.274333882308138
>>> perimeter(1)
6.283185307179586
>>> perimeter(2.5)
15.707963267948966
```





## Rectangle
<a href="../rectangle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rectangle`
---
<a href="../rectangle.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a, b)
```
Calculates the area of a rectangle 


**Args:**
 
 - <b>`a`</b> (float):  width of the rectangle 
 - <b>`b`</b> (float):  height of the rectangle 


**Returns:**
 
 - <b>`float`</b>:  the area 

---

<a href="../rectangle.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a, b)
```

Calculates the perimeter of a rectangle 


**Args:**
 
 - <b>`a`</b> (float):  width of the rectangle 
 - <b>`b`</b> (float):  height of the rectangle 


**Returns:**
 
 - <b>`float`</b>:  _description_ 


### Example usage
```
>>> from rectangle import area, perimeter
>>> area(2, 3.5)
7.0
>>> perimeter(1.2, 2)
6.4
```



## Square


<a href="../square.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `square`

---

<a href="../square.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a)
```

Calculates the area of a square 

**Args:**
 
 - <b>`a`</b> (float):  size of the square's side 

**Returns:**
 
 - <b>`float`</b>:  the area  

---

<a href="../square.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a)
```

Calculates the perimeter of a square 


**Args:**
 
 - <b>`a`</b> (float):  size of the square's side 


**Returns:**
 
 - <b>`float`</b>:  the perimeter 





## Triangle

<a href="../triangle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `triangle`


---

<a href="../triangle.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a, h)
```

Calculates the area of a triangle 

**Args:**
 
 - <b>`a`</b> (float):  size of the triangle's side 
 - <b>`h`</b> (float):  triangle's height measured from the provided side 

**Returns:**
 
 - <b>`float`</b>:  the area 

---

<a href="../triangle.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a, b, c)
```
Calculates the perimeter of a triangle 


**Args:**
 
 - <b>`a`</b> (float):  size of the first side (any order) 
 - <b>`b`</b> (float):  size of the second side  
 - <b>`c`</b> (float):  size of the third side 



**Returns:**
 
 - <b>`float`</b>:  the perimeter 


### Example usage

```
>>> from triangle import area, perimeter
>>> area(6, 5.19615242271) 
15.58845726813
>>> perimeter(2, 3, 9)
14
```






## Git commit history
![commit history](./git_history.png)