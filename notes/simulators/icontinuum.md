# iContinuum
## Basic Information
- **Programming Language**: Python
- **Base Framework**: Custom (Docker, Kubernetes, Linux networking)
- **First Published**: July 2024
- **Last Updated** (Access: July 2025): April 2024
> README.md was updated this year in March
- [Paper](https://ieeexplore.ieee.org/abstract/document/10643932) | [Code](https://github.com/disnetlab/iContinuum)
- **Development Status**: Active

### Core Architecture & Design
- **Simulation Type**: Emulation (container-based, real application execution)
- **Focus**: Cloud-to-edge continuum, orchestration, reproducibility, large-scale experimentation
- **Design Philosophy**: Realistic, reproducible, and scalable experimentation for cloud-edge-native applications
- **Architecture Pattern**: Modular (Declarative topology, Orchestrator, Resource/network emulator)
- **Key Innovation / Differentiator**: Multi-domain orchestration, reproducible experiments, continuum-wide resource management

---

## Functional Capabilities
- **Topology Support**: Hierarchical, mesh, multi-domain (cloud, edge, IoT)
- **Network Types**: Ethernet, WiFi, Cellular (emulated)
- **Protocol Support**: All protocols supported by containers
- **Mobility Support**: Limited (dynamic topology changes, but not advanced models)
- **Network Delays**: Configurable (latency, jitter, bandwidth, packet loss)
- **Bandwidth Modeling**: Configurable per link
- **Communication Patterns**: All patterns supported by real applications

### Device & Infrastructure Modeling
- **Device Types**: Cloud, edge, IoT nodes (as containers/VMs)
- **Resource Modeling**: CPU, memory, storage, network limits (container-level)
- **Heterogeneity Support**: Yes (different container specs)
- **Scaling Capabilities**: Scalable to hundreds of containers (hardware-limited)
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
- **Attack Simulation**: Possible (via network emulation)
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
- **Community Support**: Growing

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
- **Large-scale Support**: Hundreds of containers
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
- Realistic, reproducible cloud-to-edge continuum testbeds
- Multi-domain orchestration
- Declarative scenario description
- Active development, good documentation
- Real application execution

### Weaknesses
- Hardware-limited scalability
- Not a pure simulator (no synthetic time)
- No built-in energy modeling

### Best Use Cases
- Orchestration research across cloud-edge continuum
- Testing real applications in distributed scenarios
- Network/resource emulation

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
- Focuses on the continuum (cloud-edge-IoT), not just edge/fog
- Excellent for orchestration, reproducibility, and cloud-native research