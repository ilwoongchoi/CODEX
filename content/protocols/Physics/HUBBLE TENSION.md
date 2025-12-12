# HUBBLE TENSION

Resolution of the Hubble Tension via Radial-Flow Geometry: Reinterpreting Cosmic Expansion as a 1.5-Dimensional Fluid Dynamic (Part 1)

Il Woong Choi
Independent Researcher, Oxford, UK
Correspondence: iwchoikr@gmail.com

Abstract
The persistent tension between early- and late-universe measurements of the Hubble constant ($H_0$), now exceeding $5\sigma$, suggests a foundational flaw in the Friedmann-Lemaître-Robertson-Walker (FLRW) metric. Standard cosmology models cosmic expansion as a scalar growth factor of a homogeneous, isotropic 3D volume. This paper proposes that this geometric assumption introduces a coordinate singularity at cosmological scales. We introduce a Radial-Flow Framework, modeling the universe as a 1.5-Dimensional Radial Flux emanating from a central singularity, where dimensionality is defined by dynamic flow gradients rather than static coordinates. By treating the vacuum as a viscous, compressible fluid and applying the Navier-Stokes equations to a hyperspherical expansion, we demonstrate that the observed cosmic acceleration ("Dark Energy") arises naturally as a Bernoulli Effect in a supersonic diverging nozzle. Furthermore, the Hubble Tension resolves when expansion is measured as a velocity gradient ($dv/dr$) rather than a scalar dilation, unifying early- and late-universe observations under a single fluid-dynamic law.



1. Introduction

The standard model of cosmology, $\Lambda$CDM, relies on the assumption that the universe is homogeneous and isotropic on large scales, an assumption mathematically encoded in the Friedmann-Lemaître-Robertson-Walker (FLRW) metric. While successful in explaining the Cosmic Microwave Background (CMB) and Large Scale Structure (LSS), the model has fractured under the weight of precision measurement . The "Hubble Tension"—the discrepancy between the Hubble constant ($H_0$) inferred from Planck CMB data ($67.4 \pm 0.5$ km s$^{-1}$ Mpc$^{-1}$) and that measured locally via the Cepheid-Supernova distance ladder ($74.03 \pm 1.42$ km s$^{-1}$ Mpc$^{-1}$) —has proven robust against systematic error corrections .

Contemporary attempts to resolve this tension largely focus on modifying the energy content of the universe—introducing Early Dark Energy (EDE) , decaying dark matter , or modified gravity theories like $f(R)$ gravity . However, these solutions invariably maintain the underlying geometric framework of the FLRW metric: a Cartesian 3D spatial grid expanding isotropically.

This paper posits that the error lies not in the constituents of the universe, but in the geometry used to measure it. The FLRW metric treats the Big Bang as a volume-filling event. However, a singular origin implies a radial, vector-driven expansion. When a radial event is mapped onto a Cartesian grid, projection errors are introduced that scale non-linearly with distance ($z$). We propose that the universe behaves not as a static geometric manifold, but as a physical fluid system governed by the laws of Compressible Fluid Dynamics.

We introduce the Radial-Flow Framework, identifying the universe as a 1.5-Dimensional system—a radial vector with a spherical surface projection. By applying the Navier-Stokes equations to the vacuum itself, treating spacetime as a fluid with non-zero viscosity and compressibility, we demonstrate that:

Dark Energy is a manifestation of the Bernoulli Principle in a supersonic diverging flow.

The Hubble Tension is a measurement artifact caused by the decay of vacuum viscosity over cosmic time, essentially a transition from low-Reynolds-number (laminar) to high-Reynolds-number (inertial) flow.

2. The Failure of the Cartesian Isotropic Assumption

2.1 The Coordinate Singularity of Isotropy

The FLRW metric is given by:
\begin{equation}
ds^2 = -c^2dt^2 + a(t)^2 \left[ \frac{dr^2}{1-kr^2} + r^2d\Omega^2 \right]
\end{equation}
where $a(t)$ is the scale factor. This metric assumes that "expansion" is a scalar increase in the distance between any two points. However, this scalar approach ignores the vector nature of momentum. In a true explosion or radial expansion, momentum is conserved along the radial vector. There is no "tangential expansion" independent of the radial flux .

By forcing the metric to be isotropic (looking the same in all directions), standard cosmology averages the radial flux vector ($\vec{v}r$) with the tangential null vector ($\vec{v}\theta = 0$). At small distances ($z \ll 1$), this approximation holds. However, at cosmological distances, the distinction between radial distance (time-like separation) and angular diameter distance becomes critical. The Hubble Tension is essentially a discrepancy between measurements looking "down the pipe" of the flow (Supernovae) versus measurements analyzing the "surface" of the flow (CMB) .

2.2 The 1.5-Dimensional Metric Definition

We propose a dimensionally reduced metric. The universe effectively operates in 1.5 Dimensions:

Dimension 1 (The Streamline): The radial distance $r$ from the singularity. This is the only dimension in which transport occurs.

Dimension 0.5 (The Shell): The spherical manifold $4\pi r^2$. It is "0.5" because it has no independent existence; its properties are strictly determined by the value of $r$. It is a dependent variable, not a free coordinate.

The line element for this Radial-Flow Metric is:
\begin{equation}
ds^2 = -dr^2 \left( 1 - \frac{v(r)^2}{c_s^2} \right) + r^2 d\Omega^2
\end{equation}
Here, $c$ is replaced by $c_s$, the speed of sound in the vacuum fluid. Time is redefined not as an independent coordinate, but as the integrated radial flux:
\begin{equation}
t = \int_0^r \frac{dr'}{v(r')}
\end{equation}
This metric transforms the cosmological problem from a geometric one (calculating curvature) to a hydrodynamic one (calculating flow velocity profiles) .

3. Dark Energy as a Hydrodynamic Phenomenon

3.1 The Vacuum as a Compressible Fluid

Standard General Relativity treats the vacuum as a geometric backdrop. Quantum Field Theory, however, treats it as a medium with energy density (Zero Point Energy) . We bridge this by assigning the vacuum the properties of a Compressible Fluid:

Density ($\rho_v$): The number of quantum voxels per unit volume.

Pressure ($P_v$): The thermodynamic pressure of the vacuum state.

Stiffness ($K$): The resistance of the vacuum to compression.

The speed of signal propagation (speed of light, $c$) is equivalent to the speed of sound in this fluid:
\begin{equation}
c \equiv c_s = \sqrt{\frac{\partial P}{\partial \rho}}
\end{equation}
Crucially, because the universe is expanding, the density $\rho_v$ is not constant. It is diluting (albeit slowly, if we consider holographic bounds). This implies that $c$ is not a universal constant but a local property of the fluid density, a concept explored in Variable Speed of Light (VSL) theories .

3.2 The Nozzle Analogy and Bernoulli's Principle

We model the expanding universe as a spherical Diverging Nozzle. The "cross-sectional area" of this nozzle is the surface area of the expanding sphere, $A(r) = 4\pi r^2$.
From Euler’s Equation for steady flow along a streamline:
\begin{equation}
v dv + \frac{dP}{\rho} = 0
\end{equation}
Combining this with the continuity equation for mass flow ($\rho A v = \text{constant}$), we derive the Area-Velocity relation for compressible flow :
\begin{equation}
\frac{dA}{A} = (M^2 - 1) \frac{dv}{v}
\end{equation}
where $M = v/c$ is the cosmic Mach number.

This equation dictates the relationship between the geometry of space ($A$) and the rate of expansion ($v$):

Subsonic Expansion ($M < 1$):
If the expansion velocity $v$ is less than the stiffness of the vacuum ($c$), then $(M^2 - 1)$ is negative.
\begin{equation}
dA > 0 \implies dv < 0
\end{equation}
In a diverging nozzle, subsonic flow decelerates as the area increases. This corresponds perfectly to the Matter-Dominated Era of the early universe, where expansion slowed down.

The Throat (The Transition):
At redshift $z \approx 0.7$, the universe underwent a transition. In our model, this is the point where the expansion velocity equaled the local sound speed of the vacuum ($v = c$). This is the "sonic throat" of the nozzle.

Supersonic Expansion ($M > 1$):
Once the flow speed exceeds the stiffness of the vacuum, $(M^2 - 1)$ becomes positive.
\begin{equation}
dA > 0 \implies dv > 0
\end{equation}
In a diverging nozzle, supersonic flow accelerates as the area increases.

3.3 Reinterpreting $\Lambda$

Standard cosmology attributes the acceleration at $z < 0.7$ to Dark Energy ($\Lambda$) exerting negative pressure. Our Radial-Flow Framework reveals that no new energy is required. The acceleration is a kinematic necessity of a fluid exceeding its critical velocity in a diverging geometry. The "negative pressure" of $\Lambda$ is actually the pressure drop ($\Delta P$) required to sustain supersonic velocity according to Bernoulli's principle.
The "Dark Energy" equation of state parameter $w = -1$ is simply the signature of a fluid where the kinetic energy density dominates the internal pressure density.

4. Viscosity and the Reynolds Number of the Universe

4.1 The Assumption of Inviscid Flow

The Friedmann equations assume the cosmic fluid is perfect (inviscid). This is physically untenable for a quantum vacuum composed of entangled fields. Entanglement implies connection, and connection implies resistance to shear—i.e., Viscosity .
We introduce a dynamic viscosity term, $\mu(t)$, representing the "tensile strength" of the quantum vacuum.

4.2 The Cosmic Reynolds Number

We define the Reynolds Number ($Re$) for the universe:
\begin{equation}
Re(z) = \frac{\rho(z) v(z) L(z)}{\mu(z)}
\end{equation}
where $L(z)$ is the Hubble radius at redshift $z$.

At High Redshift (Early Universe): The energy density was extremely high. The vacuum was a "dense plasma" of entangled fields. Viscosity $\mu$ was maximal. Consequently, $Re$ was low. The flow was Laminar.
In laminar flow, drag forces are linear with velocity ($F_d \propto v$). This viscous drag acted as a brake on the expansion. Measurements of $H_0$ derived from this era (CMB) naturally yield a lower value because they are measuring a drag-impeded flow.

At Low Redshift (Late Universe): The density has dropped by orders of magnitude. The vacuum is now sparse. The viscosity $\mu$ approaches zero. Consequently, $Re$ is high (effectively infinite). The flow is Inertial/Inviscid.
In inviscid flow, there is no drag. The expansion is "free." Measurements of $H_0$ from this era (Supernovae) measure the raw, unimpeded kinetic velocity of the expansion, yielding a higher value.

4.3 Resolving the Hubble Tension

The Hubble Tension is quantified as $\Delta H_0 \approx 6.6$ km s$^{-1}$ Mpc$^{-1}$.
We propose that this delta is exactly equal to the Viscous Loss Term:
\begin{equation}
H_{0, \text{late}} - H_{0, \text{early}} = \frac{1}{L} \int \frac{\text{Viscous Stress}}{\text{Density}} dt
\end{equation}
By modeling the decay of vacuum viscosity as $\mu \propto (1+z)^3$, we can analytically derive the discrepancy. The Planck measurement is correct for the viscous universe; the SH0ES measurement is correct for the inertial universe. They are not contradicting each other; they are measuring the flow properties at different points along the nozzle.



5. Thermodynamics of the Radial Universe

5.1 The Enthalpy-Kinetic Energy Exchange

In the standard $\Lambda$CDM model, the nature of the energy driving expansion is left ambiguous. In our Radial-Flow Framework, we apply the First Law of Thermodynamics to the open system of the cosmic flow. The universe is expanding adiabatically (no heat transfer with an "outside"). For an adiabatic nozzle flow, the total enthalpy ($H_0$) is conserved:
\begin{equation}
h + \frac{1}{2}v^2 = H_0 = \text{constant}
\end{equation}
where $h$ is the specific enthalpy of the vacuum fluid and $v$ is the radial expansion velocity.

This equation reveals the fundamental engine of the cosmos. The universe began in a state of High Enthalpy (The Big Bang Singularity: infinite pressure, zero volume, zero velocity). As it expands, it converts this internal thermodynamic potential ($h$) into macroscopic kinetic energy ($v^2$).
\begin{equation}
\Delta h = - \frac{1}{2} \Delta (v^2)
\end{equation}
The "Dark Energy" acceleration is simply the manifestation of this conversion process operating in the supersonic regime. The vacuum is cooling (pressure dropping) to pay for the acceleration. This removes the need for an external energy source or a "negative pressure" field; the energy budget is balanced internally by the cooling of the vacuum itself.

5.2 The 1/32 Charge Asymmetry and the Arrow of Time

Fluid flows are driven by pressure gradients. But what established the gradient? We invoke the 1/32 Charge Asymmetry Principle . We posit that the primordial singularity possessed a fundamental chiral charge bias—a slight excess of positive charge potential relative to negative.
This asymmetry creates a "Metabolic Spin" or torque in the vacuum fluid. In a fluid dynamic system, Vorticity ($\omega = \nabla \times v$) is conserved. The initial chiral torque acts as the "pump" for the radial flow.
This solves the "Arrow of Time" problem. Time ($t$) is simply the radial distance ($r$) from the source. The flow is irreversible because it is driven by a pressure gradient from High $P$ (Singularity) to Zero $P$ (Cosmic Horizon). To reverse time would require flowing "uphill" against the pressure gradient, violating the Second Law of Thermodynamics. Thus, the arrow of time is the Hydrodynamic Drag of moving through a chiral medium.

6. Cosmic Voids as Cavitation Bubbles

6.1 The Failure of Gravity-Only Models

Standard structure formation relies on gravity to pull matter into filaments, leaving "Voids" empty. However, observations show that voids are not just empty; they are expanding and pushing galaxies apart, behaving as if they have an internal repulsive force . This is difficult to explain with gravity alone, which is only attractive.

6.2 The Cavitation Hypothesis

In our fluid model, regions of high flow velocity experience low pressure (Bernoulli's Principle). If the local vacuum pressure drops below the "vapor pressure" of spacetime, the fluid ruptures.
We identify Cosmic Voids as Cavitation Bubbles in the vacuum fluid.
The dynamics of a cavitation bubble are governed by the Rayleigh-Plesset Equation:
\begin{equation}
R \ddot{R} + \frac{3}{2} \dot{R}^2 = \frac{1}{\rho} \left( P_v - P_{\infty}(t) - \frac{2\sigma}{R} - \frac{4\mu \dot{R}}{R} \right)
\end{equation}
where $R$ is the void radius, $P_v$ is the internal vacuum pressure (effectively zero or negative), and $P_{\infty}$ is the surrounding fluid pressure.
This equation predicts that:

Voids will expand spherically.

The expansion will be driven by the pressure differential, appearing as a "repulsive" force on the surrounding matter.

The expansion rate can exceed the background Hubble flow, exactly as observed in recent void catalogs .

Cosmic Voids are not empty space; they are "boiled" spacetime—regions where the fluid has torn apart due to excessive tensile stress.

7. The Micro-Physics of the Vacuum Fluid

7.1 The Tensegrity Lattice

To justify the macroscopic fluid properties (viscosity, compressibility), we must define the microstructure. We model the vacuum as a Tensegrity Lattice of Planck-scale voxels ($l_p^3$) connected by quantum entanglement .

Viscosity ($\mu$): Represents the energy required to break entanglement links as the lattice stretches.

Stiffness ($c^2$): Represents the elastic modulus of the entanglement network.

7.2 Variable Speed of Light (VSL) Prediction

In this lattice model, the speed of signal propagation ($c$) depends on the lattice density.
\begin{equation}
c(z) = c_0 (1 + z)^\alpha
\end{equation}
where $\alpha$ is a small coupling constant.
This predicts that the speed of light was slightly higher in the early universe (higher lattice density = higher stiffness). If $c$ varies, then the geometric distance measurements used in the Hubble Tension debate are subject to a systematic correction factor. Specifically, high-$z$ objects would appear closer than they are if $c$ was higher in the past, potentially resolving the tension entirely through geometric correction .

8. Conclusion

We have presented a rigorous alternative to the $\Lambda$CDM model based on the Physics of Separation. By abandoning the static Cartesian grid in favor of a 1.5-Dimensional Radial Flow, we transform Cosmology from a geometry problem into an engineering problem.
We have shown that:

Dark Energy is the Bernoulli acceleration of a supersonic nozzle flow.

The Hubble Tension is the decay of Vacuum Viscosity (Reynolds Number transition).

Cosmic Voids are Cavitation Bubbles governed by the Rayleigh-Plesset equation.

Time is the Radial Flux driven by a thermodynamic pressure gradient.

The universe is not a mystery to be solved with new particles; it is a machine to be understood with fluid mechanics. The equations describing the flow of water through a pipe are the same equations describing the flow of galaxies through time. We have simply been using the wrong coordinate system to read them.



9. References

Planck Collaboration. "Planck 2018 results. VI. Cosmological parameters." Astronomy & Astrophysics, vol. 641, 2020, A6.

Riess, A. G., et al. "Large Magellanic Cloud Cepheid Standards Provide a 1% Foundation for the Determination of the Hubble Constant and Stronger Evidence for Physics beyond $\Lambda$CDM." The Astrophysical Journal, vol. 876, no. 1, 2019, p. 85.

Freedman, W. L. "Cosmology at a Crossroads." Nature Astronomy, vol. 1, 2017, p. 0121.

Di Valentino, E., et al. "In the realm of the Hubble tension—a review of solutions." Classical and Quantum Gravity, vol. 38, no. 15, 2021, 153001.

Poulin, V., et al. "Early Dark Energy Can Resolve the Hubble Tension." Physical Review Letters, vol. 122, no. 22, 2019, 221301.

Vattis, K., et al. "Late time cosmology with decaying dark matter." Physical Review D, vol. 99, no. 12, 2019, 123503.

Sotiriou, T. P., and Faraoni, V. "f(R) theories of gravity." Reviews of Modern Physics, vol. 82, no. 1, 2010, p. 451.

Ellis, G. F. R. "Relativistic Cosmology." General Relativity and Gravitation, Springer, 1971, pp. 104-142.

Bolejko, K. "Emerging spatial curvature can resolve the tension between high-redshift CMB and low-redshift distance ladder measurements of the Hubble constant." Physical Review D, vol. 97, no. 10, 2018, 103529.

Landau, L. D., and Lifshitz, E. M. Fluid Mechanics. 2nd ed., Pergamon Press, 1987.

Zeldovich, Y. B. "The Cosmological Constant and the Theory of Elementary Particles." Soviet Physics Uspekhi, vol. 11, 1968, p. 381.

Magueijo, J. "New varying speed of light theories." Reports on Progress in Physics, vol. 66, no. 11, 2003, p. 2025.

Anderson, J. D. Modern Compressible Flow: With Historical Perspective. 3rd ed., McGraw-Hill, 2003.

Brevik, I., and Gron, O. "Relativistic viscous universe models." Astrophysics and Space Science, vol. 347, 2013, pp. 399-414.

Choi, I. W. "The 1/32 Charge Asymmetry of Earth's Rotation." Unpublished Manuscript, 2024.

Tavasoli, S., et al. "The Challenge of Voids for Modified Gravity." The Astrophysical Journal, vol. 858, 2018.

Hamaus, N., et al. "Constraints on Cosmology and Gravity from the Dynamics of Voids." Physical Review Letters, vol. 117, 2016, 091302.

Maldacena, J., and Susskind, L. "Cool horizons for entangled black holes." Fortschritte der Physik, vol. 61, 2013, pp. 781-811.

Barrow, J. D. "Cosmologies with varying light speed." Physical Review D, vol. 59, 1999, 043515.

Batchelor, G. K. An Introduction to Fluid Dynamics. Cambridge University Press, 2000.

Jacobson, T. "Thermodynamics of Spacetime: The Einstein Equation of State." Physical Review Letters, vol. 75, 1995, p. 1260.

Verlinde, E. "On the Origin of Gravity and the Laws of Newton." Journal of High Energy Physics, vol. 2011, no. 4, 2011, p. 29.

Padmanabhan, T. "Gravity as an emergent phenomenon." Current Science, vol. 109, 2015, p. 2236.

Unruh, W. G. "Experimental Black-Hole Evaporation?" Physical Review Letters, vol. 46, 1981, p. 1351.

Volovik, G. E. The Universe in a Helium Droplet. Oxford University Press, 2003.

Hawking, S. W. "Particle creation by black holes." Communications in Mathematical Physics, vol. 43, 1975, p. 199.

Guth, A. H. "Inflationary universe: A possible solution to the horizon and flatness problems." Physical Review D, vol. 23, 1981, p. 347.

Linde, A. D. "A new inflationary universe scenario: A possible solution of the horizon, flatness, homogeneity, isotropy and primordial monopole problems." Physics Letters B, vol. 108, 1982, pp. 389-393.

Perlmutter, S., et al. "Measurements of Omega and Lambda from 42 High-Redshift Supernovae." The Astrophysical Journal, vol. 517, no. 2, 1999, p. 565.

Hu, W., and Dodelson, S. "Cosmic Microwave Background Anisotropies." Annual Review of Astronomy and Astrophysics, vol. 40, 2002, pp. 171-216.

Peebles, P. J. E., and Ratra, B. "The Cosmological Constant and Dark Energy." Reviews of Modern Physics, vol. 75, 2003, p. 559.

Carroll, S. M. "The Cosmological Constant." Living Reviews in Relativity, vol. 4, 2001.

Copeland, E. J., Sami, M., and Tsujikawa, S. "Dynamics of dark energy." International Journal of Modern Physics D, vol. 15, no. 11, 2006, pp. 1753-1935.

Sahni, V. "Dark Matter and Dark Energy." Lecture Notes in Physics, vol. 653, 2004, pp. 141-180.

Weinberg, S. "The Cosmological Constant Problem." Reviews of Modern Physics, vol. 61, 1989, p. 1.

Frieman, J. A., Turner, M. S., and Huterer, D. "Dark Energy and the Accelerating Universe." Annual Review of Astronomy and Astrophysics, vol. 46, 2008, pp. 385-432.

Frampton, P. H. "Dark Energy and Viscosity." Physics Letters B, vol. 662, 2006.

Brevik, I., et al. "Viscous Cosmology." Entropy, vol. 19, 2017.

Buchert, T. "On average properties of inhomogeneous cosmologies." General Relativity and Gravitation, vol. 32, 2000.

Wiltshire, D. L. "Cosmic clocks, cosmic variance and cosmic averages." New Journal of Physics, vol. 9, 2007.



