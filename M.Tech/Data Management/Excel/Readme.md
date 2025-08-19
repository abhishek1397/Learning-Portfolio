# Excel

***

### 1. Tables and Groups  
- **Command inside table**: Operates within groups of data.  
- **Collection of all tables**: Called a **Workbook** (earlier written as “chilion”).  
- **Intersection of rows and columns**: Forms a **Cell**.  

***

### 2. Types of Cell References (Excel/Spreadsheet Concepts)  

1. **Relative Reference**  
   - Example: `A1`  
   - Adjusts automatically when the formula is copied to another location.  
   - If formula is `=A1+B1` in row 2 and copied to row 3, it becomes `=A2+B2`.  

2. **Absolute Reference**  
   - Example: `$A$1`  
   - Always refers to the same fixed cell, regardless of where the formula is copied.  
   - `$A$1` will always point to cell A1.  

3. **Mixed Reference**  
   - Combination of fixed (absolute) and relative references:  
     - `$A1` → Column fixed, row changes  
     - `A$1` → Row fixed, column changes  
   - Useful when only one part needs to remain constant.  

***

### 3. Other Reference Types  
- **Variable** → Standard relative reference (changes with position).  
- **Fixed** → Absolute reference (remains unchanged).  

***

### 4. Common Functions / Operators  
- **Addition (Add)** → `+` operator or `SUM()` function  
- **Multiplication (Mul)** → `*` operator or `PRODUCT()` function  

***

