'''   
What is OOP Anyway?
Imagine you’re building with LEGOs.
Instead of just having a pile of individual bricks (like in procedural programming), Object-Oriented Programming (OOP) lets you create pre-assembled units like a car, a house, or a robot.

These units have:

Specific parts (data)

Specific things they can do (actions)

That’s what OOP is all about — a way of programming focused on creating objects.

🔹 An Object is a Self-Contained Unit That Includes:
Data (Attributes):
Information about the object.
Example: For a car — color, model, speed.

Actions (Methods):
Things the object can do.
Example: A car can accelerate, brake, turn.

💡 Why Bother with OOP?
OOP offers several key advantages:

✅ Organization:
Your code becomes more structured and easier to navigate, especially in large projects.

🔁 Reusability:
You can use the same object “blueprints” (classes) multiple times, saving you from rewriting code.

🐞 Easier Debugging:
When something goes wrong, it’s easier to isolate the issue within a specific object.

🌍 Real-World Modeling:
OOP lets you represent real-world things and their relationships in a natural way.

🏛️ The Four Pillars of OOP
OOP is built on four fundamental principles:

1. Abstraction
Example: Driving a car. You use the steering wheel, pedals, and gearshift without needing to understand the complex engineering under the hood.

Definition: Hides complex details and shows only essential features to the user.

2. Encapsulation
Example: The engine of a car is sealed inside, and you interact only through interfaces (e.g., ignition switch).

Definition: Bundles data and methods within a class to protect data and control access.

3. Inheritance
Example: A SportsCar class inherits features from a Car class (like wheels and engine) and adds new features (like a spoiler).

Definition: Allows a class to inherit properties and behaviors from another class, promoting code reuse.

4. Polymorphism
Example: A Dog and a Cat both have a make_sound() method — the dog barks, the cat meows.

Definition: Objects of different classes can respond to the same method call in different ways     '''

class nigga:
    def intro(self):
        print("Hello, I am a nigga")

n = nigga()  
n.intro()
# Hello, I am a nigga