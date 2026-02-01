stations = {
    "Cutting": 12.4,
    "Welding": 18.9,
    "Assembly": 22.1
}
bottleneck_time = max(stations.values())
print("Bottleneck Cycle Time:", bottleneck_time, "seconds")

# Expected output: Bottleneck Cycle Time: 22.1 seconds