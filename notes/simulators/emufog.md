# EmuFog
## Basic Information
 > **Disclaimer**: EmuFog is not a simulator but an emulator! 
 > It mimicks (replica) a real system using actual hardware/software components, rather than mimics the behaivour of a real system!
- **Programming Language**: Kotlin 1.4 (JDK 11)
- **Base Framework**: Custom (MaxiNet/Mininet-based)
- **First Published**: October 2017
- **Last Updated** (Access: July 2025): September 2020
- [Paper](https://ieeexplore.ieee.org/document/8368525) | [Code](https://github.com/emufog/emufog)
- **Development Status**: Inactive

### Core Architecture & Design
- **Simulation Type**: Network emulation (not pure simulation)
- **Focus**: Fog Computing, Large-scale fog infrastructure emulation
- **Design Philosophy**: Emulation-based approach for testing fog computing applications with realistic network conditions instead of pure simulation
- **Architecture Pattern**: Modular (Graph processing, Node placement, Container orchestration)
- **Key Innovation / Differentiator**: Real network emulation using MaxiNet/Mininet, Docker container support, realistic topology integration from BRITE and CAIDA datasets

---

## Functional Capabilities
- **Topology Support**: Custom topologies from BRITE generator and real-world CAIDA datasets
- **Network Types**: All network types supported by MaxiNet/Mininet (Ethernet, WiFi emulation)
- **Protocol Support**: All protocols supported by MaxiNet/Mininet (TCP/IP, HTTP, custom protocols)
- **Mobility Support**: Static (no explicit mobility modeling)
- **Network Delays**: Realistic network delays through MaxiNet/Mininet emulation
- **Bandwidth Modeling**: Configurable bandwidth between host devices and edge nodes
- **Communication Patterns**: All patterns supported by underlying network stack

### Device & Infrastructure Modeling
- **Device Types**: Client devices (edge), Fog nodes (intermediate), Docker containers
- **Resource Modeling**: CPU shares, Memory limits, Network bandwidth, Container resource constraints
- **Heterogeneity Support**: Support for different fog node types with varying capabilities
- **Scaling Capabilities**: Large-scale support (designed for extensive fog infrastructures)
- **Hardware Abstraction**: Docker container-based abstraction with configurable resource limits

### Application & Workload Modeling
- **Application Types**: Any application that can be containerized with Docker
- **Task Dependencies**: Depends on containerized applications (not explicitly modeled)
- **Data Flow Patterns**: Realistic data flow through emulated network stack
- **Service Migration**: Not explicitly supported (depends on application implementation)
- **Workload Generation**: Configurable device scaling factors and connection patterns
- **QoS Requirements**: Latency thresholds, connection limits, resource constraints

### Fault Tolerance & Reliability
- **Failure Models**: Network-level failures through MaxiNet/Mininet
- **Fault Detection**: Depends on underlying network emulation and application implementation
- **Recovery Strategies**: Application-dependent recovery mechanisms
- **Reliability Metrics**: Network-level reliability through emulation

### Security & Privacy
- **Security Modeling**: Depends on containerized applications and network configuration
- **Privacy Mechanisms**: Application-dependent privacy mechanisms
- **Attack Simulation**: Network-level attacks possible through MaxiNet/Mininet
- **Security Metrics**: Application and network-dependent security analysis

### Energy & Sustainability
- **Energy Modeling**: Not explicitly supported
- **Power States**: Not modeled
- **Energy Harvesting**: Not supported
- **Carbon Footprint**: Not supported

---

## Metrics & Evaluation
- **Metric Architecture**: Application-Level (depends on containerized applications)
- **Output Configurability**: Depends on application logging and MaxiNet/Mininet output
- **Custom Metric Support**: Yes, through application implementation and network monitoring
- **Notes**: Metrics depend on emulated applications and network monitoring tools

---

## Technical Implementation

### Setup & Deployment
- **Dependencies**: Kotlin 1.4, JDK 11, Gradle, MaxiNet, Mininet, Docker
- **Installation Complexity**: Complex (requires MaxiNet/Mininet setup and Docker)
- **Platform Support**: Linux (primary), macOS (limited), Windows (limited)
- **Documentation Quality**: Good (comprehensive README, example configurations)
- **Community Support**: Inactive

### Programming Interface
- **Configuration Method**: YAML configuration files + command-line interface
- **API Design**: Command-line driven with YAML configuration
- **Extensibility**: Highly extensible through Docker containers and configuration
- **Integration Capabilities**: MaxiNet/Mininet integration, Docker ecosystem compatibility
- **Example Scenarios**: Comprehensive example configuration provided

### Performance & Scalability
- **Simulation Speed**: Real-time emulation performance (depends on hardware)
- **Memory Efficiency**: Efficient for emulation scenarios, depends on container resource allocation
- **Parallelization**: Distributed emulation through MaxiNet
- **Large-scale Support**: Designed for large-scale fog computing infrastructures
- **Optimization Features**: Efficient fog node placement algorithms, cost-based optimization

### Validation & Accuracy
- **Validation Methods**: Empirical validation through real network emulation
- **Accuracy Claims**: High accuracy through real network stack emulation
- **Benchmarking**: Validated against real deployments and network measurements
- **Known Limitations**: Requires significant computational resources for large-scale emulation
- **Calibration Requirements**: Proper configuration of network parameters and container resources

---
## Research & Development Support

### Experimental Design
- **Scenario Management**: YAML-based configuration management
- **Reproducibility**: Deterministic through configuration files and seed control
- **Statistical Analysis**: Depends on application implementation and monitoring tools
- **Visualization**: Depends on MaxiNet/Mininet visualization tools

### Data Generation & Management
- **Synthetic Data Generation**: Topology generation through BRITE integration
- **Real-world Data Integration**: CAIDA real-world topology datasets support
- **Data Pattern Support**: Configurable device scaling and connection patterns
- **Input Data**: YAML configuration files, BRITE topology files, CAIDA datasets
- **Output Data**: Python scripts for MaxiNet execution, application-dependent output
- **Trace Generation**: Network trace generation through MaxiNet/Mininet
- **Data Validation**: Configuration validation and topology consistency checks

---

## Assessment

### Strengths
- Real network emulation provides highly accurate results
- Docker container support enables testing of real applications
- Integration with established network emulation tools (MaxiNet/Mininet)
- Support for both synthetic (BRITE) and real-world (CAIDA) topologies
- Efficient fog node placement algorithms with cost optimization
- Scalable architecture designed for large-scale infrastructures
- Good documentation
- Cross-platform support through JVM

### Weaknesses
- High computational resource requirements for large-scale emulation
- Complex setup requiring multiple tools (MaxiNet, Mininet, Docker)
- Limited to static topologies (no mobility modeling)
- No built-in energy modeling capabilities
- Requires significant networking knowledge for proper configuration
- Emulation approach may be slower than pure simulation for some scenarios
- Limited built-in visualization and analysis tools
- Platform limitations (primarily Linux-focused)

### Best Use Cases
- Realistic fog computing application testing
- Large-scale fog infrastructure evaluation
- Network performance analysis in fog environments
- Application deployment and orchestration testing
- Research requiring high accuracy and realistic network conditions
- Scenarios where real application behavior is critical
- Performance evaluation of fog node placement algorithms

### Worst Use Cases (Avoid when)
- Quick prototyping and algorithm development (overhead too high)
- Scenarios requiring mobility modeling
- Energy-focused research and optimization
- Limited computational resources available
- Pure algorithmic research without need for realistic network conditions
- Scenarios requiring extensive built-in visualization
- Windows-primary development environments

### Maturity Assessment
- **Development Status**: Inactive development
- **Industry Adoption**: Growing adoption in academic research
- **Publication Impact**: Well-cited in fog computing emulation research
- **Future Roadmap**: No information

---

## Additional Notes
- EmuFog is an emulator rather than a pure simulator, providing more realistic results at the cost of computational complexity
- Strong integration with the Docker ecosystem enables testing of real applications
- The tool focuses on network topology generation and fog node placement optimization
- Requires expertise in network emulation and containerization technologies
- Best suited for researchers who need realistic network conditions and can afford the computational overhead