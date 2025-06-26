# EdgeCloudSim
## Basic Information
- Programming Language: Java
- Base: CloudSim
- First Published: August 2018
- Last Updated (Access: June 2025): March 2019
- [Paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/ett.3493)
- [Github](https://github.com/purdue-dcsl/EdgeCloudSim)

### Core Architecture & Design
- Simulation Type: Event-driven simulation
- Focus: General Edge Computing Simulation, Mobile Edge Computing (MEC), Cloudlets
- Design Philosophy: CloudSim-based framework designed for Edge Computing scenarios with focus on both computational and networking resources
- Architecture: Five Main Modules (Core Simulation, Networking, Load Generator, Mobility and Edge Orchestrator)
  - **Mobility**: Manages Location of edge devices and clients with coordinates updated via dynamically managed hash table
  - **Load generator**: Poisson distribution for active / idle task generation pattern
  - **Networking**: Transmission delay in WLAN and WAN considering both upload and download data
  - **Edge orchestrator**: Decision Maker using probabilistic approach to decide where to handle incoming tasks

### Reported Use Cases
- Primary: Mobile Edge Computing Scenarios, Augmented Reality applications, IoT task offloading
- Academic: MEC performance evaluation, task offloading algorithms, edge server placement
- Industrial: Automotive edge computing, smart city applications, mobile gaming

---

## Functional Capabilities
### Network Modeling
- Topology Support: Multi-tier (Cloud-Edge-Mobile) with hierachical structure
- Network Types: WLAN and WAN, cellular networks
- Mobility Support: Advanced device mobility model with realistic movement patterns
- Network Delays: Single server queue model for network delay calculation, distance based latency
### Device & Resource Modeling
- Device Types: Mobile devices, Edge Servers, Cloud datacenters, WiFi access points
- Resource Modeling: CPU (MIPS), Memory, Storage, Network bandwidth
- Heterogencity: Support for heterogeneous edge server configurations
- Scaling: Designed for moderate to large-scale edge deployments
### Application Modeling
- Application Types: Mobile applications, IoT applications, compute-intensive tasks
- Task Depedencies: Task-based application modeling with offloading decisions
- Data Flow: Request-response patterns, data uplaod / download modeling
- Service Migration: Basic task offloading between edge and cloud
### Fault Tolerance
- Detailed mobility-aware fault modeling (movement and handoffs)
- Network-centric failure simulation (wirless network failures, edge connectivity issues)
- Fine-grained resource failure modeling (CPU Throttling, memory pressure)
- Real-world inspired failure patterns (based on actual deployments)
### Metrics
- **Service Time**: Total processing time at servers (pure computation time)
- **Network Delay**: Calculated using single server queue model with propagation delay based on distance
- **Task Completion Time**: End-to-end time (includes all delays)
- **Response Time**: Time from task submission to first response (excludes data download time)
- **CPU Utilization**: Instantaneous processor usage as % of total MIPS capacity
- **Server Load**: Number of concurrent tasks being processed at each server
- **Processing Capacity Usage**: Cumulative resource consumption over simulation time
- **Computational Cost**: Resource usage cost (MIPS-second consumed)
- **Energy Consumption**: Basic linear model based on CPU utilization (simplified)
- **Network Usage**: Total bytes transmitted (WLAN and WAN separately)
- **Bandwidth Consumption**: Link utilization measured against maximum capacity
- **Data Transmission Costs**: Cost per byte for upload / download operations
- **Handoff Frequency**: Number of access point changes per mobile device per time unit
- **Location-based Performance**: Performance metrics correlated with geographic positions
- **Task Failure Rate**: % of tasks that fail due to resource constraints or timeouts
- **Network Congestion Failures**: Tasks dropped due to network capacity limits
- **Service Availability**: Percentage of time services are accessible and responsive
#### Others
- **Custom Metrics**: Allowed through simulation event hooks, user-defined calculations can access device states, network conditions and application metrics
- **Output Format**: CSV export, Visual Charts (MATLAB Integration), Statistical reports (mean, median, 95th percentile)

## Technical Implementation
### Setup & Installation
- Dependencies: Java 8+, CloudSim 4.0, MATLAB
- Installation Complexity: Medium
- Platform Support: Cross-platform (via Java)
- Documentation Quality: Good (Github documentation, research papers, example scenarios)
### Programming Interface
- Configuration Method: XML configuration files + Java code for custom scenarios
- API Design: Object-oriented CloudSim-based API with modular components for edge-specific functionality
- Extensibility: Highly extensible through inheritance and interface implementation, custom mobility models, orchestration policies
- Example Scenarios: Multiple comprehensive examples including augmented reality, IoT offloading, automotive edge computing
### Performance & Scalability
- Simulation Speed: Optimized for edge computing scenarios
- Memory Usage: Efficient memory management for mobile edge scenarios
- Parallelization: Limited (single-threaded discrete event simulation)
- Large-scale Support: Supports hundereds of mobile devices and multiple edge servers
### Validation & Accuracy
- Validation Methods: Validated against theoretical models, compared with other simulators
- Accuracy Claims: Realistic modeling of MEC environments with validated networking models
- Known Limitations: Limited to discrete event simulation simplified energy modeling
- Calibration Requirements: Requires proper configuration of network and mobility parameters

---

## Assessment
### Strengths
- Specifically designed for Mobile Edge Computing scenarios
- Excellent mobility modeling capabilities
- Realistic network modeling for WLAN/WAN
- Good visualization support with MATLAB integration
- Well-documented with clear example scenarios
- Modular architecture allows easy customization
### Weaknesses
- Limited scope compared to general-purpose edge simulators
- Requires MATLAB for full visualization capabilities
- Less suitable for pure IoT or cloud computing scenarios
- Limited built-in support for modern AI/ML workloads
- Single-threaded execution limits scalability
### Best Use Cases
- Mobile Edge Computing research and evaluation
- Task offloading algorithm development
- MEC infrastructure planning and optimization
- Augmented Reality and mobile application studies
- Network performance analysis in edge scenarios
### Worst Use Cases (Avoid when)
- Pure cloud computing simulations
- Large-scale IoT deployments without mobility
- AI/ML-specific edge computing research
- Scenarios requiring massive parallel execution
- Simple proof-of-concept without networking complexity
---

## Additional Notes
No native Kubernetes support, go-to simulator for MEC research, easy to extend,
very simplified energy consumption metric