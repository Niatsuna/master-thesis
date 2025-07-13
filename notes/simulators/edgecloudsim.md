# EdgeCloudSim
## Basic Information
- **Programming Language**: Java
- **Base Framework**: CloudSim
- **First Published**: August 2018
- **Last Updated** (Access: June 2025): October 2020
- [Paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/ett.3493) | [Code](https://github.com/CagataySonmez/EdgeCloudSim/tree/master)
  > **Disclaimer** : The original EdgeCloudSim Repository is not up-to-date anymore (v.1.). One of the original authors has their own fork and developed up until October 2020 (v.4.)
- **Development Status**: Inactive

### Core Architecture & Design
- **Simulation Type**: Event-driven simulation
- **Focus**: Mobile Edge Computing (MEC), General Edge Computing Simulation, Cloudlets
- **Design Philosophy**: CloudSim-based framework designed for Edge Computing scenarios with focus on both computational and networking resources
- **Architecture Pattern**: Modular (Five main modules: Core Simulation, Networking, Load Generator, Mobility, Edge Orchestrator)
- **Key Innovation / Differentiator**: Advanced mobility modelling with realistic movement patterns (not real trace integration), distance-based latency calculation, probabilistic edge orchestration

---

## Functional Capabilities
- **Topology Support**: Hierarchical (Multi-tier: Cloud-Edge-Mobile)
- **Network Types**: WLAN, WAN, Cellular networks
- **Protocol Support**: Basic network protocols (not further specified)
- **Mobility Support**: Advanced mobility models with realistic movement patterns (not real trace integration)
- **Network Delays**: Propagation, Queuing (single server queue model), Distance-based latency
- **Bandwidth Modeling**: Fixed bandwidth allocation
- **Communication Patterns**: Request-response patterns, Upload/Download modeling

### Device & Infrastructure Modeling
- **Device Types**: Mobile devices, Edge servers, Cloud datacenters, WiFi access points
- **Resource Modeling**: CPU (MIPS), Memory, Storage, Network bandwidth
- **Heterogeneity Support**: Support for heterogeneous edge server configurations
- **Scaling Capabilities**: Hundreds of mobile devices and multiple edge servers
- **Hardware Abstraction**: Generic hardware models with MIPS-based processing

### Application & Workload Modeling
- **Application Types**: Mobile applications, IoT applications, Compute-intensive tasks
- **Task Dependencies**: Independent task-based modeling
- **Data Flow Patterns**: Request-response, Data upload/download
- **Service Migration**: Basic task offloading between edge and cloud
- **Workload Generation**: Poisson distribution for task generation patterns
- **QoS Requirements**: Latency-focused requirements

### Fault Tolerance & Reliability
- **Failure Models**: Mobility-aware failures, Network failures, Resource failures
- **Fault Detection**: Movement-based handoff detection, Resource monitoring
- **Recovery Strategies**: Task re-offloading, Network handoffs
- **Reliability Metrics**: Task failure rate, Service availability

### Security & Privacy
- **Security Modeling**: Not supported
- **Privacy Mechanisms**: Not supported
- **Attack Simulation**: Not supported
- **Security Metrics**: Not supported

### Energy & Sustainability
- **Energy Modeling**: Not supported; only resource utilization approximations
- **Power States**: Active/Processing states only
- **Energy Harvesting**: Not supported
- **Carbon Footprint**: Not supported

---

## Metrics & Evaluation
- **Metric Architecture**: Simulator-Level (centralized in SimLogger.java)
- **Output Configurability**: Limited (console output, .log files; MATLAB required for full visualization)
- **Custom Metric Support**: Yes, but requires modifying SimLogger.java
- **Notes**: 43 predefined metrics available, derived metrics often calculated in research papers

---

## Technical Implementation

### Setup & Deployment
- **Dependencies**: Java 8+, MATLAB (for visualization), provides compiling options for Linux & Mac but encourages IDE (e.g. Eclipse) for Windows Users
- **Installation Complexity**: Medium
- **Platform Support**: Cross-platform (via Java)
- **Documentation Quality**: Fair (Guide in form of a youtube playlist, no written guide)
- **Community Support**: Limited (inactive development)

### Programming Interface
- **Configuration Method**: XML configuration files + Java code for custom scenarios and metrics
- **API Design**: Object-oriented CloudSim-based API with modular components
- **Extensibility**: Highly extensible through inheritance and interface implementation
- **Integration Capabilities**: MATLAB integration for visualization
- **Example Scenarios**: Multiple (5) comprehensive examples

### Performance & Scalability
- **Simulation Speed**: Optimized for edge computing scenarios
- **Memory Efficiency**: Efficient memory management for mobile edge scenarios
- **Parallelization**: Single threaded
- **Large-scale Support**: Hundreds of mobile devices and multiple edge servers
- **Optimization Features**: Basic caching and optimization

### Validation & Accuracy
- **Validation Methods**: Validated against theoretical models compared with other simulators
- **Accuracy Claims**: Realistic modeling of MEC environments with validated networking models
- **Benchmarking**: Comparison studies with other edge simulators
- **Known Limitations**: Limited to discrete event simulation, simplified energy modeling through approximation of resource utilization
- **Calibration Requirements**: Proper configuration of network and mobility parameters

---

## Research & Development Support

### Experimental Design
- **Scenario Management**: XML-based scenario configuration
- **Reproducibility**: Deterministic execution with seed control
- **Statistical Analysis**: Statistical summaries and percentile calculations
- **Visualization**: MATLAB compatible (integration for sample apps)

### Data Generation & Management
- **Synthetic Data Generation**: Poisson distribution for task arrival patterns, synthetic mobility traces with realistic movement patterns
- **Real-world Data Integration**: Limited support for importing real-world mobility traces
- **Data Pattern Support**: Periodic task generation, bursty traffic patterns, random mobility patterns
- **Input Data**: XML configuration files, Java parameter settings
- **Output Data**: Log files
- **Trace Generation**: Synthetic mobility traces, Poisson-based task generation
- **Data Validation**: Basic input validation for configuration parameters

---

## Assessment

### Strengths
- Specifically designed for MEC scenarios
- Excellent mobility modeling capabilities
- Realistic network modeling for WLAN / WAN with distance-based latency
- Documentation with five example scenarios
- Modular architecture allows easy customization

### Weaknesses
- Inactive development
- Limited scope due to focus on MEC
- Requires MATLAB for full visualization capabilities
- Less suitable for pure IoT or cloud computing scenarios
- Limited built-in support for modern AI/ML workloads
- Single-threaded execution limits scalability
- No security or privacy modeling capabilities
- No energy modeling
- Output is .log file formatted and therefore needs a translator for csv for MATLAB

### Best Use Cases
- MEC research and evaluation
- Task offloading algorithm development
- MEC infrastructure planning and optimization
- Augmented reality and mobile application studies
- Network performance analysis in edge scenarios with mobility

### Worst Use Cases (Avoid when)
- Pure cloud computing simulations
- Large-scale IoT deployments without mobility requirements
- AI/ML-specific edge computing research
- Scenarios requiring massive parallel execution
- Security-focused edge computing research
- Modern microservice-based applications

### Maturity Assessment
- **Development Status**: Inactive
- **Industry Adoption**: Academic use primarily
- **Publication Impact**: Well-cited in MEC research community
- **Future Roadmap**: No apparent future development plans
  > **Note**: "Needed Features" in the README.md mentions:
  > - Task migration among the Edge or Cloud VMs
  > - Energy consumption model for the mobile and edge devices as well as the cloud datacenters
  > - Adding probabilistic network failure model by considering the congestion or other parameters such as the distance between mobile device and the WiFi access point
  > - Visual tool for displaying the network topology

---

## Additional Notes
- No native Kubernetes or container support
- Easy to extend
- Good for general edge computing, Great for MEC research