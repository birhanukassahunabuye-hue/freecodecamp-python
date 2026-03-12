# 🇪🇹 My Python & OOP Mastery Journey
> **Path:** From Functional Logic to Addis Ababa Smart City Architect  
> **Certification Prep:** FreeCodeCamp Scientific Computing with Python (Steps 1-70+)

---

## 📂 Phase 1: Functional Foundations (FreeCodeCamp Basics)
<details>
<summary><b>Click to view Basic Python Projects</b></summary>

### 1. Social Media Profile Manager
- **Logic:** Classes/Objects, Boolean state flags, and list iteration.
- **Highlight:** Privacy gates that hide content based on `is_private` status.

### 2. CRUD To-Do List Manager
- **Logic:** Full Lifecycle (Create, Read, Update, Delete).

### 3. Caesar Cipher (Security Tool)
- **Logic:** Mathematical modulo operator (`% 26`).

### 4. Expense Tracker & Contact Book
- **Logic:** Dictionaries and `try/except` error handling.
</details>

---

## 🏙️ Phase 2: Addis Ababa Smart City (The OOP Pillars)

### 🛡️ Pillar 1: Encapsulation 
**Goal:** Protecting the internal state of Addis Ababa's infrastructure.

| Module | Encapsulation Technique | Real-World Logic |
| :--- | :--- | :--- |
| **Citizen** | Private Attributes (`__`) | ID Masking (e.g., `*****6789`) |
| **PowerPlant** | Reactive Setters | Auto-OFFLINE when fuel hits 0% |
| **BankAccount** | Object Composition | Protecting balance via method-only updates |
| **SmartHome** | Validation Logic | Temp restricted to 18°C-28°C |
| **Hospital** | Dictionary Mapping | Instant $O(1)$ patient lookup by ID |
| **City Council** | Privileged Access | Budget updates require an `admin_key` |

---

### 🧬 Pillar 2: Inheritance
**Goal:** Creating specialized roles by extending the `Citizen` base class.

* **The `super()` Bridge:** Used to pass common data (Name, Age, ID) to the parent while adding unique specialist traits.
* **Method Overriding:** Customizing the `__str__` method to append professional credentials (like Badge Numbers or Specialties) to the standard profile.
* **Code Reusability:** Zero repetition of ID masking or birthday logic; children classes (`PoliceOfficer`, `Doctor`, `Constructor`) "borrow" everything from the parent.



---

### 🎭 Pillar 3: Polymorphism
**Goal:** Running a city-wide simulation through a unified interface.

* **Unified Interface:** Every specialist (and the base Citizen) now shares a `perform_duty()` method.
* **Dynamic Dispatch:** I implemented a single `for` loop that iterates through the `addis_population` list. Python automatically identifies the object type and runs the specific duty:
    * **Police:** 🚨 Patrolling the streets of Addis.
    * **Doctor:** 🏥 Treating patients in specific wards.
    * **Constructor:** 🏗️ Working on the corridor development.
    * **Citizen:** 🚶 General commuting.



---

## 🏆 Milestone Achievement
This repository documents my successful completion of the **FreeCodeCamp Scientific Computing** logic blocks, mastering the transition into class-based architecture and the first three pillars of OOP.
