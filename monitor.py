import psutil
import matplotlib.pyplot as plt
# Lists to store CPU, RAM, and Disk Usage
cpu_values, ram_values, disk_values = [], [], []
high_cpu_count = 0  # Counter for high CPU usage duration

plt.ion()  # Enable interactive mode for real-time graph updates

# Run for 30 seconds
for _ in range(30):
    cpu = psutil.cpu_percent(interval=0)
    ram = psutil.virtual_memory().percent  # Get RAM usage
    disk = psutil.disk_usage('/').percent  # Get Disk usage

    # Store only last 100 values (to prevent memory overflow)
    cpu_values = cpu_values[-99:] + [cpu]
    ram_values = ram_values[-99:] + [ram]
    disk_values = disk_values[-99:] + [disk]

    # **Graph Update**
    plt.clf()
    plt.plot(cpu_values, label="CPU Usage (%)", color='r')
    plt.plot(ram_values, label="RAM Usage (%)", color='g')
    plt.plot(disk_values, label="Disk Usage (%)", color='b')

    # **Show Latest Value as Text on Graph**
    if cpu_values:
        plt.text(
            len(cpu_values) - 1,
            cpu_values[-1],
            f"{cpu_values[-1]}%",
            color='r',
            fontsize=10,
            ha='right'
        )

    if ram_values:
        plt.text(
            len(ram_values) - 1,
            ram_values[-1],
            f"{ram_values[-1]}%",
            color='g',
            fontsize=10,
            ha='right'
        )

    if disk_values:
        plt.text(
            len(disk_values) - 1,
            disk_values[-1],
            f"{disk_values[-1]}%",
            color='b',
            fontsize=10,
            ha='right'
        )
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Usage (%)")
    plt.title("System Performance Monitor")
    plt.pause(1)  # Pause for smooth updates

# Save the Final Graph as an Image
plt.ioff()  # Disable interactive mode
plt.savefig("performance_report.png")  # Save the graph as an image
plt.show()  # Show the final graph

print("✅Performance graph saved as 'performance_report.png'")
