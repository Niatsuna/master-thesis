# Comparison of characteristics of listed simulators
> This file lists similarities and differences in regards of 8 simulators (see `state-of-art.md` and notes in `/simulators`)
> to deduct the characteristics necessary for a "good" / "proper" edge computing simulator

## Overview

| Simulator    | Language | Sim vs Emu | Scale         | Focus                                 | Status    | First Published; Last Updated |
| ------------ | -------- | ---------- | ------------- | ------------------------------------- | --------- | ----------------------------- |
| iFogSim2     | Java     | Sim        | Large         | Mobility, Microservices, IoT          | Sporadic  | September 2017; August 2021   |
| EdgeCloudSim | Java     | Sim        | Moderate      | Mobility, MEC                         | Inactive  | August 2018; October 2020     |
| YAFS         | Python   | Sim        | Moderate      | Custom algorithms, IoT, Resource alloc| Inactive  | July 2019; June 2022          |
| EdgeAISim    | Python   | Sim        | Moderate      | AI/ML resource management             | Inactive  | October 2023; February 2024   |
| MockFog 2.0  | Node.js  | Emu        | Cloud-limited | Real infra emulation                  | Inactive  | September 2021; June 2021     |
| FogNetSim++  | C++      | Sim        | Large         | Network-centric                       | Inactive  | October 2018; October 2018    |
| EmuFog       | Kotlin   | Emu        | Large         | Real network emulation                | Inactive  | October 2017; September 2020  |
| FogTorchΠ    | Java     | Sim        | Moderate      | Deployment analysis                   | Inactive  | May 2017; January 2019        |

---

## Aspects
### Topology Support
**Hierarchical / Multi-tier (Cloud-Fog-Edge-Device):**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim, MockFog 2.0, FogTorchΠ

**Custom / Flexible Topologies:**
- YAFS (complex networks, arbitrary topologies), EmuFog (import from BRITE/CAIDA, custom)

> **Insight**: Simulators should at least support Hierachical / Multi-tier and at best custom / flexible topologies

---

### Network Types
**WiFi, Cellular, Ethernet, WAN/LAN:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EmuFog

**Generic / Custom Network Modeling:**
- YAFS, FogTorchΠ (abstracted through QoS profiles), MockFog 2.0 (depends on cloud provider)

**AI-Optimized Networking:**
- EdgeAISim

> **Insight**: Support of multiple network types is required for edge/fog scenarios (Selection based on Focus)
---

### Protocol Support
**Standard Protocols (TCP/IP, HTTP, MQTT, UDP):**
- iFogSim2, FogNetSim++, EmuFog

**Generic / Abstracted Protocols:**
- EdgeCloudSim, YAFS, FogTorchΠ

**AI-Enhanced Protocols:**
- EdgeAISim

**Real Infrastructure Protocols:**
- MockFog 2.0 (all protocols supported by underlying infrastructure)

> **Insight**: Protocol abstraction and customization are necessary for diverse application support

---

### Mobility Support
**Advanced Mobility Models:**
- iFogSim2 (real datasets), EdgeCloudSim (movement patterns), FogNetSim++ (INET framework), EdgeAISim (AI-optimized)

**Basic / Dynamic Topology Changes:**
- YAFS

**No Mobility Support:**
- FogTorchΠ, MockFog 2.0, EmuFog

> **Insight**: Mobility is crucial for mobile edge (e.g. IoT) / fog scenarios, but optional for static deployments

---

### Device & Infrastructure Modeling
**Detailed Device Types (IoT, Edge, Fog, Cloud, Mobile):**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Generic Nodes / Highly Customizable:**
- YAFS

**Real Devices (VMs, Containers):**
- MockFog 2.0, EmuFog

**Component-based / Deployment Focus:**
- FogTorchΠ


> **Insight**: Detailed and heterogeneous device modeling is required for edge/fog research

---

### Resource Modeling
**CPU, Memory, Storage, Bandwidth, Battery:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Customizable Resource Attributes:**
- YAFS

**Real Resource Limits:**
- MockFog 2.0, EmuFog

**Discrete Resource Specs:**
- FogTorchΠ

> **Insight**:  Comprehensive resource modeling is essential for accurate simulation

---

### Application & Workload Modeling
**Microservices, DAGs, Real/Synthetic Workloads:**
- iFogSim2, EdgeAISim

**Mobile/IoT Apps, Independent Tasks:**
- EdgeCloudSim

**Custom Algorithms, Flexible Workloads:**
- YAFS

**Network-centric Workloads:**
- FogNetSim++

**Real Applications (Containerized):**
- MockFog 2.0, EmuFog

**Deployment Mapping (No Runtime Simulation):**
- FogTorchΠ

> **Insight**: Support for both synthetic and real workloads is required

---

### Fault Tolerance & Reliability

**Configurable Failure Models & Recovery:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Custom Failure Policies:**
- YAFS

**Real-world Failures & Recovery:**
- MockFog 2.0, EmuFog

**Probabilistic Analysis:**
- FogTorchΠ

> **Insight**:  Failure and recovery modeling is essential for robust edge computing research

---

### Security & Privacy

**Basic Security Modeling:**
- iFogSim2, EdgeAISim, FogNetSim++

**No Security Modeling:**
- EdgeCloudSim, YAFS, FogTorchΠ

**Real Security Implementations:**
- MockFog 2.0, EmuFog (depends on deployed applications)

> **Insight**: Security is important for sensitive applications, but is not always mandatory.

---

### Energy & Sustainability

**Device-level Energy Modeling:**
- iFogSim2, EdgeAISim, FogNetSim++

**Resource Utilization Approximation:**
- EdgeCloudSim

**No Energy Modeling:**
- YAFS, FogTorchΠ, EmuFog

**Real Energy Consumption (Cloud Billing):**
- MockFog 2.0

> **Insight**: Energy modeling is a must for edge/fog scenarios due to resource constraints.

---

### Metrics & Evaluation
> Legend:
> - S : Simulator-Level (Metrics are defined **in** said Simulators code basis)
> - A : Application-Level (Metrics are defined in the deployed Applications)

**Customizable Metrics:**
- iFogSim2 (A), EdgeCloudSim (S), FogNetSim++ (S), YAFS (S, but flexible), EdgeAISim (A)

**Real System Metrics:**
- MockFog 2.0 (A), EmuFog (A)

**Deployment Metrics (QoS, Cost, Feasibility):**
- FogTorchΠ (A)

> **Insight**: Comprehensive, customizable application-leveled metrics and export (CSV) are required.

---

### Extensibility & Customization

**Highly Extensible (Python/Java):**
- YAFS, EdgeAISim, iFogSim2

**Modular but Requires Expertise:**
- EdgeCloudSim, FogNetSim++

**Extensible via Scripts/APIs:**
- MockFog 2.0, EmuFog

**Limited Extensibility:**
- FogTorchΠ

> **Insight**: Extensibility is essential for adpating the simulator to new research needs

---

### Scalability

**Large-scale (Thousands of Nodes):**
- FogNetSim++, iFogSim2, EmuFog

**Moderate Scale:**
- EdgeCloudSim, YAFS, EdgeAISim, FogTorchΠ

**Cloud-limited:**
- MockFog 2.0

> **Insight**:  Scalability is required for realistic edge/fog scenarios and should at least cover the "moderate" aspect.

---

### Documentation & Community

**Good Documentation, Sporadic Community:**
- iFogSim2, EdgeCloudSim

**Good Docs, Small/Inactive Community:**
- YAFS, EdgeAISim

**Technical Docs, Limited Community:**
- FogNetSim++

**Minimal Docs, Inactive:**
- MockFog 2.0, EmuFog

**Academic Docs, Limited Support:**
- FogTorchΠ

> **Insight**: Good documentations and (multiple) examples are essential for usability and reproducibility.