Based on the material that could be extracted from the uploaded files, the content follows a standard Scala learning progression. Some DOCX files appear to contain mostly screenshots/slides, so text extraction was limited, but the topic sequence is clear.

# Scala Notes (Concept-Based Order)

---

# 1. Introduction to Scala

## What is Scala?

Scala (Scalable Language) was created by Martin Odersky in 2001.

It combines:

1. Object-Oriented Programming (OOP)
2. Functional Programming (FP)

into a single language.

### Key Features

* Runs on JVM (Java Virtual Machine)
* Interoperable with Java
* Concise syntax
* Strong static typing
* Supports immutability
* Suitable for Big Data and Distributed Systems

### Industry Usage

Used in:

* Twitter
* LinkedIn
* Netflix
* Sony

### Why Scala for Hadoop/Spark?

Spark itself is written in Scala.

Benefits:

* Native Spark APIs
* Functional transformations
* Better performance
* Less boilerplate than Java

---

# 2. Basic Output Statements

## print()

Prints output on the same line.

```scala
print("Hello")
print("World")
```

Output:

```text
HelloWorld
```

---

## println()

Prints output and moves to the next line.

```scala
println("Hello")
println("World")
```

Output:

```text
Hello
World
```

---

## printf()

Used for formatted output.

```scala
printf("Number = %d", 123)
```

Output:

```text
Number = 123
```

---

# 3. Variables in Scala

Scala provides two types of variables.

## val (Immutable)

Cannot be changed after assignment.

```scala
val name = "Scala"
```

Attempting reassignment:

```scala
name = "Java"
```

Produces compilation error.

---

## var (Mutable)

Can be modified.

```scala
var name = "Scala"

name = "Java"
```

---

## When to Use?

### Prefer val

```scala
val pi = 3.14
```

### Use var only when necessary

```scala
var counter = 0
```

---

# 4. Data Types in Scala

## Numeric Types

| Type   | Size   |
| ------ | ------ |
| Byte   | 8-bit  |
| Short  | 16-bit |
| Int    | 32-bit |
| Long   | 64-bit |
| Float  | 32-bit |
| Double | 64-bit |

Example:

```scala
var age:Int = 21
var salary:Double = 50000.5
```

---

## Character Type

```scala
var grade:Char = 'A'
```

---

## Boolean Type

```scala
var status:Boolean = true
```

---

## String Type

```scala
var name:String = "Abhishek"
```

---

# 5. Type Casting

## Implicit Casting (Widening)

Smaller type → Larger type

```scala
val a:Int = 10

val b:Long = a
```

---

## Explicit Casting (Narrowing)

```scala
val x:Double = 12.8

val y:Int = x.toInt
```

Output:

```text
12
```

---

# 6. Operators

## Arithmetic

```scala
+
-
*
/
%
```

Example:

```scala
val a = 10
val b = 20

println(a+b)
println(a-b)
println(a*b)
```

---

## Relational

```scala
==
!=
>
<
>=
<=
```

---

## Logical

```scala
&&
||
!
```

---

# 7. Strings

## Creating Strings

```scala
val name = "Scala"
```

---

## Concatenation

```scala
println("Hello " + name)
```

Output:

```text
Hello Scala
```

---

## String Interpolation

### s Interpolator

```scala
val name = "Abhishek"

println(s"My name is $name")
```

---

### f Interpolator

```scala
val salary = 50000.25

println(f"$salary%.2f")
```

Output:

```text
50000.25
```

---

### raw Interpolator

```scala
println(raw"Hello \n Scala")
```

Output:

```text
Hello \n Scala
```

---

## Common String Methods

```scala
length
toUpperCase
toLowerCase
charAt()
substring()
contains()
replace()
```

Example:

```scala
val name = "Scala"

println(name.length)
println(name.toUpperCase)
```

---

# 8. Collections Framework

Scala Collections are divided into:

```text
Collections
│
├── Immutable
│
└── Mutable
```

Default collections are immutable.

---

# 9. Arrays

## Definition

Fixed-size collection.

```scala
val arr = Array(10,20,30,40)
```

---

## Accessing Elements

```scala
println(arr(0))
```

Output:

```text
10
```

---

## Updating Elements

```scala
arr(0) = 100
```

---

## Traversing Arrays

### for loop

```scala
for(i <- arr)
{
 println(i)
}
```

---

### foreach()

```scala
arr.foreach(println)
```

---

# 10. ArrayBuffer

ArrayBuffer belongs to mutable collections.

Import required:

```scala
import scala.collection.mutable.ArrayBuffer
```

---

## Creation

```scala
val nums = ArrayBuffer(1,2,3)
```

---

## Add Elements

```scala
nums += 4
```

---

## Add Multiple Elements

```scala
nums += (5,6,7)
```

---

## Remove Elements

```scala
nums -= 2
```

---

### Use When

Size changes frequently.

---

# 11. List

Immutable collection.

```scala
val nums = List(10,20,30)
```

---

## Head

```scala
nums.head
```

Returns first element.

---

## Tail

```scala
nums.tail
```

Returns remaining elements.

---

## Append

```scala
nums :+ 40
```

---

## Prepend

```scala
5 :: nums
```

---

### Advantage

Fast insertion at beginning.

---

# 12. Vector

Alternative to List.

```scala
val nums = Vector(1,2,3)
```

### Advantages

* Faster random access
* Immutable
* Efficient updates

---

# 13. LazyList

Elements are generated only when needed.

```scala
val nums = LazyList.from(1)
```

### Benefit

Memory efficient for large or infinite sequences.

Example:

```scala
nums.take(10).toList
```

---

# 14. Functions

## Function Definition

```scala
def add(a:Int,b:Int):Int =
{
 a+b
}
```

---

## Calling Function

```scala
add(10,20)
```

Output:

```text
30
```

---

## Parameterless Function

```scala
def greet() =
{
 println("Hello")
}
```

---

## Anonymous Function

```scala
(x:Int) => x*x
```

---

## Higher Order Function

Function accepting another function.

```scala
def operate(a:Int,b:Int,f:(Int,Int)=>Int)
{
 f(a,b)
}
```

Important in Spark because:

```scala
map()
filter()
reduce()
foreach()
```

all use functions as arguments.

---

# 15. Recursive Functions

A function calling itself.

---

## Factorial Example

```scala
def factorial(n:Int):Int =
{
 if(n==0)
   1
 else
   n * factorial(n-1)
}
```

---

## Recursive Flow

```text
factorial(4)

4 * factorial(3)
3 * factorial(2)
2 * factorial(1)
1 * factorial(0)

= 24
```

---

## Recursion vs Loop

| Loop             | Recursion                 |
| ---------------- | ------------------------- |
| Iterative        | Self-calling              |
| Less stack usage | Uses call stack           |
| Faster generally | Cleaner for tree problems |

---

# Scala Topics Most Important for Spark

For Hadoop/Spark preparation, prioritize:

1. val vs var
2. Data Types
3. Strings
4. Arrays
5. ArrayBuffer
6. List
7. Vector
8. Functions
9. Anonymous Functions
10. Higher Order Functions
11. Recursion (basic understanding)
12. Immutable Collections

These concepts directly appear in Spark RDD, DataFrame, Dataset, and GraphX programming.
