# MockFog 2.0
## Basic Information
 > **Disclaimer**: MockFog 2.0 is not a simulator but an emulator! 
 > It mimicks (replica) a real system using actual hardware/software components, rather than mimics the behaivour of a real system!
- **Programming Language**: JavaScript (Node.js)
- **Base Framework**: Custom (Cloud-based emulation)
- **First Published**: September 2021
  > **MockFog 1.0**: August 2019
- **Last Updated** (Access: July 2025): June 2019
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
- **Community Support**: Active (maintained by TU Berlin)

### Programming Interface
- **Configuration Method**: JSON configuration files, CLI interface
- **API Design**: RESTful API for Node Agent, CLI for Node Manager
- **Extensibility**: Highly extensible through custom applications and configurations
- **Integration Capabilities**: Full integration with Docker, AWS, monitoring tools
- **Example Scenarios**: Multiple examples with different application types

### Performance & Scalability
- **Simulation Speed**: Real-time execution (not simulation speed)
- **Memory Efficiency**: Real memory usage from cloud infrastructure
- **Parallelization**: Real parallelization through cloud infrastructure
- **Large-scale Support**: Limited by cloud provider quotas and budget
- **Optimization Features**: Real optimization through cloud auto-scaling

### Validation & Accuracy
- **Validation Methods**: Real-world validation (not simulation validation)
- **Accuracy Claims**: 100% accuracy as it uses real infrastructure
- **Benchmarking**: Real benchmarking capabilities
- **Known Limitations**: Cost limitations, Cloud provider dependency, Setup complexity
- **Calibration Requirements**: Cloud provider configuration, Network setup

---
## Research & Development Support

### Experimental Design
- **Scenario Management**: JSON-based configuration, Automated experiment orchestration
- **Reproducibility**: High reproducibility through deterministic configurations
- **Statistical Analysis**: External analysis required, Raw data collection
- **Visualization**: Integration with external visualization tools

### Data Generation & Management
- **Synthetic Data Generation**: Through real application execution
- **Real-world Data Integration**: Full support for real-world data
- **Data Pattern Support**: All patterns supported through real applications
- **Input Data**: JSON configuration files, Docker images, Application code
- **Output Data**: Log files, Application-specific output, Monitoring data
- **Trace Generation**: Real trace generation from actual execution
- **Data Validation**: Real-world data validation through application execution

---

## Assessment

### Strengths
- **Real infrastructure emulation** provides 100% accuracy
- **Runtime network manipulation** allows dynamic testing scenarios
- **Docker containerization** supports modern application architectures
- **Automated experiment orchestration** reduces manual effort
- **Cloud-based scaling** allows testing at realistic scales
- **Full application lifecycle management** from deployment to results collection
- **Comprehensive documentation** and examples

### Weaknesses
- **High cost** due to cloud infrastructure usage
- **Complex setup** requiring cloud expertise
- **Limited by cloud provider** capabilities and quotas
- **Not suitable for large-scale theoretical studies** due to cost
- **Requires real applications** - cannot test theoretical algorithms easily
- **Network dependency** on cloud provider infrastructure
- **Limited mobility support** compared to traditional simulators
- **Steep learning curve** for cloud infrastructure management

### Best Use Cases
- **Real application testing** in fog environments
- **Performance validation** of fog applications
- **Infrastructure capacity planning** with real workloads
- **Prototype validation** before production deployment
- **Algorithm validation** with real network conditions
- **Industrial research** with budget for cloud resources
- **Comparative studies** requiring realistic conditions

### Worst Use Cases (Avoid when)
- **Large-scale theoretical studies** due to cost constraints
- **Algorithm development** in early stages
- **Educational purposes** with limited budgets
- **Purely analytical research** not requiring real infrastructure
- **Scenarios requiring mobility modeling**
- **Studies requiring thousands of nodes** due to cost
- **Research requiring custom hardware modeling**

### Maturity Assessment
- **Development Status**: Inactive development
- **Industry Adoption**: Growing adoption in research and industry
- **Publication Impact**: Well-cited in fog computing research
- **Future Roadmap**: Continuous development with new features planned

---

## Additional Notes
- **Unique approach**: Only cloud-based emulation platform in the comparison
- **Cost consideration**: Requires careful budget planning for experiments
- **Real-world applicability**: Highest real-world applicability among simulators
- **Infrastructure agnostic**: Can work with different cloud providers
- **Experiment automation**: Advanced automation capabilities for complex experiments
- **Multi-stage development**: Supports different complexity levels (Stage 1-4)
- **No traditional simulation**: Focus on emulation rather than simulation