# 3Y Test Rig — Signal Flow Diagram

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#2ecc71', 'primaryTextColor': '#ecf0f1', 'lineColor': '#95a5a6', 'secondaryColor': '#3498db', 'tertiaryColor': '#1a1a2e'}}}%%

flowchart TB
    subgraph POWER["Power Supply"]
        PSU["12V 3A PSU<br/>mains input"]
    end

    subgraph GENERATION["Signal Generation"]
        ARD1["Arduino Mega 2560<br/>3-phase sine generator<br/>frequency sweep control"]
        SIG["AD9833 Module<br/>(Tier 2+: 0.1 Hz resolution)"]
        SI5351["SI5351 Clock Gen<br/>(Tier 3: up to 160 MHz)"]
    end

    subgraph AMPLIFICATION["Amplification Stage"]
        AMP1["TDA2030 #1<br/>18W channel"]
        AMP2["TDA2030 #2<br/>18W channel"]
        AMP3["TDA2030 #3<br/>18W channel"]
    end

    subgraph RIG["Test Rig (inside Faraday cage)"]
        direction TB
        subgraph COILS["Copper Phase Drivers"]
            C1["Coil 1<br/>phase = 0°<br/>100 turns, 0.5mm Cu"]
            C2["Coil 2<br/>phase = 120°<br/>100 turns, 0.5mm Cu"]
            C3["Coil 3<br/>phase = 240°<br/>100 turns, 0.5mm Cu"]
        end
        NODE["Y-Junction Centre Node<br/>Z3 topological defect<br/>psi_1 + psi_2 + psi_3 = 0<br/>alpha = cos(psi - phi) -> 0"]
        MASS["Lead Test Mass<br/>50g on torsion balance"]
    end

    subgraph DETECTION["Detection System"]
        direction TB
        WIRE["Tungsten Wire<br/>0.1mm, 30cm<br/>torsion constant ~10^-8 N*m/rad"]
        MIRROR["Mirror<br/>on torsion arm"]
        LASER["Red Laser<br/>< 5mW"]
        PD["Photodiode BPW34<br/>(or quadrant detector Tier 3)"]
    end

    subgraph DAQ["Data Acquisition"]
        ARD2["Arduino Due<br/>12-bit ADC<br/>lock-in correlator"]
        LOCKIN["Lock-In Algorithm<br/>modulate drive ON/OFF<br/>correlate with reference<br/>noise rejection ~100-200x"]
    end

    subgraph ANALYSIS["Analysis & Logging"]
        LAPTOP["Laptop<br/>Python serial logger"]
        SWEEP["sweep_data.csv<br/>freq, PD_signal, baseline,<br/>SNR, timestamp"]
        PLOT["Real-time plot<br/>signal vs frequency"]
        FLAG["Anomaly flagging<br/>threshold: 3 sigma<br/>above baseline"]
    end

    subgraph CONTROLS["Control Runs"]
        CTRL1["Control 1<br/>shielding OFF<br/>(EM baseline)"]
        CTRL2["Control 2<br/>coils OFF<br/>(vibration baseline)"]
        CTRL3["Control 3<br/>random phases<br/>(no Z3 topology)"]
    end

    %% Power connections
    PSU --> AMP1 & AMP2 & AMP3
    PSU --> ARD1
    PSU --> ARD2

    %% Signal generation chain
    ARD1 --> SIG
    ARD1 --> SI5351
    SIG --> AMP1
    SIG --> AMP2
    SIG --> AMP3

    %% Amplifier to coils
    AMP1 -->|"twisted pair"| C1
    AMP2 -->|"twisted pair"| C2
    AMP3 -->|"twisted pair"| C3

    %% Coils to node
    C1 -->|"B-field<br/>phase 0°"| NODE
    C2 -->|"B-field<br/>phase 120°"| NODE
    C3 -->|"B-field<br/>phase 240°"| NODE

    %% Node to mass
    NODE -->|"gravitational<br/>anomaly?"| MASS

    %% Detection chain
    MASS --- WIRE
    WIRE --- MIRROR
    LASER -->|"beam"| MIRROR
    MIRROR -->|"reflected beam<br/>angle encodes force"| PD

    %% DAQ chain
    PD -->|"analog signal"| ARD2
    ARD1 -->|"reference signal<br/>(modulation sync)"| ARD2
    ARD2 --> LOCKIN
    LOCKIN -->|"filtered signal"| LAPTOP

    %% Analysis
    LAPTOP --> SWEEP
    LAPTOP --> PLOT
    LAPTOP --> FLAG

    %% Controls
    CTRL1 -.->|"compare"| FLAG
    CTRL2 -.->|"compare"| FLAG
    CTRL3 -.->|"compare"| FLAG

    %% Styling
    classDef power fill:#3a2a1a,stroke:#f39c12,color:#f39c12
    classDef gen fill:#1a3a2e,stroke:#2ecc71,color:#2ecc71
    classDef amp fill:#2e1a3a,stroke:#9b59b6,color:#9b59b6
    classDef coil fill:#3d2b1a,stroke:#b87333,color:#e67e22
    classDef node fill:#2c1a1a,stroke:#e74c3c,color:#e74c3c
    classDef detect fill:#1a2a3a,stroke:#3498db,color:#3498db
    classDef daq fill:#1a3a2e,stroke:#2ecc71,color:#2ecc71
    classDef analysis fill:#2a2a3e,stroke:#ecf0f1,color:#ecf0f1
    classDef ctrl fill:#1a1a2e,stroke:#7f8c8d,color:#7f8c8d

    class PSU power
    class ARD1,SIG,SI5351 gen
    class AMP1,AMP2,AMP3 amp
    class C1,C2,C3 coil
    class NODE,MASS node
    class WIRE,MIRROR,LASER,PD detect
    class ARD2,LOCKIN daq
    class LAPTOP,SWEEP,PLOT,FLAG analysis
    class CTRL1,CTRL2,CTRL3 ctrl
```

## Signal Path Summary

1. **Generation:** Arduino Mega generates 3 sine waves at 120° phase offset, sweeping frequency
2. **Amplification:** TDA2030 boards amplify each channel to drive coils
3. **Excitation:** 3 copper coils create oscillating B-fields converging at Y-junction centre
4. **Physics:** At centre node, Z3 phase cancellation forces alpha → 0 (if resonant frequency found)
5. **Detection:** Any gravitational anomaly torques the torsion balance, rotating the mirror
6. **Readout:** Laser reflects off mirror to photodiode — angle change = spot displacement
7. **Filtering:** Lock-in amplifier correlates signal with drive modulation, rejecting noise
8. **Analysis:** Python logs data, flags any frequency where signal exceeds 3-sigma threshold
9. **Validation:** 3 control runs establish baselines; only signals present WITH shielding AND Z3 topology count
