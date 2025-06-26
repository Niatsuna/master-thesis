# YAFS (Yet Another Fog Simulator)
## Basic Information
- Programming Language: Python
- Base: SimPy
- First Published: July 2019
- Last Updated (Access: June 2025): June 2022
- [Paper](https://ieeexplore.ieee.org/document/8758823)
- [Github](https://github.com/acsicuib/YAFS)

### Core Architecture & Design
- Simulation Type: Discrete event simulation (SimPy-based)
- Focus: Fog Computing, IoT scenarios, Dynamic topologies, Complex Network Analysis
- Design Philosophy: Highly customizable and adaptable simulator based on Complex Network theory for dynamic fog computing environments with JSON-based configuration
- Architecture: Modular design with dynamic components
  - **Dynamic Topology Management**: Entities and network links can be created or removed during simulation runtime
  - **Dynamic Message Sources**: Sensors can generate messages from different access points throughout the simulation
  - **Complex Network Integration**: Network topology based on Complex Network theory enabling topological feature analysis
  - **NoSQL Database Storage**: Raw format results storage for flexible statistical analysis
  - **Runtime Algorithm Execution**: Placement allocation and orchestration algorithms run continuously during simulation

### Reported Use Cases
- Primary: IoT scenarios in fog computing, Dynamic resource placement, Network topology analysis
- Academic: Service placement policies, fog computing optimization, complex network analysis in distributed systems
- Industrial: Smart city applications, IoT deployments, fog-based service architectures

---

## Functional Capabilities
### Network Modeling
- Topology Support: Dynamic multi-tier topologies based on Complex Network theory, hierarchical fog architectures
- Network Types: Fog networks, IoT wireless networks, backbone connections
- Mobility Support: Advanced mobility modeling with GPX trace support, dynamic endpoint movement
- Network Delays: Complex network-based delay modeling with topological considerations
### Device & Resource Modeling
- Device Types: IoT sensors, Fog nodes, Cloud servers, Mobile endpoints, Network gateways
- Resource Modeling: CPU, Memory, Storage, Network bandwidth, Custom resource attributes
- Heterogeneity: Full support for heterogeneous fog node configurations
- Scaling: Designed for large-scale IoT and fog deployments
### Application Modeling
- Application Types: IoT applications, Fog services, Distributed applications, Mobile applications
- Task Dependencies: Complex application workflows with service dependencies
- Data Flow: Message-based communication, sensor data streams, request-response patterns
- Service Migration: Dynamic service migration with placement optimization algorithms
### Fault Tolerance
- Dynamic topology changes during runtime (node failures, network partitions)
- Service migration during failures
- Network link failures and recovery
- Custom failure modeling through event-driven mechanisms
### Metrics
- **Service Response Time**: End-to-end time from request initiation to response completion
- **Network Transmission Delay**: Time for data transmission across fog network tiers
- **Service Placement Efficiency**: Optimization metrics for service allocation decisions
- **Resource Utilization**: CPU, memory, and network resource usage across fog nodes
- **Network Topology Metrics**: Complex network centrality measures, clustering coefficients, path lengths
- **Service Migration Overhead**: Cost and time associated with dynamic service migrations
- **Message Transmission Statistics**: Volume and patterns of IoT message flows
- **Geographic Performance**: Location-based performance metrics for mobile scenarios
- **Service Availability**: Uptime and accessibility metrics for fog services
- **Dynamic Workload Metrics**: Performance under varying IoT workload conditions
- **Energy Consumption**: Basic energy modeling for fog nodes and IoT devices
- **Network Congestion**: Utilization and congestion metrics across network links
- **Service Discovery Time**: Time for service location and binding in dynamic topologies
- **Handoff Performance**: Metrics for mobile endpoint transitions between fog nodes
- **Complex Network Indicators**: Betweenness centrality, closeness centrality, degree distribution

#### Others
- **Custom Metrics**: Extensible through Python event hooks and custom analysis functions
- **Output Format**: NoSQL database (raw format), CSV export, JSON results, statistical summaries, network visualization support

## Technical Implementation
### Setup & Installation
- Dependencies: Python 3.6+, SimPy, NetworkX, geopy (for mobility), NoSQL database
- Installation Complexity: Medium (pip-based installation, multiple dependencies)
- Platform Support: Cross-platform (Python-based)
- Documentation Quality: Excellent (comprehensive documentation, tutorials, user guide, API reference)
### Programming Interface
- Configuration Method: JSON-based configuration files + Python scripting for custom scenarios
- API Design: Object-oriented Python API with modular components, event-driven architecture
- Extensibility: Highly extensible through Python inheritance, custom placement algorithms, orchestration policies
- Example Scenarios: Rich set of examples (basic, service movement, topology changes, user movement, dynamic workloads)
### Performance & Scalability
- Simulation Speed: Optimized for dynamic fog computing scenarios
- Memory Usage: Efficient memory management with NoSQL storage
- Parallelization: Single-threaded discrete event simulation
- Large-scale Support: Supports hundreds of IoT devices and multiple fog nodes
### Validation & Accuracy
- Validation Methods: Validated against theoretical models, published in peer-reviewed journals
- Accuracy Claims: Realistic modeling of fog computing environments with complex network theory integration
- Known Limitations: Single-threaded execution, discrete event simulation constraints
- Calibration Requirements: Requires proper JSON configuration and network topology parameters

---

## Assessment
### Strengths
- **Unique Complex Network Integration**: Only simulator leveraging complex network theory for topology analysis
- **Dynamic Topology Support**: Runtime creation/removal of network entities and links
- **Excellent Documentation**: Comprehensive tutorials, examples, and API documentation
- **JSON-based Configuration**: User-friendly configuration without deep programming knowledge
- **Flexible Architecture**: Highly customizable through Python scripting
- **Academic Foundation**: Strong research backing with multiple publications
- **Mobility Support**: Advanced mobility modeling with GPX trace integration
- **NoSQL Storage**: Flexible result storage for statistical analysis
- **Open Source**: MIT license with active community support

### Weaknesses
- **Limited AI/ML Support**: No built-in support for modern AI workloads or machine learning models
- **Single-threaded**: No parallel execution capabilities
- **Python Performance**: May be slower than Java-based simulators for large-scale scenarios
- **Complexity**: Requires understanding of complex network theory for full utilization
- **Limited Energy Modeling**: Basic energy consumption modeling
- **Dependency Heavy**: Multiple Python dependencies required for full functionality

### Best Use Cases
- IoT scenarios requiring dynamic topology changes
- Fog computing research with complex network analysis
- Service placement algorithm development and evaluation
- Mobile fog computing with mobility requirements
- Research requiring topological feature analysis
- Dynamic workload scenarios with runtime changes
- Academic research in fog computing architectures

### Worst Use Cases (Avoid when)
- Pure cloud computing simulations without fog components
- AI/ML-specific edge computing research
- Real-time simulation requirements
- Massive parallel processing needs
- Simple static topology scenarios
- Performance-critical simulations requiring high execution speed
- Scenarios not requiring complex network analysis

---

## Additional Notes
No native Kubernetes support, unique complex network theory integration, excellent for research but limited for AI/ML workloads, very flexible configuration through JSON