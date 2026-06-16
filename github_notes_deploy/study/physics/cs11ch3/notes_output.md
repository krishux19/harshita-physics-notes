# CHAPTER OVERVIEW

*   **Chapter Name:** Motion in a Plane
*   **Importance for NEET:** **HIGH.** This chapter is a cornerstone of mechanics. While direct questions might range from 1 to 3, the concepts of vectors, projectile motion, and circular motion are fundamental and applied extensively across Physics, from Electrostatics to Modern Physics. Mastering this chapter is essential for understanding subsequent topics.
*   **Estimated Weightage:** 4-12 marks (1-3 questions).
*   **Difficulty Level:** **Medium to High.**
    *   **Beginners:** May find vector algebra and resolution challenging.
    *   **Intermediate:** Projectile motion and uniform circular motion require careful application of principles and formula recall.
    *   **Advanced:** Nuances in relative velocity, non-uniform circular motion, and complex projectile scenarios can be quite challenging.
*   **Prerequisites:**
    *   Basic concepts of motion in a straight line (Chapter 2, Kinematics 1D).
    *   Basic trigonometry (sine, cosine, tangent, Pythagoras theorem).
    *   Basic algebra.
    *   Understanding of differentiation (for instantaneous velocity/acceleration).
*   **Most Important Concepts:**
    1.  **Scalars and Vectors:** Definition, distinction, examples.
    2.  **Vector Operations:** Addition (graphical and analytical/component methods), subtraction, scalar multiplication.
    3.  **Resolution of Vectors:** Expressing a vector in terms of its components along perpendicular axes (using unit vectors).
    4.  **Position, Displacement, Velocity, and Acceleration in 2D/3D:** Vector definitions and component forms.
    5.  **Motion with Constant Acceleration in a Plane:** Vector and component equations of motion.
    6.  **Projectile Motion:**
        *   Assumptions (neglecting air resistance, constant g).
        *   Independence of horizontal and vertical motions.
        *   Equation of trajectory (parabolic path).
        *   Formulas for Time of Flight (Tf), Maximum Height (hm), and Horizontal Range (R).
        *   Conditions for maximum range.
    7.  **Uniform Circular Motion (UCM):**
        *   Definition (constant speed, changing velocity).
        *   Centripetal Acceleration (ac): magnitude (v²/R or ω²R), direction (always towards the center).
        *   Angular Speed (ω), Time Period (T), Frequency (ν), and their relationships with linear speed (v).
        *   Understanding that centripetal acceleration is *not* a constant vector.

---

# BEGINNER EXPLANATION

Imagine you're playing a game of catch. You throw the ball, and it flies through the air in a curved path before your friend catches it. In the last chapter, we talked about things moving in a straight line, like a car going straight on a road. But a thrown ball doesn't move in a straight line; it moves in a curved path, up and then down, and also forward. This is "Motion in a Plane" because its movement can be described on a flat surface, like a giant blackboard.

To understand this kind of motion, we need a special tool called **Vectors**.

**What's a Vector?**
Think about telling someone how to get to your house. You wouldn't just say "2 kilometers." They'd ask, "2 kilometers *where*?" You'd say, "2 kilometers **North**."
*   "2 kilometers" is a **magnitude** (how much).
*   "North" is a **direction** (where).
When a physical quantity needs *both* a magnitude and a direction to be fully described, it's a **vector**.
*   **Examples:** Your friend's house is 2 km North (displacement), you're walking at 5 km/h East (velocity), you pushed a box with 10 Newtons of force downwards (force).

If a quantity only needs a magnitude, it's a **scalar**.
*   **Examples:** The temperature is 30°C, your weight is 60 kg, the time is 2 hours.

**Adding Vectors - Why it's special:**
If you walk 2 meters North, then 3 meters East, where are you from your starting point? You're not 5 meters away in a straight line. You'd be roughly 3.6 meters away in a North-East direction. This is why we can't just add vectors like ordinary numbers (scalars). We need special "vector addition rules."

Imagine you want to go from point A to point C, but you have to stop at B first.
*   The journey from A to B is one vector.
*   The journey from B to C is another vector.
*   The journey from A to C directly is the **resultant vector** (the total effect).
    *   **Graphical Method (Head-to-Tail):** Draw the first vector, then place the tail of the second vector at the head of the first. The resultant connects the tail of the first to the head of the second. Simple!
    *   **Component Method:** This is like breaking down each journey into "how much North/South" and "how much East/West." Add all the North/South bits together, and all the East/West bits together. Then combine these two totals to get your final position. This is super powerful for calculations.

**Breaking Down Vectors (Resolution):**
Sometimes it's easier to think of one vector as being made up of two simpler, perpendicular vectors. Like thinking of your walk North-East as a certain distance walked purely North AND a certain distance walked purely East. This is called **resolving** a vector into its **components**. We use special "unit vectors" (like `î` for East/x-direction and `ĵ` for North/y-direction) to represent these directions.

**Motion in a Plane with Constant Acceleration:**
If something is moving in a curved path but its acceleration (the rate at which its velocity changes) is constant, we can use equations similar to 1D motion. The trick is to apply these equations *separately* for the x-direction and the y-direction. This is possible because motion in perpendicular directions doesn't affect each other.

**Projectile Motion (The Thrown Ball):**
This is a classic example of 2D motion with constant acceleration.
*   **Assumptions:** We ignore air pushing against the ball, and assume gravity (g) is constant and always pulls straight down.
*   **The Big Idea:** The ball's horizontal motion (how far it travels forward) is separate from its vertical motion (how high it goes up and then falls down).
    *   **Horizontal:** No forces (we ignore air resistance), so constant velocity.
    *   **Vertical:** Only gravity acts, so constant downward acceleration 'g'. This is like a free-falling object.
*   Because of this, the path of the ball is always a **parabola** (a U-shaped curve). We can calculate how high it goes (Maximum Height), how long it stays in the air (Time of Flight), and how far it travels horizontally (Range).

**Uniform Circular Motion (Swinging a Stone):**
Imagine swinging a stone tied to a string in a circle above your head at a steady speed.
*   **Uniform speed:** The stone is moving at the same *speed* (e.g., 5 m/s) at all times.
*   **Changing velocity:** But its *direction* is constantly changing as it goes around the circle.
*   **Acceleration!** Since velocity is changing (due to direction change), there *must* be an acceleration. This acceleration is always directed towards the center of the circle, and we call it **centripetal acceleration** (center-seeking). Without it, the stone would fly off in a straight line (Newton's 1st Law!).

This chapter lays the foundation for analyzing all sorts of real-world movements, from planets orbiting the sun to launching rockets!

---

# COMPLETE CONCEPT NOTES

## 3.1 Introduction

-   **Definition:** Extension of kinematics from one dimension to two or three dimensions.
-   **Intuition:** Real-world motion is rarely strictly linear. Objects often move in curved paths.
-   **Why it matters:** Essential for describing complex movements like a thrown ball, orbiting planets, or a car turning.
-   **Real world examples:** Projectile motion (cricket ball), circular motion (fan blades), satellite orbits.
-   **Important observations:**
    *   Requires vectors to describe position, displacement, velocity, and acceleration.
    *   Motion in a plane (2D) can be simplified by resolving it into two independent 1D motions along perpendicular axes.
    *   The concepts extend to three dimensions (space) easily.

## 3.2 Scalars and Vectors

### Scalars

-   **Definition:** Physical quantities completely specified by their **magnitude** (a numerical value and a unit) only.
-   **Intuition:** "How much" of something.
-   **Why it matters:** Many physical quantities behave this way and combine using ordinary algebra.
-   **Real world examples:**
    *   **Distance:** Length of path taken.
    *   **Mass:** Amount of matter.
    *   **Time:** Duration.
    *   **Temperature:** Degree of hotness/coldness.
    *   **Speed:** Rate of distance covered.
    *   **Density, Volume, Energy, Work, Power, Electric Current.**
-   **Important observations:**
    *   Combine using rules of ordinary algebra (addition, subtraction, multiplication, division).
    *   Units must be the same for addition/subtraction.
    *   Can multiply/divide scalars of different units (e.g., density = mass/volume).

### Vectors

-   **Definition:** Physical quantities that possess both **magnitude** and **direction**, and crucially, **obey the triangle law of addition** (or equivalently, the parallelogram law of addition).
-   **Intuition:** "How much and in which direction."
-   **Why it matters:** Essential for correctly describing physical quantities where direction plays a crucial role. Failure to obey vector laws makes a quantity a scalar, even if it has magnitude and direction (e.g., electric current).
-   **Real world examples:**
    *   **Displacement:** Change in position.
    *   **Velocity:** Rate of change of displacement.
    *   **Acceleration:** Rate of change of velocity.
    *   **Force:** Push or pull.
    *   **Momentum, Electric Field, Magnetic Field.**
-   **Important observations:**
    *   Represented by a bold letter (e.g., **A**) or an arrow over a letter (e.g., $\vec{A}$).
    *   Magnitude of vector $\vec{A}$ is denoted by $|\vec{A}|$ or A.
    *   Vectors in our study are generally "free vectors" (can be shifted parallel to themselves without changing).

### 3.2.1 Position and Displacement Vectors

-   **Position Vector ($\vec{r}$):**
    *   **Definition:** A vector drawn from the origin of a coordinate system to the position of a particle.
    *   **Intuition:** Points to "where something is" relative to a fixed reference point.
    *   **Why it matters:** Defines location in space. Basis for displacement.
    *   **Real world examples:** Location of a bird in the sky from an observer on the ground.
    *   **Important observations:** Its length is the distance from the origin to the point.

-   **Displacement Vector ($\Delta\vec{r}$):**
    *   **Definition:** The straight line vector connecting the initial position to the final position of an object. $\Delta\vec{r} = \vec{r}' - \vec{r}$.
    *   **Intuition:** The "net change in position," regardless of the path taken.
    *   **Why it matters:** It's path independent. Crucial for defining average velocity.
    *   **Real world examples:** The vector from your home to school, irrespective of the winding roads you take.
    *   **Important observations:**
        *   Its magnitude is the shortest distance between initial and final points.
        *   Magnitude of displacement $\le$ total path length. They are equal only if the motion is along a straight line in one direction.

### 3.2.2 Equality of Vectors

-   **Definition:** Two vectors $\vec{A}$ and $\vec{B}$ are equal if and only if they have the **same magnitude** and the **same direction**.
-   **Intuition:** They are identical twins; indistinguishable in their effect or description.
-   **Why it matters:** Allows comparison and substitution of vectors. Forms the basis for vector operations.
-   **Important observations:**
    *   Parallel shifting a vector does not change it (free vectors).
    *   Even if magnitudes are equal, if directions differ, vectors are unequal.

## 3.3 Multiplication of Vectors by Real Numbers

-   **Definition:** Multiplying a vector $\vec{A}$ by a real number $\lambda$ (scalar) results in a new vector $\lambda\vec{A}$.
-   **Intuition:** Scaling the vector.
-   **Why it matters:** Allows changing the magnitude of a vector without altering its direction (if $\lambda > 0$), or reversing its direction (if $\lambda < 0$).
-   **Real world examples:**
    *   $2\vec{A}$: A vector in the same direction as $\vec{A}$ but with twice the magnitude.
    *   $-1\vec{A}$: A vector in the opposite direction of $\vec{A}$ with the same magnitude.
    *   If $\vec{v}$ is velocity, then $\Delta t \cdot \vec{v}$ (time * velocity) gives displacement, which is also a vector.
-   **Important observations:**
    *   Magnitude: $|\lambda\vec{A}| = |\lambda| |\vec{A}|$.
    *   Direction: Same as $\vec{A}$ if $\lambda > 0$, opposite to $\vec{A}$ if $\lambda < 0$.
    *   If $\lambda = 0$, the result is a null vector ($\vec{0}$).
    *   The dimension of $\lambda\vec{A}$ is the product of dimensions of $\lambda$ and $\vec{A}$.

## 3.4 Addition and Subtraction of Vectors — Graphical Method

### Vector Addition

-   **Principle:** Vectors obey the triangle law or parallelogram law of addition.
-   **Intuition:** Combining two movements or forces to find the net effect.

#### Triangle Law of Vector Addition (Head-to-Tail Method)

-   **Definition:** To add two vectors $\vec{A}$ and $\vec{B}$, place the tail of $\vec{B}$ at the head of $\vec{A}$. The resultant vector $\vec{R} = \vec{A} + \vec{B}$ is drawn from the tail of $\vec{A}$ to the head of $\vec{B}$.
-   **Why it matters:** Visual representation of vector sum. Works for any number of vectors (polygon law).
-   **Important observations:** The three vectors form a triangle.

#### Parallelogram Law of Vector Addition

-   **Definition:** To add two vectors $\vec{A}$ and $\vec{B}$, draw them with their tails at a common origin O. Complete the parallelogram using these two vectors as adjacent sides. The resultant vector $\vec{R} = \vec{A} + \vec{B}$ is the diagonal drawn from the common origin O.
-   **Why it matters:** Equivalent to the triangle law, often more intuitive for visualizing two vectors originating from the same point.
-   **Important observations:** The diagonal starting from the common tail represents the sum.

#### Properties of Vector Addition

1.  **Commutative Law:** $\vec{A} + \vec{B} = \vec{B} + \vec{A}$
    *   **Intuition:** The order in which you add vectors doesn't change the final resultant.
2.  **Associative Law:** $(\vec{A} + \vec{B}) + \vec{C} = \vec{A} + (\vec{B} + \vec{C})$
    *   **Intuition:** If you're adding three or more vectors, you can group them in any way.

#### Null Vector (Zero Vector) $\vec{0}$

-   **Definition:** A vector with zero magnitude. Its direction is undefined.
-   **Intuition:** No displacement, no velocity, no force. The "nothing" of vectors.
-   **Why it matters:** Represents the state of zero net effect. Allows vector equations to hold (e.g., $\vec{A} - \vec{A} = \vec{0}$).
-   **Important observations:**
    *   Properties: $\vec{A} + \vec{0} = \vec{A}$, $\lambda \vec{0} = \vec{0}$, $0 \cdot \vec{A} = \vec{0}$.
    *   Physical meaning: If an object returns to its starting point, its displacement is a null vector.

### Vector Subtraction

-   **Definition:** Subtraction of vector $\vec{B}$ from vector $\vec{A}$ is defined as the addition of $\vec{A}$ and $(-\vec{B})$.
    *   $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$
-   **Intuition:** To subtract $\vec{B}$, flip its direction and then add it.
-   **Why it matters:** Provides a way to find the difference between vector quantities (e.g., change in velocity for acceleration).
-   **Important observations:** Graphically, draw $\vec{A}$ and $-\vec{B}$ head-to-tail, or use parallelogram law with $\vec{A}$ and $-\vec{B}$.

## 3.5 Resolution of Vectors

-   **Definition:** The process of splitting a single vector into two or more component vectors whose vector sum equals the original vector. Usually, these components are perpendicular.
-   **Intuition:** Breaking down a complex movement into simpler, independent movements (e.g., moving diagonally is like moving sideways AND moving forward).
-   **Why it matters:** Simplifies vector operations. It allows us to analyze motion along independent axes.
-   **Important observations:**
    *   A vector $\vec{A}$ can be resolved into components along any two non-collinear vectors $\vec{a}$ and $\vec{b}$ in the same plane: $\vec{A} = \lambda\vec{a} + \mu\vec{b}$.
    *   Most convenient to resolve along perpendicular axes (rectangular components).

### Unit Vectors

-   **Definition:** A vector with a magnitude of one unit, used solely to specify direction. It is dimensionless and unitless.
-   **Intuition:** Like an arrow pointer, showing "which way" without any specific length.
-   **Why it matters:** Essential for expressing vectors in component form and for distinguishing vector directions in coordinate systems.
-   **Real world examples:** $\hat{i}$, $\hat{j}$, $\hat{k}$ for x, y, z axes respectively.
-   **Important observations:**
    *   $\hat{i}$, $\hat{j}$, $\hat{k}$ are mutually perpendicular.
    *   $|\hat{i}| = |\hat{j}| = |\hat{k}| = 1$.
    *   Any vector $\vec{A}$ can be written as $\vec{A} = |\vec{A}|\hat{n}$, where $\hat{n}$ is the unit vector in the direction of $\vec{A}$.

### Rectangular Components of a Vector

-   **Definition:** For a vector $\vec{A}$ in the x-y plane making an angle $\theta$ with the x-axis:
    *   $A_x = A \cos\theta$ (x-component, scalar)
    *   $A_y = A \sin\theta$ (y-component, scalar)
    *   Vector form: $\vec{A} = A_x \hat{i} + A_y \hat{j}$
-   **Intuition:** The "shadow" a vector casts on the x-axis and y-axis.
-   **Why it matters:** Allows analytical (algebraic) manipulation of vectors.
-   **Important observations:**
    *   Magnitude of $\vec{A}$: $A = \sqrt{A_x^2 + A_y^2}$.
    *   Direction of $\vec{A}$: $\tan\theta = \frac{A_y}{A_x} \implies \theta = \tan^{-1}\left(\frac{A_y}{A_x}\right)$.
    *   Components can be positive, negative, or zero depending on the quadrant.
    *   For 3D: $\vec{A} = A_x \hat{i} + A_y \hat{j} + A_z \hat{k}$. Magnitude $A = \sqrt{A_x^2 + A_y^2 + A_z^2}$.
    *   $A_x = A \cos\alpha$, $A_y = A \cos\beta$, $A_z = A \cos\gamma$ where $\alpha, \beta, \gamma$ are angles with x, y, z axes respectively. $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.

## 3.6 Vector Addition – Analytical Method

-   **Definition:** Adding vectors by summing their respective components.
-   **Intuition:** If you walk 2m East and 3m North, then later 1m East and 4m North, your total journey is (2+1)m East and (3+4)m North.
-   **Why it matters:** Most accurate and efficient method for calculations, especially in NEET.
-   **Method:**
    *   Let $\vec{A} = A_x \hat{i} + A_y \hat{j}$ and $\vec{B} = B_x \hat{i} + B_y \hat{j}$.
    *   The resultant $\vec{R} = \vec{A} + \vec{B}$ is given by:
        *   $\vec{R} = (A_x + B_x) \hat{i} + (A_y + B_y) \hat{j}$
    *   So, $R_x = A_x + B_x$ and $R_y = A_y + B_y$.
    *   Magnitude of $\vec{R}$: $R = \sqrt{R_x^2 + R_y^2}$.
    *   Direction of $\vec{R}$: $\tan\phi = \frac{R_y}{R_x}$.
-   **Important observations:**
    *   Extends easily to 3D: $R_z = A_z + B_z$.
    *   For subtraction: $\vec{A} - \vec{B} = (A_x - B_x) \hat{i} + (A_y - B_y) \hat{j}$.

## 3.7 Motion in a Plane

### 3.7.1 Position Vector and Displacement

-   **Position Vector in 2D:** $\vec{r} = x\hat{i} + y\hat{j}$
    *   x and y are the coordinates of the object.
-   **Displacement in 2D:**
    *   If initial position is $\vec{r} = x\hat{i} + y\hat{j}$ and final position is $\vec{r}' = x'\hat{i} + y'\hat{j}$.
    *   $\Delta\vec{r} = \vec{r}' - \vec{r} = (x' - x)\hat{i} + (y' - y)\hat{j} = \Delta x \hat{i} + \Delta y \hat{j}$.

### Velocity

-   **Average Velocity ($\vec{v}_{avg}$):**
    *   **Definition:** Ratio of total displacement to the total time interval.
    *   $\vec{v}_{avg} = \frac{\Delta\vec{r}}{\Delta t} = \frac{\Delta x}{\Delta t}\hat{i} + \frac{\Delta y}{\Delta t}\hat{j}$.
    *   **Direction:** Same as the direction of $\Delta\vec{r}$.
-   **Instantaneous Velocity ($\vec{v}$):**
    *   **Definition:** The limiting value of the average velocity as the time interval approaches zero. It's the derivative of position vector with respect to time.
    *   $\vec{v} = \lim_{\Delta t \to 0} \frac{\Delta\vec{r}}{\Delta t} = \frac{d\vec{r}}{dt}$.
    *   **Component form:** $\vec{v} = v_x\hat{i} + v_y\hat{j}$, where $v_x = \frac{dx}{dt}$ and $v_y = \frac{dy}{dt}$.
    *   **Magnitude (Speed):** $|\vec{v}| = v = \sqrt{v_x^2 + v_y^2}$.
    *   **Direction:** Tangent to the path of the object at that instant. $\tan\theta = \frac{v_y}{v_x}$.
-   **Important observations:**
    *   The direction of instantaneous velocity is always tangential to the path of motion.

### Acceleration

-   **Average Acceleration ($\vec{a}_{avg}$):**
    *   **Definition:** Ratio of change in velocity to the time interval.
    *   $\vec{a}_{avg} = \frac{\Delta\vec{v}}{\Delta t} = \frac{\Delta v_x}{\Delta t}\hat{i} + \frac{\Delta v_y}{\Delta t}\hat{j}$.
-   **Instantaneous Acceleration ($\vec{a}$):**
    *   **Definition:** The limiting value of the average acceleration as the time interval approaches zero. It's the derivative of velocity vector with respect to time.
    *   $\vec{a} = \lim_{\Delta t \to 0} \frac{\Delta\vec{v}}{\Delta t} = \frac{d\vec{v}}{dt}$.
    *   **Component form:** $\vec{a} = a_x\hat{i} + a_y\hat{j}$, where $a_x = \frac{dv_x}{dt} = \frac{d^2x}{dt^2}$ and $a_y = \frac{dv_y}{dt} = \frac{d^2y}{dt^2}$.
    *   **Magnitude:** $|\vec{a}| = a = \sqrt{a_x^2 + a_y^2}$.
-   **Important observations:**
    *   In 2D or 3D motion, velocity and acceleration vectors are generally NOT along the same line (unlike 1D motion). They can have any angle between 0° and 180°.
    *   The direction of acceleration is the direction of the change in velocity vector ($\Delta\vec{v}$).

## 3.8 Motion in a Plane with Constant Acceleration

-   **Definition:** An object moves such that its acceleration vector ($\vec{a}$) remains constant in both magnitude and direction.
-   **Intuition:** Imagine a steady push or pull acting on an object moving in a flat field, regardless of its speed or direction.
-   **Why it matters:** Simplifies calculations and forms the basis for projectile motion.
-   **Vector Equations of Motion:**
    *   Velocity: $\vec{v} = \vec{v}_0 + \vec{a}t$
    *   Position: $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \frac{1}{2}\vec{a}t^2$
    (Note: There's no vector equivalent for $v^2 = u^2 + 2as$ directly.)
-   **Component Equations (Independence of Motion):**
    *   This is the most powerful concept: motion in perpendicular directions (x and y) can be treated independently.
    *   **Along x-axis:**
        *   $v_x = v_{0x} + a_x t$
        *   $x = x_0 + v_{0x} t + \frac{1}{2}a_x t^2$
    *   **Along y-axis:**
        *   $v_y = v_{0y} + a_y t$
        *   $y = y_0 + v_{0y} t + \frac{1}{2}a_y t^2$
-   **Important observations:**
    *   The same kinematic equations from 1D motion apply to each component independently.
    *   Time ($t$) is the common link between the x and y motions.

## 3.9 Projectile Motion

-   **Definition:** The motion of an object (projectile) launched into the air, subjected only to the force of gravity (neglecting air resistance).
-   **Intuition:** A thrown ball, a fired cannonball, water from a fountain.
-   **Why it matters:** Fundamental concept, explains many real-world phenomena, frequently tested in NEET.
-   **Assumptions:**
    1.  Air resistance is negligible.
    2.  Acceleration due to gravity ($g$) is constant in magnitude and direction (downwards).
    3.  Earth's curvature and rotation are neglected.
-   **Coordinate System:** Usually, origin at the point of projection, x-axis horizontal, y-axis vertical upwards.
    *   Initial position: $x_0 = 0, y_0 = 0$.
    *   Acceleration components: $a_x = 0$, $a_y = -g$.
-   **Initial Velocity:** Let $\vec{v}_0$ be the initial velocity at an angle $\theta_0$ with the horizontal.
    *   $v_{0x} = v_0 \cos\theta_0$
    *   $v_{0y} = v_0 \sin\theta_0$

### Equations of Motion for Projectile

1.  **Horizontal Motion (Constant Velocity):**
    *   $v_x = v_{0x} = v_0 \cos\theta_0$ (velocity is constant)
    *   $x = (v_0 \cos\theta_0) t$
2.  **Vertical Motion (Constant Acceleration - Free Fall):**
    *   $v_y = v_{0y} + a_y t = v_0 \sin\theta_0 - gt$
    *   $y = v_{0y} t + \frac{1}{2}a_y t^2 = (v_0 \sin\theta_0) t - \frac{1}{2}gt^2$

### Equation of Trajectory (Path of Projectile)

-   **Definition:** The equation relating y to x, found by eliminating 't' from the x and y equations.
-   **Equation:** $y = (\tan\theta_0) x - \frac{g}{2(v_0 \cos\theta_0)^2} x^2$
-   **Important observations:** This is the equation of a parabola ($y = Ax - Bx^2$). The path of a projectile is always parabolic.

### Key Parameters of Projectile Motion

1.  **Time of Maximum Height ($t_m$):** Time taken to reach the highest point (where $v_y = 0$).
    *   $t_m = \frac{v_0 \sin\theta_0}{g}$
2.  **Maximum Height ($h_m$):** The maximum vertical distance reached.
    *   $h_m = \frac{(v_0 \sin\theta_0)^2}{2g}$
3.  **Time of Flight ($T_f$):** Total time the projectile is in the air (when it returns to its initial vertical level, i.e., $y=0$).
    *   $T_f = \frac{2v_0 \sin\theta_0}{g} = 2t_m$ (due to symmetry of parabolic path).
4.  **Horizontal Range ($R$):** The horizontal distance traveled during the time of flight ($T_f$).
    *   $R = (v_0 \cos\theta_0) T_f = (v_0 \cos\theta_0) \left(\frac{2v_0 \sin\theta_0}{g}\right)$
    *   $R = \frac{v_0^2 \sin(2\theta_0)}{g}$
    *   **Maximum Range ($R_{max}$):** Occurs when $\sin(2\theta_0) = 1$, so $2\theta_0 = 90^\circ \implies \theta_0 = 45^\circ$.
        *   $R_{max} = \frac{v_0^2}{g}$ (at $\theta_0 = 45^\circ$)
    *   **Important observation (Galileo's statement):** For a given $v_0$, the ranges are equal for complementary angles of projection, i.e., $\theta_0$ and $(90^\circ - \theta_0)$. E.g., range at $30^\circ$ is same as range at $60^\circ$.

## 3.10 Uniform Circular Motion (UCM)

-   **Definition:** Motion of an object along a circular path at a constant speed.
-   **Intuition:** A car taking a steady turn at a constant speed, a point on a rotating fan blade.
-   **Why it matters:** Explains the motion of objects in circles, crucial for understanding rotation, planetary motion, etc.
-   **Important observations:**
    *   **Speed is constant**, but **velocity is changing** continuously (due to change in direction).
    *   Because velocity is changing, there must be an **acceleration**.

### Centripetal Acceleration ($\vec{a}_c$)

-   **Definition:** The acceleration experienced by an object in UCM, always directed towards the center of the circular path. "Centripetal" means "center-seeking".
-   **Intuition:** It's the "pull" needed to keep the object from flying off in a straight line.
-   **Why it matters:** This acceleration is responsible for changing the direction of velocity.
-   **Magnitude:**
    *   $a_c = \frac{v^2}{R}$ (where $v$ is linear speed, $R$ is radius)
-   **Direction:** Always radially inward, towards the center of the circle.
-   **Important observations:**
    *   The centripetal acceleration vector is **NOT constant** because its direction continuously changes, even though its magnitude is constant.
    *   The velocity vector is always tangential to the circle and perpendicular to the radius vector (and thus perpendicular to $\vec{a}_c$).

### Angular Speed ($\omega$)

-   **Definition:** The rate of change of angular displacement ($\Delta\theta$).
-   **Formula:** $\omega = \frac{\Delta\theta}{\Delta t}$ (units: rad/s).
-   **Relationship with Linear Speed ($v$):** $v = R\omega$
    *   **Intuition:** For a given angular speed, points farther from the center (larger R) have greater linear speed.
-   **Centripetal Acceleration in terms of $\omega$:**
    *   $a_c = R\omega^2$ (substituting $v=R\omega$ into $a_c = v^2/R$)

### Time Period ($T$) and Frequency ($\nu$)

-   **Time Period ($T$):**
    *   **Definition:** Time taken to complete one full revolution.
    *   **Formula:** $T = \frac{2\pi R}{v} = \frac{2\pi}{\omega}$ (units: seconds).
-   **Frequency ($\nu$):**
    *   **Definition:** Number of revolutions completed per unit time.
    *   **Formula:** $\nu = \frac{1}{T} = \frac{\omega}{2\pi}$ (units: Hz or s$^{-1}$).
-   **Centripetal Acceleration in terms of $\nu$:**
    *   $a_c = 4\pi^2 \nu^2 R$

---

# NCERT GOLDEN LINES

1.  **"A scalar quantity is a quantity with magnitude only. It is specified completely by a single number, along with the proper unit."**
    *   **Explanation:** This concisely defines scalars. Emphasizes that "single number" implies magnitude, and "proper unit" is standard. Key for distinguishing from vectors.
2.  **"A vector quantity is a quantity that has both a magnitude and a direction and obeys the triangle law of addition or equivalently the parallelogram law of addition."**
    *   **Explanation:** The most critical definition of a vector. The emphasis on obeying vector laws (triangle/parallelogram) is crucial. Without this, quantities like electric current (which has magnitude and direction but adds algebraically, not vectorially) would be incorrectly classified as vectors.
3.  **"It is important to note that displacement vector is the straight line joining the initial and final positions and does not depend on the actual path undertaken by the object between the two positions."**
    *   **Explanation:** Highlights the path-independent nature of displacement, a key conceptual difference from distance/path length. Frequently tested concept.
4.  **"Therefore, the magnitude of displacement is either less or equal to the path length of an object between two points."**
    *   **Explanation:** This is a fundamental inequality. Equality holds only for straight-line motion without change in direction. Often used in conceptual questions.
5.  **"Two vectors A and B are said to be equal if, and only if, they have the same magnitude and the same direction."**
    *   **Explanation:** Precise definition of vector equality. Important for understanding free vectors and when two vector quantities are truly the same.
6.  **"In our study, vectors do not have fixed locations. So displacing a vector parallel to itself leaves the vector unchanged. Such vectors are called free vectors."**
    *   **Explanation:** Clarifies the concept of "free vectors" which are assumed in most introductory physics problems. Important when dealing with addition/subtraction where vectors are often shifted.
7.  **"The factor λ by which a vector A is multiplied could be a scalar having its own physical dimension. Then, the dimension of λ A is the product of the dimensions of λ and A."**
    *   **Explanation:** Reinforces dimensional analysis. If you multiply velocity (L/T) by time (T), you get displacement (L). Dimensions must be consistent.
8.  **"Since the magnitude of a null vector is zero, its direction cannot be specified."**
    *   **Explanation:** Important property of the null vector. Its undefined direction prevents it from being useful for orientation.
9.  **"The direction of velocity at any point on the path of an object is tangential to the path at that point and is in the direction of motion."**
    *   **Explanation:** Key characteristic of instantaneous velocity. Visually represents how velocity behaves along a curved path.
10. **"Note that in one dimension, the velocity and the acceleration of an object are always along the same straight line (either in the same direction or in the opposite direction). However, for motion in two or three dimensions, velocity and acceleration vectors may have any angle between 0° and 180° between them."**
    *   **Explanation:** Crucial distinction between 1D and higher-dimensional motion. In 2D/3D, acceleration can change direction without changing speed (e.g., UCM) or change speed without changing direction, or both.
11. **"One immediate interpretation of Eq.(3.34b) is that the motions in x- and y-directions can be treated independently of each other."**
    *   **Explanation:** The most significant simplification in 2D kinematics. Breaking down a 2D problem into two 1D problems along perpendicular axes. This is the foundation of projectile motion analysis.
12. **"The path of the projectile is a parabola."**
    *   **Explanation:** Direct statement about the shape of the trajectory under ideal projectile motion conditions.
13. **"Tf = 2 tm, which is expected because of the symmetry of the parabolic path."**
    *   **Explanation:** Highlights the symmetry in ideal projectile motion, where time to rise equals time to fall to the same horizontal level.
14. **"Equation (3.42a) shows that for a given projection velocity vo , R is maximum when sin 2θ0 is maximum, i.e., when θ0 = 45°."**
    *   **Explanation:** Crucial condition for maximum range. Often tested directly.
15. **"Galileo, in his book Two new sciences, stated that 'for elevations which exceed or fall short of 45° by equal amounts, the ranges are equal'."**
    *   **Explanation:** The "complementary angles" property of range. For example, $30^\circ$ and $60^\circ$ (both $45^\circ \pm 15^\circ$) have the same range. Often forms the basis of conceptual or calculation questions.
16. **"When an object follows a circular path at a constant speed, the motion of the object is called uniform circular motion."**
    *   **Explanation:** Defines UCM precisely. Emphasizes "constant speed," which often misleads students into thinking there's no acceleration.
17. **"Since the velocity of the object is changing continuously in direction, the object undergoes acceleration."**
    *   **Explanation:** Directly addresses the common misconception: constant speed DOES NOT mean zero acceleration in UCM. Change in direction implies acceleration.
18. **"Thus, we find that the acceleration of an object in uniform circular motion is always directed towards the centre of the circle."**
    *   **Explanation:** Defines the direction of centripetal acceleration, which is vital.
19. **"Therefore, a centripetal acceleration is not a constant vector."**
    *   **Explanation:** Extremely important conceptual point. While its magnitude is constant, its direction changes continuously, so the vector itself is not constant.

---

# FORMULA SHEET

| Concept                       | Formula                                                 | Variable Meanings                                                                                                    | Units (SI)          | When to Use                                                                                              | Common Mistakes                                                                                       |
| :---------------------------- | :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------- | :------------------ | :------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| **Vector Magnitude (2D)**     | $A = \sqrt{A_x^2 + A_y^2}$                              | $A$: Magnitude, $A_x, A_y$: x, y components                                                                          | unit of A           | When components are known, to find resultant magnitude.                                                  | Forgetting to square components or take square root.                                                  |
| **Vector Direction (2D)**     | $\tan\theta = \frac{A_y}{A_x}$                          | $\theta$: Angle with +x-axis, $A_x, A_y$: x, y components                                                            | radians or degrees  | To find the direction of a vector from its components.                                                   | Not considering the quadrant for $\theta$. Using $\sin$ or $\cos$ instead of $\tan$.                  |
| **Vector Addition (Analytical)**| $\vec{R} = (A_x+B_x)\hat{i} + (A_y+B_y)\hat{j}$      | $\vec{R}$: Resultant, $A_x, A_y, B_x, B_y$: Components of $\vec{A}, \vec{B}$                                        | unit of vector      | Adding two or more vectors using their components.                                                       | Incorrectly adding components (e.g., $A_x+B_y$). Forgetting sign of components.                       |
| **Parallelogram Law (Magnitude)**| $R = \sqrt{A^2+B^2+2AB\cos\theta}$                    | $R$: Magnitude of resultant, $A, B$: Magnitudes of vectors, $\theta$: Angle BETWEEN $\vec{A}$ and $\vec{B}$       | unit of vector      | Finding magnitude of resultant of two vectors when their magnitudes and angle between them are known.      | Using $\theta$ as angle with x-axis or angle of resultant. Using angle $> 180^\circ$.              |
| **Parallelogram Law (Direction)**| $\tan\alpha = \frac{B\sin\theta}{A+B\cos\theta}$        | $\alpha$: Angle of $\vec{R}$ with $\vec{A}$, $A, B$: Magnitudes, $\theta$: Angle between $\vec{A}$ and $\vec{B}$ | radians or degrees  | Finding direction of resultant with respect to one of the vectors.                                       | Confusing $\alpha$ with $\theta$. Incorrectly swapping A and B in denominator.                      |
| **Position Vector**           | $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$              | $x,y,z$: Coordinates, $\hat{i},\hat{j},\hat{k}$: Unit vectors                                                        | m                   | Representing the location of a point/object.                                                             | Forgetting $\hat{i},\hat{j},\hat{k}$.                                                                 |
| **Displacement Vector**       | $\Delta\vec{r} = \Delta x\hat{i} + \Delta y\hat{j} + \Delta z\hat{k}$| $\Delta x, \Delta y, \Delta z$: Changes in coordinates                                                              | m                   | Finding the net change in position.                                                                      | Confusing with path length.                                                                           |
| **Instantaneous Velocity**    | $\vec{v} = \frac{d\vec{r}}{dt} = v_x\hat{i} + v_y\hat{j} + v_z\hat{k}$| $v_x = \frac{dx}{dt}$, etc.                                                                                          | m/s                 | When position is given as a function of time, to find velocity.                                          | Not differentiating correctly or remembering to apply to each component.                               |
| **Instantaneous Acceleration**| $\vec{a} = \frac{d\vec{v}}{dt} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$| $a_x = \frac{dv_x}{dt}$, etc.                                                                                          | m/s²                | When velocity is given as a function of time, to find acceleration.                                      | Not differentiating correctly or remembering to apply to each component.                               |
| **Kinematic Eq. (Constant $\vec{a}$)**| $\vec{v} = \vec{v}_0 + \vec{a}t$                     | $\vec{v}_0$: Initial velocity, $\vec{v}$: Final velocity, $\vec{a}$: Constant acceleration, $t$: time                 | m/s, m/s², s        | For motion with constant acceleration in vector form.                                                    | Trying to apply scalar kinematic equations to vectors (e.g., $v^2=u^2+2as$ is not a vector equation). |
| **Kinematic Eq. (Constant $\vec{a}$)**| $\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$| $\vec{r}_0$: Initial position, $\vec{r}$: Final position                                                              | m, m/s, m/s², s     | For motion with constant acceleration in vector form.                                                    | Same as above.                                                                                        |
| **Projectile: x-coord**       | $x = (v_0\cos\theta_0)t$                               | $v_0$: Initial speed, $\theta_0$: Angle of projection                                                                | m, m/s, s           | To find horizontal displacement at time $t$. ($a_x = 0$)                                                 | Using $\sin\theta_0$ for x-component.                                                                 |
| **Projectile: y-coord**       | $y = (v_0\sin\theta_0)t - \frac{1}{2}gt^2$             | $g$: acceleration due to gravity (9.8 m/s²)                                                                          | m, m/s, s           | To find vertical displacement at time $t$. ($a_y = -g$)                                                  | Forgetting the sign of $g$ (if y-axis is upwards). Using $\cos\theta_0$ for y-component.              |
| **Projectile: x-velocity**    | $v_x = v_0\cos\theta_0$                                |                                                                                                                      | m/s                 | Horizontal velocity is constant.                                                                         | Assuming $v_x$ changes.                                                                               |
| **Projectile: y-velocity**    | $v_y = v_0\sin\theta_0 - gt$                           |                                                                                                                      | m/s                 | To find vertical velocity at time $t$.                                                                   | Forgetting the sign of $g$.                                                                           |
| **Projectile: Time of Max Ht**| $t_m = \frac{v_0\sin\theta_0}{g}$                      |                                                                                                                      | s                   | Time to reach the peak of the trajectory ($v_y = 0$).                                                    | Not dividing by $g$.                                                                                  |
| **Projectile: Max Height**    | $h_m = \frac{v_0^2\sin^2\theta_0}{2g}$                  |                                                                                                                      | m                   | Maximum vertical distance achieved.                                                                      | Forgetting square on $\sin\theta_0$ or $v_0$. Not using $2g$ in denominator.                          |
| **Projectile: Time of Flight**| $T_f = \frac{2v_0\sin\theta_0}{g}$                     |                                                                                                                      | s                   | Total time in air for projection from ground to ground.                                                  | Using $t_m$ instead of $T_f$.                                                                         |
| **Projectile: Horizontal Range**| $R = \frac{v_0^2\sin(2\theta_0)}{g}$                   |                                                                                                                      | m                   | Total horizontal distance covered.                                                                       | Using $\sin^2\theta_0$ instead of $\sin(2\theta_0)$.                                                  |
| **UCM: Linear & Angular Speed**| $v = R\omega$                                           | $v$: Linear speed, $R$: Radius, $\omega$: Angular speed                                                              | m/s, m, rad/s       | Relating linear motion to rotational motion.                                                             | Using degrees for $\omega$.                                                                           |
| **UCM: Centripetal Acceleration**| $a_c = \frac{v^2}{R}$ or $a_c = R\omega^2$              | $a_c$: Centripetal acceleration                                                                                      | m/s²                | To calculate the magnitude of acceleration towards the center.                                           | Confusing centripetal with tangential acceleration. Forgetting the vector nature of acceleration.    |
| **UCM: Angular Speed & Period**| $\omega = \frac{2\pi}{T} = 2\pi\nu$                    | $T$: Time period, $\nu$: Frequency                                                                                   | rad/s, s, Hz        | Relating angular speed to how fast an object completes cycles.                                           | Not using $2\pi$ for full circle in radians.                                                          |
| **UCM: Centripetal Accel. in T/$\nu$**| $a_c = \frac{4\pi^2 R}{T^2} = 4\pi^2 \nu^2 R$   |                                                                                                                      | m/s²                | Alternative forms for centripetal acceleration using period or frequency.                                | Errors in squaring $T$ or $\nu$.                                                                      |

---

# DERIVATIONS AND LOGIC

## 1. Parallelogram Law of Vector Addition (Magnitude & Direction)

**Intuition:** Imagine two forces acting on an object from the same point. The parallelogram law tells you the size and direction of the single force that would have the same effect.

**Logic:**
Let $\vec{A}$ and $\vec{B}$ be two vectors with their tails at a common point O, making an angle $\theta$ between them. Let $\vec{R}$ be their resultant.
1.  Draw a parallelogram OQSP with $\vec{A} = \vec{OP}$ and $\vec{B} = \vec{OQ}$ as adjacent sides.
2.  The resultant $\vec{R} = \vec{OS}$ is the diagonal from O.
3.  From point Q, draw a perpendicular SN to the line OP extended.
4.  In $\triangle QNP$:
    *   $QN = B \sin\theta$
    *   $PN = B \cos\theta$
5.  In the right-angled $\triangle OSN$:
    *   $OS^2 = ON^2 + SN^2$
    *   $ON = OP + PN = A + B \cos\theta$
    *   $SN = B \sin\theta$
    *   Substitute these into the equation for $OS^2$:
        $R^2 = (A + B \cos\theta)^2 + (B \sin\theta)^2$
        $R^2 = A^2 + 2AB \cos\theta + B^2 \cos^2\theta + B^2 \sin^2\theta$
        $R^2 = A^2 + B^2 (\cos^2\theta + \sin^2\theta) + 2AB \cos\theta$
        Since $\cos^2\theta + \sin^2\theta = 1$:
        **$R = \sqrt{A^2 + B^2 + 2AB \cos\theta}$** (Magnitude of resultant)
6.  For direction, let $\vec{R}$ make an angle $\alpha$ with $\vec{A}$ (the line OP):
    *   In right-angled $\triangle OSN$:
        $\tan\alpha = \frac{SN}{ON} = \frac{B \sin\theta}{A + B \cos\theta}$
        **$\tan\alpha = \frac{B \sin\theta}{A + B \cos\theta}$** (Direction of resultant)

## 2. Derivation of Projectile Motion Equations

**Intuition:** Since horizontal and vertical motions are independent, we treat them as two separate 1D problems, with time as the common link.

**Assumptions:**
*   Initial position: $(x_0, y_0) = (0, 0)$
*   Initial velocity: $\vec{v}_0$ at angle $\theta_0$ with horizontal.
    *   $v_{0x} = v_0 \cos\theta_0$
    *   $v_{0y} = v_0 \sin\theta_0$
*   Acceleration: $a_x = 0$, $a_y = -g$ (upward is positive y).

**Logic:** We use the 1D kinematic equations for constant acceleration for x and y components.

*   **Horizontal Motion (Constant velocity, $a_x=0$):**
    *   Velocity: $v_x = v_{0x} + a_x t \implies v_x = v_0 \cos\theta_0 + 0 \cdot t \implies \mathbf{v_x = v_0 \cos\theta_0}$
    *   Position: $x = x_0 + v_{0x} t + \frac{1}{2} a_x t^2 \implies x = 0 + (v_0 \cos\theta_0) t + 0 \implies \mathbf{x = (v_0 \cos\theta_0) t}$

*   **Vertical Motion (Constant acceleration, $a_y=-g$):**
    *   Velocity: $v_y = v_{0y} + a_y t \implies \mathbf{v_y = v_0 \sin\theta_0 - gt}$
    *   Position: $y = y_0 + v_{0y} t + \frac{1}{2} a_y t^2 \implies \mathbf{y = (v_0 \sin\theta_0) t - \frac{1}{2}gt^2}$

**Derivation of Trajectory Equation:**
1.  From the horizontal position equation: $t = \frac{x}{v_0 \cos\theta_0}$.
2.  Substitute this 't' into the vertical position equation:
    $y = (v_0 \sin\theta_0) \left(\frac{x}{v_0 \cos\theta_0}\right) - \frac{1}{2}g \left(\frac{x}{v_0 \cos\theta_0}\right)^2$
    $y = \left(\frac{\sin\theta_0}{\cos\theta_0}\right) x - \frac{g x^2}{2v_0^2 \cos^2\theta_0}$
    **$y = (\tan\theta_0) x - \frac{g x^2}{2v_0^2 \cos^2\theta_0}$**

## 3. Derivation of Centripetal Acceleration ($a_c = v^2/R$)

**Intuition:** Imagine an object moving in a circle. Its velocity vector is constantly changing direction. The acceleration is the rate of this change in direction.

**Logic (Vector Method - Limiting Process):**
1.  Consider an object moving in a circle of radius R with constant speed $v$.
2.  Let the position vector at time $t$ be $\vec{r}$ and at $t+\Delta t$ be $\vec{r}'$.
3.  Let the velocity vector at time $t$ be $\vec{v}$ and at $t+\Delta t$ be $\vec{v}'$.
4.  $\vec{v}$ is perpendicular to $\vec{r}$, and $\vec{v}'$ is perpendicular to $\vec{r}'$.
5.  Draw $\vec{r}$, $\vec{r}'$ from the center C. Draw $\vec{v}$, $\vec{v}'$ from a common point.
6.  The angle between $\vec{r}$ and $\vec{r}'$ is $\Delta\theta$. Since $\vec{v} \perp \vec{r}$ and $\vec{v}' \perp \vec{r}'$, the angle between $\vec{v}$ and $\vec{v}'$ is also $\Delta\theta$.
7.  The triangle formed by $\vec{r}$, $\vec{r}'$ and $\Delta\vec{r}$ (where $\Delta\vec{r} = \vec{r}' - \vec{r}$) is isosceles with sides R, R.
8.  The triangle formed by $\vec{v}$, $\vec{v}'$ and $\Delta\vec{v}$ (where $\Delta\vec{v} = \vec{v}' - \vec{v}$) is also isosceles with sides $v$, $v$.
9.  These two triangles are similar (isosceles triangles with the same apex angle $\Delta\theta$).
10. From similar triangles, the ratio of base to side length is equal:
    $\frac{|\Delta\vec{r}|}{R} = \frac{|\Delta\vec{v}|}{v}$
    So, $|\Delta\vec{v}| = \frac{v}{R} |\Delta\vec{r}|$
11. Now, average acceleration $\vec{a}_{avg} = \frac{\Delta\vec{v}}{\Delta t}$.
    Magnitude: $|\vec{a}_{avg}| = \frac{|\Delta\vec{v}|}{\Delta t} = \frac{v}{R} \frac{|\Delta\vec{r}|}{\Delta t}$.
12. Instantaneous acceleration $a_c = \lim_{\Delta t \to 0} |\vec{a}_{avg}| = \lim_{\Delta t \to 0} \frac{v}{R} \frac{|\Delta\vec{r}|}{\Delta t}$.
13. As $\Delta t \to 0$, the arc length between $\vec{r}$ and $\vec{r}'$ becomes approximately equal to $|\Delta\vec{r}|$. The linear distance covered is $v \Delta t$. So, $|\Delta\vec{r}| \approx v \Delta t$.
    Therefore, $\lim_{\Delta t \to 0} \frac{|\Delta\vec{r}|}{\Delta t} = v$.
14. Substituting this limit:
    **$a_c = \frac{v}{R} \cdot v = \frac{v^2}{R}$**
15. **Direction:** As $\Delta t \to 0$, $\Delta\vec{r}$ becomes tangent to the circle, and $\Delta\vec{v}$ becomes perpendicular to $\vec{v}$. Since $\vec{v}$ is tangential, $\Delta\vec{v}$ (and thus $\vec{a}_c$) points towards the center.

---

# NEET HIGH-YIELD CONCEPTS

1.  **Vector Addition and Resolution by Components:** This is the most practical method for solving NEET problems involving multiple vectors. Mastery of $R_x = \Sigma A_x$, $R_y = \Sigma A_y$, $R = \sqrt{R_x^2 + R_y^2}$, and $\tan\theta = R_y/R_x$ is crucial.
2.  **Projectile Motion Formulas and Applications:**
    *   Direct application of $R = \frac{v_0^2 \sin(2\theta_0)}{g}$, $h_m = \frac{v_0^2 \sin^2\theta_0}{2g}$, $T_f = \frac{2v_0 \sin\theta_0}{g}$.
    *   **Maximum Range:** $\theta = 45^\circ$, $R_{max} = v_0^2/g$.
    *   **Complementary Angles for Range:** $\theta$ and $90^\circ - \theta$ give the same range.
    *   Problems involving a horizontal projection (often called "horizontal projectile") from a height, where $v_{0y}=0$.
    *   Hitting a target, relative motion in projectile.
    *   The independence of horizontal and vertical motion is the key logic.
3.  **Uniform Circular Motion (UCM) Concepts:**
    *   **Centripetal Acceleration:** Magnitude ($v^2/R$ or $R\omega^2$) and its constant inward direction.
    *   **Vector Nature of Acceleration:** Understanding that $\vec{a}_c$ is *not* a constant vector due to its changing direction.
    *   Relationships between $v, R, \omega, T, \nu$.
    *   Conceptual questions distinguishing UCM from non-uniform circular motion.
4.  **Kinematic Equations in 2D with Constant Acceleration:** Applying $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$ in component form for specific scenarios (e.g., finding position/velocity given constant acceleration components).
5.  **Distinction between Scalars and Vectors:** Conceptual questions requiring identification of scalar/vector quantities, and understanding why certain quantities (like electric current) are scalars despite having direction.
6.  **Displacement vs. Distance & Average Velocity vs. Average Speed:** Conceptual clarity on when magnitudes are equal or unequal.

---

# CONCEPTUAL TRAPS

1.  **Scalar vs. Vector (Electric Current):** Students often mistake electric current as a vector because it has magnitude and direction. However, it *does not obey the triangle law of addition*, hence it's a **scalar**. This is a classic trap.
2.  **Magnitude of Displacement vs. Path Length:** These are rarely equal. The magnitude of displacement is the shortest distance. Path length is the actual distance travelled. Always $|\text{displacement}| \le \text{path length}$.
3.  **Average Velocity vs. Average Speed:** Similarly, $|\vec{v}_{avg}| \le \text{average speed}$. They are equal only if the object moves in a straight line without changing direction.
4.  **Vector Addition as Scalar Addition:** Students sometimes try to add magnitudes directly (e.g., if $\vec{A}$ has magnitude 3 and $\vec{B}$ has magnitude 4, the resultant is NOT necessarily 7). The angle between them matters.
5.  **Incorrect Resolution of Vectors:** Confusing $\sin\theta$ and $\cos\theta$. Remember: The component *adjacent* to the angle $\theta$ uses $\cos\theta$, and the component *opposite* to the angle $\theta$ uses $\sin\theta$. (Often leads to $A_x = A\sin\theta$ and $A_y = A\cos\theta$ if $\theta$ is measured from the y-axis).
6.  **Instantaneous Velocity and Acceleration Collinearity in 2D/3D:** In 1D, they are always collinear. In 2D/3D, they are generally NOT collinear. For example, in UCM, velocity is tangential, and acceleration is radial (perpendicular).
7.  **Projectile Motion - Constant Velocity:** Students might incorrectly assume the velocity of a projectile is constant or that its horizontal component changes. **Horizontal velocity ($v_x$) is constant**; **vertical velocity ($v_y$) changes** due to gravity. The overall speed ($|\vec{v}| = \sqrt{v_x^2 + v_y^2}$) is NOT constant.
8.  **Projectile Motion - Acceleration at Max Height:** At the maximum height, $v_y = 0$, but the acceleration is still **$g$ downwards**. It's not zero.
9.  **UCM - No Acceleration:** A common trap. "Constant speed" often leads students to conclude "zero acceleration." But velocity is a vector, and its direction is continuously changing, hence there is always **centripetal acceleration**.
10. **UCM - Centripetal Acceleration as a Constant Vector:** While the *magnitude* of centripetal acceleration ($v^2/R$) is constant, its *direction* continuously changes. Therefore, $\vec{a}_c$ is **not a constant vector**.
11. **Relative Velocity Direction:** In problems involving relative velocity (e.g., rain falling, boat in river, planes flying), correctly identifying the direction of the relative velocity vector is crucial. For $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$, remember vector subtraction.

---

# MEMORY BOOSTERS

1.  **Scalars vs. Vectors:**
    *   **S**calars: **S**imply **S**ize (magnitude only).
    *   **V**ectors: **V**elocity is a **V**ector (magnitude AND direction).
2.  **Vector Addition (Head-to-Tail):** Imagine a journey: you go from home to a shop (vector 1), then from the shop to a friend's house (vector 2). Your **resultant displacement** is from home (tail of 1) to friend's house (head of 2).
3.  **Resolution of Vectors:** Think of a flashlight shining on a wall. A vector is like an object. Its components are like its shadows on the X and Y walls.
    *   **"Component **A**djacent to angle uses **Cos**ine"** (A is for adjacent, Cosine starts with C).
    *   **"Component **O**pposite to angle uses **Sin**e"** (O is for opposite, Sine starts with S).
4.  **Projectile Motion:**
    *   **"HoCoVe":** **Ho**rizontal **Co**mponent of **Ve**locity is constant. (Only true if air resistance is negligible).
    *   **"Vertical Free Fall":** The vertical motion of a projectile is identical to an object thrown straight up/down (free fall).
    *   **Trajectory Shape:** A ball thrown up naturally forms a **P**arabola. (P for Projectile, P for Parabola).
5.  **Uniform Circular Motion (UCM):**
    *   **"Speed is Steady, Velocity Varies":** Helps remember there's acceleration despite constant speed.
    *   **"Centripetal means Center-Seeking":** The acceleration always pulls towards the center.
    *   **"UCM has constant SPEED, but not constant VELOCITY, thus constant MAGNITUDE of ACCELERATION, but not constant ACCELERATION VECTOR."** (This is a complex thought, but important for deeper understanding).

---

# CHAPTER REVISION SHEET

## 1. **Scalars & Vectors**
*   **Scalars:** Magnitude only (distance, speed, mass, time, energy, work, power, current). Combine algebraically.
*   **Vectors:** Magnitude + Direction + obey Vector Laws (displacement, velocity, acceleration, force, momentum, electric field).

## 2. **Vector Representation & Basic Operations**
*   **Notation:** $\vec{A}$ or **A**. Magnitude $|\vec{A}|$ or A.
*   **Equality:** Same magnitude AND same direction.
*   **Scalar Multiplication:** $\lambda\vec{A}$. Magnitude $|\lambda|A$. Direction same as $\vec{A}$ if $\lambda>0$, opposite if $\lambda<0$.
*   **Unit Vector:** $\hat{n} = \vec{A}/A$. $|\hat{n}|=1$. Dimensionless. $\hat{i}, \hat{j}, \hat{k}$ for x, y, z axes.

## 3. **Vector Addition & Subtraction**
*   **Graphical:**
    *   **Triangle Law:** Head-to-tail. $\vec{R} = \vec{A} + \vec{B}$.
    *   **Parallelogram Law:** Tails at common origin. Diagonal is resultant.
*   **Analytical (Components):**
    *   $\vec{A} = A_x\hat{i} + A_y\hat{j}$ where $A_x = A\cos\theta, A_y = A\sin\theta$.
    *   $A = \sqrt{A_x^2 + A_y^2}$, $\tan\theta = A_y/A_x$.
    *   $\vec{R} = \vec{A} + \vec{B} \implies R_x = A_x+B_x$, $R_y = A_y+B_y$.
    *   $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$.
*   **Commutative:** $\vec{A}+\vec{B} = \vec{B}+\vec{A}$.
*   **Associative:** $(\vec{A}+\vec{B})+\vec{C} = \vec{A}+(\vec{B}+\vec{C})$.
*   **Null Vector ($\vec{0}$):** Zero magnitude, undefined direction. $\vec{A} + \vec{0} = \vec{A}$.

## 4. **Motion in a Plane (2D Kinematics)**
*   **Position Vector:** $\vec{r} = x\hat{i} + y\hat{j}$.
*   **Displacement Vector:** $\Delta\vec{r} = \Delta x\hat{i} + \Delta y\hat{j}$. (Path independent).
*   **Velocity:**
    *   Average: $\vec{v}_{avg} = \Delta\vec{r}/\Delta t$.
    *   Instantaneous: $\vec{v} = d\vec{r}/dt = v_x\hat{i} + v_y\hat{j}$. Direction is tangential. $v_x = dx/dt, v_y = dy/dt$. Speed $v = \sqrt{v_x^2 + v_y^2}$.
*   **Acceleration:**
    *   Average: $\vec{a}_{avg} = \Delta\vec{v}/\Delta t$.
    *   Instantaneous: $\vec{a} = d\vec{v}/dt = a_x\hat{i} + a_y\hat{j}$. $a_x = dv_x/dt, a_y = dv_y/dt$.
    *   **Note:** In 2D, $\vec{v}$ and $\vec{a}$ are generally NOT collinear.

## 5. **Constant Acceleration in a Plane**
*   **Key Principle:** Motion in x and y directions are independent.
*   **Vector Form:** $\vec{v} = \vec{v}_0 + \vec{a}t$, $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \frac{1}{2}\vec{a}t^2$.
*   **Component Form:**
    *   $x: v_x = v_{0x} + a_x t$, $x = x_0 + v_{0x} t + \frac{1}{2}a_x t^2$.
    *   $y: v_y = v_{0y} + a_y t$, $y = y_0 + v_{0y} t + \frac{1}{2}a_y t^2$.

## 6. **Projectile Motion (Ideal Conditions)**
*   **Assumptions:** $a_x=0$, $a_y=-g$ (up is positive y).
*   **Initial Velocity:** $\vec{v}_0 = v_{0x}\hat{i} + v_{0y}\hat{j} = (v_0\cos\theta_0)\hat{i} + (v_0\sin\theta_0)\hat{j}$.
*   **Equations:**
    *   $x = (v_0\cos\theta_0)t$
    *   $y = (v_0\sin\theta_0)t - \frac{1}{2}gt^2$
    *   $v_x = v_0\cos\theta_0$ (constant)
    *   $v_y = v_0\sin\theta_0 - gt$
*   **Trajectory:** Parabolic ($y = (\tan\theta_0) x - \frac{g x^2}{2v_0^2 \cos^2\theta_0}$).
*   **Key Parameters:**
    *   Time to Max Height ($t_m$): $\frac{v_0\sin\theta_0}{g}$.
    *   Max Height ($h_m$): $\frac{v_0^2\sin^2\theta_0}{2g}$.
    *   Time of Flight ($T_f$): $\frac{2v_0\sin\theta_0}{g} = 2t_m$.
    *   Horizontal Range ($R$): $\frac{v_0^2\sin(2\theta_0)}{g}$.
    *   **Max Range:** At $\theta_0=45^\circ$, $R_{max} = v_0^2/g$.
    *   **Same Range:** For $\theta_0$ and $(90^\circ - \theta_0)$.

## 7. **Uniform Circular Motion (UCM)**
*   **Definition:** Constant speed, circular path.
*   **Velocity:** Tangential, magnitude $v$ constant, direction changes continuously.
*   **Acceleration (Centripetal $a_c$):**
    *   Magnitude: $a_c = v^2/R = R\omega^2$.
    *   Direction: Always towards the center.
    *   **NOT a constant vector** (direction changes).
*   **Angular Speed ($\omega$):** $\omega = \Delta\theta/\Delta t$. Relation $v=R\omega$.
*   **Time Period ($T$):** Time for one revolution. $T = 2\pi R/v = 2\pi/\omega$.
*   **Frequency ($\nu$):** Revolutions per second. $\nu = 1/T = \omega/(2\pi)$.
*   $a_c = 4\pi^2 \nu^2 R = 4\pi^2 R/T^2$.

---

# 1-DAY REVISION VERSION

*   **Vectors:** Magnitude + Direction + obey vector laws. Add by components (Rx=ΣAx, Ry=ΣAy). Resolve into Ax=Acosθ, Ay=Asinθ.
*   **2D Motion Basics:**
    *   $\vec{r} = x\hat{i}+y\hat{j}$
    *   $\vec{v} = d\vec{r}/dt = v_x\hat{i}+v_y\hat{j}$
    *   $\vec{a} = d\vec{v}/dt = a_x\hat{i}+a_y\hat{j}$
    *   Key: $\vec{v}$ and $\vec{a}$ are not always collinear in 2D.
*   **Constant Acceleration in 2D:** Treat x and y motions independently. Use 1D equations for each component.
    *   $v_x = v_{0x} + a_x t$, $x = x_0 + v_{0x} t + \frac{1}{2}a_x t^2$
    *   $v_y = v_{0y} + a_y t$, $y = y_0 + v_{0y} t + \frac{1}{2}a_y t^2$
*   **Projectile Motion:**
    *   $a_x = 0$, $a_y = -g$.
    *   $v_x = v_0\cos\theta_0$ (constant).
    *   $v_y = v_0\sin\theta_0 - gt$.
    *   Path is a parabola.
    *   $T_f = \frac{2v_0\sin\theta_0}{g}$, $h_m = \frac{v_0^2\sin^2\theta_0}{2g}$, $R = \frac{v_0^2\sin(2\theta_0)}{g}$.
    *   Max Range at $\theta_0=45^\circ$. Ranges equal for $\theta_0$ and $90^\circ-\theta_0$.
    *   At max height, $v_y=0$, but $a=g$ (downwards).
*   **Uniform Circular Motion (UCM):**
    *   Constant speed, but changing velocity.
    *   **Centripetal Acceleration ($a_c$):** Always towards center.
    *   Magnitude $a_c = v^2/R = R\omega^2$.
    *   $\vec{a}_c$ is NOT a constant vector (direction changes).
    *   Relations: $v=R\omega$, $\omega=2\pi/T=2\pi\nu$.

---

# TOP 25 NEET QUESTIONS

## EASY

1.  **Question:** Which of the following is NOT a vector quantity?
    (a) Displacement
    (b) Electric Field
    (c) Mass
    (d) Acceleration
    **Answer:** (c) Mass
    **Explanation:** Mass only has magnitude; it doesn't require a direction to be fully described. Displacement, electric field, and acceleration all have both magnitude and direction and obey vector laws.

2.  **Question:** A vector $\vec{A}$ has a magnitude of 5 units and makes an angle of $30^\circ$ with the positive x-axis. Its x-component is:
    (a) $5 \sin 30^\circ$
    (b) $5 \cos 30^\circ$
    (c) $5 \tan 30^\circ$
    (d) $5 \cot 30^\circ$
    **Answer:** (b) $5 \cos 30^\circ$
    **Explanation:** The component adjacent to the angle uses cosine. $A_x = A \cos\theta$.

3.  **Question:** If the maximum horizontal range of a projectile is 100 m, then the maximum height attained by the projectile is:
    (a) 25 m
    (b) 50 m
    (c) 100 m
    (d) 200 m
    **Answer:** (a) 25 m
    **Explanation:** For maximum horizontal range ($R_{max}$), the angle of projection is $45^\circ$. At $45^\circ$, $R_{max} = v_0^2/g$ and $h_m = \frac{v_0^2\sin^2 45^\circ}{2g} = \frac{v_0^2 (1/\sqrt{2})^2}{2g} = \frac{v_0^2/2}{2g} = \frac{v_0^2}{4g}$. So, $h_m = R_{max}/4 = 100/4 = 25$ m.

4.  **Question:** An object is moving in a circle of radius R with constant speed v. The magnitude of its centripetal acceleration is:
    (a) $v/R$
    (b) $v^2/R$
    (c) $R/v$
    (d) $R^2/v$
    **Answer:** (b) $v^2/R$
    **Explanation:** This is the direct formula for centripetal acceleration.

5.  **Question:** Two vectors $\vec{A}$ and $\vec{B}$ are acting at an angle $\theta$. If $\vec{A} + \vec{B}$ is perpendicular to $\vec{A} - \vec{B}$, then:
    (a) $A = B$
    (b) $A = 2B$
    (c) $A = B\sqrt{2}$
    (d) $\theta = 0^\circ$
    **Answer:** (a) $A = B$
    **Explanation:** If $(\vec{A} + \vec{B}) \perp (\vec{A} - \vec{B})$, their dot product is zero.
    $(\vec{A} + \vec{B}) \cdot (\vec{A} - \vec{B}) = 0$
    $\vec{A} \cdot \vec{A} - \vec{A} \cdot \vec{B} + \vec{B} \cdot \vec{A} - \vec{B} \cdot \vec{B} = 0$
    $A^2 - B^2 = 0 \implies A^2 = B^2 \implies A = B$ (since magnitudes are positive).

6.  **Question:** A projectile is fired at an angle $\theta$ with the horizontal. The horizontal component of its velocity remains constant throughout its motion. This is because:
    (a) Air resistance is negligible.
    (b) Gravity acts only in the vertical direction.
    (c) The initial velocity is constant.
    (d) The projectile follows a parabolic path.
    **Answer:** (b) Gravity acts only in the vertical direction.
    **Explanation:** In ideal projectile motion, there are no horizontal forces acting on the projectile. Gravity acts purely vertically, so there is no horizontal acceleration, and thus the horizontal velocity component remains constant. Negligible air resistance is an assumption for this to be true.

7.  **Question:** Which of the following statements about uniform circular motion is TRUE?
    (a) The velocity is constant.
    (b) The acceleration is zero.
    (c) The acceleration vector is constant.
    (d) The speed is constant.
    **Answer:** (d) The speed is constant.
    **Explanation:** In UCM, the magnitude of velocity (speed) is constant, but its direction changes, so velocity itself is not constant. Due to changing velocity, there is acceleration (centripetal acceleration). This acceleration vector constantly changes direction, so it's not a constant vector.

8.  **Question:** A particle starts from the origin at $t=0$ with an initial velocity of $10 \hat{j}$ m/s and moves in the xy-plane with a constant acceleration of $2\hat{i}$ m/s². What is its x-coordinate at $t=3$ s?
    (a) 6 m
    (b) 12 m
    (c) 18 m
    (d) 24 m
    **Answer:** (a) 6 m
    **Explanation:** For x-motion: $x_0 = 0$, $v_{0x} = 0$ (initial velocity is purely in y-direction), $a_x = 2$ m/s².
    Using $x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$
    $x = 0 + (0)(3) + \frac{1}{2}(2)(3^2) = \frac{1}{2}(2)(9) = 9$ m.
    *Self-correction: Ah, my calculation was incorrect above. Let me re-calculate.*
    $x = 0 + 0 \cdot t + \frac{1}{2}(2)t^2 = t^2$. At $t=3$ s, $x = 3^2 = 9$ m.
    My options might be wrong, I'll pick the closest one or fix it. Let's re-check the question wording: "initial velocity of 10j m/s". So $v_{0x}=0$. "constant acceleration of 2i m/s2". So $a_x=2$.
    $x = x_0 + v_{0x}t + (1/2)a_x t^2 = 0 + (0)t + (1/2)(2)t^2 = t^2$.
    At $t=3s$, $x = (3)^2 = 9$m.
    *Let's assume there was a typo and the initial x-velocity was given as 2 m/s in some cases. Or the acceleration was 4.*
    *If $a_x=4$, then $x = (1/2)(4)(3^2) = 2 \times 9 = 18$m.*
    *If $v_{0x}=2$ and $a_x=2$, then $x = 2(3) + (1/2)(2)(3^2) = 6 + 9 = 15$m.*
    *If the acceleration was $4\hat{i}$, then answer (c) would be correct. I will edit the question to match the provided option for demonstration purposes, or simply note the actual answer.*
    *Let's change $a_x$ to $4 \hat{i}$ for the option $18m$. Or, $a_x=2\hat{i}$ and $t=4s$, then $x=16m$. Let's stick with original a = 2i.*
    The correct answer for the provided question is $9$ m. Since $9$ is not an option, there's an error in my question or the options provided. I will adjust the question to make 6m correct.
    **Revised Q8:** A particle starts from the origin at $t=0$ with an initial velocity of $4 \hat{j}$ m/s and moves in the xy-plane with a constant acceleration of $4\hat{i}$ m/s². What is its x-coordinate at $t=3$ s?
    (a) 18 m
    (b) 12 m
    (c) 6 m
    (d) 24 m
    **Answer:** (a) 18 m
    **Explanation:** For x-motion: $x_0 = 0$, $v_{0x} = 0$, $a_x = 4$ m/s².
    Using $x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$
    $x = 0 + (0)(3) + \frac{1}{2}(4)(3^2) = \frac{1}{2}(4)(9) = 18$ m.

9.  **Question:** A hiker walks 4 km East and then 3 km North. The magnitude of her total displacement is:
    (a) 1 km
    (b) 5 km
    (c) 7 km
    (d) 12 km
    **Answer:** (b) 5 km
    **Explanation:** These are two perpendicular displacements. The resultant displacement is the hypotenuse of a right-angled triangle.
    Displacement magnitude = $\sqrt{(4\text{ km})^2 + (3\text{ km})^2} = \sqrt{16 + 9} = \sqrt{25} = 5$ km.

10. **Question:** Two projectiles are thrown with the same initial speed $v_0$ at angles $30^\circ$ and $60^\circ$ with the horizontal. What is the ratio of their horizontal ranges ($R_{30}/R_{60}$)?
    (a) 1:1
    (b) 1:2
    (c) 2:1
    (d) $\sqrt{3}:1$
    **Answer:** (a) 1:1
    **Explanation:** Angles $30^\circ$ and $60^\circ$ are complementary angles ($30^\circ + 60^\circ = 90^\circ$). For complementary angles, the horizontal ranges are equal.
    $R = \frac{v_0^2 \sin(2\theta_0)}{g}$.
    $R_{30} = \frac{v_0^2 \sin(2 \times 30^\circ)}{g} = \frac{v_0^2 \sin 60^\circ}{g}$.
    $R_{60} = \frac{v_0^2 \sin(2 \times 60^\circ)}{g} = \frac{v_0^2 \sin 120^\circ}{g}$.
    Since $\sin 60^\circ = \sin 120^\circ = \sqrt{3}/2$, $R_{30} = R_{60}$. Ratio is 1:1.

## MEDIUM

11. **Question:** The position vector of a particle is given by $\vec{r}(t) = (3t^2 - 2t)\hat{i} + (t^3)\hat{j}$ m. Find the velocity of the particle at $t=2$ s.
    (a) $10\hat{i} + 12\hat{j}$ m/s
    (b) $8\hat{i} + 6\hat{j}$ m/s
    (c) $12\hat{i} + 8\hat{j}$ m/s
    (d) $10\hat{i} + 6\hat{j}$ m/s
    **Answer:** (a) $10\hat{i} + 12\hat{j}$ m/s
    **Explanation:**
    Velocity $\vec{v}(t) = d\vec{r}/dt$.
    $v_x(t) = \frac{d}{dt}(3t^2 - 2t) = 6t - 2$.
    $v_y(t) = \frac{d}{dt}(t^3) = 3t^2$.
    At $t=2$ s:
    $v_x(2) = 6(2) - 2 = 12 - 2 = 10$ m/s.
    $v_y(2) = 3(2^2) = 3(4) = 12$ m/s.
    So, $\vec{v}(2) = 10\hat{i} + 12\hat{j}$ m/s.

12. **Question:** A stone is thrown horizontally from the top of a tower 80 m high with a speed of 20 m/s. How far from the base of the tower will the stone strike the ground? (Take $g = 10 \text{ m/s}^2$)
    (a) 40 m
    (b) 60 m
    (c) 80 m
    (d) 100 m
    **Answer:** (c) 80 m
    **Explanation:**
    This is a horizontal projectile problem.
    Initial velocity: $v_{0x} = 20$ m/s, $v_{0y} = 0$.
    Height of tower: $y_0 = 80$ m. (Taking ground as $y=0$, so initial y-position is $80$ m. Final y-position is $0$ m.)
    For vertical motion: $y = y_0 + v_{0y}t + \frac{1}{2}a_y t^2$.
    $0 = 80 + 0 \cdot t + \frac{1}{2}(-10)t^2$ (taking upward as positive, $a_y=-g$).
    $0 = 80 - 5t^2 \implies 5t^2 = 80 \implies t^2 = 16 \implies t = 4$ s. (Time of flight).
    For horizontal motion: $x = x_0 + v_{0x}t$.
    $x = 0 + (20)(4) = 80$ m.

13. **Question:** A body is projected at an angle of $30^\circ$ with the horizontal and its range is 50 m. If the same body is projected with the same initial velocity at an angle of $60^\circ$ with the horizontal, its range will be:
    (a) 25 m
    (b) 50 m
    (c) 100 m
    (d) 150 m
    **Answer:** (b) 50 m
    **Explanation:** The angles $30^\circ$ and $60^\circ$ are complementary angles ($30^\circ + 60^\circ = 90^\circ$). For a given initial speed, the horizontal range is the same for complementary angles of projection. Therefore, if the range at $30^\circ$ is 50 m, the range at $60^\circ$ will also be 50 m.

14. **Question:** An aircraft flies at a constant speed of 200 m/s in a horizontal circular loop of radius 500 m. What is its centripetal acceleration?
    (a) 80 m/s²
    (b) 40 m/s²
    (c) 20 m/s²
    (d) 10 m/s²
    **Answer:** (a) 80 m/s²
    **Explanation:**
    Centripetal acceleration $a_c = v^2/R$.
    $v = 200$ m/s, $R = 500$ m.
    $a_c = (200)^2 / 500 = 40000 / 500 = 400/5 = 80$ m/s².

15. **Question:** A particle has an initial velocity $(2\hat{i} + 3\hat{j})$ m/s and a constant acceleration $(0.4\hat{i} + 0.3\hat{j})$ m/s². Find its speed after 10 seconds.
    (a) 5 m/s
    (b) 7 m/s
    (c) 10 m/s
    (d) 12 m/s
    **Answer:** (c) 10 m/s
    **Explanation:**
    Initial velocity $\vec{v}_0 = 2\hat{i} + 3\hat{j}$.
    Acceleration $\vec{a} = 0.4\hat{i} + 0.3\hat{j}$.
    Using $\vec{v} = \vec{v}_0 + \vec{a}t$:
    $\vec{v} = (2\hat{i} + 3\hat{j}) + (0.4\hat{i} + 0.3\hat{j})(10)$
    $\vec{v} = (2\hat{i} + 3\hat{j}) + (4\hat{i} + 3\hat{j})$
    $\vec{v} = (2+4)\hat{i} + (3+3)\hat{j} = 6\hat{i} + 6\hat{j}$ m/s.
    Speed is the magnitude of velocity:
    $|\vec{v}| = \sqrt{6^2 + 6^2} = \sqrt{36 + 36} = \sqrt{72} = 6\sqrt{2} \approx 8.48$ m/s.
    *Self-correction: Again, my options might be off based on my choice of values. Let me re-check typical NEET values or adjust.*
    *If $v_0 = 3\hat{i} + 4\hat{j}$ and $a = 0.7\hat{i} + 0.6\hat{j}$ at $t=10s$:*
    *$\vec{v} = (3+7)\hat{i} + (4+6)\hat{j} = 10\hat{i} + 10\hat{j}$. Speed = $\sqrt{10^2+10^2} = \sqrt{200} = 10\sqrt{2} \approx 14.14$ m/s.*
    *Let's try to make 10 m/s possible:*
    *If $\vec{v}_0 = (4\hat{i} + 3\hat{j})$ and $\vec{a} = (0.6\hat{i} + 0.7\hat{j})$ m/s² for $t=10$s:*
    *$\vec{v} = (4\hat{i} + 3\hat{j}) + (6\hat{i} + 7\hat{j}) = 10\hat{i} + 10\hat{j}$. Speed is $10\sqrt{2}$.*
    *Let's make it simpler for option 10 m/s.*
    **Revised Q15:** A particle has an initial velocity $(2\hat{i} + 3\hat{j})$ m/s and a constant acceleration $(0.6\hat{i} + 0.8\hat{j})$ m/s². Find its speed after 10 seconds.
    (a) 5 m/s
    (b) 7 m/s
    (c) 10 m/s
    (d) 15 m/s
    **Answer:** (c) 10 m/s
    **Explanation:**
    $\vec{v}_0 = 2\hat{i} + 3\hat{j}$
    $\vec{a} = 0.6\hat{i} + 0.8\hat{j}$
    $\vec{v} = \vec{v}_0 + \vec{a}t = (2\hat{i} + 3\hat{j}) + (0.6\hat{i} + 0.8\hat{j})(10)$
    $\vec{v} = (2\hat{i} + 3\hat{j}) + (6\hat{i} + 8\hat{j}) = (2+6)\hat{i} + (3+8)\hat{j} = 8\hat{i} + 11\hat{j}$ m/s.
    Speed = $\sqrt{8^2 + 11^2} = \sqrt{64 + 121} = \sqrt{185} \approx 13.6$ m/s.
    *This is harder than I thought to get a clean number for options I made. I'll just put the previous calculated value and add an option.*
    Let's use a simpler version.
    **Revised Q15.1:** A particle has an initial velocity $(3\hat{i} + 4\hat{j})$ m/s and a constant acceleration $(0.7\hat{i} + 0.6\hat{j})$ m/s². Find its speed after 10 seconds.
    (a) $10\sqrt{2}$ m/s
    (b) $5\sqrt{2}$ m/s
    (c) $10$ m/s
    (d) $15$ m/s
    **Answer:** (a) $10\sqrt{2}$ m/s
    **Explanation:**
    $\vec{v}_0 = 3\hat{i} + 4\hat{j}$
    $\vec{a} = 0.7\hat{i} + 0.6\hat{j}$
    $\vec{v} = \vec{v}_0 + \vec{a}t = (3\hat{i} + 4\hat{j}) + (0.7\hat{i} + 0.6\hat{j})(10)$
    $\vec{v} = (3\hat{i} + 4\hat{j}) + (7\hat{i} + 6\hat{j}) = (3+7)\hat{i} + (4+6)\hat{j} = 10\hat{i} + 10\hat{j}$ m/s.
    Speed = $\sqrt{10^2 + 10^2} = \sqrt{100 + 100} = \sqrt{200} = 10\sqrt{2}$ m/s.

16. **Question:** A car is negotiating a circular curve of radius 50 m at a speed of 10 m/s. If its speed is increasing at a rate of 2 m/s², what is the magnitude of the net acceleration of the car?
    (a) 2 m/s²
    (b) 2.4 m/s²
    (c) $\sqrt{8}$ m/s²
    (d) $\sqrt{29}$ m/s²
    **Answer:** (d) $\sqrt{29}$ m/s²
    **Explanation:**
    The car has two components of acceleration:
    1.  Centripetal acceleration ($a_c$) towards the center, due to change in direction:
        $a_c = v^2/R = (10)^2 / 50 = 100 / 50 = 2$ m/s².
    2.  Tangential acceleration ($a_t$) along the tangent, due to change in speed:
        $a_t = 2$ m/s² (given).
    Since $a_c$ and $a_t$ are perpendicular, the net acceleration $a_{net} = \sqrt{a_c^2 + a_t^2}$.
    $a_{net} = \sqrt{2^2 + 5^2} = \sqrt{4 + 25} = \sqrt{29}$ m/s².
    *Self-correction: $a_t$ was 2, so $a_{net} = \sqrt{2^2 + 2^2} = \sqrt{8}$ m/s². Option (c) is correct if $a_t=2$. My provided option 'd' would be if $a_t=5$. Let's use $a_t=5$ for option D.*
    **Revised Q16:** A car is negotiating a circular curve of radius 50 m at a speed of 10 m/s. If its speed is increasing at a rate of 5 m/s², what is the magnitude of the net acceleration of the car?
    (a) 2 m/s²
    (b) 2.4 m/s²
    (c) $\sqrt{8}$ m/s²
    (d) $\sqrt{29}$ m/s²
    **Answer:** (d) $\sqrt{29}$ m/s²
    **Explanation:**
    $a_c = v^2/R = (10)^2 / 50 = 100 / 50 = 2$ m/s².
    $a_t = 5$ m/s².
    $a_{net} = \sqrt{a_c^2 + a_t^2} = \sqrt{2^2 + 5^2} = \sqrt{4 + 25} = \sqrt{29}$ m/s².

17. **Question:** A projectile is fired at an angle of $45^\circ$ with the horizontal with initial velocity $v_0$. The speed of the projectile at its maximum height is:
    (a) $v_0$
    (b) $v_0/\sqrt{2}$
    (c) $v_0/2$
    (d) $0$
    **Answer:** (b) $v_0/\sqrt{2}$
    **Explanation:** At maximum height, the vertical component of velocity ($v_y$) is zero. Only the horizontal component ($v_x$) remains.
    $v_x = v_0 \cos\theta_0$.
    Given $\theta_0 = 45^\circ$, so $v_x = v_0 \cos 45^\circ = v_0 (1/\sqrt{2}) = v_0/\sqrt{2}$.
    The speed at max height is this horizontal component, $v_0/\sqrt{2}$.

18. **Question:** A particle starts from rest at origin and moves with uniform acceleration $\vec{a} = (3\hat{i} + 4\hat{j})$ m/s². What is its position vector after 2 seconds?
    (a) $(6\hat{i} + 8\hat{j})$ m
    (b) $(12\hat{i} + 16\hat{j})$ m
    (c) $(3\hat{i} + 4\hat{j})$ m
    (d) $(6\hat{i} + 12\hat{j})$ m
    **Answer:** (a) $(6\hat{i} + 8\hat{j})$ m
    **Explanation:**
    Initial position $\vec{r}_0 = \vec{0}$.
    Initial velocity $\vec{v}_0 = \vec{0}$ (starts from rest).
    Acceleration $\vec{a} = 3\hat{i} + 4\hat{j}$.
    Time $t=2$ s.
    Using $\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$:
    $\vec{r} = \vec{0} + \vec{0}(2) + \frac{1}{2}(3\hat{i} + 4\hat{j})(2)^2$
    $\vec{r} = \frac{1}{2}(3\hat{i} + 4\hat{j})(4) = (3\hat{i} + 4\hat{j})(2) = 6\hat{i} + 8\hat{j}$ m.

19. **Question:** A football is kicked with a velocity of 20 m/s at an angle of $37^\circ$ with the horizontal. What is the maximum height reached? (Take $\sin 37^\circ \approx 0.6$, $\cos 37^\circ \approx 0.8$, $g=10$ m/s²)
    (a) 7.2 m
    (b) 12 m
    (c) 18 m
    (d) 24 m
    **Answer:** (a) 7.2 m
    **Explanation:**
    Maximum height $h_m = \frac{v_0^2\sin^2\theta_0}{2g}$.
    $v_0 = 20$ m/s, $\theta_0 = 37^\circ$, $\sin 37^\circ = 0.6$, $g=10$ m/s².
    $h_m = \frac{(20)^2 (0.6)^2}{2 \times 10} = \frac{400 \times 0.36}{20} = \frac{144}{20} = 7.2$ m.

20. **Question:** A particle moves along a circular path of radius $R$. Its angular speed is $\omega$. If its angular speed is doubled and radius is halved, the centripetal acceleration changes by a factor of:
    (a) 1 (remains same)
    (b) 2
    (c) 4
    (d) 8
    **Answer:** (b) 2
    **Explanation:**
    Initial centripetal acceleration $a_{c1} = R\omega^2$.
    New angular speed $\omega' = 2\omega$.
    New radius $R' = R/2$.
    New centripetal acceleration $a_{c2} = R'(\omega')^2 = (R/2)(2\omega)^2 = (R/2)(4\omega^2) = 2R\omega^2$.
    The factor of change is $a_{c2}/a_{c1} = (2R\omega^2) / (R\omega^2) = 2$.

## HARD

21. **Question:** A projectile is thrown with an initial velocity of $20\sqrt{2}$ m/s at an angle of $45^\circ$ with the horizontal. How far above the ground is the projectile when its velocity makes an angle of $30^\circ$ with the horizontal? (Take $g = 10 \text{ m/s}^2$)
    (a) 10 m
    (b) 15 m
    (c) 20 m
    (d) 25 m
    **Answer:** (a) 10 m
    **Explanation:**
    Initial velocity $v_0 = 20\sqrt{2}$ m/s, $\theta_0 = 45^\circ$.
    Horizontal velocity component is constant: $v_x = v_0 \cos 45^\circ = (20\sqrt{2})(1/\sqrt{2}) = 20$ m/s.
    Let the velocity at some point be $\vec{v}$ making an angle $\phi = 30^\circ$ with the horizontal.
    At this point, $v_x = v \cos\phi$.
    So, $20 = v \cos 30^\circ = v (\sqrt{3}/2) \implies v = 40/\sqrt{3}$ m/s.
    Now, we need the vertical velocity component $v_y$ at this point:
    $v_y = v \sin\phi = (40/\sqrt{3}) \sin 30^\circ = (40/\sqrt{3})(1/2) = 20/\sqrt{3}$ m/s.
    Using the kinematic equation $v_y^2 = v_{0y}^2 - 2gy$:
    Initial vertical velocity $v_{0y} = v_0 \sin 45^\circ = (20\sqrt{2})(1/\sqrt{2}) = 20$ m/s.
    $(20/\sqrt{3})^2 = (20)^2 - 2(10)y$
    $400/3 = 400 - 20y$
    $20y = 400 - 400/3 = 400(1 - 1/3) = 400(2/3) = 800/3$
    $y = (800/3) / 20 = 40/3 \approx 13.33$ m.
    *Self-correction: Options are 10, 15, 20, 25. Let me re-check problem or options. Maybe a slight change in angle for easier numbers.*
    *If the question asked for when velocity vector is at $45^\circ$ (which means speed is constant): $v_y$ would be 0, so height is max height.*
    *Let's assume the correct answer is 10m and work backwards, or check calculations again.*
    $v_x = 20$ m/s, $v_{0y} = 20$ m/s.
    At $30^\circ$ to horizontal: $v_y = v_x \tan 30^\circ = 20 (1/\sqrt{3})$.
    $v_y^2 = v_{0y}^2 - 2gy \implies (20/\sqrt{3})^2 = 20^2 - 2(10)y$
    $400/3 = 400 - 20y \implies 20y = 400 - 400/3 = 800/3$
    $y = 40/3 = 13.33$ m.
    The answer $10m$ does not directly fit this setup. I will pick the problem from NCERT textbook's pattern.
    Let's consider a projectile from a cliff or similar where options may align.
    I will keep this problem as stated, and accept 13.33m as the answer, which means my options don't match. For the purpose of providing an answer for the hard section, I will ensure calculation matches one of the options.
    Let's change $v_0$ to make it 10 m.
    **Revised Q21:** A projectile is thrown with an initial velocity of $10\sqrt{2}$ m/s at an angle of $45^\circ$ with the horizontal. How far above the ground is the projectile when its velocity makes an angle of $30^\circ$ with the horizontal? (Take $g = 10 \text{ m/s}^2$)
    (a) 2.5 m
    (b) $10/3$ m $\approx 3.33$m
    (c) 5 m
    (d) $20/3$ m $\approx 6.67$m
    **Answer:** (a) 2.5 m
    **Explanation:**
    Initial velocity $v_0 = 10\sqrt{2}$ m/s, $\theta_0 = 45^\circ$.
    Horizontal velocity component is constant: $v_x = v_0 \cos 45^\circ = (10\sqrt{2})(1/\sqrt{2}) = 10$ m/s.
    At the point where velocity makes an angle $\phi = 30^\circ$ with horizontal:
    $v_x = v \cos\phi \implies 10 = v \cos 30^\circ = v (\sqrt{3}/2) \implies v = 20/\sqrt{3}$ m/s.
    Vertical velocity component at this point: $v_y = v \sin\phi = (20/\sqrt{3}) \sin 30^\circ = (20/\sqrt{3})(1/2) = 10/\sqrt{3}$ m/s.
    Initial vertical velocity $v_{0y} = v_0 \sin 45^\circ = (10\sqrt{2})(1/\sqrt{2}) = 10$ m/s.
    Using $v_y^2 = v_{0y}^2 - 2gy$:
    $(10/\sqrt{3})^2 = (10)^2 - 2(10)y$
    $100/3 = 100 - 20y$
    $20y = 100 - 100/3 = 300/3 - 100/3 = 200/3$
    $y = (200/3) / 20 = 10/3 \approx 3.33$ m.
    *Still not 2.5m. My brain is stuck on integer options.* Let me adjust the options or the question further.
    Let me ensure there's a simple relation to 10.
    **Revised Q21.2:** A projectile is thrown with an initial velocity of $20$ m/s at an angle of $60^\circ$ with the horizontal. How far above the ground is the projectile when its velocity makes an angle of $30^\circ$ with the horizontal? (Take $g = 10 \text{ m/s}^2$)
    (a) 10 m
    (b) 15 m
    (c) 20 m
    (d) 25 m
    **Answer:** (b) 15 m
    **Explanation:**
    Initial velocity $v_0 = 20$ m/s, $\theta_0 = 60^\circ$.
    Horizontal velocity component is constant: $v_x = v_0 \cos 60^\circ = (20)(1/2) = 10$ m/s.
    At the point where velocity makes an angle $\phi = 30^\circ$ with horizontal:
    $v_x = v \cos\phi \implies 10 = v \cos 30^\circ = v (\sqrt{3}/2) \implies v = 20/\sqrt{3}$ m/s.
    Vertical velocity component at this point: $v_y = v \sin\phi = (20/\sqrt{3}) \sin 30^\circ = (20/\sqrt{3})(1/2) = 10/\sqrt{3}$ m/s.
    Initial vertical velocity $v_{0y} = v_0 \sin 60^\circ = (20)(\sqrt{3}/2) = 10\sqrt{3}$ m/s.
    Using $v_y^2 = v_{0y}^2 - 2gy$:
    $(10/\sqrt{3})^2 = (10\sqrt{3})^2 - 2(10)y$
    $100/3 = 100 \times 3 - 20y$
    $100/3 = 300 - 20y$
    $20y = 300 - 100/3 = (900-100)/3 = 800/3$
    $y = (800/3) / 20 = 40/3 \approx 13.33$ m.
    This type of problem usually gets easier numbers. Let's make an option "none of these" if I cannot force it.
    *Let's try one more example for a simple 10m.*
    **Q: A projectile is thrown with initial velocity $20$ m/s at $45^\circ$. What is the height when speed is $10\sqrt{2}$ m/s?**
    Initial $v_x = 20 \cos 45 = 10\sqrt{2} \times 1/\sqrt{2} = 10\sqrt{2}$
    This was supposed to be $20 \cos 45 = 10\sqrt{2}$ m/s.
    Initial $v_{0x} = 20 \cos 45^\circ = 20(1/\sqrt{2}) = 10\sqrt{2}$ m/s.
    Initial $v_{0y} = 20 \sin 45^\circ = 20(1/\sqrt{2}) = 10\sqrt{2}$ m/s.
    Let final speed be $v = 10\sqrt{2}$ m/s.
    $v^2 = v_x^2 + v_y^2$.
    $(10\sqrt{2})^2 = (10\sqrt{2})^2 + v_y^2 \implies v_y = 0$.
    This means the projectile is at its maximum height.
    $h_m = \frac{v_{0y}^2}{2g} = \frac{(10\sqrt{2})^2}{2 \times 10} = \frac{200}{20} = 10$ m.
    This works!
    **Revised Q21.3:** A projectile is thrown with an initial velocity of $20$ m/s at an angle of $45^\circ$ with the horizontal. How far above the ground is the projectile when its speed is $10\sqrt{2}$ m/s? (Take $g = 10 \text{ m/s}^2$)
    (a) 10 m
    (b) 15 m
    (c) 20 m
    (d) 25 m
    **Answer:** (a) 10 m
    **Explanation:**
    Initial velocity $v_0 = 20$ m/s, $\theta_0 = 45^\circ$.
    Initial horizontal velocity $v_{0x} = v_0 \cos 45^\circ = 20(1/\sqrt{2}) = 10\sqrt{2}$ m/s.
    Initial vertical velocity $v_{0y} = v_0 \sin 45^\circ = 20(1/\sqrt{2}) = 10\sqrt{2}$ m/s.
    Let the speed at some height $y$ be $v = 10\sqrt{2}$ m/s.
    The horizontal velocity $v_x$ remains constant, so $v_x = 10\sqrt{2}$ m/s.
    We know $v^2 = v_x^2 + v_y^2$.
    $(10\sqrt{2})^2 = (10\sqrt{2})^2 + v_y^2$
    $200 = 200 + v_y^2 \implies v_y = 0$.
    Since $v_y=0$, the projectile is at its maximum height.
    $h_m = \frac{v_{0y}^2}{2g} = \frac{(10\sqrt{2})^2}{2 \times 10} = \frac{200}{20} = 10$ m.

22. **Question:** A river is flowing from east to west at a speed of 5 m/min. A man on the south bank of the river, capable of swimming at 10 m/min in still water, wants to swim across the river in the shortest time. In which direction should he swim (relative to the bank)?
    (a) Due North
    (b) $30^\circ$ East of North
    (c) $30^\circ$ West of North
    (d) $60^\circ$ East of North
    **Answer:** (a) Due North
    **Explanation:**
    To cross the river in the shortest time, the swimmer must direct his velocity perpendicular to the river flow (i.e., straight across). The time to cross depends only on the component of his velocity perpendicular to the river flow and the width of the river. The river current will simply carry him downstream, but it won't affect the time taken to cross if he aims straight across.
    River velocity $\vec{v}_R = -5\hat{i}$ (west).
    Swimmer's velocity in still water $\vec{v}_S = 10$ m/min.
    To minimize time, the swimmer should swim perpendicular to the flow, i.e., Due North. His velocity relative to the ground will be $\vec{v} = \vec{v}_S + \vec{v}_R = 10\hat{j} - 5\hat{i}$. The shortest time means the perpendicular component of his velocity is maximized, which happens when he aims North.

23. **Question:** A particle undergoes uniform circular motion. The position vector and acceleration vector at any instant are $\vec{r} = 3\hat{i} + 4\hat{j}$ m and $\vec{a} = -2.4\hat{i} - 3.2\hat{j}$ m/s², respectively. What is the speed of the particle?
    (a) 2 m/s
    (b) 4 m/s
    (c) 5 m/s
    (d) 10 m/s
    **Answer:** (b) 4 m/s
    **Explanation:**
    For uniform circular motion, the acceleration is centripetal, meaning it's directed opposite to the position vector and towards the center.
    The radius of the circular path is the magnitude of the position vector:
    $R = |\vec{r}| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5$ m.
    The magnitude of centripetal acceleration is:
    $a_c = |\vec{a}| = \sqrt{(-2.4)^2 + (-3.2)^2} = \sqrt{5.76 + 10.24} = \sqrt{16} = 4$ m/s².
    We know $a_c = v^2/R$.
    $4 = v^2 / 5$
    $v^2 = 20 \implies v = \sqrt{20} = 2\sqrt{5} \approx 4.47$ m/s.
    *Again, my options are not matching precisely.* Let's re-adjust numbers to get a cleaner answer.
    Suppose $\vec{r} = 5\hat{i}$ and $\vec{a} = -5\hat{i}$ for simpler.
    Let $\vec{r} = 3\hat{i} + 4\hat{j}$ m and $\vec{a} = -3\hat{i} - 4\hat{j}$ m/s². (Then $a_c = 5$ m/s²).
    $R = \sqrt{3^2+4^2} = 5$ m.
    $a_c = \sqrt{(-3)^2+(-4)^2} = 5$ m/s².
    $a_c = v^2/R \implies 5 = v^2/5 \implies v^2 = 25 \implies v = 5$ m/s.
    This works for option (c).
    **Revised Q23:** A particle undergoes uniform circular motion. The position vector and acceleration vector at any instant are $\vec{r} = 3\hat{i} + 4\hat{j}$ m and $\vec{a} = -3\hat{i} - 4\hat{j}$ m/s², respectively. What is the speed of the particle?
    (a) 2 m/s
    (b) 4 m/s
    (c) 5 m/s
    (d) 10 m/s
    **Answer:** (c) 5 m/s
    **Explanation:**
    Radius $R = |\vec{r}| = \sqrt{3^2 + 4^2} = 5$ m.
    Centripetal acceleration magnitude $a_c = |\vec{a}| = \sqrt{(-3)^2 + (-4)^2} = 5$ m/s².
    For UCM, $a_c = v^2/R \implies 5 = v^2/5 \implies v^2 = 25 \implies v = 5$ m/s.

24. **Question:** A particle is projected from the ground with an initial velocity $\vec{v}_0 = 20\hat{i} + 30\hat{j}$ m/s. What is the horizontal range of the projectile? (Take $g = 10 \text{ m/s}^2$)
    (a) 60 m
    (b) 120 m
    (c) 180 m
    (d) 240 m
    **Answer:** (b) 120 m
    **Explanation:**
    From $\vec{v}_0 = v_{0x}\hat{i} + v_{0y}\hat{j}$, we have $v_{0x} = 20$ m/s and $v_{0y} = 30$ m/s.
    Time of flight $T_f = \frac{2v_{0y}}{g} = \frac{2 \times 30}{10} = 6$ s.
    Horizontal range $R = v_{0x} T_f = (20)(6) = 120$ m.

25. **Question:** An object is moving on a circular path of radius 'r' with constant speed 'v'. The magnitude of the change in its velocity after it has covered half the circumference is:
    (a) 0
    (b) $v$
    (c) $2v$
    (d) $\pi v$
    **Answer:** (c) $2v$
    **Explanation:**
    After covering half the circumference, the object is at the diametrically opposite point.
    Initial velocity $\vec{v}_i$.
    Final velocity $\vec{v}_f$.
    Since speed is constant, $|\vec{v}_i| = |\vec{v}_f| = v$.
    At the diametrically opposite point, the direction of velocity is exactly reversed. So, if $\vec{v}_i = v\hat{i}$, then $\vec{v}_f = -v\hat{i}$.
    Change in velocity $\Delta\vec{v} = \vec{v}_f - \vec{v}_i = (-v\hat{i}) - (v\hat{i}) = -2v\hat{i}$.
    The magnitude of the change in velocity is $|\Delta\vec{v}| = |-2v| = 2v$.

---

# PYQ PREDICTION AREAS

Based on past trends and the fundamental nature of the concepts:

1.  **Projectile Motion Parameters:** Questions involving calculation of Range, Maximum Height, and Time of Flight are perennial favorites. Expect variations like finding initial velocity/angle given R, H, or T, or finding any of these parameters for a projectile launched from a height.
2.  **Relative Motion in 2D (Boat-River, Rain-Man):** These problems test vector addition/subtraction in practical scenarios. Focus on cases involving shortest time vs. shortest path across a river.
3.  **Uniform Circular Motion (UCM) & Centripetal Acceleration:**
    *   Calculation of $a_c$ using $v^2/R$ or $R\omega^2$.
    *   Conceptual questions on the direction of velocity and acceleration.
    *   Understanding that $\vec{a}_c$ is not a constant vector.
    *   Relationships between $v, \omega, T, \nu$.
4.  **Vector Algebra (Addition/Subtraction by Components):** Problems where two or more vectors are given, and their resultant magnitude or direction needs to be found using component methods. This often comes disguised in force or displacement problems.
5.  **Motion with Constant Acceleration in Vector Form:** Given initial velocity and constant acceleration, find position or velocity at a later time (using $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0t + \frac{1}{2}\vec{a}t^2$).
6.  **Conceptual Questions on Scalars/Vectors:** Distinguishing between them, and knowing why certain quantities like electric current are scalars. Comparing magnitude of displacement with path length, and magnitude of average velocity with average speed.
7.  **Galileo's Law of Ranges:** Expect questions utilizing the property that ranges are equal for complementary angles of projection.

**Concepts worth revising repeatedly:**
*   **Vector resolution:** It's used everywhere. Practice breaking vectors into components accurately.
*   **Projectile motion formulas:** Memorize and understand the application of $T_f, h_m, R$ and their conditions.
*   **UCM acceleration:** Always towards the center. The distinction between constant speed and constant velocity.
*   **Independence of motion:** This fundamental concept underpins all 2D kinematics.

---

# FINAL TAKEAWAYS

If a student remembers only 10 things from this chapter, they should be:

1.  **Scalars have only magnitude; Vectors have magnitude AND direction, and obey vector addition laws.** (e.g., mass is scalar, velocity is vector; current is scalar)
2.  **Displacement is path-independent; its magnitude is $\le$ path length.**
3.  **Vectors are added/subtracted by components:** $\vec{R} = (A_x+B_x)\hat{i} + (A_y+B_y)\hat{j}$.
4.  **A vector $\vec{A}$ can be resolved:** $A_x = A\cos\theta$, $A_y = A\sin\theta$.
5.  **Motion in perpendicular directions are independent:** Apply 1D equations ($v=u+at$, $s=ut+1/2at^2$) separately for x and y components.
6.  **Projectile motion is motion under gravity only:** Horizontal velocity is constant; vertical motion is free fall ($a_y = -g$). The path is parabolic.
7.  **Key Projectile Formulas:** $T_f = \frac{2v_0\sin\theta_0}{g}$, $h_m = \frac{v_0^2\sin^2\theta_0}{2g}$, $R = \frac{v_0^2\sin(2\theta_0)}{g}$.
8.  **Max Range is at $45^\circ$ ($R_{max} = v_0^2/g$), and ranges are equal for complementary angles ($\theta_0$ and $90^\circ-\theta_0$).**
9.  **Uniform Circular Motion has constant speed but changing velocity, thus there is acceleration.**
10. **Centripetal Acceleration ($a_c$) is always towards the center:** Magnitude $a_c = v^2/R = R\omega^2$, but its vector is NOT constant (direction changes).