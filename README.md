# FreeCodeCamp Python Journey 

This repository is a collection of practice challenges and curriculum projects completed during my Python study journey on FreeCodeCamp. It tracks my progress from basic data logic to advanced concepts, specifically focusing on the transition from functional programming to **Class-based logic.**

---

## Featured Projects

### 1. Social Media Profile Manager (Class & State Logic)
The "Graduation Project" of my 15-part logic series, moving from simple functions to full Class structures.
- **Key Features:**
  - **Secure Login:** Authenticates users before allowing access to private methods.
  - **Privacy Gates:** Conditional logic that hides content if the account is `is_private`.
  - **State-Dependent Actions:** Users can only create posts if their `is_logged_in` status is `True`.
  - **Content Display:** An iteration engine that loops through followers and posts.
- **Logic Used:** **Classes and Objects (`self`)**, Boolean state flags, logical operators (`and`/`or`), and list iteration.



### 2. To-Do List Manager (Final CRUD Version)
A complete task management system that handles the full data lifecycle.
- **Key Features:** - **Create:** Add new tasks with specific statuses.
  - **Read:** View all tasks or filter to see only "Pending" items.
  - **Update:** Find specific tasks and mark them as "Done."
  - **Delete:** Remove tasks entirely from the system.
- **Logic Used:** Lists of dictionaries, Boolean flags (`found_any`), case-insensitive string matching, and `while` loop menu systems.

### 3. Contact Book Manager
A search-based application for managing personal data.
- **Key Features:** Dynamic storage of names and contact details.
- **Logic Used:** Python dictionaries, user-input handling, and data retrieval.

### 4. Expense Tracker (Robust Version)
A financial tool that handles numerical data and currency formatting.
- **Key Features:** CRUD logic, numerical data processing, and **Error Handling (`try/except`)** to prevent crashes.
- **Skills:** Type casting, f-string precision, and list manipulation.

### 5. Caesar Cipher (Security Tool)
A cryptography tool that encrypts and decrypts messages using a shift-based algorithm.
- **Key Features:** Dual mode support (Encode/Decode) and handling of non-alphabetical characters.
- **Skills:** Mathematical logic using the **Modulo operator (`% 26`)**, function parameters, and input sanitization.

---

## Skills Demonstrated
- **Object-Oriented Logic:** Mastering `__init__`, `self`, and class methods.
- **Data Management:** Mastering CRUD (Create, Read, Update, Delete) operations.
- **Security & State:** Implementing login systems and privacy toggles.
- **Problem Solving:** Implementing logic to filter and search through datasets.
- **Clean Code:** Using functions, classes, and proper naming conventions.

---


# 🏙️ Addis Ababa Smart City: The Encapsulation Saga
### *Python Object-Oriented Programming (OOP) Study — Pillar 1*

## 📜 Project Overview
This project simulates the urban infrastructure of **Addis Ababa** to demonstrate the first pillar of OOP: **Encapsulation**. By building various city modules—from the Power Grid to the City Council—I practiced how to bundle data and methods together while protecting the internal state of objects from unauthorized access or accidental corruption.



---
##  ----oop-------
## Encapsulation Features in Addis Ababa

### 1. Identity & Privacy (`Citizen` Class)
We protect residents' sensitive data using private attributes (`__id_number`). Access is controlled through a `@property` that masks the ID, showing only the last 4 digits (e.g., `*****6789`).

### 2. The Energy Grid (`PowerPlant` Class)
The power plant manages its own lifecycle. Using a `@setter` for `fuel_level`, the plant automatically switches between `ONLINE` and `OFFLINE` status based on available resources. This prevents the system from being in an "Active" state with zero fuel.



### 3. Financial Integrity (`BankAccount` Class)
A `Citizen` object is passed into the `BankAccount` as an owner. Encapsulation ensures the balance can only be changed via `deposit` or `withdraw` methods, enforcing rules like "Insufficient Funds" checks.

### 4. Smart Living (`SmartHome` Class)
Located at **Bole Dembel**, the SmartHome demonstrates input validation. The climate control setter strictly blocks any temperature outside the safe range of **18°C - 28°C**, protecting the home's infrastructure.

### 5. Centralized Records (`CityHospital` Class)
The **Addis Ababa City General Hospital** uses a **Dictionary** to map unique IDs to `Citizen` objects. This allows for fast lookup times, demonstrating efficient data management through encapsulated records.



### 6. Administrative Governance (`CityCouncil` Class)
This module introduces **Privileged Access**. The city budget cannot be changed directly; it requires a specific `admin_key` to be passed into the `update_budget` method, simulating real-world security protocols.

---

## Key OOP Concepts Applied
* **Private Attributes:** Using `__attribute` to prevent direct external modification.
* **Property Decorators:** Using `@property` and `@setter` to create "Managed Attributes."
* **Data Validation:** Checking the type and length of data (like IDs or Temperatures) before saving it.
* **Object Composition:** Passing one object (like `Citizen`) into another (like `Bus` or `BankAccount`).

---

## 🏁 Conclusion
By the end of this module, the **Addis Ababa** system is fully encapsulated. The city is secure, the data is valid, and the objects handle their own logic internally. 

**Next Step:** Moving to **Pillar 2: Inheritance** to create specialized citizens like Doctors and Police Officers!



## Milestone Achievement
This repository documents my preparation for the **FreeCodeCamp Scientific Computing with Python Certification**, successfully mastering the logic required for the first 70 steps of the curriculum.
