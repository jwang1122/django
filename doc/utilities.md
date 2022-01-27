## Useful Icons

❓✔️ 📌❗️ 👍😄 👎😱 👎😢❌✔️ 💡👉 🔔⚡️ 🔒🔑⚡️🔥 ☝️👌
✏️📄✂️♻️
📝🔍🔨☝️😢👇👈👉👍👎👌👊⭐️👎😢🌎💾🗑🐛📒⚠️📐🛠🎯✉️☎️

:hammer:
:department_store:

## Change image size
<img src="images/bug.png" width="32"/><img src="images/waiting.gif" width="32">
[](images/bug.png) [](images/waiting.gif)

## references
* [Color Picker](https://www.webfx.com/web-design/color-picker/)
* [favorite icon website](https://www.webfx.com/tools/emoji-cheat-sheet/)

## Notations
📝 **Source Code**
❌ **Mistake:**
👌 **Reasong:**
✔️ **Solution:**
🔑⚡️ **Knowlodge Base:**
👍😄 **Conclusion**

## Fast way to learn something new:
  1. DIY (do it yourself);
  2. learn from mistake;
  3. repeat;
  4. take good note for future review;
  5. teach someone else.

## Sample File Structure:

```output
<project root>
    ├── 📝doc/
    |    ├── mistakes.md 
    |    └── python.md 
    ├── 🔨homeworks/
    |       └── filenameXX.md
    ├── 🔥src/
    |       └── string.py
    └── 👉ReadMe.md
```

## Sample Mermaid Graph Diagram

😄Include frequently used mermaid diagram features below👇

```mermaid
graph TB

START((start))
END[end]
B[code block]
C(["fa:fa-align-left Round box<br>function(arguments)"])
IF{condition<br> block}
DB[("fa:fa-hammer database")]
L([loop])

START-->L-->IF
IF--True-->DB-->L
IF--False-->B-->END

classDef start fill:#2DD276,stroke:#096125,stroke-width:4px,color:white;
classDef process fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef loop fill:#6CB4F2,stroke:black,stroke-width:1px;
classDef end1 fill:#E0486E,stroke:#840F45,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:black,stroke-width:2px;
classDef if fill:#EEDB88,stroke:#B19211,stroke-width:2px;
classDef db fill:#BEBDB7,stroke:black,stroke-width:2px;


class START start
class B,D,E process
class IF if
class DB db
class END end1
class L loop
```

## Simple Mermaid Relational Diagram

```mermaid
 erDiagram
    PROJECT ||--o{ TASK : contains
    PROJECT {
        int id
        string name
        date begineDate
        date endDate
    }
    TASK {
        int id
        string name
        date beginDate
        date endDate
    }
```

## Simple Mermaid Class Diagram

```mermaid
classDiagram
direction RL

class Occupation{
  Occupation: +getOccupation() String
}
<<interface>> Occupation

class Person{
  #name: String
  #ssn: String
  #age: int
  #gender: String
}
<<abstract>> Person

Occupation <|-- Person
Person <|-- Teacher
Person <|-- Doctor
Person <|-- Developer
```