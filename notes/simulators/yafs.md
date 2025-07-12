# YAFS (Yet Another Fog Simulator)
## Basic Information
- **Programming Language**: Python 2.7
- **Base Framework**: SimPy (discrete event simulator)
- **First Published**: July 2019
- **Last Updated** (Access: July 2025): June 2022
- [Paper](https://ieeexplore.ieee.org/document/8758823) | [Code](https://github.com/acsicuib/YAFS)
- **Development Status**: Inactive

### Core Architecture & Design
- **Simulation Type**: Discrete event simulation
- **Focus**: IoT, Fog Computing, Edge Computing, Resource allocation
- **Design Philosophy**: Lightweight, robust and highly configurable simulator based on Complex Network theory with minimal class structure (only 7 classes)
- **Architecture Pattern**: Modular with minimal class architecture for low learning curve
- **Key Innovation / Differentiator**: Complex Network theory integration for topology modeling, dynamic control of all processes, customized distribution support

---

## Functional Capabilities
- **Topology Support**: Complex Networks theory-based modeling (any topology possible)
- **Network Types**: Generic network modeling through Complex Networks
- **Protocol Support**: Generic protocol abstraction
- **Mobility Support**: Dynamic topology changes, node mobility through topology evolution
- **Network Delays**: Configurable network delays through link properties
- **Bandwidth Modeling**: Configurable bandwidth through link attributes
- **Communication Patterns**: Customizable routing through selection algorithms

### Device & Infrastructure Modeling
- **Device Types**: Generic nodes (network devices, cloud abstractions, software modules, workloads)
- **Resource Modeling**: Configurable resource modeling through node attributes
- **Heterogeneity Support**: Full heterogeneity support through node properties
- **Scaling Capabilities**: Scalable through Complex Networks theory
- **Hardware Abstraction**: Generic hardware abstraction through node modeling

### Application & Workload Modeling
- **Application Types**: Generic application modeling, IoT applications, fog services
- **Task Dependencies**: Configurable through application module dependencies
- **Data Flow Patterns**: Customizable data flow through selection algorithms
- **Service Migration**: Dynamic service placement through placement algorithms
- **Workload Generation**: Customizable distributions including timestamp arrays
- **QoS Requirements**: Configurable QoS through custom policies

### Fault Tolerance & Reliability
- **Failure Models**: Link failures, node failures through dynamic topology control
- **Fault Detection**: Event-based detection through simulation events
- **Recovery Strategies**: Configurable through custom policies
- **Reliability Metrics**: Accessible through raw event data

### Security & Privacy
- **Security Modeling**: Not explicitly supported
- **Privacy Mechanisms**: Not explicitly supported
- **Attack Simulation**: Not explicitly supported
- **Security Metrics**: Not explicitly supported

### Energy & Sustainability
- **Energy Modeling**: Not explicitly supported
- **Power States**: Not explicitly supported
- **Energy Harvesting**: Not explicitly supported
- **Carbon Footprint**: Not explicitly supported

---

## Metrics & Evaluation
- **Metric Architecture**: Simulator-Level (raw event data accessible from any point)
- **Output Configurability**: Highly configurable (raw event data format)
- **Custom Metric Support**: Yes, full access to all simulation events and data
- **Notes**: No hidden variables, complete transparency of simulation data

---

## Technical Implementation

### Setup & Deployment
- **Dependencies**: Python 2.7, SimPy, NetworkX, other Python libraries
- **Installation Complexity**: Easy (manual download and installation)
- **Platform Support**: Cross-platform (Python-based)
- **Documentation Quality**: Good (tutorial, architecture details, examples, API reference)
- **Community Support**: Limited (inactive development)

### Programming Interface
- **Configuration Method**: Pure Python programming
- **API Design**: Object-oriented with minimal class structure (7 classes)
- **Extensibility**: Highly extensible through custom policies and algorithms
- **Integration Capabilities**: Python ecosystem integration
- **Example Scenarios**: Multiple examples provided

### Performance & Scalability
- **Simulation Speed**: Efficient discrete event simulation
- **Memory Efficiency**: Lightweight design
- **Parallelization**: Single-threaded (SimPy limitation)
- **Large-scale Support**: Scalable through Complex Networks
- **Optimization Features**: Raw event access for optimization

### Validation & Accuracy
- **Validation Methods**: Comparative studies with iFogSim
- **Accuracy Claims**: Validated against other simulators
- **Benchmarking**: Performance comparison studies available
- **Known Limitations**: Python 2.7 dependency, single-threaded execution
- **Calibration Requirements**: Manual configuration of network and resource parameters

---
## Research & Development Support

### Experimental Design
- **Scenario Management**: Python-based scenario configuration
- **Reproducibility**: Deterministic execution through SimPy
- **Statistical Analysis**: Raw data access for custom analysis
- **Visualization**: Custom visualization through Python libraries

### Data Generation & Management
- **Synthetic Data Generation**: Customizable distributions, timestamp arrays
- **Real-world Data Integration**: Python-based data integration capabilities
- **Data Pattern Support**: Customizable patterns through distributions
- **Input Data**: Python configuration, custom data formats
- **Output Data**: Raw event data format
- **Trace Generation**: Custom trace generation capabilities
- **Data Validation**: Python-based validation

---

## Assessment

### Strengths
- Extremely lightweight and simple architecture (only 7 classes)
- Complex Network theory integration for advanced topology modeling
- Highly configurable and extensible
- Full transparency of simulation data
- Low learning curve
- Dynamic control of all simulation aspects
- Strong theoretical foundation with Complex Networks
- Python ecosystem integration

### Weaknesses
- Limited to Python 2.7 (deprecated Python version)
- Inactive development
- No built-in energy modeling
- No security or privacy features
- Limited documentation compared to larger simulators
- Requires significant programming knowledge
- No GUI or visual configuration tools
- Single-threaded execution

### Best Use Cases
- Research requiring custom algorithms and policies
- Complex network topology analysis
- Fog computing resource allocation studies
- Scenarios requiring high customization
- Academic research with programming focus
- Prototype development for new fog computing concepts

### Worst Use Cases (Avoid when)
- Production or commercial environments
- Large-scale parallel simulations
- Energy-focused studies
- Security-focused research
- GUI-based simulation requirements
- Modern Python 3.x development environments
- Scenarios requiring extensive built-in features

### Maturity Assessment
- **Development Status**: Inactive
- **Industry Adoption**: Limited academic adoption
- **Publication Impact**: Moderate citation impact
- **Future Roadmap**: No apparent future development

---

## Additional Notes
- Based on SimPy discrete event simulation framework
- Emphasizes simplicity and customization over built-in features
- Requires Python 2.7 which limits modern adoption
- Strong theoretical foundation but limited practical features
- Excellent for researchers who prefer building from scratch