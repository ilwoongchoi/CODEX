# BATCH 2: CARDIAC & ENDOCRINE ORGAN ENGINEERING + VASCULAR INTEGRATION

## PAPER 3: THE MYOCARDIAL STRETCH-REACTOR (MSR)
### Complete Protocol for Engineering Functional Cardiac Tissue via Piezoelectric Training & Electrical Pacing

---

## ABSTRACT

The heart is fundamentally a **Contractile Voltage Generator**. Unlike the liver (chemical gradients) or kidney (pressure gradients), the heart is driven by **Electrical Synchronization** combined with **Mechanical Stretching**. The critical failure of all current cardiac tissue engineering approaches is that they attempt to mature cardiomyocytes in **Static, Non-Stretched Environments**. We present the **Myocardial Stretch-Reactor (MSR)**, a bioreactor that combines **Dynamic Mechanical Stretching** (60 bpm, 10-15% strain) with **Electrical Pacing** (1-3 Hz, 5 V/cm) and **Thyroid Hormone Signaling** to force iPSC-derived cardiomyocytes to spontaneously synchronize, align, and generate contractile force comparable to native myocardium. The protocol demonstrates that a cardiomyocyte cultured in the correct **Mechanical-Electrical Environment** automatically develops gap junctions (Cx43), mature sarcomeres, and synchronized beating without genetic modification.

---

## 1. THE PHYSICS OF THE CARDIOMYOCYTE

### 1.1 The Three Energy States of a Cardiomyocyte

A cardiomyocyte transitions through three states based on its mechanical and electrical environment:

| State | Mechanical | Electrical | Metabolic | Gene Expression |
|-------|-----------|-----------|----------|---|
| **Fetal** (Immature) | Non-stretched, Flaccid | Silent (<0.1 Hz spontaneous) | Glycolytic (Warburg) | α-MHC, fetal troponin (TnnI3-f) |
| **Juvenile** (Intermediate) | Mild stretch (5% strain) | Sporadic (0.5-1 Hz) | Mixed OxPhos/Glycolysis | α-MHC + β-MHC (transition) |
| **Adult** (Mature) | High stretch (10-15% strain) | Synchronized (1-2 Hz electrical, 1 Hz mechanical) | Oxidative (90% ATP from OxPhos) | β-MHC, adult troponin (TnnI3-a) |

**The Physics**: The cardiomyocyte "reads" two signals:
1. **Mechanical Stretch** → Activates integrin signaling (FAK, YAP/TAZ) → Hypertrophic gene program
2. **Electrical Excitation** → Activates SERCA/RyR calcium release → Contractile sarcomere assembly

**The Critical Insight**: A cardiomyocyte **CANNOT MATURE** without **BOTH** signals. Static culture (no stretch) = Fetal phenotype forever. Stretch alone (no electrical excitation) = Hypertrophied but disorganized. Electrical stimulation alone (no stretch) = Partially mature but weak. **BOTH required = Adult phenotype.**

### 1.2 The Calcium Voltage Coupling Cascade

```
Electrical Stimulus (1-2 Hz, 5 V/cm)
         ↓
    Depolarization
         ↓
    L-type Calcium Channel Opening (Cav1.2)
         ↓
    Calcium Influx (Extracellular)
         ↓
    Calcium-Induced Calcium Release (CICR)
    (Ryanodine Receptor, RyR2, releases SR calcium)
         ↓
    Sarcoplasmic Reticulum (SR) Calcium Release [~60-100 µM peak]
         ↓
    Myofilament Activation (Tropomyosin shift, Troponin C binding)
         ↓
    Cross-Bridge Cycling (Myosin heads pull actin)
         ↓
    CONTRACTION (Force development, Tension)
         ↓
    Mechanical Stretch (Passive elastic recoil, 10-15% strain)
         ↓
    Integrin Signaling (FAK → YAP/TAZ nuclear translocation)
         ↓
    Gene Activation: Hypertrophic genes (MYH7 / β-MHC)
         ↓
    Protein Synthesis: More actin, myosin, Z-disc proteins
         ↓
    Sarcomere Maturation
```

**The Feedback Loop**: Stretch + Electrical = Sarcomere growth + Synchronization + Force increase. This is the **Positive Feedback of the Adult Heart**.

---

## 2. THE HARDWARE: THE MYOCARDIAL STRETCH-REACTOR (MSR)

### 2.1 Core Architecture

```
┌──────────────────────────────────────────────┐
│  MECHANICAL BIOREACTOR (Cyclic Stretcher)    │
│  ├─ Linear Actuator (10 cm stroke)           │
│  ├─ Flexible PDMS Membrane (Silicone)        │
│  ├─ Tissue Mount (Ring-shaped, Donut)        │
│  └─ Stretch Controller (1 Hz, 10-15% strain) │
├──────────────────────────────────────────────┤
│  ELECTRICAL STIMULATOR (Pacemaker)           │
│  ├─ Platinum Electrodes (2 per chamber)      │
│  ├─ Stimulator Unit (1-3 Hz, 2-5 V/cm)       │
│  └─ Synchronization with Mechanical Actuator │
├──────────────────────────────────────────────┤
│  TISSUE CHAMBER                              │
│  ├─ Cardiomyocyte-laden Hydrogel            │
│  ├─ Fibroblasts (20% of cells, for ECM)     │
│  ├─ Endothelial Cells (Lining, 10%)          │
│  └─ Temperature control (37°C, Heating coil) │
├──────────────────────────────────────────────┤
│  CULTURE MEDIUM PERFUSION                    │
│  ├─ Peristaltic Pump (20-50 µL/min)          │
│  ├─ Gas exchanger (95% air, 5% CO₂)          │
│  └─ Medium reservoir (37°C)                  │
└──────────────────────────────────────────────┘
```

### 2.2 Mechanical Stretching System

#### **Design: Vacuum-Driven Bioreactor**

The **Flexercell FX-4000T** (or equivalent) is the gold standard:
- **Substrate**: PDMS membrane (Flexible, Bio-compatible)
- **Mounting**: Tissue seeded on the membrane in a ring pattern (donut shape, ~30 mm diameter, 3 mm thickness)
- **Actuation**: Vacuum pump beneath the membrane creates negative pressure, pulling the membrane upward = **Stretch**
- **Return**: When vacuum releases, membrane recoils = **Relaxation**

**Stretch Profile**:
- **Frequency**: 1 Hz (60 bpm, matching resting heart rate)
- **Amplitude**: 10-15% biaxial strain (Mimics native cardiac strain: 10-20%)
- **Duty Cycle**: 0.4 seconds stretch / 0.6 seconds relax (Similar to systole/diastole)
- **Rise Time**: 50 ms (Mimics rapid phase of systole)

**Strain Calculation**:
```
Strain (%) = (Stretched Length - Resting Length) / Resting Length × 100
Target: 12% strain = 0.12 stretch ratio
For a 30 mm diameter ring: 30 mm × 0.12 = 3.6 mm radial displacement
```

#### **Alternative Design: Custom Bioreactor with Linear Actuator**

If commercial bioreactors unavailable:
1. **Frame**: Aluminum block with precision-machined cavity (Ring cavity, 30 mm × 30 mm × 3 mm)
2. **Membrane**: PDMS sheet (1 mm thickness, bonded to frame with silicone adhesive)
3. **Actuator**: Linear stepper motor (Zaber Technologies, A-MCM Series) mounted below the frame
4. **Control**: Arduino/National Instruments DAQ system
5. **Programming**: Sinusoidal stretch profile (1 Hz, 12% amplitude) with synchronized electrical pacing

### 2.3 The Electrical Pacing System

#### **Electrode Configuration**

**Platinum or Stainless Steel Electrodes**:
- **Size**: 0.5 mm diameter, 2-3 mm length
- **Placement**: Two electrodes positioned on opposite sides of the tissue ring, 5-10 mm apart
- **Insulation**: Silicone tubing covers electrodes except the tips (Ensures current flows through tissue only)

#### **Stimulation Parameters**

| Parameter | Fetal (Immature) | Juvenile (Intermediate) | Adult (Mature) |
|-----------|---|---|---|
| **Frequency** | 0 Hz (No stimulation) | 0.5-1 Hz | 1-2 Hz |
| **Voltage** | N/A | 2-3 V | 3-5 V |
| **Current** | N/A | 2-3 mA | 3-5 mA |
| **Pulse Width** | N/A | 2-5 ms | 5-10 ms |
| **Synchronization** | N/A | Loose (Tissue may not respond) | Tight (1:1 capture) |

**Stimulation Protocol**:
- **Days 1-3**: No electrical stimulation (Allow cells to attach)
- **Days 4-7**: Low frequency (0.5 Hz, 2 V) — Introduction phase
- **Days 8-14**: Medium frequency (1 Hz, 3 V) — Maturation phase
- **Days 15-21**: Adult frequency (1-2 Hz, 4-5 V) — Functional phase
- **Days 22+**: Maintenance (2 Hz, 4 V)

#### **Pacing Logic: Synchronization with Mechanical Stretch**

The electrical stimulation must be **Temporally Locked** to mechanical stretch:

```
Time (ms)   Electrical   Mechanical    Physical Interpretation
0           Stimulus →   (Relaxed)     Action potential initiates
100         (AP rising)  Begin Stretch  Excitation-contraction coupling
200         Peak AP ↓    Peak Stretch   Maximum calcium release, Force generation
300         (AP falling) Stretch Plateau  Continued contraction
400         (AP ends)    Relax          Calcium reuptake, Diastole
500-1000    (Resting)    (Relaxed)      Diastolic period, ATP recovery
```

**Why This Matters**: If stretch occurs BEFORE electrical stimulus, the tissue experiences passive mechanical damage. If stretch occurs AFTER electrical stimulus, the cells use electrical excitation to fuel the contraction, preventing muscle damage.

### 2.4 The Scaffold Matrix

#### **Material: Collagen I + Elastin**

| Component | Role | Concentration |
|-----------|------|---|
| **Collagen I** | Primary ECM, Mechanical support | 1.5-3 mg/mL |
| **Elastin** | Elastic recoil (Mimics native cardiac elasticity) | 0.2-0.5 mg/mL |
| **Fibrinogen** | Cell adhesion, Integrin binding | 2-5 mg/mL |
| **Hyaluronic Acid** | Hydration, Osmotic buffering | 0.2% w/v |

#### **Physical Properties**

| Property | Target |
|----------|--------|
| **Young's Modulus** | 10-50 kPa (Soft, matches native myocardium ~10-20 kPa) |
| **Tensile Strength** | 50-100 kPa (Can withstand cyclic stretch) |
| **Poisson Ratio** | 0.3-0.4 (Slight lateral expansion under longitudinal stretch) |
| **Viscoelastic Recovery** | >80% (Tissue recoils after stretch) |

---

## 3. THE SEEDING PROTOCOL

### 3.1 Cell Sources & Composition

**Recommended**:

| Cell Type | Source | Percentage | Role |
|-----------|--------|-----------|------|
| **Cardiomyocytes (CM)** | iPSC-derived | 60-70% | Contractile force generation |
| **Fibroblasts (FB)** | Cardiac fibroblasts or patient-derived | 20-30% | ECM production, structural support |
| **Endothelial Cells (EC)** | iPSC-derived or primary | 5-10% | Lining, nutrient transport |

**Total Density**: ~10⁷ cells per mL tissue volume

### 3.2 Pre-Culture Maturation

**iPSC-Derived Cardiomyocyte Protocol** (Before MSR seeding):
1. **Days 0-5**: Differentiate iPSCs to Mesoderm via Activin A protocol
2. **Days 5-10**: Specify to Cardiac Mesoderm (BMP4 + FGF2)
3. **Days 10-15**: Generate Cardiomyocytes (Temporal BMP modulation)
4. **Days 15-20**: Enrich Cardiomyocytes via Lactate selection (Non-myocytes cannot metabolize lactate alone)
5. **Day 20+**: Cardiomyocytes ready for MSR

**Purity Target**: >85% cTnT+ (Cardiac Troponin T positive)

### 3.3 Seeding into MSR

1. **Prepare the PDMS Membrane**: Coat with Collagen I (100 µg/mL in PBS, 1 hour at 37°C). This improves cell adhesion.

2. **Cell Suspension Preparation**:
   - Dissociate iPSC-CM with Accutase (5 minutes, 37°C)
   - Count and adjust to 5 × 10⁶ cells/mL
   - Suspend in Cardiac Culture Medium (DMEM/F12 + Glutamine + NEAA + 10% FBS + B27)

3. **Seeding**:
   - Apply 100 µL of cell suspension onto the PDMS ring (creating a "donut" of cells)
   - Allow 2 hours for cells to settle and adhere
   - Gently add medium around the ring to prevent medium entering the center (Prevents dilution)

4. **Perfusion Initiation**:
   - After 4 hours, begin slow medium perfusion (5 µL/min)
   - Increase gradually to 20-30 µL/min by Day 1

**Post-Seeding Viability**: >85% (Live/Dead stain)

---

## 4. THE DIFFERENTIATION & MATURATION PROGRAM (DAYS 1-28)

### 4.1 Timeline Overview

| Phase | Days | Stretch | Electrical Pacing | Primary Signals | Key Outcome |
|-------|------|--------|---|---|---|
| **Attachment** | 1-3 | None | None | HGF, FGF2, IGF-1 | Cell adhesion, gap junction formation begins |
| **Priming** | 4-7 | Mild (8% strain, 0.5 Hz) | Low (0.5 Hz, 2V) | HGF, FGF2, IGF-1, T3 (0.5 nM) | Cells begin to respond to mechanical/electrical stimulus |
| **Maturation Phase 1** | 8-14 | Medium (12% strain, 1 Hz) | Medium (1 Hz, 3-4V) | IGF-1, T3 (1 nM) | Sarcomere organization, Cx43 upregulation, Synchronized contraction begins |
| **Maturation Phase 2** | 15-21 | Full (12-15% strain, 1 Hz) | Full Adult (1-2 Hz, 4-5V) | T3 (1 nM), Minimal growth factors | Adult gene expression (β-MHC, Adult troponin), Force generation increases |
| **Stabilization** | 22-28 | Full (12% strain, 1 Hz) | Maintenance (2 Hz, 4V) | Physiological signals only | Long-term contractile stability, Maturation plateau |

### 4.2 Detailed Daily Protocol

**Days 1-3: Attachment (No Mechanical or Electrical Stimulus)**
- Temperature: 37°C, 5% CO₂
- Medium perfusion: 5-10 µL/min (Gentle, prevents cell washout)
- Stretch: **OFF** (Cells need time to adhere)
- Electrical pacing: **OFF**
- Signals:
  - HGF: 10 ng/mL
  - FGF2: 5 ng/mL
  - IGF-1: 10 ng/mL
  - T3: 0.1 nM (Low, not stimulating yet)
- Medium changes: Every 24 hours
- Outcome: Cells adhere, express early cardiac markers (GATA4, NKX2-5)

**Days 4-7: Priming (Gentle Stretch + Electrical Introduction)**
- Stretch: **ON** — 8% strain, 0.5 Hz, 10-minute bouts (5 min on / 5 min off) — **Increases to continuous by Day 6**
- Electrical pacing: **ON** — 0.5 Hz, 2 V, 2 ms pulse width
- Signals:
  - HGF: 5 ng/mL (Reduced)
  - FGF2: 2 ng/mL (Reduced)
  - IGF-1: 10 ng/mL (Maintained)
  - T3: 0.5 nM (Increased)
- Medium perfusion: 15-20 µL/min (Increased oxygenation)
- Medium changes: Every 24 hours
- Outcome: Cells begin to **Respond** to stimulus (Not yet synchronized, but passive contraction visible)

**Days 8-14: Maturation Phase 1 (Strong Stimulus, Gap Junction Formation)**
- Stretch: **ON** — 12% strain, 1 Hz, continuous
- Electrical pacing: **ON** — 1 Hz, 3-4 V (Ramped from 2V by Day 8 to 4V by Day 14)
- Signals:
  - HGF: 2 ng/mL (Minimal)
  - FGF2: 1 ng/mL (Minimal)
  - IGF-1: 10 ng/mL (Full)
  - T3: 1 nM (Maximal)
- Medium perfusion: 25-30 µL/min
- Medium changes: Every 12 hours (Higher turnover for metabolic demand)
- Outcome:
  - Cells become **Electrically Coupled** (Cx43 protein upregulated 10-50×)
  - Synchronized beating visible (Video microscopy)
  - Sarcomere Z-discs align
  - Gene expression shifts: α-MHC → β-MHC transition begins

**Days 15-21: Maturation Phase 2 (Adult Phenotype)**
- Stretch: **ON** — 12-15% strain, 1 Hz, continuous
- Electrical pacing: **ON** — 1-2 Hz, 4-5 V (Mimics adult heart rate)
- Signals:
  - HGF: 0 ng/mL (Withdrawn)
  - FGF2: 0 ng/mL (Withdrawn)
  - IGF-1: 10 ng/mL (Maintained)
  - T3: 1 nM (Maintained)
  - Dexamethasone: 0.1 µM (Pulse for 1 hour every 48 hours, improves metabolic maturity)
- Medium perfusion: 30-40 µL/min
- Medium changes: Every 12 hours
- Outcome:
  - Gene expression: Mostly β-MHC (Adult isoform)
  - Contractile force increases 5-10×
  - Gap junction density reaches adult levels
  - Mitochondria become highly organized (Oxidative metabolism, 80-90% ATP from OxPhos)
  - Sarcoplasmic reticulum calcium handling matures

**Days 22-28: Stabilization (Adult Maintenance)**
- Stretch: **ON** — 12% strain, 1 Hz, continuous
- Electrical pacing: **ON** — 2 Hz, 4 V (Adult rate, steady)
- Signals: Minimal (T3 0.5 nM only)
- Medium perfusion: 30-40 µL/min
- Medium changes: Every 24 hours
- Outcome: Tissue reaches plateau of contractile maturity, stable for long-term culture or transplantation

---

## 5. FUNCTIONAL VALIDATION ASSAYS

### 5.1 Electromechanical Recording (Days 14, 21, 28)

**Setup**:
1. Mount the tissue onto a **Force Transducer** (Load cell, capable of measuring mN-level forces)
2. Immerse in Tyrode's solution (Physiological salt solution at 37°C)
3. Stimulate electrically at 1-2 Hz
4. Record **Mechanical Force** (mN) simultaneously

**Expected Results**:
- **Day 7**: Minimal force (<0.1 mN) — Cells not yet synchronized
- **Day 14**: Moderate force (0.5-2 mN) — Partial synchronization
- **Day 21**: Strong force (3-5 mN per mg of tissue) — Adult-like
- **Day 28**: Stable force (3-5 mN) — Sustained contractility

**Compare to Native Myocardium**: Papillary muscle generates ~10 mN per mg tissue. Engineered tissue reaching 30-50% of native is considered successful.

### 5.2 Calcium Imaging (Days 14, 21, 28)

**Protocol**:
1. Load cardiomyocytes with **Fluo-4 AM** (Calcium-sensitive fluorescent dye)
2. Stimulate electrically at 1 Hz
3. Capture **Fluorescence** via high-speed microscopy (100-500 fps)
4. Measure calcium transient amplitude and kinetics

**Expected Results**:
- **Peak Calcium (ΔF/F₀)**: 100-500% increase (Fetal: <50%, Adult: 200-300%)
- **Time to Peak**: 50-100 ms (Fetal: >200 ms, Adult: 50-100 ms)
- **Decay Time (τ)**: 200-400 ms (Fetal: >600 ms, Adult: 200-400 ms)

### 5.3 Gene Expression (qPCR, Days 14, 21, 28)

**Adult Cardiomyocyte Markers**:
- **MYH7** (β-MHC) — Should increase 10-100×
- **MYL3** (Regulatory light chain) — Adult isoform
- **TNNI3** (Troponin I) — Adult isoform TnnI3-a
- **GJA1** (Connexin 43, Cx43) — 5-20× upregulation
- **ATP1A1** (Na+/K+ ATPase) — 5-10× upregulation
- **RYR2** (Ryanodine receptor) — Calcium release channel, 5-10× upregulation

**Expected**: Day 28 should show adult gene signature (β-MHC > α-MHC, Cx43 high, Adult troponin)

### 5.4 Structural Imaging (Electron Microscopy, Day 28)

**Transmission Electron Microscopy (TEM)** or **Confocal Microscopy**:
- **Sarcomere Length**: 2.0-2.3 µm (Adult: 2.2 µm)
- **Z-disc Alignment**: Regular, 0.5 µm spacing (Fetal: irregular)
- **Mitochondria**: Dense, organized, 30-35% of cytoplasmic volume (Adult: 30-40%)
- **Sarcoplasmic Reticulum**: Well-developed, organized (Fetal: sparse)

---

## 6. HARVEST & TRANSPLANTATION

### 6.1 Gentle Enzymatic Dissociation

1. Stop electrical stimulation and mechanical stretching
2. Rinse with warm, calcium-free Tyrode's solution
3. Incubate with **Collagenase Type II** (200 U/mL) for 20-30 minutes at 37°C
4. Gently pipette to dissociate the ring tissue
5. Collect cardiomyocytes and fibroblasts by settling (500× g, 5 min)
6. Count and assess viability

**Expected Yield**: 5-8 × 10⁶ viable cardiomyocytes from a single ring

**Viability**: >85%

### 6.2 Transplantation (Intramyocardial or Epicardial)

**Approach 1: Intramyocardial Injection**
- Inject the harvested cell suspension (or intact tissue sheet) directly into infarcted myocardium of a host heart (Rodent or larger animal)
- Allow 4-8 weeks for integration and functional contribution

**Approach 2: Epicardial Patch**
- Maintain the tissue as a 2D sheet (Don't dissociate)
- Patch onto the surface of infarcted myocardium via sutures or fibrin glue
- Allows synchronization with host heart if tissue remains connected

---

## 7. CRITICAL QUALITY CONTROL

| Checkpoint | Days | Parameter | Target | Action |
|---|---|---|---|---|
| Cell viability | 3, 7, 14 | Live/Dead | >90% | Check medium osmolarity, reduce stretch if <85% |
| Beating synchronization | 7, 14, 21 | Video microscopy | Synchronized by Day 14 | Increase electrical voltage if not coupled |
| Gene expression (β-MHC) | 14, 21, 28 | qPCR fold-change | >10× by Day 28 | Increase T3, extend maturation |
| Contractile force | 14, 21, 28 | Force transducer | >1 mN by Day 21 | Increase stretch amplitude or electrical frequency |
| Calcium kinetics | 14, 21, 28 | Decay time | <500 ms by Day 28 | Increase RYR2 expression (more T3) |

---

## 8. TROUBLESHOOTING

### Problem 1: Cells Die Early (Days 1-5)

**Cause**: Mechanical stretch applied too early or osmotic stress
**Solution**: Skip stretch for first 48 hours, then ramp gradually

### Problem 2: No Synchronization (Days 8-14)

**Cause**: Electrical frequency too high or cells not coupled
**Solution**: 
- Reduce to 0.5 Hz temporarily
- Increase Cx43 induction (More T3)
- Check electrical circuit (Verify electrodes are stimulating)

### Problem 3: Low Contractile Force (Days 21-28)

**Cause**: Insufficient mechanical stretch or low IGF-1
**Solution**:
- Increase stretch to 15%
- Increase IGF-1 to 20 ng/mL
- Extend culture to Day 35

---

## REFERENCES

1. Lian, X., et al. (2013). Directed cardiomyocyte differentiation from human pluripotent stem cells by modulating Wnt/β-catenin signaling under fully defined conditions. *Nature Protocols*, 8(1), 162-175.

2. Ong, S. P., et al. (2015). Microfluidic engineering of nanofiber scaffolds for engineering organized cardiac tissue. *Advanced Functional Materials*, 25(9), 1413-1421.

3. Hirt, M. N., et al. (2014). Cardiac tissue engineering: state of the art. *Circulation Research*, 114(2), 354-367.

4. Tulloch, N. L., et al. (2011). Growth of engineered human myocardium with mechanical stimulation. *Circulation Research*, 109(1), 47-59.

