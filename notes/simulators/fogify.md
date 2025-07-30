# Fogify
## Basic Information
- **Programming Language**: Python
- **Base Framework**: Custom (Docker, Kubernetes, Linux networking)
- **First Published**: November 2020
- **Last Updated** (Access: July 2025): April 2023
> Last active was a merge of a pull request last year in January, active code change is from April 2023
- [Paper](https://ieeexplore.ieee.org/document/9355701) | [Code](https://github.com/UCY-LINC-LAB/Fogify)
- **Development Status**: Active

### Core Architecture & Design
- **Simulation Type**: Emulation (container-based, real application execution)
- **Focus**: Fog/Edge Computing, Cloud-native, Container orchestration, Network emulation
- **Design Philosophy**: Realistic, reproducible, and scalable edge/fog testbeds using containers
- **Architecture Pattern**: Modular (Declarative topology, Orchestrator, Network emulator)
- **Key Innovation / Differentiator**: Declarative scenario description, real application execution, dynamic network/resource emulation, Kubernetes integration

---

## Functional Capabilities
- **Topology Support**: Hierarchical, mesh, custom topologies (via YAML)
- **Network Types**: Ethernet, WiFi, Cellular (emulated via Linux networking)
- **Protocol Support**: All protocols supported by containers (TCP/IP, HTTP, MQTT, etc.)
- **Mobility Support**: Limited (dynamic topology changes possible, but not advanced mobility models)
- **Network Delays**: Configurable (latency, jitter, bandwidth, packet loss)
- **Bandwidth Modeling**: Configurable per link
- **Communication Patterns**: All patterns supported by real applications

### Device & Infrastructure Modeling
- **Device Types**: Edge, fog, cloud nodes (as containers/VMs)
- **Resource Modeling**: CPU, memory, storage, network limits (container-level)
- **Heterogeneity Support**: Yes (different container specs)
- **Scaling Capabilities**: Scalable to dozens/hundreds of containers (hardware-limited)
- **Hardware Abstraction**: Container/VM abstraction

### Application & Workload Modeling
- **Application Types**: Real containerized applications, microservices, IoT workloads
- **Task Dependencies**: Real application dependencies
- **Data Flow Patterns**: All real-world patterns
- **Service Migration**: Supported (container migration, scaling)
- **Workload Generation**: Real/synthetic via application logic
- **QoS Requirements**: Measured in real time

### Fault Tolerance & Reliability
- **Failure Models**: Node/link failures, resource exhaustion, network partitioning
- **Fault Detection**: Real monitoring, event triggers
- **Recovery Strategies**: Container restart, migration, scaling
- **Reliability Metrics**: Real system metrics

### Security & Privacy
- **Security Modeling**: Real security mechanisms (depends on application)
- **Privacy Mechanisms**: Application-dependent
- **Attack Simulation**: Possible (e.g., DDoS, via network emulation)
- **Security Metrics**: Real system metrics

### Energy & Sustainability
- **Energy Modeling**: Not natively supported (can be measured externally)
- **Power States**: Not modeled
- **Energy Harvesting**: Not supported
- **Carbon Footprint**: Not supported

---

## Metrics & Evaluation
- **Metric Architecture**: Application-level (real metrics from containers/applications)
- **Output Configurability**: Fully configurable (depends on application/monitoring)
- **Custom Metric Support**: Yes, via application instrumentation
- **Notes**: Real system metrics, not simulated

---

## Technical Implementation

### Setup & Deployment
- **Dependencies**: Docker, Python 3.x, Linux (best), Kubernetes (optional)
- **Installation Complexity**: Medium (requires Docker, Linux networking)
- **Platform Support**: Linux (primary), macOS (limited), Windows (WSL2)
- **Documentation Quality**: Good (docs, examples, tutorials)
- **Community Support**: Active

### Programming Interface
- **Configuration Method**: YAML scenario files, Python API
- **API Design**: Declarative (YAML), Python API
- **Extensibility**: High (custom plugins, new resource/network models)
- **Integration Capabilities**: Kubernetes, Docker, monitoring tools
- **Example Scenarios**: Several provided

### Performance & Scalability
- **Simulation Speed**: Real-time (depends on hardware)
- **Memory Efficiency**: Container-based, hardware-limited
- **Parallelization**: Multi-container, multi-host (with Kubernetes)
- **Large-scale Support**: Dozens/hundreds of containers
- **Optimization Features**: Efficient orchestration, resource isolation

### Validation & Accuracy
- **Validation Methods**: Empirical (real application behavior)
- **Accuracy Claims**: High (real system execution)
- **Benchmarking**: Yes (published studies)
- **Known Limitations**: Hardware-limited, not a pure simulator
- **Calibration Requirements**: Realistic resource/network configuration

---

## Research & Development Support

### Experimental Design
- **Scenario Management**: YAML files, reproducible deployments
- **Reproducibility**: High (declarative, container-based)
- **Statistical Analysis**: External tools (Prometheus, Grafana, etc.)
- **Visualization**: External (Grafana, dashboards)

### Data Generation & Management
- **Synthetic Data Generation**: Application-dependent
- **Real-world Data Integration**: Yes (real applications, datasets)
- **Data Pattern Support**: All (application logic)
- **Input Data**: Any (depends on application)
- **Output Data**: Real logs, metrics
- **Trace Generation**: Yes (via monitoring)
- **Data Validation**: Real system validation

---

## Assessment

### Strengths
- Realistic, reproducible edge/fog testbeds
- Container/Kubernetes integration
- Declarative scenario description
- Active development, good documentation
- Real application execution

### Weaknesses
- Hardware-limited scalability
- Not a pure simulator (no synthetic time)
- No built-in energy modeling

### Best Use Cases
- Testing real applications in edge/fog scenarios
- Network/resource emulation
- Cloud-native edge/fog research

### Worst Use Cases (Avoid when)
- Large-scale, time-accelerated simulation
- Energy-focused research (unless instrumented externally)
- Scenarios requiring synthetic time

### Maturity Assessment
- **Development Status**: Active
- **Industry Adoption**: Growing (academic/industrial)
- **Publication Impact**: Increasing
- **Future Roadmap**: Ongoing development

---

## Additional Notes
- Bridges gap between simulation and real deployment
- Excellent for DevOps, reproducibility, and cloud-native research