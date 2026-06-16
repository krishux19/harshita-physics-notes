# SYSTEMS OF PARTICLES AND ROTATIONAL MOTION: NEET INTELLIGENCE NOTES

---

# CHAPTER OVERVIEW

*   **Chapter Name:** Systems of Particles and Rotational Motion
*   **Importance for NEET:** VERY HIGH. This chapter is a cornerstone of mechanics, bridging previous concepts (linear motion, forces) to the more complex world of extended bodies and rotation. It forms the basis for understanding many real-world phenomena and is frequently tested.
*   **Estimated Weightage:** 2-3 questions (8-12 marks). Often includes numerical problems, conceptual questions, and sometimes integrated with other topics like gravitation or work-energy.
*   **Difficulty Level:** Medium to Hard. Requires strong vector understanding, spatial visualization, and a good grasp of analogies between linear and rotational motion. Derivations and problem-solving can be challenging for beginners.
*   **Prerequisites:**
    *   Vectors (addition, subtraction, scalar product, vector product).
    *   Newton's Laws of Motion.
    *   Kinematics (equations of motion).
    *   Work, Energy, and Power.
    *   Basic Calculus (differentiation and integration).
*   **Most Important Concepts:**
    1.  **Centre of Mass (CM):** Definition, calculation for discrete and continuous systems, its motion under external forces.
    2.  **Torque (Moment of Force):** Definition (vector product), calculation, effect on rotational motion.
    3.  **Angular Momentum:** Definition (vector product), conservation principle, relation with torque.
    4.  **Moment of Inertia:** Definition, physical significance (rotational inertia), dependence on mass distribution and axis, calculation for simple shapes.
    5.  **Rotational Kinematics & Dynamics:** Analogies with linear motion, equations of motion, τ = Iα.
    6.  **Equilibrium of Rigid Bodies:** Conditions for translational and rotational equilibrium, concept of a couple.
    7.  **Combined Translational & Rotational Motion:** Introduction to rolling (though detailed rolling motion is covered later, the concept is introduced here).

---

# BEGINNER EXPLANATION

Imagine you've been studying how a tiny little ball (a 'particle') moves. It slides, it jumps, it speeds up, slows down. But in real life, most things aren't tiny balls, right? Your book, a fan, a wheel – these are all big objects with a definite shape. We call these **extended bodies**.

Now, when you push a tiny ball, it just moves forward. But what happens if you push a door? If you push it near the hinge, it hardly moves. If you push it hard at the edge, it swings open! This swinging motion is called **rotational motion**.

This chapter is all about understanding how these 'big objects' move. We'll learn two main things:

1.  **How the object moves as a whole:** Even if a complex object like a cricket bat is spinning and flying, there's one special point on it, called the **Centre of Mass (CM)**, that moves simply – almost like a tiny ball! We'll learn how to find this point and how its motion describes the overall movement of the object.
2.  **How the object spins or rotates:** We'll introduce new ideas like **Torque**, which is like a 'twisting force' that makes things rotate (like opening a bottle cap). We'll also talk about **Angular Momentum**, which is a measure of how much an object is 'spinning' and how hard it is to stop that spin.

Think of it this way:
*   **Translation** is like moving from one place to another without spinning (e.g., a car driving straight).
*   **Rotation** is like spinning in place (e.g., a fan blade, a top).
*   Most real-life movements are a **combination** of both (e.g., a car wheel rolling, a ball thrown with spin).

The goal is to simplify the complex motion of these extended bodies by focusing on their Centre of Mass for translational motion and on concepts like Torque and Angular Momentum for rotational motion.

---

# COMPLETE CONCEPT NOTES

## 6.1 Introduction

### Particle vs. Extended Body

*   **Definition:**
    *   **Particle:** An idealized point mass with no size or internal structure. All its mass is concentrated at a single point.
    *   **Extended Body (System of Particles):** A real body with finite size, composed of many particles. Its mass is distributed over a volume.
*   **Intuition:** Imagine a dot vs. a book.
*   **Why it matters:** The particle model is useful for simple translational motion. However, it's inadequate when the size and shape of an object influence its motion, especially when it rotates or deforms.
*   **Real-world examples:**
    *   Particle: A distant planet considered as a point for orbital calculations.
    *   Extended Body: A cricket ball, a car, a fan, a human body.
*   **Important observations:**
    *   An extended body is fundamentally a system of particles.
    *   To analyze the motion of extended bodies, we need to consider the motion of the *system as a whole* and the *motion of its parts relative to each other*.

### Rigid Body

*   **Definition:** An idealized extended body that has a perfectly definite and unchanging shape. The distances between all pairs of particles within a rigid body remain constant, regardless of the forces applied.
*   **Intuition:** A perfectly stiff, unbendable, unbreakable object.
*   **Why it matters:** Simplifies analysis significantly by ignoring deformations. Many real-world objects can be treated as rigid bodies if deformations are negligible.
*   **Real-world examples:** Wheels, tops, steel beams, molecules (often treated as rigid for vibration analysis), planets.
*   **Important observations:**
    *   No real body is truly rigid, as all materials deform under force.
    *   The rigid body model is an approximation, valid when internal changes are insignificant.

### Types of Rigid Body Motion

*   **Pure Translational Motion:**
    *   **Definition:** Motion where all particles of the body have the exact same velocity (magnitude and direction) at any given instant. The orientation of the body in space does not change.
    *   **Intuition:** A block sliding down a ramp without rotating.
    *   **Real-world examples:** A box sliding on a smooth floor, a car moving straight on a highway (ignoring wheel rotation for a moment).
    *   **Important observations:** The body's orientation remains constant throughout the motion. The trajectory of any point on the body is identical to that of any other point.

*   **Pure Rotational Motion (about a fixed axis):**
    *   **Definition:** Motion where the body spins around a fixed line (the axis of rotation). Every particle of the body moves in a circle, and all these circles lie in planes perpendicular to the axis, with their centers on the axis. Particles on the axis of rotation remain stationary.
    *   **Intuition:** A ceiling fan rotating, a potter's wheel spinning.
    *   **Real-world examples:** A door opening/closing, a merry-go-round, a spinning top (if its point of contact is fixed).
    *   **Important observations:**
        *   All particles have the same *angular velocity*.
        *   Linear velocity varies with distance from the axis (v = ωr).
        *   In general, the axis of rotation can move (e.g., a precessing top, an oscillating fan), but in this chapter, we primarily focus on rotation about a *fixed axis*.

*   **Combined Translational and Rotational Motion:**
    *   **Definition:** Motion that is a superposition of translational and rotational motion. The body both moves forward and spins simultaneously.
    *   **Intuition:** A rolling cylinder or wheel.
    *   **Real-world examples:** A car wheel, a bowling ball, a bicycle moving.
    *   **Important observations:** This is the most general type of motion for an unfixed rigid body. The velocity of different points on the body will be different due to the rotational component.

## 6.2 Centre of Mass (CM)

### Definition & Calculation for Discrete Systems

*   **Definition:** The Centre of Mass (CM) of a system of particles is a point that represents the average position of all the mass in the system. It's the point where, for translational motion, we can imagine the entire mass of the system is concentrated and all external forces act.
*   **Intuition:** It's the "balance point" of an object. If you balance an object on a single point, that point is its CM (or more accurately, its Centre of Gravity, which often coincides with CM).
*   **Why it matters:** Simplifies the analysis of complex systems. The translational motion of a system can be described solely by the motion of its CM, regardless of internal forces or the motion of individual particles.
*   **Real-world examples:**
    *   A projectile exploding in mid-air: The CM of all the fragments continues along the original parabolic trajectory as if no explosion occurred.
    *   Balancing a book on your finger.
*   **Formulas:**
    *   **For two particles (1D, along x-axis):**
        $X = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$
    *   **For 'n' particles (1D, along x-axis):**
        $X = \frac{m_1 x_1 + m_2 x_2 + ... + m_n x_n}{m_1 + m_2 + ... + m_n} = \frac{\sum m_i x_i}{\sum m_i} = \frac{\sum m_i x_i}{M_{total}}$
        (Similarly for Y and Z coordinates)
    *   **For 'n' particles (3D, vector form):**
        $\vec{R}_{CM} = \frac{m_1 \vec{r}_1 + m_2 \vec{r}_2 + ... + m_n \vec{r}_n}{M_{total}} = \frac{\sum m_i \vec{r}_i}{M_{total}}$
        Where $\vec{r}_i = x_i \hat{i} + y_i \hat{j} + z_i \hat{k}$ is the position vector of the $i^{th}$ particle.
*   **Important observations:**
    *   If masses are equal, CM is the arithmetic mean of positions (midpoint for two, centroid for three).
    *   The origin of the coordinate system affects the values of $X, Y, Z$ but not the *physical location* of the CM relative to the body.
    *   If the origin is chosen at the CM, then $\sum m_i \vec{r}_i = 0$.

### Calculation for Continuous Mass Distribution

*   **Definition:** For a body with mass continuously distributed (like a solid object), we treat it as an infinite number of infinitesimal mass elements.
*   **Intuition:** Instead of adding discrete points, we sum over tiny 'chunks' using integration.
*   **Why it matters:** Allows calculating CM for real, solid objects.
*   **Formulas:**
    *   $X = \frac{\int x \ dm}{\int dm} = \frac{1}{M_{total}} \int x \ dm$
    *   $Y = \frac{\int y \ dm}{M_{total}}$
    *   $Z = \frac{\int z \ dm}{M_{total}}$
    *   **Vector form:** $\vec{R}_{CM} = \frac{1}{M_{total}} \int \vec{r} \ dm$
*   **Important observations:**
    *   The integral $\int dm$ is simply the total mass $M_{total}$ of the body.
    *   If the origin is chosen at the CM, then $\int \vec{r} \ dm = 0$.

### Symmetry and Centre of Mass

*   **Definition:** For homogeneous (uniformly distributed mass) bodies with geometric symmetry, the Centre of Mass often coincides with their geometric center.
*   **Intuition:** If an object looks the same from different angles, its balance point is usually in the middle.
*   **Why it matters:** Simplifies CM determination for many common shapes, avoiding complex calculations.
*   **Real-world examples:**
    *   Thin rod: CM at its midpoint.
    *   Ring/Disc/Sphere: CM at its geometric center (center of circle/sphere).
    *   Cube: CM at the intersection of its diagonals.
*   **Important observations:** This applies only to *homogeneous* bodies. If a body is non-homogeneous (mass not uniformly distributed), its CM will not necessarily be at its geometric center.

## 6.3 Motion of Centre of Mass

### Velocity of CM

*   **Definition:** The velocity of the Centre of Mass is the time rate of change of its position vector.
*   **Formula:**
    $\vec{V}_{CM} = \frac{d\vec{R}_{CM}}{dt} = \frac{\sum m_i (d\vec{r}_i/dt)}{M_{total}} = \frac{\sum m_i \vec{v}_i}{M_{total}}$
*   **Intuition:** It's the weighted average of the velocities of all individual particles.
*   **Important observations:** This holds even if the masses $m_i$ change with time (e.g., a rocket ejecting fuel), but in this chapter, masses are generally assumed constant.

### Acceleration of CM

*   **Definition:** The acceleration of the Centre of Mass is the time rate of change of its velocity.
*   **Formula:**
    $\vec{A}_{CM} = \frac{d\vec{V}_{CM}}{dt} = \frac{\sum m_i (d\vec{v}_i/dt)}{M_{total}} = \frac{\sum m_i \vec{a}_i}{M_{total}}$
*   **Intuition:** It's the weighted average of the accelerations of all individual particles.

### Newton's Second Law for a System of Particles

*   **Definition:** The total external force acting on a system of particles equals the product of the total mass of the system and the acceleration of its Centre of Mass.
*   **Formula:** $\vec{F}_{ext} = M_{total} \vec{A}_{CM}$
    *   Where $\vec{F}_{ext} = \sum \vec{F}_{ext,i}$ (vector sum of all external forces).
*   **Intuition:** The CM moves exactly as if all the system's mass were concentrated there, and all external forces were applied directly to it. Internal forces (forces between particles within the system) cancel out in pairs due to Newton's Third Law and therefore do not affect the motion of the CM.
*   **Why it matters:** This is a powerful principle that allows us to analyze the translational motion of complex systems (even deformable ones or those with internal explosions) by treating them as a single particle at the CM.
*   **Real-world examples:**
    *   An exploding bomb in mid-air: The fragments fly everywhere, but the CM of the bomb continues its original parabolic trajectory.
    *   A rocket: The exhaust gases are internal, the CM of the rocket+fuel system moves according to external forces only (gravity, air resistance).
*   **Important observations:**
    *   Knowledge of internal forces is NOT required to determine the motion of the CM.
    *   This equation describes only the *translational* component of the motion.

## 6.4 Linear Momentum of a System of Particles

### Total Linear Momentum (P)

*   **Definition:** The total linear momentum of a system of particles is the vector sum of the linear momenta of all individual particles in the system.
*   **Formula:** $\vec{P} = \sum_{i=1}^{n} \vec{p}_i = \sum_{i=1}^{n} m_i \vec{v}_i$
*   **Relation to CM:** $\vec{P} = M_{total} \vec{V}_{CM}$
*   **Intuition:** It's the "total quantity of motion" for the entire system, as seen from the movement of its CM.

### Newton's Second Law in terms of Momentum

*   **Definition:** The time rate of change of the total linear momentum of a system of particles is equal to the total external force acting on the system.
*   **Formula:** $\vec{F}_{ext} = \frac{d\vec{P}}{dt}$
*   **Intuition:** This is the generalized form of Newton's second law, applicable to systems of particles.

### Conservation of Linear Momentum

*   **Definition:** If the total external force acting on a system of particles is zero ($\vec{F}_{ext} = 0$), then the total linear momentum of the system ($\vec{P}$) remains constant (conserved).
*   **Formula:** If $\vec{F}_{ext} = 0$, then $\vec{P} = \text{constant}$
    *   This implies $\vec{V}_{CM} = \text{constant}$ (since $M_{total}$ is assumed constant).
*   **Intuition:** If nothing from outside pushes or pulls the system, its overall forward motion won't change.
*   **Why it matters:** Allows prediction of system motion in cases like collisions, explosions, or radioactive decay where internal forces are significant but external forces are negligible.
*   **Real-world examples:**
    *   A gun firing a bullet: The total momentum of the gun+bullet system before firing (zero) equals the momentum after firing (bullet forward, gun recoils backward).
    *   Radioactive decay: The product particles fly apart, but their CM remains at rest (or moves with constant velocity) if the parent nucleus was initially at rest (or constant velocity).
    *   Binary star system: The CM of the two stars moves with constant velocity if no external forces act.
*   **Important observations:**
    *   Internal forces do not affect the total linear momentum of the system. They can change individual particle momenta but not the sum.
    *   The law applies to *components* of momentum too: if $F_{ext,x}=0$, then $P_x=$ constant.

## 6.5 Vector Product of Two Vectors (Cross Product)

*   **Definition:** A vector product of two vectors $\vec{a}$ and $\vec{b}$ is a new vector $\vec{c}$ (written as $\vec{a} \times \vec{b}$) such that:
    1.  **Magnitude:** $c = |\vec{a}| |\vec{b}| \sin\theta$, where $\theta$ is the smaller angle between $\vec{a}$ and $\vec{b}$ (0° ≤ θ ≤ 180°).
    2.  **Direction:** $\vec{c}$ is perpendicular to the plane containing $\vec{a}$ and $\vec{b}$. Its direction is given by the **Right-Hand Rule** or **Right-Hand Screw Rule**.
*   **Intuition:** It measures the "perpendicular effect" of one vector on another, crucial for rotational effects. Think of a screw turning.
*   **Why it matters:** Torque and angular momentum are defined as vector products, making this a fundamental concept for rotational motion.
*   **Properties:**
    *   **Non-commutative:** $\vec{a} \times \vec{b} = - (\vec{b} \times \vec{a})$. The order matters!
    *   **Distributive:** $\vec{a} \times (\vec{b} + \vec{c}) = (\vec{a} \times \vec{b}) + (\vec{a} \times \vec{c})$
    *   **Parallel Vectors:** If $\vec{a}$ and $\vec{b}$ are parallel ($\theta=0^\circ$) or anti-parallel ($\theta=180^\circ$), then $\vec{a} \times \vec{b} = 0$. (This means $\vec{a} \times \vec{a} = 0$).
    *   **Reflection:** $\vec{a} \times \vec{b}$ does *not* change sign under reflection.
*   **Component Form:**
    If $\vec{a} = a_x \hat{i} + a_y \hat{j} + a_z \hat{k}$ and $\vec{b} = b_x \hat{i} + b_y \hat{j} + b_z \hat{k}$, then:
    $\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}$
    $= (a_y b_z - a_z b_y) \hat{i} + (a_z b_x - a_x b_z) \hat{j} + (a_x b_y - a_y b_x) \hat{k}$
*   **Elementary Cross Products (for orthogonal unit vectors):**
    *   $\hat{i} \times \hat{i} = \hat{j} \times \hat{j} = \hat{k} \times \hat{k} = 0$
    *   $\hat{i} \times \hat{j} = \hat{k}$
    *   $\hat{j} \times \hat{k} = \hat{i}$
    *   $\hat{k} \times \hat{i} = \hat{j}$
    *   $\hat{j} \times \hat{i} = -\hat{k}$ (and so on)
    *   (Follow a cyclic order: i -> j -> k -> i for positive results).

## 6.6 Angular Velocity and its Relation with Linear Velocity

### Angular Velocity ($\vec{\omega}$)

*   **Definition:** For a particle undergoing circular motion, angular velocity ($\omega$) is the rate of change of angular displacement ($\theta$). For a rigid body rotating about a fixed axis, all its particles have the same angular velocity.
*   **Scalar Form:** $\omega = \frac{d\theta}{dt}$
*   **Vector Nature:** Angular velocity is a vector quantity.
    *   **Magnitude:** $\omega = |\frac{d\theta}{dt}|$
    *   **Direction:** Along the axis of rotation, determined by the Right-Hand Rule: If fingers curl in the direction of rotation, the thumb points in the direction of $\vec{\omega}$.
*   **Intuition:** How fast something is spinning.
*   **Why it matters:** Describes rotational speed and direction. Essential for relating linear and rotational motion.
*   **Units:** radians per second (rad/s).

### Relation between Linear Velocity ($\vec{v}$) and Angular Velocity ($\vec{\omega}$)

*   **Definition:** For a particle at a position $\vec{r}$ from the origin (chosen on the axis of rotation) in a rigid body rotating with angular velocity $\vec{\omega}$, its linear velocity $\vec{v}$ is given by the vector cross product.
*   **Formula:** $\vec{v} = \vec{\omega} \times \vec{r}$
*   **Intuition:** A point further from the axis moves faster linearly, even if all points have the same angular speed. The linear velocity is always tangential to the circular path.
*   **Why it matters:** Connects the kinematics of linear motion to rotational motion.
*   **Magnitude:** $v = \omega r_\perp$, where $r_\perp$ is the perpendicular distance of the particle from the axis of rotation (radius of the circle). Since $\vec{\omega}$ and $\vec{r}_\perp$ are perpendicular, $\sin\theta=1$.
*   **Important observations:**
    *   $\vec{v}$ is always tangential to the circular path of the particle.
    *   $\vec{v}$ is perpendicular to both $\vec{\omega}$ and $\vec{r}$.
    *   For a fixed axis of rotation, the origin is conveniently chosen anywhere on the axis. $\vec{r}$ is the position vector from that origin to the particle.

### Angular Acceleration ($\vec{\alpha}$)

*   **Definition:** The time rate of change of angular velocity.
*   **Formula:** $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$
*   **Intuition:** How fast the spinning speed is changing.
*   **Why it matters:** Causes changes in rotational motion (speeding up or slowing down rotation).
*   **Units:** radians per second squared (rad/s²).
*   **Important observations:** For fixed-axis rotation, if the magnitude of $\vec{\omega}$ changes, $\vec{\alpha}$ is along the same direction as $\vec{\omega}$ (or opposite if slowing down).

## 6.7 Torque and Angular Momentum

### Moment of Force (Torque, $\vec{\tau}$)

*   **Definition:** Torque is the rotational analogue of force. It is a measure of the effectiveness of a force in producing or changing rotational motion about a pivot point or axis.
*   **Formula:** $\vec{\tau} = \vec{r} \times \vec{F}$
    *   Where $\vec{r}$ is the position vector from the pivot point (origin) to the point where the force $\vec{F}$ is applied.
*   **Intuition:** The "twisting effect" of a force. Imagine pushing a door: pushing far from the hinge with force perpendicular to the door creates maximum torque.
*   **Why it matters:** Causes angular acceleration. Determines rotational equilibrium.
*   **Units:** Newton-meter (N·m). Dimensions: [M L² T⁻²] (same as work/energy, but they are fundamentally different quantities, torque is a vector).
*   **Magnitude:** $\tau = r F \sin\theta$
    *   Can also be written as $\tau = F r_\perp$ (where $r_\perp = r \sin\theta$ is the perpendicular distance from the pivot to the line of action of the force, called the "moment arm" or "lever arm").
    *   Or $\tau = r F_\perp$ (where $F_\perp = F \sin\theta$ is the component of force perpendicular to $\vec{r}$).
*   **Direction:** Given by the Right-Hand Rule applied to $\vec{r} \times \vec{F}$.
*   **Important observations:**
    *   Torque is zero if: (1) $\vec{F} = 0$, (2) $\vec{r} = 0$ (force applied at the pivot), or (3) $\vec{F}$ is parallel or anti-parallel to $\vec{r}$ (line of action of force passes through the pivot).

### Angular Momentum of a Particle ($\vec{l}$)

*   **Definition:** Angular momentum is the rotational analogue of linear momentum. For a single particle, it describes its "quantity of rotational motion" about a specified origin.
*   **Formula:** $\vec{l} = \vec{r} \times \vec{p}$
    *   Where $\vec{r}$ is the position vector of the particle from the origin, and $\vec{p} = m\vec{v}$ is its linear momentum.
*   **Intuition:** A particle moving in a straight line can still have angular momentum about a point not on its path. It depends on how far its path is from the reference point and its momentum.
*   **Why it matters:** It's a conserved quantity under certain conditions, very powerful for analyzing rotational systems.
*   **Units:** kg m²/s. Dimensions: [M L² T⁻¹].
*   **Magnitude:** $l = r p \sin\theta$
    *   Can also be written as $l = p r_\perp$ (where $r_\perp = r \sin\theta$ is the perpendicular distance from the origin to the line of action of $\vec{p}$).
    *   Or $l = r p_\perp$ (where $p_\perp = p \sin\theta$ is the component of linear momentum perpendicular to $\vec{r}$).
*   **Direction:** Given by the Right-Hand Rule applied to $\vec{r} \times \vec{p}$.
*   **Important observations:**
    *   Angular momentum is zero if: (1) $\vec{p} = 0$ (particle at rest), (2) $\vec{r} = 0$ (particle at the origin), or (3) $\vec{p}$ is parallel or anti-parallel to $\vec{r}$ (particle moving directly towards or away from the origin).
    *   For a particle, $\vec{l}$ and $\vec{p}$ are generally not parallel.

### Relation between Torque and Angular Momentum (for a particle)

*   **Definition:** The time rate of change of a particle's angular momentum about an origin is equal to the net torque acting on it about the same origin.
*   **Formula:** $\vec{\tau} = \frac{d\vec{l}}{dt}$
*   **Intuition:** Just as force changes linear momentum, torque changes angular momentum. This is Newton's second law for rotational motion for a particle.
*   **Derivation:**
    $\vec{l} = \vec{r} \times \vec{p}$
    $\frac{d\vec{l}}{dt} = \frac{d}{dt} (\vec{r} \times \vec{p})$
    Using product rule for differentiation:
    $\frac{d\vec{l}}{dt} = \left(\frac{d\vec{r}}{dt} \times \vec{p}\right) + \left(\vec{r} \times \frac{d\vec{p}}{dt}\right)$
    Since $\frac{d\vec{r}}{dt} = \vec{v}$ and $\vec{p} = m\vec{v}$, the first term is $(\vec{v} \times m\vec{v})$. Since $\vec{v}$ is parallel to itself, their cross product is zero: $\vec{v} \times m\vec{v} = 0$.
    Also, from Newton's second law, $\frac{d\vec{p}}{dt} = \vec{F}$.
    So, $\frac{d\vec{l}}{dt} = \vec{r} \times \vec{F} = \vec{\tau}$.

### Torque and Angular Momentum for a System of Particles

*   **Total Angular Momentum ($\vec{L}$):** The vector sum of the angular momenta of all individual particles in the system.
    *   $\vec{L} = \sum_{i=1}^{n} \vec{l}_i = \sum_{i=1}^{n} (\vec{r}_i \times \vec{p}_i)$
*   **Total Torque ($\vec{\tau}_{total}$):** The vector sum of the torques acting on all individual particles in the system.
    *   $\vec{\tau}_{total} = \sum_{i=1}^{n} \vec{\tau}_i = \sum_{i=1}^{n} (\vec{r}_i \times \vec{F}_i)$
*   **Relation to Total Angular Momentum:** $\vec{\tau}_{ext} = \frac{d\vec{L}}{dt}$
    *   **Intuition:** Only external torques can change the total angular momentum of a system. Internal torques (due to internal forces between particles) cancel out due to Newton's Third Law and the assumption that internal forces are central (act along the line joining particles).
    *   **Why it matters:** This is the fundamental equation for rotational dynamics of a system.

### Conservation of Angular Momentum

*   **Definition:** If the total external torque acting on a system of particles is zero ($\vec{\tau}_{ext} = 0$), then the total angular momentum of the system ($\vec{L}$) remains constant (conserved).
*   **Formula:** If $\vec{\tau}_{ext} = 0$, then $\vec{L} = \text{constant}$
*   **Intuition:** If there's no overall twisting effect from outside, the system's total spin will remain the same.
*   **Why it matters:** Explains many phenomena from planetary orbits to ice skaters' spins.
*   **Real-world examples:**
    *   **Ice skater:** When an ice skater pulls her arms in, her moment of inertia (I) decreases, so her angular velocity ($\omega$) increases to keep $L=I\omega$ constant.
    *   **Diver:** A diver curling into a tuck position to increase rotational speed for multiple somersaults.
    *   **Planetary motion:** Planets orbit the sun with conserved angular momentum (assuming negligible external torques).
*   **Important observations:**
    *   This applies to *any* system of particles (rigid or non-rigid).
    *   Each component of the angular momentum vector is independently conserved if the corresponding component of external torque is zero.

## 6.8 Equilibrium of a Rigid Body

### Mechanical Equilibrium

*   **Definition:** A rigid body is in mechanical equilibrium if both its linear momentum and angular momentum are not changing with time. This means it has neither linear acceleration nor angular acceleration.
*   **Conditions:**
    1.  **Translational Equilibrium:** The vector sum of all external forces acting on the body is zero.
        *   $\sum \vec{F}_{ext} = 0$
        *   This means $\frac{d\vec{P}}{dt} = 0$, so $\vec{P}$ is constant. (If initially at rest, $\vec{P}=0$ remains).
    2.  **Rotational Equilibrium:** The vector sum of all external torques acting on the body about *any* point is zero.
        *   $\sum \vec{\tau}_{ext} = 0$ (about any point)
        *   This means $\frac{d\vec{L}}{dt} = 0$, so $\vec{L}$ is constant. (If initially not rotating, $\vec{L}=0$ remains).
*   **Intuition:** The body is perfectly balanced and either at rest or moving with constant linear and angular velocity.
*   **Why it matters:** Crucial for designing stable structures (buildings, bridges) and understanding static objects.
*   **Important observations:**
    *   Translational and rotational equilibrium are independent conditions. One can exist without the other.
    *   For 2D problems (forces in a plane), these two vector equations reduce to three scalar equations: $\sum F_x = 0$, $\sum F_y = 0$, and $\sum \tau_z = 0$. (Assuming z is perpendicular to the plane).
    *   If a body is in translational equilibrium ($\sum \vec{F}_{ext} = 0$), then the net torque is the same regardless of the point about which moments are taken. Hence, if it is in rotational equilibrium about one point, it is in rotational equilibrium about any point.

### Couple

*   **Definition:** A pair of forces of equal magnitude, acting in opposite directions, but along different lines of action.
*   **Intuition:** Twisting a bottle cap, turning a steering wheel.
*   **Why it matters:** A couple produces *pure rotational motion* without causing any translational motion.
*   **Properties:**
    *   The net force due to a couple is zero ($\sum \vec{F} = 0$).
    *   The net torque due to a couple is non-zero and is the *same about any point*.
*   **Formula for Magnitude of Couple Torque:** $\tau = F \times d$, where F is the magnitude of one force and d is the perpendicular distance between the lines of action of the two forces (arm of the couple).

### Principle of Moments (Lever)

*   **Definition:** For a lever in rotational equilibrium, the sum of clockwise moments about the fulcrum equals the sum of anticlockwise moments about the fulcrum.
*   **Formula:** $d_1 F_1 = d_2 F_2$
    *   Where $F_1, F_2$ are forces and $d_1, d_2$ are their respective perpendicular distances (lever arms) from the fulcrum.
*   **Intuition:** A seesaw balanced.
*   **Why it matters:** Explains how levers work, providing mechanical advantage.
*   **Mechanical Advantage (MA):** $MA = \frac{\text{Load}}{\text{Effort}} = \frac{F_1}{F_2} = \frac{d_2}{d_1}$
*   **Important observations:** A small effort can lift a large load if the effort arm ($d_2$) is much larger than the load arm ($d_1$).

### Centre of Gravity (CG)

*   **Definition:** The point where the total gravitational torque on the body is zero. It's the point through which the entire weight of the body appears to act.
*   **Intuition:** The point where an object can be perfectly balanced.
*   **Relation to CM:** In a uniform gravitational field (where 'g' is constant throughout the body), the Centre of Gravity coincides with the Centre of Mass. For very large bodies where 'g' varies significantly across its extent (e.g., a mountain range relative to Earth's center), CG and CM might differ. For all practical purposes in NEET, they are usually considered to be the same.
*   **How to find CG (experimental):** Suspend the irregular body from different points. The CG lies at the intersection of the vertical lines drawn downwards from each suspension point.

## 6.9 Moment of Inertia (I)

*   **Definition:** Moment of Inertia is the rotational analogue of mass. It quantifies an object's resistance to changes in its rotational motion (i.e., its rotational inertia). It depends on both the mass of the body and how that mass is distributed relative to the axis of rotation.
*   **Intuition:** How "hard" it is to get something spinning or to stop it from spinning. A heavier object is harder to push, and an object with its mass spread out (like a long rod) is harder to spin than one with mass concentrated near the axis (like a small disc).
*   **Why it matters:** It's a key parameter in rotational dynamics, linking torque to angular acceleration and defining rotational kinetic energy.
*   **Formula:**
    *   **For discrete particles:** $I = \sum_{i=1}^{n} m_i r_i^2$
        *   Where $m_i$ is the mass of the $i^{th}$ particle and $r_i$ is its perpendicular distance from the axis of rotation.
    *   **For continuous body:** $I = \int r^2 dm$
        *   Where $dm$ is an infinitesimal mass element at perpendicular distance $r$ from the axis.
*   **Units:** kg m². Dimensions: [M L²].
*   **Kinetic Energy of Rotation:** $K_{rot} = \frac{1}{2} I \omega^2$
    *   This is the rotational analogue of $K_{linear} = \frac{1}{2} m v^2$.
*   **Important observations:**
    *   Unlike mass, Moment of Inertia is NOT a fixed property of a body. It depends critically on the **axis of rotation** chosen and the **distribution of mass** about that axis.
    *   A flywheel uses a large moment of inertia to resist sudden changes in speed, providing smooth motion.

### Radius of Gyration (k)

*   **Definition:** The radius of gyration of a body about an axis is the distance from the axis at which the entire mass of the body ($M_{total}$) could be concentrated to have the same moment of inertia ($I$) as the actual body.
*   **Formula:** $I = M_{total} k^2 \Rightarrow k = \sqrt{\frac{I}{M_{total}}}$
*   **Intuition:** It's a way to characterize the "effective" distribution of mass from the axis.
*   **Units:** meter (m).
*   **Important observations:** $k$ is a geometric property of the body and the axis.

### Moments of Inertia for Standard Shapes (Table 6.1 Summary from NCERT)

| Body                   | Axis                                      | Moment of Inertia (I) |
| :--------------------- | :---------------------------------------- | :-------------------- |
| Thin circular ring, R  | Perpendicular to plane, at centre         | $M R^2$               |
| Thin circular ring, R  | Diameter                                  | $M R^2 / 2$           |
| Thin rod, length L     | Perpendicular to rod, at midpoint        | $M L^2 / 12$          |
| Circular disc, radius R | Perpendicular to disc at centre           | $M R^2 / 2$           |
| Circular disc, radius R | Diameter                                  | $M R^2 / 4$           |
| Hollow cylinder, R     | Axis of cylinder                          | $M R^2$               |
| Solid cylinder, R      | Axis of cylinder                          | $M R^2 / 2$           |
| Solid sphere, R        | Diameter                                  | $2/5 M R^2$           |

## 6.10 Kinematics of Rotational Motion about a Fixed Axis

*   **Analogies between Linear and Rotational Kinematics (for constant acceleration):**

| Linear Motion             | Rotational Motion (Fixed Axis)          |
| :------------------------ | :-------------------------------------- |
| Displacement: $x$         | Angular Displacement: $\theta$          |
| Velocity: $v = dx/dt$     | Angular Velocity: $\omega = d\theta/dt$ |
| Acceleration: $a = dv/dt$ | Angular Acceleration: $\alpha = d\omega/dt$ |

*   **Equations of Motion (for constant angular acceleration $\alpha$):**
    1.  $\omega = \omega_0 + \alpha t$ (Rotational analogue of $v = v_0 + at$)
    2.  $\theta = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2$ (Rotational analogue of $x = x_0 + v_0 t + \frac{1}{2} at^2$)
    3.  $\omega^2 = \omega_0^2 + 2 \alpha (\theta - \theta_0)$ (Rotational analogue of $v^2 = v_0^2 + 2 a (x - x_0)$)
    *   Where $\theta_0$ and $\omega_0$ are initial angular displacement and angular velocity at $t=0$.
*   **Intuition:** These equations describe how angles, angular speeds, and angular accelerations change over time, just like their linear counterparts describe linear motion.
*   **Why it matters:** Allows calculation of rotational motion parameters when angular acceleration is constant.

## 6.11 Dynamics of Rotational Motion about a Fixed Axis

*   **Simplifications for Fixed Axis Rotation:**
    *   Only torque components *along the fixed axis* cause rotation about that axis. Other torque components (perpendicular to the axis) would tend to change the direction of the axis, but these are assumed to be counteracted by constraint forces from the bearings.
    *   Only force components in planes perpendicular to the axis and position vector components perpendicular to the axis are relevant for calculating torque.

### Work Done by a Torque

*   **Definition:** When a torque acts on a body and causes an angular displacement, it does work.
*   **Formula:** $dW = \tau d\theta$
    *   For a constant torque over an angular displacement $\Delta\theta$: $W = \tau \Delta\theta$
*   **Intuition:** Analogous to $dW = F dx$ for linear motion. More twist and more rotation means more work.
*   **Units:** Joules (J).

### Power in Rotational Motion

*   **Definition:** The rate at which work is done by a torque.
*   **Formula:** $P = \frac{dW}{dt} = \tau \frac{d\theta}{dt} = \tau \omega$
*   **Intuition:** Analogous to $P = Fv$ for linear motion.
*   **Units:** Watts (W).

### Rotational Analogue of Newton's Second Law ($\vec{\tau} = I\vec{\alpha}$)

*   **Definition:** The net external torque acting on a rigid body about a fixed axis is directly proportional to its angular acceleration and the constant of proportionality is its moment of inertia about that axis.
*   **Formula:** $\vec{\tau}_{ext,z} = I_z \vec{\alpha}_z$ (for rotation about z-axis)
    *   Often written as $\tau = I\alpha$ for a fixed axis, considering only magnitudes along that axis.
*   **Intuition:** A larger twist (torque) produces a larger change in spinning speed (angular acceleration). A "heavier" spinner (larger moment of inertia) needs more torque to achieve the same angular acceleration.
*   **Why it matters:** This is the fundamental equation for solving problems involving changes in rotational motion due to applied torques.
*   **Derivation (from work-energy principle):**
    $dW = \tau d\theta$
    By Work-Energy Theorem, $dW = dK = d(\frac{1}{2} I \omega^2)$
    $d(\frac{1}{2} I \omega^2) = \frac{1}{2} I (2\omega d\omega) = I \omega d\omega$ (assuming I is constant)
    So, $\tau d\theta = I \omega d\omega$
    Divide by $dt$: $\tau \frac{d\theta}{dt} = I \omega \frac{d\omega}{dt}$
    $\tau \omega = I \omega \alpha$
    If $\omega \neq 0$, then $\tau = I\alpha$.

## 6.12 Angular Momentum in case of Rotation about a Fixed Axis

*   **Total Angular Momentum for a Rigid Body about a Fixed Axis:**
    *   For a particle in the body, $\vec{l} = \vec{r} \times \vec{p}$. In general, $\vec{l}$ is not parallel to the axis of rotation.
    *   For the *entire rigid body* rotating about a fixed axis (say, the z-axis), the component of the total angular momentum *along the fixed axis* is:
        $L_z = I_z \omega_z$ (or simply $L_z = I\omega$)
        Where $I$ is the moment of inertia about that axis and $\omega$ is the angular velocity about that axis.
*   **When is $\vec{L}$ parallel to $\vec{\omega}$?**
    *   $\vec{L} = I\vec{\omega}$ (vector equation) holds true only for cases where the axis of rotation is an **axis of symmetry** of the rigid body. For such symmetric bodies, the components of angular momentum perpendicular to the axis cancel out.
    *   For bodies that are not symmetric about the axis of rotation (e.g., a cuboid rotating about an axis not passing through its center of mass or along a symmetry axis), the total angular momentum vector $\vec{L}$ is *not* necessarily parallel to the angular velocity vector $\vec{\omega}$.
*   **Conservation of Angular Momentum for Fixed Axis Rotation:**
    *   From $\vec{\tau}_{ext} = \frac{d\vec{L}}{dt}$, for a fixed axis (e.g., z-axis), we consider only the z-component of torque and angular momentum.
    *   If the external torque component along the fixed axis is zero ($\tau_{ext,z} = 0$), then the angular momentum component along that axis ($L_z = I\omega$) is conserved.
    *   **Formula:** If $\tau_{ext,z} = 0$, then $I\omega = \text{constant}$
        *   This means $I_1 \omega_1 = I_2 \omega_2$ if the moment of inertia changes.
*   **Intuition:** An ice skater pulling in her arms reduces her $I$, so her $\omega$ increases to keep $I\omega$ constant.
*   **Why it matters:** Explains how objects change their rotational speed when their mass distribution (and thus $I$) changes, like in many sports and dance.

---

# NCERT GOLDEN LINES

1.  **"A particle is ideally represented as a point mass having no size."**
    *   **Explanation:** This highlights the idealized nature of a particle, useful for simplifying initial mechanics problems, but limited for extended bodies.
2.  **"In pure translational motion at any instant of time, all particles of the body have the same velocity."**
    *   **Explanation:** Defines the key characteristic of pure translation – uniform velocity for all parts.
3.  **"In rotation of a rigid body about a fixed axis, every particle of the body moves in a circle, which lies in a plane perpendicular to the axis and has its centre on the axis."**
    *   **Explanation:** Precise definition of fixed-axis rotation, detailing the paths of individual particles.
4.  **"The centre of mass of a system of particles moves as if all the mass of the system was concentrated at the centre of mass and all the external forces were applied at that point."**
    *   **Explanation:** The most crucial conceptual statement about the utility of CM; it decouples translational motion from internal dynamics.
5.  **"To determine the motion of the centre of mass no knowledge of internal forces of the system of particles is required; for this purpose we need to know only the external forces."**
    *   **Explanation:** Reinforces the power of the CM concept by showing its independence from complex internal interactions.
6.  **"Thus, when the total external force acting on a system of particles is zero, the total linear momentum of the system is constant. This is the law of conservation of the total linear momentum of a system of particles."**
    *   **Explanation:** Direct statement of a fundamental conservation law.
7.  **"A vector product of two vectors a and b is a vector c such that magnitude of c = ab sinθ... and c is perpendicular to the plane containing a and b."**
    *   **Explanation:** Provides the definition of the cross product, which is foundational for torque and angular momentum.
8.  **"The magnitude of the linear velocity v of a particle moving in a circle is related to the angular velocity of the particle ω by the simple relation v = ωr."**
    *   **Explanation:** Scalar relation between linear and angular speed, for circular motion.
9.  **"The angular velocity vector lies along the axis of rotation, and points out in the direction in which a right handed screw would advance, if the head of the screw is rotated with the body."**
    *   **Explanation:** Defines the vector nature and direction of angular velocity.
10. **"The time rate of change of the angular momentum of a particle is equal to the torque acting on it." ($\vec{\tau} = \frac{d\vec{l}}{dt}$)**
    *   **Explanation:** The rotational analogue of Newton's second law for a particle.
11. **"Thus, the time rate of the total angular momentum of a system of particles about a point... is equal to the sum of the external torques... acting on the system taken about the same point." ($\vec{\tau}_{ext} = \frac{d\vec{L}}{dt}$)**
    *   **Explanation:** Generalization of Newton's second law for rotational motion to a system of particles. Crucial for conservation of angular momentum.
12. **"If the total external torque on a system of particles is zero, then the total angular momentum of the system is conserved, i.e. remains constant."**
    *   **Explanation:** Statement of the principle of conservation of angular momentum.
13. **"A rigid body is said to be in mechanical equilibrium, if both its linear momentum and angular momentum are not changing with time, or equivalently, the body has neither linear acceleration nor angular acceleration."**
    *   **Explanation:** Defines the conditions for mechanical equilibrium (both translational and rotational).
14. **"If the translational equilibrium condition... holds for a rigid body, then such a shift of origin does not matter, i.e. the rotational equilibrium condition is independent of the location of the origin about which the torques are taken."**
    *   **Explanation:** An important property of torque in equilibrium – if net force is zero, net torque is zero about ANY point.
15. **"A pair of forces of equal magnitude but acting in opposite directions with different lines of action is known as a couple or torque. A couple produces rotation without translation."**
    *   **Explanation:** Defines a couple and its unique effect.
16. **"The centre of gravity of a body coincides with the centre of mass in uniform gravity or gravity-free space."**
    *   **Explanation:** Clarifies the relationship between CG and CM for practical purposes.
17. **"The parameter, moment of inertia I, is the desired rotational analogue of mass in linear motion."**
    *   **Explanation:** States the fundamental analogy that makes moment of inertia so important.
18. **"Moment of inertia is not a fixed quantity but depends on distribution of mass about the axis of rotation, and the orientation and position of the axis of rotation with respect to the body as a whole."**
    *   **Explanation:** Emphasizes that moment of inertia is axis-dependent, unlike mass.
19. **"Just as force produces acceleration, torque produces angular acceleration in a body. The angular acceleration is directly proportional to the applied torque and is inversely proportional to the moment of inertia of the body." ($\tau = I\alpha$)**
    *   **Explanation:** Newton's second law for rotational motion about a fixed axis.
20. **"For such bodies [symmetric about axis of rotation], ... L_z = Iω holds good."**
    *   **Explanation:** Clarifies when the simple scalar relation between angular momentum and angular velocity holds.

---

# FORMULA SHEET

## I. Centre of Mass (CM)

1.  **For Discrete Particles:**
    *   $\vec{R}_{CM} = \frac{\sum m_i \vec{r}_i}{\sum m_i} = \frac{\sum m_i \vec{r}_i}{M_{total}}$
    *   $X_{CM} = \frac{\sum m_i x_i}{M_{total}}$, $Y_{CM} = \frac{\sum m_i y_i}{M_{total}}$, $Z_{CM} = \frac{\sum m_i z_i}{M_{total}}$
    *   **Variables:** $m_i$ = mass of $i^{th}$ particle (kg), $\vec{r}_i$ = position vector of $i^{th}$ particle (m), $M_{total}$ = total mass of system (kg).
    *   **Units:** meters (m).
    *   **When to use:** To find the average position of mass for a system of point masses.
    *   **Common Mistakes:** Forgetting to divide by total mass. Incorrectly choosing origin.

2.  **For Continuous Bodies:**
    *   $\vec{R}_{CM} = \frac{1}{M_{total}} \int \vec{r} \ dm$
    *   $X_{CM} = \frac{1}{M_{total}} \int x \ dm$, etc.
    *   **Variables:** $dm$ = infinitesimal mass element (kg), $\vec{r}$ = position vector of $dm$ (m).
    *   **Units:** meters (m).
    *   **When to use:** To find the CM of extended objects with distributed mass.
    *   **Common Mistakes:** Incorrect setup of integral limits or expression for $dm$.

3.  **Velocity of CM:**
    *   $\vec{V}_{CM} = \frac{d\vec{R}_{CM}}{dt} = \frac{\sum m_i \vec{v}_i}{M_{total}}$
    *   **Variables:** $\vec{v}_i$ = velocity of $i^{th}$ particle (m/s).
    *   **Units:** m/s.
    *   **When to use:** To find the translational velocity of the system as a whole.

4.  **Acceleration of CM:**
    *   $\vec{A}_{CM} = \frac{d\vec{V}_{CM}}{dt} = \frac{\sum m_i \vec{a}_i}{M_{total}}$
    *   **Variables:** $\vec{a}_i$ = acceleration of $i^{th}$ particle (m/s²).
    *   **Units:** m/s².
    *   **When to use:** To find the translational acceleration of the system as a whole.

5.  **Newton's 2nd Law for CM:**
    *   $\vec{F}_{ext} = M_{total} \vec{A}_{CM}$
    *   **Variables:** $\vec{F}_{ext}$ = net external force (N).
    *   **Units:** Newtons (N).
    *   **When to use:** To relate external forces to the motion of the system's CM.
    *   **Common Mistakes:** Including internal forces in $\vec{F}_{ext}$.

## II. Linear Momentum

1.  **Total Linear Momentum of a System:**
    *   $\vec{P} = \sum m_i \vec{v}_i = M_{total} \vec{V}_{CM}$
    *   **Variables:** $\vec{P}$ = total linear momentum (kg m/s).
    *   **Units:** kg m/s.
    *   **When to use:** To quantify the total translational motion of a system.

2.  **Newton's 2nd Law (Momentum Form):**
    *   $\vec{F}_{ext} = \frac{d\vec{P}}{dt}$
    *   **When to use:** Alternative form of Newton's 2nd Law for systems.

3.  **Conservation of Linear Momentum:**
    *   If $\vec{F}_{ext} = 0$, then $\vec{P} = \text{constant}$.
    *   **When to use:** In systems where external forces are negligible (e.g., collisions, explosions).
    *   **Common Mistakes:** Applying when external forces are non-zero.

## III. Vector Product (Cross Product)

1.  **Definition:**
    *   $\vec{c} = \vec{a} \times \vec{b}$
    *   Magnitude: $|\vec{c}| = |\vec{a}| |\vec{b}| \sin\theta$
    *   Direction: Perpendicular to plane of $\vec{a}$ and $\vec{b}$ by Right-Hand Rule.
    *   **Units:** Product of units of $\vec{a}$ and $\vec{b}$.
    *   **When to use:** For calculations involving torque, angular momentum, etc.
    *   **Common Mistakes:** Incorrect direction due to faulty right-hand rule application. Incorrect sign for non-commutative property.

2.  **Component Form:**
    *   $\vec{a} \times \vec{b} = (a_y b_z - a_z b_y) \hat{i} + (a_z b_x - a_x b_z) \hat{j} + (a_x b_y - a_y b_x) \hat{k}$
    *   **When to use:** When vectors are given in Cartesian components.

## IV. Angular Velocity & Acceleration

1.  **Angular Velocity:**
    *   $\omega = \frac{d\theta}{dt}$ (scalar magnitude)
    *   $\vec{\omega}$ direction by Right-Hand Rule.
    *   **Units:** rad/s.
    *   **When to use:** To describe rotational speed.

2.  **Linear and Angular Velocity Relation:**
    *   $\vec{v} = \vec{\omega} \times \vec{r}$
    *   Magnitude: $v = \omega r_\perp$ (where $r_\perp$ is perpendicular distance to axis).
    *   **Units:** m/s.
    *   **When to use:** To find linear velocity of a point on a rotating body.
    *   **Common Mistakes:** Using full 'r' instead of perpendicular 'r' for scalar magnitude calculation.

3.  **Angular Acceleration:**
    *   $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$
    *   **Units:** rad/s².
    *   **When to use:** To describe rate of change of rotational speed.

## V. Torque (Moment of Force)

1.  **Definition:**
    *   $\vec{\tau} = \vec{r} \times \vec{F}$
    *   Magnitude: $\tau = r F \sin\theta = F r_\perp = r F_\perp$
    *   **Variables:** $\vec{F}$ = force (N), $\vec{r}$ = position vector from pivot (m).
    *   **Units:** N m.
    *   **When to use:** To calculate the twisting effect of a force.
    *   **Common Mistakes:** Confusing r with r_perp. Incorrectly identifying pivot point for 'r'.

## VI. Angular Momentum

1.  **For a Particle:**
    *   $\vec{l} = \vec{r} \times \vec{p} = \vec{r} \times (m\vec{v})$
    *   Magnitude: $l = r p \sin\theta = p r_\perp = r p_\perp$
    *   **Variables:** $\vec{p}$ = linear momentum (kg m/s).
    *   **Units:** kg m²/s.
    *   **When to use:** To calculate angular momentum of a single particle.

2.  **For a System of Particles:**
    *   $\vec{L} = \sum \vec{l}_i = \sum (\vec{r}_i \times \vec{p}_i)$
    *   **Units:** kg m²/s.
    *   **When to use:** To find total angular momentum of a system.

3.  **Relation between Torque and Angular Momentum:**
    *   $\vec{\tau}_{ext} = \frac{d\vec{L}}{dt}$
    *   **When to use:** Fundamental equation relating net external torque to change in total angular momentum.

4.  **Conservation of Angular Momentum:**
    *   If $\vec{\tau}_{ext} = 0$, then $\vec{L} = \text{constant}$.
    *   For fixed axis (and symmetric bodies): $I\omega = \text{constant} \implies I_1 \omega_1 = I_2 \omega_2$
    *   **When to use:** When net external torque is zero (e.g., ice skater, planetary motion).
    *   **Common Mistakes:** Assuming total L is conserved when only one component is. Forgetting that $I$ can change.

## VII. Equilibrium of a Rigid Body

1.  **Conditions for Mechanical Equilibrium:**
    *   Translational Equilibrium: $\sum \vec{F}_{ext} = 0$
    *   Rotational Equilibrium: $\sum \vec{\tau}_{ext} = 0$ (about any point)
    *   **When to use:** For static equilibrium problems (beams, ladders, etc.).
    *   **Common Mistakes:** Not taking moments about the correct point (though any point works if $\sum F=0$, choosing a pivot wisely simplifies calculations).

2.  **Principle of Moments (Lever):**
    *   $F_1 d_1 = F_2 d_2$ (for forces creating opposite turning effects)
    *   **When to use:** Lever problems.

## VIII. Moment of Inertia (I)

1.  **Definition (Discrete Particles):**
    *   $I = \sum m_i r_i^2$
    *   **Units:** kg m².
    *   **When to use:** To calculate rotational inertia of systems of point masses.

2.  **Definition (Continuous Body):**
    *   $I = \int r^2 dm$
    *   **Units:** kg m².
    *   **When to use:** To calculate rotational inertia of extended bodies.

3.  **Rotational Kinetic Energy:**
    *   $K_{rot} = \frac{1}{2} I \omega^2$
    *   **Units:** Joules (J).
    *   **When to use:** To calculate kinetic energy due to rotation.

4.  **Radius of Gyration:**
    *   $k = \sqrt{\frac{I}{M_{total}}}$ or $I = M_{total} k^2$
    *   **Units:** meters (m).
    *   **When to use:** To characterize mass distribution relative to an axis.

## IX. Rotational Dynamics (Fixed Axis)

1.  **Newton's 2nd Law (Rotational):**
    *   $\tau_{ext} = I \alpha$
    *   **Units:** N m = kg m²/s².
    *   **When to use:** To relate net torque to angular acceleration.
    *   **Common Mistakes:** Using linear force/mass instead of torque/moment of inertia.

2.  **Work Done by Torque:**
    *   $dW = \tau d\theta$
    *   **Units:** Joules (J).
    *   **When to use:** To calculate work done during rotational motion.

3.  **Power (Rotational):**
    *   $P = \tau \omega$
    *   **Units:** Watts (W).
    *   **When to use:** To calculate instantaneous power in rotational motion.

## X. Rotational Kinematics (Fixed Axis, Constant $\alpha$)

1.  $\omega = \omega_0 + \alpha t$
2.  $\theta = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2$
3.  $\omega^2 = \omega_0^2 + 2 \alpha (\theta - \theta_0)$
    *   **Variables:** $\theta$ = angular displacement (rad), $\omega$ = angular velocity (rad/s), $\alpha$ = angular acceleration (rad/s²), $t$ = time (s).
    *   **Units:** rad, rad/s, rad/s², s.
    *   **When to use:** Problems involving constant angular acceleration.
    *   **Common Mistakes:** Forgetting to convert RPM to rad/s. Using degrees instead of radians.

---

# DERIVATIONS AND LOGIC

## 1. Centre of Mass Position, Velocity, and Acceleration

*   **Logic:** Start with the definition of the position vector of the CM. Then, differentiate it with respect to time to get velocity, and differentiate velocity with respect to time to get acceleration. This shows how the CM's motion is the 'average' motion of the system's particles.
*   **Derivation:**
    1.  **Position:** $\vec{R}_{CM} = \frac{\sum m_i \vec{r}_i}{M_{total}}$ (Definition)
    2.  **Velocity:** Differentiate $\vec{R}_{CM}$ w.r.t. $t$:
        $\vec{V}_{CM} = \frac{d\vec{R}_{CM}}{dt} = \frac{1}{M_{total}} \sum m_i \frac{d\vec{r}_i}{dt} = \frac{\sum m_i \vec{v}_i}{M_{total}}$ (assuming $m_i$ are constant).
    3.  **Acceleration:** Differentiate $\vec{V}_{CM}$ w.r.t. $t$:
        $\vec{A}_{CM} = \frac{d\vec{V}_{CM}}{dt} = \frac{1}{M_{total}} \sum m_i \frac{d\vec{v}_i}{dt} = \frac{\sum m_i \vec{a}_i}{M_{total}}$

## 2. Newton's Second Law for a System of Particles ($\vec{F}_{ext} = M_{total} \vec{A}_{CM}$)

*   **Logic:** Start with $\vec{A}_{CM}$ and multiply by $M_{total}$. Then use Newton's 2nd Law for individual particles ($\vec{F}_i = m_i \vec{a}_i$) and sum all forces. The crucial step is to show that internal forces cancel out.
*   **Derivation:**
    1.  We have $\vec{A}_{CM} = \frac{\sum m_i \vec{a}_i}{M_{total}}$
    2.  So, $M_{total} \vec{A}_{CM} = \sum m_i \vec{a}_i$
    3.  From Newton's 2nd Law, $m_i \vec{a}_i = \vec{F}_i$, where $\vec{F}_i$ is the net force on particle $i$.
    4.  Thus, $M_{total} \vec{A}_{CM} = \sum \vec{F}_i$
    5.  The force $\vec{F}_i$ on particle $i$ can be written as the sum of external forces ($\vec{F}_{ext,i}$) and internal forces ($\vec{F}_{int,i}$) acting on it: $\vec{F}_i = \vec{F}_{ext,i} + \vec{F}_{int,i}$.
    6.  So, $M_{total} \vec{A}_{CM} = \sum (\vec{F}_{ext,i} + \vec{F}_{int,i}) = \sum \vec{F}_{ext,i} + \sum \vec{F}_{int,i}$
    7.  According to Newton's 3rd Law, internal forces occur in equal and opposite pairs. For any pair of particles $i$ and $j$, the force $\vec{F}_{ij}$ (on $i$ due to $j$) and $\vec{F}_{ji}$ (on $j$ due to $i$) are such that $\vec{F}_{ij} = -\vec{F}_{ji}$. Therefore, when summed over all pairs, $\sum \vec{F}_{int,i} = 0$.
    8.  Hence, $M_{total} \vec{A}_{CM} = \sum \vec{F}_{ext,i} = \vec{F}_{ext}$.
        So, $\vec{F}_{ext} = M_{total} \vec{A}_{CM}$.

## 3. Relation between Torque and Angular Momentum ($\vec{\tau} = \frac{d\vec{L}}{dt}$)

*   **Logic:** This derivation follows the same pattern as for a single particle, but now for the total angular momentum of the system. The key insight is again that internal forces, and thus internal torques, cancel out.
*   **Derivation:**
    1.  Total angular momentum of the system: $\vec{L} = \sum \vec{l}_i = \sum (\vec{r}_i \times \vec{p}_i)$.
    2.  Differentiate with respect to time: $\frac{d\vec{L}}{dt} = \sum \frac{d\vec{l}_i}{dt}$.
    3.  For each particle, we know $\frac{d\vec{l}_i}{dt} = \vec{\tau}_i$, where $\vec{\tau}_i = \vec{r}_i \times \vec{F}_i$ is the net torque on particle $i$.
    4.  So, $\frac{d\vec{L}}{dt} = \sum \vec{\tau}_i$.
    5.  Each torque $\vec{\tau}_i$ can be due to external forces ($\vec{\tau}_{ext,i} = \vec{r}_i \times \vec{F}_{ext,i}$) and internal forces ($\vec{\tau}_{int,i} = \vec{r}_i \times \vec{F}_{int,i}$).
        $\frac{d\vec{L}}{dt} = \sum \vec{\tau}_{ext,i} + \sum \vec{\tau}_{int,i} = \vec{\tau}_{ext} + \vec{\tau}_{int}$.
    6.  For internal torques to cancel, we assume not only $\vec{F}_{ij} = -\vec{F}_{ji}$ (Newton's 3rd Law), but also that these forces are **central**, meaning they act along the line joining the two particles.
    7.  Consider two particles $i$ and $j$. The internal forces are $\vec{F}_{ij}$ and $\vec{F}_{ji}$.
        The internal torque due to this pair is $\vec{\tau}_{ij} = \vec{r}_i \times \vec{F}_{ij} + \vec{r}_j \times \vec{F}_{ji}$.
        Since $\vec{F}_{ji} = -\vec{F}_{ij}$: $\vec{\tau}_{ij} = \vec{r}_i \times \vec{F}_{ij} - \vec{r}_j \times \vec{F}_{ij} = (\vec{r}_i - \vec{r}_j) \times \vec{F}_{ij}$.
        Since $\vec{F}_{ij}$ acts along the line joining $\vec{r}_i$ and $\vec{r}_j$, the vector $(\vec{r}_i - \vec{r}_j)$ (which points from $j$ to $i$) is parallel to $\vec{F}_{ij}$.
        Therefore, their cross product is zero: $(\vec{r}_i - \vec{r}_j) \times \vec{F}_{ij} = 0$.
    8.  Thus, the sum of all internal torques $\sum \vec{\tau}_{int,i} = 0$.
    9.  Hence, $\frac{d\vec{L}}{dt} = \vec{\tau}_{ext}$.

## 4. Rotational Kinetic Energy ($K_{rot} = \frac{1}{2} I \omega^2$)

*   **Logic:** Start with the definition of linear kinetic energy for each particle and sum them up, using the relationship between linear and angular velocity.
*   **Derivation:**
    1.  Consider a rigid body rotating about a fixed axis with angular velocity $\omega$.
    2.  Each particle $i$ of mass $m_i$ at a perpendicular distance $r_i$ from the axis has a linear velocity $v_i = \omega r_i$.
    3.  The kinetic energy of this particle is $K_i = \frac{1}{2} m_i v_i^2 = \frac{1}{2} m_i (\omega r_i)^2 = \frac{1}{2} m_i r_i^2 \omega^2$.
    4.  The total kinetic energy of the rigid body is the sum of kinetic energies of all its particles:
        $K_{rot} = \sum K_i = \sum \left(\frac{1}{2} m_i r_i^2 \omega^2\right)$.
    5.  Since $\frac{1}{2}$ and $\omega^2$ are common for all particles (for a rigid body), we can take them out of the summation:
        $K_{rot} = \frac{1}{2} \left(\sum m_i r_i^2\right) \omega^2$.
    6.  By definition, $\sum m_i r_i^2$ is the moment of inertia $I$ of the body about the axis of rotation.
    7.  Therefore, $K_{rot} = \frac{1}{2} I \omega^2$.

## 5. Rotational Equations of Motion (for constant $\alpha$)

*   **Logic:** These are derived directly by integrating the definitions of angular velocity and angular acceleration, analogous to linear kinematics.
*   **Derivation:**
    1.  **From $\alpha = d\omega/dt$ (definition of angular acceleration):**
        *   $d\omega = \alpha dt$
        *   Integrate from initial time $t=0$ (where $\omega = \omega_0$) to time $t$ (where $\omega = \omega$):
            $\int_{\omega_0}^{\omega} d\omega = \int_0^t \alpha dt$
            $\omega - \omega_0 = \alpha t$ (since $\alpha$ is constant)
            $\boxed{\omega = \omega_0 + \alpha t}$
    2.  **From $\omega = d\theta/dt$ (definition of angular velocity) and the first equation:**
        *   $d\theta = \omega dt = (\omega_0 + \alpha t) dt$
        *   Integrate from $t=0$ (where $\theta = \theta_0$) to $t$ (where $\theta = \theta$):
            $\int_{\theta_0}^{\theta} d\theta = \int_0^t (\omega_0 + \alpha t) dt$
            $\theta - \theta_0 = \int_0^t \omega_0 dt + \int_0^t \alpha t dt$
            $\theta - \theta_0 = \omega_0 t + \frac{1}{2} \alpha t^2$
            $\boxed{\theta = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2}$
    3.  **To get the third equation (independent of time):**
        *   From $\omega = \omega_0 + \alpha t$, we have $t = \frac{\omega - \omega_0}{\alpha}$.
        *   Substitute this into the second equation:
            $\theta - \theta_0 = \omega_0 \left(\frac{\omega - \omega_0}{\alpha}\right) + \frac{1}{2} \alpha \left(\frac{\omega - \omega_0}{\alpha}\right)^2$
            $\theta - \theta_0 = \frac{\omega_0 \omega - \omega_0^2}{\alpha} + \frac{1}{2} \alpha \frac{(\omega - \omega_0)^2}{\alpha^2}$
            $\theta - \theta_0 = \frac{\omega_0 \omega - \omega_0^2}{\alpha} + \frac{(\omega^2 - 2\omega \omega_0 + \omega_0^2)}{2\alpha}$
            Multiply by $2\alpha$:
            $2\alpha(\theta - \theta_0) = 2\omega_0 \omega - 2\omega_0^2 + \omega^2 - 2\omega \omega_0 + \omega_0^2$
            $2\alpha(\theta - \theta_0) = \omega^2 - \omega_0^2$
            $\boxed{\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0)}$

---

# NEET HIGH-YIELD CONCEPTS

1.  **Centre of Mass (CM) Calculations:**
    *   **Discrete Systems:** Finding CM for 2, 3 or more particles. Example: Particles at vertices of a triangle, or on an axis.
    *   **Continuous Systems (Symmetry):** Finding CM for homogeneous rods, rings, discs, spheres, cuboids by inspection (at geometric center).
    *   **Cut-out Problems:** Finding CM of a remaining portion after cutting a part from a uniform lamina. This is a common numerical type.
    *   **Motion of CM:** Understanding that $\vec{F}_{ext} = M_{total} \vec{A}_{CM}$ and $\vec{P} = M_{total} \vec{V}_{CM}$. Questions involving explosions or changing internal configurations where CM motion remains unaffected by internal forces.

2.  **Vector Product ($\vec{A} \times \vec{B}$):**
    *   **Direction:** Mastering the Right-Hand Rule is crucial for torque and angular momentum directions.
    *   **Magnitude:** $AB \sin\theta$.
    *   **Component form:** Calculation of cross product given $\hat{i}, \hat{j}, \hat{k}$ components.

3.  **Torque ($\vec{\tau} = \vec{r} \times \vec{F}$):**
    *   **Calculation:** Given position vector and force vector, find torque.
    *   **Conceptual Understanding:** When is torque zero? (Force through origin, force parallel to $\vec{r}$). What causes rotation?
    *   **Units and Dimensions.**

4.  **Angular Momentum ($\vec{L}$ and $\vec{l}$):**
    *   **For a particle:** $\vec{l} = \vec{r} \times \vec{p}$.
    *   **For a rigid body:** $L_z = I\omega$ (for fixed axis, especially symmetric bodies).
    *   **Units and Dimensions.**

5.  **Conservation of Angular Momentum ($I\omega = \text{constant}$):**
    *   **Most frequently tested concept.** Questions involving change in moment of inertia leading to change in angular velocity (ice skater, diver, rotating platforms).
    *   **Conditions:** Zero net external torque.

6.  **Newton's Second Law for Rotation ($\tau = I\alpha$):**
    *   **Numerical Problems:** Calculating $\alpha$ given $\tau$ and $I$, or $\tau$ given $I$ and $\alpha$. Often combined with rotational kinematics.
    *   **Analogies with linear motion.**

7.  **Equilibrium of Rigid Bodies:**
    *   **Conditions:** Both $\sum \vec{F}_{ext} = 0$ AND $\sum \vec{\tau}_{ext} = 0$.
    *   **Ladder Problems, Beam Problems:** These are classic applications where reactions and tensions need to be calculated using both translational and rotational equilibrium conditions.
    *   **Independence of origin for torque:** Understanding why if $\sum F=0$, then $\sum \tau=0$ about *any* point.

8.  **Moment of Inertia (I):**
    *   **Conceptual understanding:** Dependence on mass distribution and axis.
    *   **Standard formulae (from Table 6.1):** Memorization for various shapes (ring, disc, rod, sphere, cylinder).
    *   **Radius of Gyration ($k$):** Definition and relation to $I$.

9.  **Rotational Kinematics Equations:**
    *   Solving problems involving constant angular acceleration, finding $\omega$, $\theta$, $t$.
    *   Conversion between revolutions per minute (RPM) and radians per second (rad/s).

10. **Work and Power in Rotational Motion:**
    *   $W = \tau \Delta\theta$ and $P = \tau \omega$. Simple direct application often asked.

---

# CONCEPTUAL TRAPS

1.  **Confusing Centre of Mass (CM) and Centre of Gravity (CG):** While often coincident in NEET problems (uniform 'g'), they are conceptually distinct. CM depends on mass distribution, CG depends on gravity field.
2.  **Internal Forces/Torques:** Internal forces do NOT affect the motion of the CM. Internal torques do NOT affect the total angular momentum of the system (assuming central forces). Many problems try to trick students into considering internal effects on CM/L.
3.  **Vector vs. Scalar Quantities:**
    *   Angular velocity $\vec{\omega}$ and Angular momentum $\vec{L}$ are vectors. Their directions matter.
    *   For a single particle, $\vec{l}$ is not necessarily parallel to $\vec{\omega}$.
    *   For a rigid body, $\vec{L}$ is parallel to $\vec{\omega}$ only if the axis of rotation is an axis of symmetry. Don't always assume $\vec{L} = I\vec{\omega}$ vectorially.
4.  **Direction of Vector Product ($\vec{r} \times \vec{F}$ or $\vec{r} \times \vec{p}$):** Mistakes in applying the Right-Hand Rule are common. A positive z-axis torque means anti-clockwise rotation in xy-plane.
5.  **Moment of Inertia (I) Dependence:** Forgetting that $I$ depends on the **axis of rotation** (position and orientation) and **mass distribution**, not just the total mass.
6.  **Pivot Point for Torque Calculation:** Choosing a convenient pivot point for equilibrium problems (e.g., where an unknown force acts) can simplify calculations, but ensure you sum torques about *that same point* for all forces. For non-equilibrium problems, the pivot must be clearly defined.
7.  **Conditions for Equilibrium:** Forgetting one of the two conditions ($\sum \vec{F}_{ext}=0$ OR $\sum \vec{\tau}_{ext}=0$). Both must be met for complete mechanical equilibrium.
8.  **Units:** Using RPM instead of rad/s, or using degrees instead of radians in rotational kinematic equations or work/power calculations.
9.  **"Pure Translation" vs. "Pure Rotation":** Misinterpreting what these terms imply for particle velocities and accelerations within the body.
10. **Conservation Laws Application:** Applying conservation of linear momentum when external forces are present (e.g., collision on a rough surface). Applying conservation of angular momentum when external torques are present.
11. **Sign Convention for Torque:** Be consistent. Clockwise torques as negative, anticlockwise as positive (or vice-versa), or use vector notation consistently.
12. **Work Done by Centripetal Force:** Centripetal force does no work because it's always perpendicular to displacement. This might be relevant in rotational work-energy problems.

---

# MEMORY BOOSTERS

1.  **Linear vs. Rotational Analogies:** Create a mental table and constantly compare. This is the most powerful booster for this chapter.
    *   Mass ($m$) $\leftrightarrow$ Moment of Inertia ($I$)
    *   Force ($\vec{F}$) $\leftrightarrow$ Torque ($\vec{\tau}$)
    *   Linear Displacement ($\vec{x}$) $\leftrightarrow$ Angular Displacement ($\vec{\theta}$)
    *   Linear Velocity ($\vec{v}$) $\leftrightarrow$ Angular Velocity ($\vec{\omega}$)
    *   Linear Acceleration ($\vec{a}$) $\leftrightarrow$ Angular Acceleration ($\vec{\alpha}$)
    *   Linear Momentum ($\vec{p}$) $\leftrightarrow$ Angular Momentum ($\vec{L}$)
    *   $F=ma \leftrightarrow \tau = I\alpha$
    *   $K = \frac{1}{2}mv^2 \leftrightarrow K = \frac{1}{2}I\omega^2$
    *   $P = Fv \leftrightarrow P = \tau\omega$
    *   $W = Fx \leftrightarrow W = \tau\theta$
2.  **Right-Hand Rule:** Practice it constantly for vector products.
    *   For $\vec{A} \times \vec{B}$: Point fingers in direction of $\vec{A}$, curl towards $\vec{B}$. Thumb points in direction of $\vec{A} \times \vec{B}$.
    *   For $\vec{\omega}$: Curl fingers in direction of rotation. Thumb points in direction of $\vec{\omega}$.
3.  **CM as "Balancing Point":** Visualize the CM as the point where you could balance the entire object. This helps for conceptual understanding of its motion.
4.  **Torque as "Twist":** Think of torque as the 'twisting' or 'turning' effect. A larger twist means more rotation.
5.  **Moment of Inertia - "Rotational Laziness":** Just like mass is inertia to linear motion, moment of inertia is inertia to rotational motion. A high I means it's 'lazy' to start or stop rotating.
    *   **Mnemonic:** "I am Lazy (I = MR²)" - a simple way to remember the basic form.
6.  **Conservation Laws:** "No external force, no change in total linear momentum. No external torque, no change in total angular momentum." Simple, yet powerful.
7.  **Ice Skater Analogy:** Always remember the ice skater for conservation of angular momentum ($I\omega=$ constant). Arms in = small $I$, large $\omega$. Arms out = large $I$, small $\omega$.
8.  **Exploding Bomb Analogy:** For conservation of linear momentum and CM motion. The CM of fragments continues the same path as if no explosion occurred.
9.  **Standard Moments of Inertia:** Visualise the shapes and their axes.
    *   **Ring/Hollow Cylinder about its axis:** All mass at radius R, so $I = MR^2$.
    *   **Disc/Solid Cylinder about its axis:** Mass distributed, so $I = MR^2/2$. (Less than ring, easier to spin).
    *   **Solid Sphere about diameter:** $I = 2/5 MR^2$ (mass concentrated near center, very easy to spin).
    *   **Rod through center:** $I = ML^2/12$ (mass far from axis).
10. **Equations of Motion:** Just like you remember $v=u+at$, remember $\omega = \omega_0 + \alpha t$. The analogy makes it easy.

---

# CHAPTER REVISION SHEET

## I. Systems of Particles & CM
*   **Particle:** Ideal point mass. **Extended Body:** Finite size, system of particles.
*   **Rigid Body:** Distances between particles fixed.
*   **Motion Types:**
    *   **Pure Translation:** All particles same $\vec{v}$.
    *   **Pure Rotation (fixed axis):** Particles in circles $\perp$ to axis, centers on axis. All have same $\vec{\omega}$.
    *   **Combined:** Translation + Rotation (e.g., rolling).
*   **Centre of Mass (CM):** Average position of mass.
    *   Discrete: $\vec{R}_{CM} = \frac{\sum m_i \vec{r}_i}{\sum m_i}$
    *   Continuous: $\vec{R}_{CM} = \frac{1}{M_{total}} \int \vec{r} \ dm$
    *   Homogeneous, symmetric bodies: CM at geometric center.
    *   **Motion of CM:** $\vec{V}_{CM} = \frac{\sum m_i \vec{v}_i}{M_{total}}$, $\vec{A}_{CM} = \frac{\sum m_i \vec{a}_i}{M_{total}}$
    *   **Newton's 2nd Law for System:** $\vec{F}_{ext} = M_{total} \vec{A}_{CM}$ (Internal forces cancel for CM motion).

## II. Linear Momentum of a System
*   **Total Linear Momentum:** $\vec{P} = \sum \vec{p}_i = M_{total} \vec{V}_{CM}$
*   **Relation to External Force:** $\vec{F}_{ext} = \frac{d\vec{P}}{dt}$
*   **Conservation of Linear Momentum:** If $\vec{F}_{ext} = 0 \implies \vec{P} = \text{constant}$ (and $\vec{V}_{CM} = \text{constant}$).

## III. Vector Product (Cross Product)
*   $\vec{c} = \vec{a} \times \vec{b}$
*   Magnitude: $|\vec{c}| = |\vec{a}| |\vec{b}| \sin\theta$
*   Direction: Right-Hand Rule. $\vec{c} \perp$ plane of $\vec{a}, \vec{b}$.
*   Properties: Non-commutative ($\vec{a} \times \vec{b} = - \vec{b} \times \vec{a}$), Distributive.
*   Components: $\hat{i} \times \hat{j} = \hat{k}$, etc.

## IV. Angular Velocity & Acceleration
*   **Angular Velocity:** $\vec{\omega} = \frac{d\vec{\theta}}{dt}$ (Vector along axis, Right-Hand Rule for direction). Units: rad/s.
*   **Linear-Angular Relation:** $\vec{v} = \vec{\omega} \times \vec{r}$. Magnitude $v = \omega r_\perp$.
*   **Angular Acceleration:** $\vec{\alpha} = \frac{d\vec{\omega}}{dt}$. Units: rad/s².

## V. Torque (Moment of Force)
*   **Definition:** $\vec{\tau} = \vec{r} \times \vec{F}$ (Rotational analogue of force). Units: N m.
*   Magnitude: $\tau = r F \sin\theta = F r_\perp = r F_\perp$.
*   Direction: Right-Hand Rule for $\vec{r} \times \vec{F}$.

## VI. Angular Momentum
*   **Particle:** $\vec{l} = \vec{r} \times \vec{p}$. Units: kg m²/s.
*   **System:** $\vec{L} = \sum \vec{l}_i$.
*   **Relation to Torque:** $\vec{\tau}_{ext} = \frac{d\vec{L}}{dt}$ (Internal torques cancel).
*   **Conservation of Angular Momentum:** If $\vec{\tau}_{ext} = 0 \implies \vec{L} = \text{constant}$.
*   **For Fixed Axis (symmetric bodies):** $L_z = I\omega$. If $\tau_{ext,z}=0 \implies I\omega = \text{constant}$.

## VII. Equilibrium of a Rigid Body
*   **Mechanical Equilibrium:** No linear or angular acceleration.
    1.  **Translational:** $\sum \vec{F}_{ext} = 0$.
    2.  **Rotational:** $\sum \vec{\tau}_{ext} = 0$ (about ANY point if translational equilibrium satisfied).
*   **Couple:** Two equal & opposite forces with different lines of action. Produces pure rotation ($\sum \vec{F}=0, \sum \vec{\tau} \ne 0$). Torque of couple is independent of origin.
*   **Principle of Moments:** For levers in equilibrium, Sum of CW moments = Sum of ACW moments. $F_1 d_1 = F_2 d_2$.
*   **Centre of Gravity (CG):** Point where total gravitational torque is zero. Coincides with CM in uniform 'g'.

## VIII. Moment of Inertia (I)
*   **Definition:** Rotational analogue of mass. Resistance to angular acceleration.
    *   Discrete: $I = \sum m_i r_i^2$.
    *   Continuous: $I = \int r^2 dm$.
*   **Depends on:** Mass, mass distribution, and axis of rotation.
*   **Units:** kg m².
*   **Rotational Kinetic Energy:** $K_{rot} = \frac{1}{2} I \omega^2$.
*   **Radius of Gyration ($k$):** $I = M_{total} k^2 \implies k = \sqrt{I/M_{total}}$.
*   **Standard I values (memorize Table 6.1).**

## IX. Rotational Kinematics (Fixed Axis, Constant $\alpha$)
*   $\omega = \omega_0 + \alpha t$
*   $\theta = \theta_0 + \omega_0 t + \frac{1}{2} \alpha t^2$
*   $\omega^2 = \omega_0^2 + 2 \alpha (\theta - \theta_0)$

## X. Rotational Dynamics (Fixed Axis)
*   **Newton's 2nd Law (Rotational):** $\tau_{ext} = I \alpha$.
*   **Work Done:** $dW = \tau d\theta$. For constant $\tau$, $W = \tau \Delta\theta$.
*   **Power:** $P = \tau \omega$.

---

# 1-DAY REVISION VERSION

*   **CM:** Balance point, $\vec{R}_{CM} = \frac{\sum m_i \vec{r}_i}{M_{total}}$. $\vec{F}_{ext} = M\vec{A}_{CM}$. Internal forces don't affect CM.
*   **Conservation of Linear Momentum:** If $\vec{F}_{ext}=0 \implies \vec{P} = M\vec{V}_{CM} = \text{constant}$.
*   **Vector Product:** $\vec{A} \times \vec{B}$, magnitude $AB\sin\theta$, direction by Right-Hand Rule.
*   **Rotational Analogies:**
    | Linear | Rotational |
    | ------ | ---------- |
    | $m$    | $I$        |
    | $\vec{F}$ | $\vec{\tau} = \vec{r} \times \vec{F}$ |
    | $\vec{v}$ | $\vec{\omega}$ ($\vec{v} = \vec{\omega} \times \vec{r}$) |
    | $\vec{a}$ | $\vec{\alpha}$ |
    | $\vec{p} = m\vec{v}$ | $\vec{L} = \vec{r} \times \vec{p}$ |
    | $F=ma$ | $\tau=I\alpha$ |
    | $K = \frac{1}{2}mv^2$ | $K = \frac{1}{2}I\omega^2$ |
    | $W=F\cdot x$ | $W=\tau\theta$ |
    | $P=Fv$ | $P=\tau\omega$ |
*   **Conservation of Angular Momentum:** If $\vec{\tau}_{ext}=0 \implies \vec{L} = \text{constant}$. For fixed axis: $I\omega = \text{constant}$. (Ice skater example).
*   **Moment of Inertia ($I$):** Depends on mass distribution and axis. Memorize standard values ($MR^2, MR^2/2, ML^2/12, 2/5 MR^2$).
*   **Equilibrium:** Both $\sum \vec{F}_{ext}=0$ AND $\sum \vec{\tau}_{ext}=0$. (Crucial for ladder/beam problems).
*   **Rotational Kinematics:** $\omega = \omega_0 + \alpha t$, etc. (Analogous to linear).

---

# TOP 25 NEET QUESTIONS

### Easy

1.  **Question:** Three particles of masses 1 kg, 2 kg, and 3 kg are located at (1,0,0), (0,2,0), and (0,0,3) meters respectively. Find the coordinates of the center of mass of the system.
    *   **Answer:** (1/2, 2/3, 3/2) m
    *   **Explanation:** $X_{CM} = (1\cdot1 + 2\cdot0 + 3\cdot0)/(1+2+3) = 1/6$. $Y_{CM} = (1\cdot0 + 2\cdot2 + 3\cdot0)/6 = 4/6 = 2/3$. $Z_{CM} = (1\cdot0 + 2\cdot0 + 3\cdot3)/6 = 9/6 = 3/2$.
2.  **Question:** A rigid body is performing pure translational motion. Which of the following statements is true for any two particles A and B in the body?
    *   a) $\vec{v}_A = \vec{v}_B$
    *   b) $\vec{a}_A = \vec{a}_B$
    *   c) Both a and b
    *   d) Neither a nor b
    *   **Answer:** c) Both a and b
    *   **Explanation:** In pure translational motion, all particles of the body have the same velocity and hence the same acceleration at any instant.
3.  **Question:** What is the magnitude of the torque produced by a force $\vec{F} = (2\hat{i} - 3\hat{j})\text{ N}$ acting at a position $\vec{r} = (4\hat{i} + 5\hat{j})\text{ m}$ from the origin?
    *   **Answer:** 22 N m
    *   **Explanation:** $\vec{\tau} = \vec{r} \times \vec{F} = (4\hat{i} + 5\hat{j}) \times (2\hat{i} - 3\hat{j}) = 8(\hat{i} \times \hat{i}) - 12(\hat{i} \times \hat{j}) + 10(\hat{j} \times \hat{i}) - 15(\hat{j} \times \hat{j})$. Since $\hat{i} \times \hat{i} = 0$, $\hat{j} \times \hat{j} = 0$, $\hat{i} \times \hat{j} = \hat{k}$, and $\hat{j} \times \hat{i} = -\hat{k}$, we get $\vec{\tau} = -12\hat{k} - 10\hat{k} = -22\hat{k}\text{ N m}$. Magnitude is 22 N m.
4.  **Question:** A wheel is rotating at 120 RPM. What is its angular speed in rad/s?
    *   **Answer:** $4\pi$ rad/s
    *   **Explanation:** 1 RPM = $2\pi/60$ rad/s. So, 120 RPM = $120 \times (2\pi/60) = 4\pi$ rad/s.
5.  **Question:** If the net external force acting on a system of particles is zero, then the total linear momentum of the system is:
    *   a) Zero
    *   b) Constant
    *   c) Increasing
    *   d) Decreasing
    *   **Answer:** b) Constant
    *   **Explanation:** This is the statement of the law of conservation of linear momentum. If $\vec{F}_{ext} = d\vec{P}/dt = 0$, then $\vec{P}$ must be constant.
6.  **Question:** Which of the following quantities is the rotational analogue of mass?
    *   a) Torque
    *   b) Angular momentum
    *   c) Moment of inertia
    *   d) Angular velocity
    *   **Answer:** c) Moment of inertia
    *   **Explanation:** Moment of inertia represents resistance to rotational motion, similar to how mass represents resistance to linear motion.
7.  **Question:** A ceiling fan is rotating at a constant angular velocity. What is its angular acceleration?
    *   **Answer:** Zero
    *   **Explanation:** Angular acceleration is the rate of change of angular velocity. If angular velocity is constant, its rate of change is zero.
8.  **Question:** If a force is applied directly through the pivot point of a rigid body, what will be the torque produced by this force?
    *   **Answer:** Zero
    *   **Explanation:** Torque $\vec{\tau} = \vec{r} \times \vec{F}$. If the force acts at the pivot, $\vec{r}=0$, so $\vec{\tau}=0$.
9.  **Question:** The unit of angular momentum is:
    *   a) J s
    *   b) J/s
    *   c) N m
    *   d) N s
    *   **Answer:** a) J s
    *   **Explanation:** Angular momentum $L = I\omega$. Units: $(\text{kg m}^2) (\text{rad/s}) = \text{kg m}^2/\text{s}$. Also, $L = \vec{r} \times \vec{p}$, units: m * (kg m/s) = kg m²/s. Joule (J) = N m = kg m²/s². So J s = (kg m²/s²) s = kg m²/s.
10. **Question:** A solid cylinder of mass M and radius R rotates about its own axis. Its moment of inertia is:
    *   a) $MR^2$
    *   b) $MR^2/2$
    *   c) $2/5 MR^2$
    *   d) $ML^2/12$
    *   **Answer:** b) $MR^2/2$
    *   **Explanation:** This is a standard formula for the moment of inertia of a solid cylinder about its own axis.

### Medium

1.  **Question:** A uniform thin rod of mass M and length L is pivoted at one end. What is its moment of inertia about this pivot?
    *   **Answer:** $ML^2/3$
    *   **Explanation:** (Requires Parallel Axis Theorem, which is usually covered in this chapter, though not in the specific extract. Assuming this knowledge is okay). The moment of inertia about the CM is $ML^2/12$. By parallel axis theorem $I = I_{CM} + Md^2 = ML^2/12 + M(L/2)^2 = ML^2/12 + ML^2/4 = ML^2/3$.
2.  **Question:** A body is in translational equilibrium but not in rotational equilibrium. Which of the following is true?
    *   a) Net force is zero, net torque is zero.
    *   b) Net force is non-zero, net torque is zero.
    *   c) Net force is zero, net torque is non-zero.
    *   d) Net force is non-zero, net torque is non-zero.
    *   **Answer:** c) Net force is zero, net torque is non-zero.
    *   **Explanation:** Translational equilibrium means $\sum \vec{F}_{ext} = 0$. Not in rotational equilibrium means $\sum \vec{\tau}_{ext} \ne 0$. This condition is typically met by a couple.
3.  **Question:** A rotating object has an angular velocity of $5\hat{i} - 2\hat{j}\text{ rad/s}$. If a point on the object has a position vector $\vec{r} = 3\hat{j} + 4\hat{k}\text{ m}$ from the origin on the axis of rotation, what is its linear velocity?
    *   **Answer:** $-8\hat{i} - 20\hat{j} + 15\hat{k}\text{ m/s}$
    *   **Explanation:** $\vec{v} = \vec{\omega} \times \vec{r} = (5\hat{i} - 2\hat{j}) \times (3\hat{j} + 4\hat{k})$.
        $= (5\hat{i} \times 3\hat{j}) + (5\hat{i} \times 4\hat{k}) + (-2\hat{j} \times 3\hat{j}) + (-2\hat{j} \times 4\hat{k})$
        $= 15\hat{k} - 20\hat{j} + 0 - 8\hat{i} = -8\hat{i} - 20\hat{j} + 15\hat{k}\text{ m/s}$.
4.  **Question:** A child stands at the center of a turntable with arms outstretched, rotating at 20 RPM. If he folds his arms, reducing his moment of inertia to half its initial value, what will be his new angular speed? (Assume no external torque).
    *   **Answer:** 40 RPM
    *   **Explanation:** By conservation of angular momentum, $I_1\omega_1 = I_2\omega_2$. Given $I_2 = I_1/2$, so $I_1\omega_1 = (I_1/2)\omega_2 \implies \omega_2 = 2\omega_1$. New angular speed = $2 \times 20 \text{ RPM} = 40 \text{ RPM}$.
5.  **Question:** A wheel starting from rest attains an angular velocity of 100 rad/s in 10 seconds. Assuming uniform angular acceleration, what is the total angular displacement in this time?
    *   **Answer:** 500 radians
    *   **Explanation:** $\omega_0 = 0$, $\omega = 100 \text{ rad/s}$, $t = 10 \text{ s}$.
        First find $\alpha$: $\omega = \omega_0 + \alpha t \implies 100 = 0 + \alpha(10) \implies \alpha = 10 \text{ rad/s}^2$.
        Then find $\theta$: $\theta = \omega_0 t + \frac{1}{2}\alpha t^2 = 0 + \frac{1}{2}(10)(10^2) = \frac{1}{2}(10)(100) = 500 \text{ radians}$.
6.  **Question:** A force $\vec{F}$ is applied at a point whose position vector from the origin is $\vec{r}$. If $\vec{F}$ is parallel to $\vec{r}$, then the magnitude of the torque produced is:
    *   a) $rF$
    *   b) $rF\sin\theta$
    *   c) $0$
    *   d) $rF\cos\theta$
    *   **Answer:** c) 0
    *   **Explanation:** If $\vec{F}$ is parallel to $\vec{r}$, the angle $\theta$ between them is $0^\circ$ (or $180^\circ$). Since $\tau = rF\sin\theta$, and $\sin0^\circ = 0$, the torque is zero.
7.  **Question:** Two particles of masses m and 2m are placed at a separation 'd'. Find the distance of their center of mass from the mass 'm'.
    *   **Answer:** $2d/3$
    *   **Explanation:** Let mass 'm' be at origin (0,0) and mass '2m' be at (d,0).
        $X_{CM} = (m \cdot 0 + 2m \cdot d) / (m + 2m) = 2md / 3m = 2d/3$.
        The distance from mass 'm' is $2d/3$.
8.  **Question:** A uniform solid sphere (mass M, radius R) is rotating about its diameter with angular speed $\omega$. Its rotational kinetic energy is:
    *   a) $MR^2\omega^2/2$
    *   b) $2MR^2\omega^2/5$
    *   c) $MR^2\omega^2/5$
    *   d) $MR^2\omega^2/4$
    *   **Answer:** c) $MR^2\omega^2/5$
    *   **Explanation:** The moment of inertia of a solid sphere about its diameter is $I = 2/5 MR^2$.
        Rotational Kinetic Energy $K = \frac{1}{2} I \omega^2 = \frac{1}{2} (2/5 MR^2) \omega^2 = MR^2\omega^2/5$.
9.  **Question:** A system consists of two equal masses connected by a light rod of length 'L'. If the system rotates about an axis perpendicular to the rod passing through its center, its moment of inertia is:
    *   a) $ML^2/2$
    *   b) $ML^2/4$
    *   c) $ML^2$
    *   d) $2ML^2$
    *   **Answer:** a) $ML^2/2$
    *   **Explanation:** Each mass 'M' is at a distance L/2 from the center. $I = M(L/2)^2 + M(L/2)^2 = ML^2/4 + ML^2/4 = ML^2/2$.
10. **Question:** What is the power delivered by a motor producing a constant torque of 20 N m at an angular speed of 10 rad/s?
    *   **Answer:** 200 W
    *   **Explanation:** Power $P = \tau \omega = (20 \text{ N m}) \times (10 \text{ rad/s}) = 200 \text{ W}$.

### Hard

1.  **Question:** A uniform square plate of side 'a' has a circular hole of radius R = a/4 cut out from its center. Find the x-coordinate of the center of mass of the remaining plate, if the origin is at the original center of the square.
    *   **Answer:** (0,0) (or CM is still at the origin)
    *   **Explanation:** Both the original square plate and the circular hole are symmetric about the center. When a symmetric part is removed concentrically from a symmetric body, the center of mass remains at the center of symmetry. So, the CM is still at (0,0).
2.  **Question:** A uniform rod of mass 'M' and length 'L' is held horizontally. It is suddenly released. What is the initial angular acceleration of the rod if it pivots about one end?
    *   **Answer:** $3g/(2L)$
    *   **Explanation:** Torque $\tau = I\alpha$. The weight Mg acts at L/2 from the pivot. So, $\tau = Mg(L/2)$. The moment of inertia of a rod about one end is $ML^2/3$.
        $Mg(L/2) = (ML^2/3)\alpha \implies \alpha = \frac{MgL/2}{ML^2/3} = \frac{3g}{2L}$.
3.  **Question:** A particle of mass $m$ is moving with constant velocity $\vec{v} = v_0\hat{i}$ along the line $y=d$. Find its angular momentum about the origin.
    *   **Answer:** $-m v_0 d \hat{k}$
    *   **Explanation:** The position vector of the particle can be written as $\vec{r} = x\hat{i} + d\hat{j}$. Its linear momentum is $\vec{p} = m\vec{v} = m v_0\hat{i}$.
        Angular momentum $\vec{l} = \vec{r} \times \vec{p} = (x\hat{i} + d\hat{j}) \times (m v_0\hat{i})$
        $= (x\hat{i} \times m v_0\hat{i}) + (d\hat{j} \times m v_0\hat{i})$
        $= 0 + d m v_0 (\hat{j} \times \hat{i}) = d m v_0 (-\hat{k}) = -m v_0 d \hat{k}$.
        The magnitude is $m v_0 d$, and it's constant, confirming conservation as no external torque acts.
4.  **Question:** A uniform ladder of length 5 m and mass 20 kg rests against a smooth vertical wall, with its lower end on a rough horizontal floor 3 m from the wall. Find the minimum coefficient of static friction required between the floor and the ladder for the ladder to not slip. (g = 10 m/s²)
    *   **Answer:** 0.375
    *   **Explanation:**
        Let the wall be y-axis, floor be x-axis. Ladder from (3,0) to (0,4) (using Pythagoras $\sqrt{5^2-3^2}=4$).
        Forces: Weight $W = 20g = 200\text{ N}$ at CM (1.5, 2) (midpoint).
        Normal force from floor $N_f$ at (3,0) (upwards).
        Friction force $f_s$ at (3,0) (towards wall, +x direction).
        Normal force from wall $N_w$ at (0,4) (away from wall, +x direction).
        **Translational Equilibrium:**
        $\sum F_x = 0 \implies N_w - f_s = 0 \implies N_w = f_s$ (1)
        $\sum F_y = 0 \implies N_f - W = 0 \implies N_f = W = 200\text{ N}$ (2)
        **Rotational Equilibrium:** Take moments about point of contact with floor (3,0) to eliminate $N_f$ and $f_s$.
        Torque due to $W$: $W \times (1.5 \text{ m})$ (clockwise, if we consider $(3,0)$ as origin)
        Torque due to $N_w$: $N_w \times (4 \text{ m})$ (anticlockwise)
        $\sum \tau = 0 \implies N_w (4) - W (1.5) = 0$
        $N_w (4) = 200 (1.5) = 300$
        $N_w = 300/4 = 75\text{ N}$
        From (1), $f_s = N_w = 75\text{ N}$.
        For no slipping, $f_s \le \mu_s N_f$.
        $75 \le \mu_s (200)$
        $\mu_s \ge 75/200 = 3/8 = 0.375$.
        Minimum $\mu_s = 0.375$.
5.  **Question:** A uniform solid cylinder of mass M and radius R rolls without slipping on a horizontal surface with a linear velocity V of its center. What is its total kinetic energy?
    *   **Answer:** $3/4 MV^2$
    *   **Explanation:** Total kinetic energy is the sum of translational and rotational kinetic energy.
        $K_{total} = K_{translational} + K_{rotational} = \frac{1}{2} MV^2 + \frac{1}{2} I\omega^2$.
        For a solid cylinder, $I = \frac{1}{2} MR^2$.
        For rolling without slipping, $V = R\omega \implies \omega = V/R$.
        $K_{total} = \frac{1}{2} MV^2 + \frac{1}{2} (\frac{1}{2} MR^2) (V/R)^2$
        $= \frac{1}{2} MV^2 + \frac{1}{4} MR^2 (V^2/R^2)$
        $= \frac{1}{2} MV^2 + \frac{1}{4} MV^2 = \frac{3}{4} MV^2$.

---

# PYQ PREDICTION AREAS

1.  **Conservation of Angular Momentum:** This is consistently a high-yield area. Look for problems involving:
    *   Changing moment of inertia (ice skater, diver, a person moving on a rotating platform).
    *   Collision problems where rotational motion is involved.
    *   Systems with changing radius (e.g., a planet's speed changes as it moves in elliptical orbit).
2.  **Equilibrium Problems:** Static equilibrium questions involving a ladder, a uniform beam, or a system of forces are very common. They test the application of both $\sum \vec{F}_{ext}=0$ and $\sum \vec{\tau}_{ext}=0$.
3.  **Centre of Mass Calculations:**
    *   Finding CM for discrete systems (2-3 particles).
    *   Finding CM for systems with a "cut-out" part (e.g., a disc with a hole). These often require understanding how to treat negative mass.
4.  **Newton's Second Law for Rotation ($\tau = I\alpha$):** Numerical questions directly applying this formula, often combined with rotational kinematics.
    *   Calculating angular acceleration for a given torque and moment of inertia.
    *   Calculating torque required for a specific angular acceleration.
5.  **Moment of Inertia:**
    *   Conceptual questions on factors affecting Moment of Inertia.
    *   Direct application of standard formulas for Moment of Inertia for common shapes (rod, ring, disc, sphere, cylinder).
6.  **Vector Product Application:** Finding torque or angular momentum from given position and force/momentum vectors. This checks basic vector calculation skills and right-hand rule.
7.  **Work and Power in Rotational Motion:** Simple direct formula applications ($\tau \theta$, $\tau \omega$).

---

# FINAL TAKEAWAYS

1.  **CM simplifies translational motion:** The entire mass of a system behaves as if concentrated at the CM, and all external forces act there. Internal forces don't affect CM motion.
2.  **Torque causes rotation:** Just as force causes linear acceleration, torque causes angular acceleration ($\tau = I\alpha$).
3.  **Angular Momentum is rotational momentum:** It's conserved when net external torque is zero ($\vec{L} = \text{constant}$). This explains how spinning objects speed up or slow down when their shape changes (like an ice skater).
4.  **Moment of Inertia is rotational mass:** It quantifies an object's resistance to angular acceleration and depends on both mass and its distribution relative to the axis of rotation.
5.  **Rotational and Linear Motion are analogous:** Many linear concepts (force, mass, velocity, acceleration, momentum, KE) have direct rotational counterparts (torque, moment of inertia, angular velocity, angular acceleration, angular momentum, rotational KE).
6.  **Equilibrium means no change:** A body is in mechanical equilibrium only if both net external force AND net external torque are zero.
7.  **Vector products define rotational quantities:** Torque ($\vec{r} \times \vec{F}$) and angular momentum ($\vec{r} \times \vec{p}$) are vector cross products, so their directions are crucial (use the Right-Hand Rule).
8.  **Internal forces/torques cancel:** For a system, internal forces do not affect $\vec{V}_{CM}$ or $\vec{A}_{CM}$, and internal torques do not affect the total $\vec{L}$ (assuming central forces).
9.  **Units matter:** Always convert RPM to rad/s and use radians for angular displacement in equations.
10. **Moment of Inertia is axis-dependent:** It's not a fixed property like mass; it changes with the choice of rotation axis.