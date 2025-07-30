# Requirements Catalogue

## General Requirements
### Overview
- Good and comprehensive documentation and tutorials
- Multiple, ready-to-use example scenarios
- High configurable implementation with configuration based on one or multiple config files
- Extensibile (e.g. due to being modular)

### Mandatory
- **Topology**:
  - Support for both hierachical (cloud-fog-edge-device) and flexible/custom topologies
- **Network**:
  - Support for multiple network and protocol types
  - Configurable network characteristics (Latency, Jitter, Bandwidth, packet loss, ...)
- **Mobility**:
  - Support for dynamic topology changes (Minimum)
- **Device & Resources**:
  - Real or abstract device representation with detailed and heterogenerous device and resource modeling
  - Configureable resource constraints per node
- **Application & Workload**:
  - Support for both synthetic and real workloads, ability to run real applications and/or simulate workloads
  - Support for different data flow patterns
- **Data Generation & Integration**:
  - Support for synthetic workload generation and real-world trace integration
  - Flexible input/output data handling
  - Trace/Log generation and export
- **Fault Tolerance & Reliability**:
  - Configurable failure models
  - Recovery strategies (restart, migration, scaling)
  - Reliability metrics
- **Energy & Sustainability**:
  - Device-level energy modeling
  - Energy consumption metrics
- **Metrics & Evaluation**:
  - Customizable, comprehensive metrics on application-level
  - Real-time monitoring and export
  - Support for benchmarking and validation
- **Scalability**:
  - Support for moderatoe to large-scale scenarios (minimum)
  - Efficient resource usage and parallelization
- **Scenario Management & Reproducibility**:
  - Scenario saving/loading and deterministic execution
  - Versionable, declarative scenario files for reproducibility
- **Validation & Accuracy**:
  - Support for benchmarking and empirical validation
  - Transparent accuracy claims and known limitations
- **Usability & User Interface**:
  - Intuitive configuration (YAML, GUI, ...)
  - Good error handling and feedback
  - Integration with external tools (e.g., monitoring, orchestration, data analytics, visualization dashboards)

### Optional, Recommended, Focus-based Mandatory
- **Mobility**:
  - Advanced Mobility modeling is required if the focus lies on mobile applications
  - Highly recommended
- **Security & Privacy**:
  - Support for security modeling is optional or mandatory based on concerns and focus
  - If present:
    - At least basic, ideally extensible
      - Extensible security/privacy modeling to allow for new attack/defense scenarios
    - Ability to simulate or implement attacks
    - Privacy mechanisms (optional, application-dependent)

- Support for SDN integration or programmable networking (recommended for advanced scenarios)
- Support Cloud-Native / DevOps integration via containerization, Kubernetes and DevOps workflows (recommended for newer simulators (Trend))
- Support for continuum-wide orchestration and resource management (recommended for advanced and future-proof simulators)
