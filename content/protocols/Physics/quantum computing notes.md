# quantum computing notes

The framework starts from the conventional picture in which decoherence in superconducting qubits is dominated by ensembles of microscopic two-level systems (TLS) located in amorphous dielectrics and at metal–oxide–substrate interfaces, each possessing an electric dipole moment that couples to the qubit’s electric field. Surface-participation studies have shown that dielectric loss is controlled not only by the TLS density, but critically by how the qubit’s electric field is distributed across interfaces and thin dielectric layers; high-field regions at capacitor edges and junction-proximal oxides contribute disproportionately to loss.​

Within this framework, the central conceptual step is to treat the near-surface electrostatic potential and static electric-field profile as a deliberate design parameter, on the same level as geometry and materials. Instead of focusing solely on reducing TLS density or geometric participation, the proposal is to engineer static local fields in high-participation regions such that: (i) the energy splittings of strongly coupled TLS are Stark-shifted away from the qubit transition, (ii) slow charge-like fluctuators are trapped in deep potential wells and become quasi-static offsets rather than active noise sources, and (iii) remaining field energy is preferentially concentrated in regions or modes that have low coupling to TLS dipoles.​​

Operationally, this is implemented through an intentionally introduced ionic-dielectric layer integrated into the device stack at locations where finite-element simulations show large electric-field participation, for example at transmon capacitor edges. The ionic-dielectric film is chosen and patterned to provide predominantly static electric fields at millikelvin temperatures, thereby modifying TLS energies via the standard Stark effect for electric dipoles and reshaping the effective TLS spectral density seen by the qubit. The resulting Hamiltonian remains the standard qubit + TLS model, augmented by a position-dependent static field term derived from the device-level electrostatics; relaxation and dephasing rates are then obtained in the usual weak-coupling, Markovian limit using Fermi’s Golden Rule and spectral-density arguments.​​

In summary, the concept can be stated rigorously as defect-landscape engineering by static electrostatics: introduce and shape ionic-dielectric layers so that the spatial profile of static electric fields in high-participation regions is optimized to detune, localize, and decouple TLS and charge fluctuators, thereby reducing dielectric loss and noise without relying solely on further reductions in defect density.​



Title: Engineering the Defect Landscape: Ionic-Dielectric Control of TLS Noise in Superconducting Qubits​



Introduction

Superconducting qubits have emerged as a leading platform for quantum information processing, but their performance is still limited by decoherence from microscopic defects in dielectrics and interfaces, commonly modeled as ensembles of two-level systems (TLS). These TLS absorb energy from the qubit’s electric field, generate dielectric loss, and induce temporal fluctuations in qubit parameters, thereby limiting energy relaxation times, dephasing, and the long-term stability required for large-scale processors. Systematic studies of surface participation ratios and material stacks have shown that, once quasiparticles and radiation are controlled, dielectric dissipation at interfaces becomes the dominant factor for  in many transmon architectures.​

Current mitigation strategies focus on reducing TLS density and participation by improving materials (e.g. cleaner oxides, thicker films, alternative substrates) and by reshaping device geometry to move electric-field energy into low-loss regions. In parallel, dynamic electric-field control has been used to Stark-tune individual TLS or small ensembles away from qubit resonance, as well as to dress qubits so they effectively “skip” resonant defect frequencies, leading to measurable improvements in coherence for specific devices. These approaches demonstrate that the TLS environment is not immutable: with appropriate fields and layouts, both the density of strongly coupled defects and their effective spectrum can be altered.​

This work develops a complementary, hardware-level strategy: a deliberately engineered ionic-dielectric layer placed in high-field regions of the qubit capacitor that statically reshapes the defect landscape. The idea is to use controlled, predominantly static electric fields from an ionic-dielectric film to (i) Stark-shift the energies of strongly coupled TLS away from the qubit transition, (ii) localize slow charge fluctuators into deep potential wells so they become quasi-static background offsets rather than active noise sources, and (iii) redirect residual field energy into modes and regions that contribute minimally to qubit loss. Rather than only trying to remove defects or avoid them geometrically, the qubit is surrounded by a designed electrostatic environment that weakens detrimental couplings at the microscopic level.​



Main contributions

Ionic-dielectric concept at device level.
The paper formalizes the idea of inserting an ionic-dielectric layer in high-participation regions of superconducting qubits to engineer static local fields that detune and immobilize TLS, complementing established geometry and materials approaches.​​

Minimal Hamiltonian plus finite-element framework.
A combined model is developed in which a transmon-like qubit couples to an ensemble of TLS with position-dependent dipole interactions, while an ionic-dielectric layer contributes a static field profile computed from finite-element simulations of the full device stack; from this, modified spectral densities, relaxation rates, and dephasing rates are derived in the weak-coupling, Markovian regime.​​

Design rules and trade-off analysis.
Using the combined analytic–numerical model, the paper extracts practical design rules for ionic-layer thickness, dielectric constant, charge density, and spatial placement that maximize TLS detuning and noise suppression while minimizing added dielectric participation and loss from the new material.​​

Experimental roadmap from single devices to small processors.
Finally, the paper outlines a staged experimental program—beginning with matched qubit pairs with and without ionic layers, progressing to TLS spectroscopy and long-term stability measurements, and culminating in small-scale multi-qubit demonstrations—to connect the proposed defect-engineering strategy to concrete improvements in coherence, frequency stability, and logical performance.​​

Faoro, L., and Ioffe, L. B. “Two-level systems in superconducting quantum devices due to trapped quasiparticles.” Sci. Adv. 6, eabc5055 (2020).​



Krantz, P. et al. “Material matters in superconducting qubits.” Appl. Phys. Lett. / arXiv:2106.05919 (2021).​



Krantz, P. et al. “Material matters in superconducting qubits.” arXiv:2106.05919. (Full preprint version, additional details on materials and interfaces.)​



Calusine, G. et al. “Mitigation of interfacial dielectric loss in aluminum‑on‑silicon superconducting qubits.” npj Quantum Inf. (2024).​



Wenner, J. et al. “Surface participation and dielectric loss in superconducting qubits.” Appl. Phys. Lett. 107, 162601 (2015).​



Wenner, J. et al. “Surface participation and dielectric loss in superconducting qubits.” (Related datasets and extended analysis.)​



Calusine, G. et al. “Surface loss calculations and design of a superconducting transmon qubit.” npj Quantum Inf. 8, 32 (2022).​



Wang, C. et al. “Investigating surface loss effects in superconducting transmon qubits.” (Van Duzer Prize paper.)​



O’Connell, A. D. et al. “Two-level system loss: Significant not only at millikelvin temperatures.” Appl. Phys. Lett. 125, 112601 (2024).​



Klimov, P. V. et al. “Dynamics of superconducting qubit relaxation times.” npj Quantum Inf. 8, 54 (2022).​



Burnett, J. et al. “Disentangling the impact of quasiparticles and two-level systems on superconducting resonator loss.” (Recent study on separate loss channels.)​



Calusine, G. et al. “Disentangling losses in tantalum superconducting circuits.” (Focus on different material‑dependent loss contributions.)​



Niepce, D. et al. “Scalable and site‑specific frequency tuning of two‑level system defects.” arXiv:2503.04702 (2025).​



Lisenfeld, J. et al. “Controlling individual TLS in superconducting quantum circuits.” arXiv:2203.07857 and related works on defect spectroscopy and control.​



Chen, Y. et al. “Escaping detrimental interactions with microwave‑dressed superconducting qubits.” Chin. Phys. Lett. 40, 070304 (2023).​



Quantum Zeitgeist summary. “Controlling Quantum Two‑Level Systems: A Leap Forward For Superconducting Qubit Performance.” (Popular overview of active TLS control experiments.)​



Mueller, C. et al. “Interacting defects generate stochastic fluctuations in superconducting qubits.” Phys. Rev. B 104, 094106 (2021).​



Nersisyan, A. et al. “Surface participation and dielectric loss in superconducting qubits: updated analysis and large‑scale simulations.” (Recent extended study.)​

