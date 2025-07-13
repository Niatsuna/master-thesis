# MockFog 2.0
## Basic Information
 > **Disclaimer**: MockFog 2.0 is not a simulator but an emulator! 
 > It mimicks (replica) a real system using actual hardware/software components, rather than mimics the behaivour of a real system!
- **Programming Language**: JavaScript (Node.js)
- **Base Framework**: Custom (Cloud-based emulation)
- **First Published**: September 2021
  > **MockFog 1.0**: August 2019
- **Last Updated** (Access: July 2025): June 2021
- [Paper](https://ieeexplore.ieee.org/document/9411706/) | [Code](https://github.com/MoeweX/MockFog2)
- **Development Status**: Inactive

### Core Architecture & Design
- **Simulation Type**: Cloud-based emulation (not traditional simulation)
- **Focus**: Fog Computing, Edge Computing, Real application testing
- **Design Philosophy**: Real infrastructure emulation in cloud environments to test fog applications under realistic conditions
- **Architecture Pattern**: Modular (Node Manager + Node Agent architecture)
- **Key Innovation / Differentiator**: Real cloud-based emulation with runtime network manipulation, Docker containerization, and automated experiment orchestration

---

## Functional Capabilities
- **Topology Support**: Custom topologies, Hierarchical (Cloud-Fog-Edge)
- **Network Types**: Any network type supported by cloud infrastructure
- **Protocol Support**: All protocols supported by underlying cloud infrastructure
- **Mobility Support**: Not explicitly supported (static infrastructure)
- **Network Delays**: Real network delays with runtime manipulation capabilities
- **Bandwidth Modeling**: Real bandwidth with runtime throttling and manipulation
- **Communication Patterns**: All patterns supported by real applications

### Device & Infrastructure Modeling
- **Device Types**: Cloud VMs, Edge nodes, Fog nodes, Docker containers
- **Resource Modeling**: Real CPU, Memory, Storage, Network resources with runtime limits
- **Heterogeneity Support**: Full heterogeneity through different VM types and configurations
- **Scaling Capabilities**: Limited by cloud provider quotas and budget
- **Hardware Abstraction**: Real hardware abstraction through cloud VMs

### Application & Workload Modeling
- **Application Types**: Real containerized applications, Microservices, Monolithic applications
- **Task Dependencies**: Real application dependencies supported
- **Data Flow Patterns**: All real-world data flow patterns
- **Service Migration**: Real container migration and orchestration
- **Workload Generation**: Real workload generation through application execution
- **QoS Requirements**: Real QoS measurements and constraints

### Fault Tolerance & Reliability
- **Failure Models**: Real infrastructure failures, Network failures, Container failures
- **Fault Detection**: Real monitoring and detection mechanisms
- **Recovery Strategies**: Real recovery mechanisms, Container restart, VM replacement
- **Reliability Metrics**: Real reliability measurements from actual infrastructure

### Security & Privacy
- **Security Modeling**: Real security implementations in applications
- **Privacy Mechanisms**: Real privacy implementations in applications
- **Attack Simulation**: Real attack simulation capabilities
- **Security Metrics**: Real security metrics from actual deployments

### Energy & Sustainability
- **Energy Modeling**: Real energy consumption from cloud infrastructure
- **Power States**: Real power states of cloud VMs
- **Energy Harvesting**: Not applicable (cloud-based)
- **Carbon Footprint**: Real carbon footprint from cloud provider

---

## Metrics & Evaluation
- **Metric Architecture**: Application-Level (real application metrics)
- **Output Configurability**: Highly configurable through custom applications and monitoring
- **Custom Metric Support**: Full support for custom metrics through application instrumentation
- **Notes**: Real metrics from actual application execution, not simulated

---

## Technical Implementation

### Setup & Deployment
- **Dependencies**: Node.js, Docker, AWS CLI, Cloud provider credentials
- **Installation Complexity**: Medium to Complex
- **Platform Support**: Cross-platform (requires cloud access)
- **Documentation Quality**: Good (detailed setup instructions, examples)
- **Community Support**: Inactive