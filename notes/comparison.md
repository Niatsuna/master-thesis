# Comparison of characteristics of listed simulators
> This file lists similarities and differences in regards of 8 simulators (see `state-of-art.md` and notes in `/simulators`)
> to deduct the characteristics necessary for a "good" / "proper" edge computing simulator

## Overview

| Simulator    | Language | Sim vs Emu | Scale         | Focus                                                   | Status    | First Published; Last Updated |
| ------------ | -------- | ---------- | ------------- | ------------------------------------------------------- | --------- | ----------------------------- |
| iFogSim2     | Java     | Sim        | Large         | Mobility, Microservices, IoT                            | Sporadic  | September 2017; August 2021   |
| EdgeCloudSim | Java     | Sim        | Moderate      | Mobility, MEC                                           | Inactive  | August 2018; October 2020     |
| YAFS         | Python   | Sim        | Moderate      | Custom algorithms, IoT, Resource alloc                  | Inactive  | July 2019; June 2022          |
| EdgeAISim    | Python   | Sim        | Moderate      | AI/ML resource management                               | Inactive  | October 2023; February 2024   |
| MockFog 2.0  | Node.js  | Emu        | Cloud-limited | Real infra emulation                                    | Inactive  | September 2021; June 2021     |
| FogNetSim++  | C++      | Sim        | Large         | Network-centric                                         | Inactive  | October 2018; October 2018    |
| EmuFog       | Kotlin   | Emu        | Large         | Real network emulation                                  | Inactive  | October 2017; September 2020  |
| FogTorchΠ    | Java     | Sim        | Moderate      | Deployment analysis                                     | Inactive  | May 2017; January 2019        |
| Fogify       | Python   | Emu        | Cloud-limited | Container-based, reproducible, cloud-native edge/fog    | Active    | November 2020; April 2023     |
| iContinuum   | Python   | Emu        | Cloud-limited | Cloud-to-edge continuum, orchestration, reproducibility | Active    | July 2024; April 2024         |

---

## Aspects
### Topology Support
**Hierarchical / Multi-tier (Cloud-Fog-Edge-Device):**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim, MockFog 2.0, FogTorchΠ

**Custom / Flexible Topologies:**
- YAFS (complex networks, arbitrary topologies), EmuFog (import from BRITE/CAIDA, custom), Fogify (YAML-defined, arbitrary), iContinuum (YAML-defined, arbitrary)

> **Insight**: Simulators/emulators should support both hierarchical and flexible/custom topologies.

---

### Network Types
**WiFi, Cellular, Ethernet, WAN/LAN:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EmuFog, Fogify, iContinuum (emulated via Linux networking)

**Generic / Custom Network Modeling:**
- YAFS, FogTorchΠ (abstracted through QoS profiles), MockFog 2.0 (depends on cloud provider)

**AI-Optimized Networking:**
- EdgeAISim

> **Insight**: Support of multiple network types is required for edge/fog scenarios (selection based on focus).

---

### Protocol Support
**Standard Protocols (TCP/IP, HTTP, MQTT, UDP):**
- iFogSim2, FogNetSim++, EmuFog, Fogify, iContinuum (all protocols supported by containers)

**Generic / Abstracted Protocols:**
- EdgeCloudSim, YAFS, FogTorchΠ

**AI-Enhanced Protocols:**
- EdgeAISim

**Real Infrastructure Protocols:**
- MockFog 2.0

> **Insight**: Protocol abstraction and customization are necessary for diverse application support.

---

### Mobility Support
**Advanced Mobility Models:**
- iFogSim2 (real datasets), EdgeCloudSim (movement patterns), FogNetSim++ (INET framework), EdgeAISim (AI-optimized)

**Basic / Dynamic Topology Changes:**
- YAFS, Fogify, iContinuum (dynamic topology changes, but not advanced mobility models)

**No Mobility Support:**
- FogTorchΠ, MockFog 2.0, EmuFog

> **Insight**: Mobility is crucial for mobile edge/fog scenarios, but optional for static deployments.

---

### Device & Infrastructure Modeling
**Detailed Device Types (IoT, Edge, Fog, Cloud, Mobile):**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Generic Nodes / Highly Customizable:**
- YAFS

**Real Devices (VMs, Containers):**
- MockFog 2.0, EmuFog, Fogify, iContinuum (containers/VMs as nodes, highly customizable)

**Component-based / Deployment Focus:**
- FogTorchΠ

> **Insight**: Detailed and heterogeneous device modeling is required for edge/fog research.

---

### Resource Modeling
**CPU, Memory, Storage, Bandwidth, Battery:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Customizable Resource Attributes:**
- YAFS

**Real Resource Limits:**
- MockFog 2.0, EmuFog, Fogify, iContinuum (container resource limits: CPU, memory, storage, bandwidth)

**Discrete Resource Specs:**
- FogTorchΠ

> **Insight**: Comprehensive resource modeling is essential for accurate simulation.

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
- MockFog 2.0, EmuFog, Fogify, iContinuum (real containerized applications, microservices, IoT workloads)

**Deployment Mapping (No Runtime Simulation):**
- FogTorchΠ

> **Insight**: Support for both synthetic and real workloads is required.

---

### Data Generation & Integration

**Supports Both Synthetic Workload Generation and Real-world Trace Integration:**
- iFogSim2 (synthetic and trace-based workloads, XML config)
- YAFS (customizable distributions, timestamp arrays, supports real traces via Python)
- EdgeAISim (AI-driven workload generation, supports real datasets)

**Supports Only Synthetic Workload Generation:**
- EdgeCloudSim (Poisson distribution, synthetic workloads)
- FogNetSim++ (synthetic traffic via OMNeT++, scenario config)

**Supports Only Real-world Data (No Synthetic Generation):**
- MockFog 2.0, EmuFog, Fogify, iContinuum (real application data, logs; synthetic possible via application logic)

**Limited Data Generation (Probabilistic Analysis, No Runtime Data):**
- FogTorchΠ (probabilistic deployment analysis, limited runtime data generation)

> **Insight**: Most flexible simulators support both synthetic and real-world trace integration.

---

### Fault Tolerance & Reliability
**Configurable Failure Models & Recovery:**
- iFogSim2, EdgeCloudSim, FogNetSim++, EdgeAISim

**Custom Failure Policies:**
- YAFS

**Real-world Failures & Recovery:**
- MockFog 2.0, EmuFog, Fogify, iContinuum (node/link failures, resource exhaustion, container restart/migration)

**Probabilistic Analysis:**
- FogTorchΠ

> **Insight**: Failure and recovery modeling is essential for robust edge computing research.

---

### Security & Privacy
**Basic Security Modeling:**
- iFogSim2, EdgeAISim, FogNetSim++

**No Security Modeling:**
- EdgeCloudSim, YAFS, FogTorchΠ

**Real Security Implementations:**
- MockFog 2.0, EmuFog, Fogify, iContinuum (depends on deployed applications; not simulated, only real-world implementations possible)

> **Insight**: Security is important for sensitive applications, but is not always mandatory.

---

### Energy & Sustainability
**Device-level Energy Modeling:**
- iFogSim2, EdgeAISim, FogNetSim++

**Resource Utilization Approximation:**
- EdgeCloudSim

**No Energy Modeling:**
- YAFS, FogTorchΠ, EmuFog, Fogify, iContinuum (no built-in energy modeling, but real consumption can be measured externally)

**Real Energy Consumption (Cloud Billing):**
- MockFog 2.0

> **Insight**: Energy modeling is a must for edge/fog scenarios due to resource constraints.

---

### Metrics & Evaluation
> - Scenario-Level (Metrics are defined outside of Simulator and Application for each scenario)
> - Simulator-Level (Metrics are defined **in** said Simulators code basis)
> - Application-Level (Metrics are defined in the deployed Applications)

**Customizable Metrics:**
- **Simulator-Level:**
  - EdgeCloudSim, FogNetSim++ (scenario-level config possible via OMNeT++ NED/INI files), YAFS (flexible and close to application-level via Python scenario code)
- **Application-Level:**
  - iFogSim2, EdgeAISim

**Real System Metrics (Application-Level):**
- MockFog 2.0, EmuFog, Fogify, iContinuum (metrics from real containers/applications, fully configurable via monitoring tools)

**Deployment Metrics (QoS, Cost, Feasibility) (Application-Level):**
- FogTorchΠ

> **Insight**: Comprehensive, customizable application-leveled metrics and export (CSV) are required. These should include metrics of all aspects of the simulation (e.g. Resources, Network Usage, Tasks Failure and Success Rates, etc.).

---

### Extensibility & Customization
**Highly Extensible (Python/Java):**
- YAFS, EdgeAISim, iFogSim2, Fogify, iContinuum (YAML, Python API, plugins, custom resource/network models)

**Modular but Requires Expertise:**
- EdgeCloudSim, FogNetSim++

**Extensible via Scripts/APIs:**
- MockFog 2.0, EmuFog

**Limited Extensibility:**
- FogTorchΠ

> **Insight**: Extensibility is essential for adapting the simulator to new research needs.

---

### Scalability
**Large-scale (Thousands of Nodes):**
- FogNetSim++, iFogSim2, EmuFog

**Moderate Scale:**
- EdgeCloudSim, YAFS, EdgeAISim, FogTorchΠ

**Cloud-limited:**
- MockFog 2.0, Fogify, iContinuum (scalable to hundreds of containers, hardware-limited)

> **Insight**: Scalability is required for realistic edge/fog scenarios and should at least cover the "moderate" aspect.

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

**Good Docs, Active Community:**
- **Fogify, iContinuum (active development, examples, tutorials)**

> **Insight**: Good documentation and (multiple) examples are essential for usability and reproducibility. 
> **Note**: EdgeCloudSim has a documentation as a YT Playlist and is very limited in the written documentation.

---

### Scenario Management & Reproducibility
**Scenario Saving/Loading, Deterministic Execution:**
- iFogSim2 (XML topology, Java config), EdgeCloudSim (XML config), YAFS (Python scripts, reproducible with seed), FogNetSim++ (OMNeT++ config files, GUI), EdgeAISim (Python scripts, seed control)
- MockFog 2.0, EmuFog, FogTorchΠ (deployment scripts/configs, limited scenario management)
- Fogify, iContinuum (YAML scenario files, reproducible deployments, deterministic via container orchestration)

> **Insight**: Scenario management and reproducibility are essential for academic research and peer review. Simulators should support saving/loading scenarios and deterministic execution via seed control.

---

### Validation & Accuracy
**Benchmarking, Empirical Validation:**
- iFogSim2, EdgeCloudSim, FogNetSim++ (published validation studies, comparative benchmarking, OMNeT++ visualization)
- YAFS, EdgeAISim (validation possible via custom scripts and comparison; user-driven, not built-in)
- MockFog 2.0, EmuFog (validation against real infrastructure)
- FogTorchΠ (probabilistic validation, deployment feasibility)
- Fogify, iContinuum (empirical validation via real application execution, benchmarking supported)

> **Insight**: Validation and accuracy are essential for trustworthy results. Simulators should provide means for benchmarking and empirical validation.

---

### Usability & User Interface
**Intuitive Configuration, Error Handling, Visualization:**
- EdgeCloudSim (YouTube tutorials, XML config), iFogSim2 (examples, Java/XML, graphical monitoring), YAFS (Python scripts, examples), EdgeAISim (Python, examples)
- FogNetSim++ (OMNeT++ GUI, built-in visualization), FogTorchΠ (academic docs)
- MockFog 2.0, EmuFog (script-based, minimal UI)
- Fogify, iContinuum (YAML config, Python API, external visualization via Grafana/Prometheus, good error feedback)

> **Insight**: Usability is essential for broad adoption. Simulators should offer intuitive configuration, error handling, clear feedback, and visualization tools.

---

### Integration & Interoperability
**External Tool Integration, Data Export:**
- iFogSim2, EdgeCloudSim, YAFS, EdgeAISim (CSV export, Python/Java ecosystem, MATLAB integration)
- FogNetSim++ (OMNeT++ integration, visualization), FogTorchΠ (CSV output)
- MockFog 2.0, EmuFog (real system logs, cloud APIs)
- Fogify, iContinuum (integration with Docker, Kubernetes, monitoring tools, data export via logs/metrics)

> **Insight**: Integration and interoperability enable advanced workflows and data analysis.

---

### Licensing & Accessibility
**Open-source, Academic-friendly Licensing:**
- All listed simulators/emulators are open-source or have academic-friendly licenses.

> **Insight**: Licensing is important for academic use and collaboration.

---

### Performance Optimization
**Parallel/Distributed Simulation, Efficient Resource Usage:**
- FogNetSim++ (OMNeT++ supports parallel simulation), iFogSim2 (optimized for large-scale), EmuFog (real infrastructure, scalable)
- EdgeCloudSim, YAFS, EdgeAISim (single-threaded, moderate scale; EdgeAISim may support AI model parallelization via PyTorch)
- MockFog 2.0 (cloud-limited)
- Fogify, iContinuum (multi-container, multi-host via Kubernetes, efficient orchestration)

> **Insight**: Performance optimization is important for large-scale scenarios.

---

### Support for Emerging Technologies
**Edge AI/ML, Containerization, New Network Tech:**
- EdgeAISim (AI/ML workloads), MockFog 2.0, EmuFog (containerization, real infra), FogNetSim++ (INET/OMNeT++ for new network tech)
- iFogSim2, EdgeCloudSim, YAFS (can be extended for new tech)
- Fogify, iContinuum (cloud-native, containerization, Kubernetes, real microservices, supports emerging paradigms)

> **Insight**: Support for emerging technologies ensures future relevance.