---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
institution: Garden City University (GCU)
program: M.Sc. Bioinformatics (Semester III)
unit: Unit 2 — Classical Machine Learning Algorithms
submodule: 2.2 Classification Algorithms
document_type: Guided Deep Dive (Classification)
ai_tier: Full AI (Learning Aid)
---

# Section 1 — How Do We Learn to Recognize Fruits?

<small><b>Course Code:</b> 02BMSBI24365 | <b>Program:</b> M.Sc. Bioinformatics (Semester III) | <b>Institution:</b> Garden City University (GCU) | <b>AI Tier:</b> Full AI (Learning Aid)</small>

---

<img src="./assets/classification_apple_orange.png" alt="Classification Infographic" width="600"/>

### 1. The Problem

Imagine that we are handed a fruit and asked a simple question:

> **“Is this an apple or an orange?”**

As humans, we naturally look at the fruit and make a quick decision based on its physical characteristics.

### 2. What Do We Look At?

We rely on different attributes of the fruit to figure it out:
* **Color**
* **Size**
* **Weight**
* **Shape**
* **Texture**

In Machine Learning, these characteristics are called **features**.

> 💡 **Features** are the measurable properties (the clues) that help us make a decision.

### 3. Using Features to Make a Decision

Let's organize our observations into a structured table. Notice how the features line up:

| Color  | Weight | Shape | Texture | Smell  | ➡️ | Decision |
| ------ | -----: | ----- | ------- | ------ |:---:| -------- |
| Red    |  150 g | Round | Smooth  | Sweet  | ➡️ | **Apple**  |
| Orange |  180 g | Round | Rough   | Citrus | ➡️ | **Orange** |
| Green  |  140 g | Round | Smooth  | Sweet  | ➡️ | **Apple**  |

We look at these features and use them to identify the fruit.

### 4. What Is the Answer?

The final answer we are trying to predict (Apple or Orange) has a special name. 
This answer is called the **label** or **target**. 

### 5. Classification

Because our possible answers are predefined categories (**Apple** and **Orange**), we call these **classes**.

When we use features to determine which class a fruit belongs to, we are performing **classification**.

> 💡 **Classification** means assigning a new observation into one of our predefined categories.

---

### Human Learning vs. Machine Learning

**Humans** learn to distinguish an apple from an orange through life experience. By seeing, touching, smelling, and tasting many apples and oranges, we gradually learn they have different characteristics. We naturally notice apples are often smooth and red/green, while oranges are rough and orange-colored. We don't need to write down a math equation; our brain learns the pattern automatically.

**A machine** can also learn from examples, but it needs data instead of human senses. A machine is given measurable features (numbers representing color, weight, texture). When we provide many examples along with their correct labels (Apple or Orange), the **machine learning algorithm** finds the hidden mathematical patterns. It then builds a **model** capable of classifying brand new fruits!

In simple terms:
> **Natural learning:** Humans learn patterns from experience.
> **Machine learning:** Machines learn patterns from data.

---
# Section 2 — Connecting the Example to Machine Learning

Now consider the same problem from the perspective of a computer. 

Instead of manually writing a rule for every fruit (e.g., *"if red and smooth then apple"*), we just provide the computer with many examples of apples and oranges.

| Color  | Weight | Shape | Texture | Smell  | ➡️ | Label  |
| ------ | -----: | ----- | ------- | ------ |:---:| ------ |
| Red    |  150 g | Round | Smooth  | Sweet  | ➡️ | **Apple**  |
| Green  |  140 g | Round | Smooth  | Sweet  | ➡️ | **Apple**  |
| Orange |  180 g | Round | Rough   | Citrus | ➡️ | **Orange** |
| Orange |  170 g | Round | Rough   | Citrus | ➡️ | **Orange** |

The computer receives **features along with their correct labels**. This collection of historical examples is called **training data**.

### The Learning Phase

The algorithm analyzes the training data to find hidden patterns.

```mermaid
flowchart TD
    A[(Training Data)] --> B[Features + Labels]
    B --> C((Machine Learning Algorithm))
    C -- Learns Patterns --> D{{Trained Model}}

    style A fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style B fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style C fill:#c8e6c9,stroke:#333,stroke-width:2px,color:#000
    style D fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
```

The **model** is simply the mathematical result of the algorithm learning patterns from the training data.

### The Prediction Phase

Now, when a brand new, unseen fruit is presented:

```mermaid
flowchart TD
    A[New Fruit] --> B[Extract Features]
    B --> C{{Trained Model}}
    C -- Predicts --> D([Apple or Orange])

    style A fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style B fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style C fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style D fill:#e1bee7,stroke:#333,stroke-width:2px,color:#000
```

Because the model learned from examples where the correct labels were *already provided* by a teacher, this process is called **Supervised Learning**. And because the prediction is one of two distinct categories, this is specifically a **Classification** problem.

### The Complete Picture

Here is the entire end-to-end Machine Learning pipeline for our Apple vs. Orange problem. Notice how the colors and shapes remain consistent:

```mermaid
flowchart TD
    subgraph Data Collection
        A[Collect Fruits] --> B[Extract Features<br/>Color, Weight, Shape, Texture]
    end

    subgraph Training Phase
        B --> C[(Training Data<br/>Features + Labels)]
        C --> D((Machine Learning Algorithm))
        D --> E{{Trained Model}}
    end

    subgraph Inference Phase
        F[New Unknown Fruit] --> G[Extract Features]
        E -.->|Applies Logic| G
        G --> H{{Trained Model}}
        H --> I([Prediction: Apple or Orange])
    end

    style A fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style B fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style C fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style D fill:#c8e6c9,stroke:#333,stroke-width:2px,color:#000
    style E fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    
    style F fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#000
    style G fill:#e1f5fe,stroke:#333,stroke-width:2px,color:#000
    style H fill:#ffe0b2,stroke:#333,stroke-width:2px,color:#000
    style I fill:#e1bee7,stroke:#333,stroke-width:2px,color:#000
```

> 🎯 **Summary:** We used **Supervised Learning** to build a **Classification** model that maps physical **Features** to a predicted **Target Label**.
