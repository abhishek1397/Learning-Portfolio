## 1. Introduction to Variables & Basic Syntax

### What is a Variable?

* A **variable** is a small box used to store data.
* Assigning a value to a variable is essentially putting something inside that box.
* When declaring a variable, you give it a **unique name**, define its **data type**, and set an **initial value**.

### Declaration Syntax

$$\text{Keyword} \quad \text{variableName: DataType} = \text{Initial Value}$$

* **Example:** `val myFirstScalaVariable: Int = 5`
* **Name:** `myFirstScalaVariable`
* **Data Type:** `Int`
* **Initial Value:** `5`



### Mutable vs. Immutable Variables

* **Immutable Variables (`val`):**
* Defined as unchangeable.
* Act like constants; once assigned, their value can never change or be reassigned.


* **Mutable Variables (`var`):**
* Defined as alterable.
* Can be reassigned throughout their lifetime as long as they remain valid.



### Printing Methods in Scala

1. **`print`**: The simplest method. It outputs everything on the **same line**.
2. **`println`**: Displays each specific output on a **separate, new line**.
3. **`printf`**: Used for **formatting text**, allowing you to append different data types to the printed text.

---

## 2. Scala Data Types & Type Hierarchy

### Type Hierarchy Structure

* In Scala, every single value has a type, and every type belongs to a unified **Type Hierarchy**.
* Generic types reside at the top, becoming increasingly specific as you move down the hierarchy.
* **`Any`**: The ultimate super-type at the top of the hierarchy. It defines universal methods like `equals`, `hashCode`, and `toString`.

```
                 Any
                /   \
           AnyVal   AnyRef
             |         |
      (Int, Double,   (List, String,
       Char, etc.)     User Classes)
             \         /
              \       Null
               \     /
                Nothing

```

### Value Types vs. Reference Types

* **Value Types (`AnyVal`):** Hold the actual data/value itself.
* *Examples:* `Double` (2.75), `Float` (2.75f), `Long` (27500000000L), `Int` (275), `Short` (1), `Byte` (0x2), `Char` ('a'), `Unit` ( () ), `Boolean` (true).


* **Reference Types (`AnyRef`):** Represent reference types. This includes all non-value types, user-defined types, and predefined Scala classes (like `String` or `List`).
* *Analogy:* If you want a paper to represent your house, you can't physically fit the house on it, so you write down the address. A reference type holds the **memory address location** of the value.



### Type Casting Flow

Not every data type can be freely converted to any other type. Scala follows a specific valid conversion direction:

$$\text{Byte} \longrightarrow \text{Short} \longrightarrow \text{Int} \longrightarrow \text{Long} \longrightarrow \text{Float} \longrightarrow \text{Double}$$

$$\text{Char} \longrightarrow \text{Int}$$

---

## 3. Operators

Scala features 5 primary categories of built-in operators:

* **Arithmetic Operators** (e.g., `+`, `-`, `*`, `/`)
* **Relational Operators** (used for comparisons)
* **Logical Operators** (e.g., `&&`, `||`, `!`)
* **Bitwise Operators**
* **Assignment Operators** (e.g., `=`, `+=`, `-=`)

---

## 4. Object-Oriented Concepts (Classes & Objects)

* **Classes as Blueprints:** A class is a blueprint or template from which objects are created.
* **Objects:** An object is a concrete instance of a class—the actual entity used inside a program.
* **Class Members:** The components making up a class:
* **Properties:** Data/fields (e.g., a `Person` class has a *name*, *gender*, and *age*).
* **Methods:** Actions/functions (e.g., a `Person` can perform actions like *walking* and *talking*).


* **Categories:** Classes are split into **Built-in classes** (provided by Scala) and **User-defined classes** (created by the programmer).

---

## 5. Scala Collections Library

Every collection in Scala is categorised as either **Mutable** or **Immutable**.

* **Mutable Collections:** Can be updated, modified, or appended in place; elements can be directly added, removed, or manipulated.
* **Immutable Collections:** Cannot be changed. Modifying or adding an element creates a **brand new collection**, leaving the original completely unaltered.

### Main Collection Categories

At the top of the collection hierarchy sit three core categories:

1. **Sequences (`Seq`):** Ordered collections where each element has a specified, index-based location for easy retrieval (e.g., `Seq(2, 4, 6, 8, 10)`).
2. **Sets (`Set`):** Collections containing unique elements with no duplicates allowed (e.g., `Set("apple", "orange")`).
3. **Maps (`Map`):** Collections consisting of `(key, value)` pairs (e.g., `Map(("a", 25), ("b", 50))`).

```
                 Library Hierarchy
                 /       |       \
               set      seq      map
              /   \    /   \    /   \
            Mut  Immut Mut Immut Mut Immut

```

---

## 6. Deep Dive: Sequence Types

### A. ArrayBuffer (Mutable Sequence)

* Belongs to the sequence (`Seq`) class branch.
* It is a **mutable** collection.
* Unlike basic arrays, you can dynamically **add and remove elements** from an `ArrayBuffer`.
* **Setup Requirements:** Must be explicitly imported using: `import scala.collection.mutable.ArrayBuffer`.
* **Syntax:** `val arrayBufferName = new ArrayBuffer[DataType]()`
* **Operations:**
* **Add element:** Use the `+=` operator.
* **Delete element:** Use the `-=` operator, the `.remove(index)` method, or `.clear()` to wipe the collection.



### B. List (Immutable Sequence)

* Belongs to the `Seq` class branch but is strictly **immutable**. Modifying a List produces a brand-new instance.
* **Creation Example:** `val intList = List.range(1, 10)`
* **Operations:**
* **Appending Elements:** Use the `:+` method.
* **Prepending Elements:** Use the `+:` method or the **cons** (`::`) operator.
* **List Concatenation:** Join two lists together using the `:::` method.
* **Head & Tail:** `.head` extracts the very first element; `.tail` returns a new list containing everything *except* the first element.



---

## 7. Functions & Evaluation Models

### Function Syntax

$$\mathbf{def} \ \text{functionName}(\text{parameter: Type}): \text{ReturnType} = \{ \text{body} \}$$

* **Example:**
```scala
def sum(x: Double, y: Double): Double = {
  x + y
}

```





### Evaluation Strategies: Call-by-Value vs. Call-by-Name
The core difference lies in the **Substitution Model**, where evaluation simply reduces expressions down to a final value.

| Strategy | Definition | Behavior Example: `func(1+1, 1+2)` where body only uses the 1st parameter | Evaluation Process Example: `evaluate(3+4, 8)` with function body $x * x$ |
| :--- | :--- | :--- | :--- |
| **Call-by-Value (CBV)** | Evaluates every argument expression to its final value **before** entering the function body, whether the function needs it or not. | Resolves to `func(2, 3)` right away. | `evaluate(7, 8)` $\rightarrow 7 * 7 \rightarrow \mathbf{49}$. |
| **Call-by-Name (CBN)** | Passes the raw expression directly into the function body. The expression is only evaluated **when and if** it is explicitly called inside the body. | Passes the expressions raw: `print(1+1)`. | $(3+4) * (3+4) \rightarrow 7 * (3+4) \rightarrow 7 * 7 \rightarrow \mathbf{49}$. |
