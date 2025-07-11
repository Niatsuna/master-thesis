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
- **Key Innovation / Differentiator**: Advanced mobility modelling with realistic movement patterns, distance-based latency calculation, probabilistic edge orchestration

---

## Functional Capabilities
- **Topology Support**: Hierachical (Multi-tier: Cloud-Edge-Mobile)
- **Network Types**: WLAN, WAN, Cellular networks
- **Protocol Support**: Basic network protocols (not further specified)
- **Mobility Support**: Advanced mobility models with realistic movement patterns
- **Network Delays**: Propagation, Queuing (single server queue model), Distance-based latency
- **Bandwidth Modeling**: Fixed bandwidth allocation
- **Communication Patterns**: Request-response patterns, Upload/Download modeling

### Device & Infrastructure Modeling
- **Device Types**: Mobile devices, Edge servers, Cloud datacenters, WiFi access points
- **Resource Modeling**: CPU (MIPS), Memory, Storage, Network bandwidth
- **Heterogeneity Support**: Support for heterogenous edge server configurations
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
- **Energy Modeling**: Not supported
- **Power States**: Active/Processing states only
- **Energy Harvesting**: Not supported
- **Carbon Footprint**: Not supported

---

## Metrics & Evaluation

### Performance Metrics
<!-- List each metric with clear definition and measurement approach -->
> **Disclaimer**: The Paper itself doesn't present the default metrics but the metrics can be found in the logger (SimLogger.java). 
> Other papers also mentioned derived metrics that are calculated metrics based on the 43 implemented default metrics from the logger, like Failure, Success and Completion Rates for Tasks as well as Response Time.

- **Latency Metrics**: 
  - **Network Delay** : Overall network delay experienced by tasks (aggregated across all network types) as well as separated delay metrics for each network type (GSM/Cellular, WAN, MAN, WLAN)
  - **Service Time**: Total time taken to service a task (includes processing + network delays) as well as seperated metrics for each layer (Cloud, Edge, Mobile)
  - **Processing Time**: Pure computational time required to execute tasks (excluding network delays) as well as seperated metrics for each layer (Cloud, Edge, Mobile)
- **Throughput Metrics**:
  - **Completed Task** : Total number of tasks that were successfully completed during the simulation as well as separated metrics for each layer (Cloud, Edge, Mobile)
  - **Failed Task**: Total number of tasks that failed during execution as well as separated metrics for each layer (Cloud, Edge, Mobile)
  - **Uncompleted Task**: Total number of tasks that were not completed during the simulation as well as seprate metrics for each layer (Cloud, Edge, Mobile)
  
- **Resource Metrics**:
  - **Bandwidth Usage Metrics**: Metrics for Bandwidth utilization for all types (GSM/cellular, WAN, MAN, WLAN)
  - **Failed Tasks Due To VM Capacity**: Total number of tasks that failed due to insuffiecient VM capacity as well as separated metrics for each layer (Cloud, Edge, Mobile)
  - **Failed Tasks Due to Bandwith**: Total number of taskt that failed due to insufficient bandwith as well as seprated metrics for each type (GSM/Cellular, WAN, MAN, WLAN)
  
- **Quality of Service**:
  - **QoE**: Quality of Experience metric measuring user satisfaction with service delivery
    > According to Sample_app5/VehicularMobileDeviceManager:
    >
    > QoE starts here at a value of 100.
    > If the service takes too much time the QoE decreases based on a set sensitivity and the factual
    > difference of QoE in between the maxDelay and the doubled maxDelay
    >
    > 1. Perfect Performance: serviceTime <= maxDelay (QoE = 100)
    > 2. Linear Degradation: serviceTime > maxDelay, QoE decreases linearly based on the excess delay
    > 3. Minimum Floor: QoE >= 100 * (1 - delaySensitivity) (Performance Floor)
    > 4. Saturation Point: At serviceTime = 2 * maxDelay, QoE reaches its minimum and stays constant
  - **Failed Tasks Due to Mobility**: Number of tasks that failued due-to mobility-related issues (e.g. out-of-range)
  - **Rejected Tass Due to WLAN Range**: Number of tastks rejected due to being outside WLAN coverage range
  
- **Cost Metrics**:
  - **Task execution cost**: Financial cost associated with task execution (e.g. Cloud resource usage costs)
- **Additional Metrics**:
  - **Orchestrator Overhead**: Overhead time/cost introduced by the orchestration system for task scheduling and management
  

### Custom Metrics & Extensibility
- **Custom Metric Support**: Yes, via simulation event hooks and user-defined calculations
- **Metric Aggregation**: Statistical summaries (mean, median, 95th percentile)
- **Output Formats**: log files, Visual Charts (MATLAB Compatible), Statistical reports

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
- **Known Limitations**: Limited to discrete event simulation, simplified energy modeling through approximation of ressource utilization
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
- **Data Pattern Support**: Periodic task generation, bursty traffic patterns, random mobilityp patterns
- **Input Data**: XML configurations files Java parameter settings
- **Output Data**: Log files
- **Trace Generation**: Synthetic mobility traces, Poisson-based task generation
- **Data Validation**: Basic input validation for configuration parameters

---

## Assessment

### Strengths
- Specifically designed for MEC scenarios
- Execellent mobility modeling capabilities
- Realistic network modeling for WLAN / WAN with distance-based latency
- Documentation with five example scenarios
- modular architecture allows easy customization

### Weaknesses
- Inactive development
- Limited scope due to focus on MEC
- Requires MATLAB for full visualization capabilities
- Less suitable for pure IoT or cloud computing scenarios
- Limited built-in support for modern AI/ML workloads
- Single-threaded execution limits scalability
- No security or privacy modeling capabilities
- No energy modeling
- Output is .log file formatted and therefore needs a translator for csv for matlab

### Best Use Cases
- MEC research and evaluation
- Task offloading algorithm development
- MEC infrastructure planning and optimization
- augmented reality and mobile application studies
- network performance analysis in edge scenarios with mobility

### Worst Use Cases (Avoid when)
- Pure cloud computing simulations
- large-scale IoT deployments without mobility requirements
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