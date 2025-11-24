import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuration
FILE_MAPPING = {
    'Edge': {
        'cpu': 'edge-cpu-utilization.csv',
        'ttft': 'edge-ttft-p95.csv',
        'throughput': 'edge-throughput-tokens-per-second.csv'
    },
    'Cloud (CPU)': {
        'cpu': 'cloud-cpu-cpu-utilization.csv',
        'ttft': 'cloud-cpu-ttft-p95.csv',
        'throughput': 'cloud-cpu-throughput-tokens-per-second.csv'
    },
    'Cloud (GPU)': {
        'cpu': 'cloud-gpu-cpu-utilization.csv',
        'ttft': 'cloud-gpu-ttft-p95.csv',
        'throughput': 'cloud-gpu-throughput-tokens-per-second.csv'
    }
}

COLORS = {
    'Edge': '#2E86AB',
    'Cloud (CPU)': '#A23B72',
    'Cloud (GPU)': '#F18F01'
}

# Read all data files
data = {device: {} for device in FILE_MAPPING.keys()}

for device_type, files in FILE_MAPPING.items():
    for metric_type, filename in files.items():
        try:
            df = pd.read_csv(filename)
            # Assume the first column is the metric value
            data[device_type][metric_type] = df.iloc[:, 0].values
            print(f"✓ Loaded {filename}: {len(df)} rows")
        except FileNotFoundError:
            print(f"✗ Error: {filename} not found")
            exit(1)
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
            exit(1)

# Get the length of data (should be 1800 for 30 minutes)
data_length = len(data['Edge']['cpu'])
time_minutes = np.arange(data_length) / 60

# Metric configurations
metrics = [
    {
        'key': 'cpu',
        'title': 'CPU Utilization Over Time',
        'ylabel': 'CPU Utilization (%)',
        'filename': 'cpu_utilization_comparison.png'
    },
    {
        'key': 'ttft',
        'title': 'Time To First Token (TTFT) - P95',
        'ylabel': 'TTFT (seconds)',
        'filename': 'ttft_comparison.png'
    },
    {
        'key': 'throughput',
        'title': 'Throughput (Tokens Per Second)',
        'ylabel': 'Tokens/Second',
        'filename': 'throughput_comparison.png'
    }
]

# Plot and save each metric separately
saved_files = []

for metric in metrics:
    # Create a new figure for each metric
    fig, ax = plt.subplots(figsize=(10, 6))
    
    key = metric['key']
    
    # Plot data for each device type
    for device_type in FILE_MAPPING.keys():
        if key in data[device_type]:
            values = data[device_type][key]
            
            ax.plot(time_minutes, values, 
                   label=device_type, 
                   color=COLORS[device_type],
                   linewidth=2,
                   alpha=0.85)
    
    # Styling
    ax.set_xlabel('Time (minutes)', fontsize=12, fontweight='bold')
    ax.set_ylabel(metric['ylabel'], fontsize=12, fontweight='bold')
    ax.set_title(metric['title'], fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), 
             ncol=3, framealpha=0.95, fontsize=11, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.set_xlim(0, 30)
    
    # Add subtle background color
    ax.set_facecolor('#f8f9fa')
    
    # Tight layout
    plt.tight_layout()
    
    # Save the figure
    output_filename = metric['filename']
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', facecolor='white')
    saved_files.append(output_filename)
    print(f"✓ Saved: {output_filename}")
    
    # Close the figure to free memory
    plt.close(fig)

print(f"\n{'='*60}")
print(f"All graphs saved successfully!")
print(f"{'='*60}")

# Display summary statistics
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)

for metric in metrics:
    key = metric['key']
    print(f"\n{metric['title']}:")
    print("-" * 60)
    
    for device_type in FILE_MAPPING.keys():
        if key in data[device_type]:
            values = data[device_type][key]
            mean_val = np.mean(values)
            std_val = np.std(values)
            min_val = np.min(values)
            max_val = np.max(values)
            
            print(f"{device_type:20s} | Mean: {mean_val:8.2f} | Std: {std_val:8.2f} | Min: {min_val:8.2f} | Max: {max_val:8.2f}")