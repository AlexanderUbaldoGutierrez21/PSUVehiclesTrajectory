import pandas as pd
import matplotlib.pyplot as plt

def plot_vehicle_trajectories(file_path):
    
    # READ FILE ASSUMING TAB OR WHITESPACE DELIMETER 
    df = pd.read_csv(file_path, delim_whitespace=True, header=None)
    df.columns = ["time", "vehicle_id", "vehicle_type", "location"]
 
    # PLOT CREATION
    plt.figure(figsize=(10, 6))

    # PLOT EACH VEHICLE TRAJECTORY
    for vid, group in df.groupby("vehicle_id"):
        plt.plot(group["time"], group["location"], label=f"Veh {vid}")

    # FORMATTING
    plt.xlabel("Time (seconds)")
    plt.ylabel("Location (feet)")
    plt.title("Time-Space Diagram (Vehicle Trajectories)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(title="Vehicle ID", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "Trajectories_Data.txt"  
    plot_vehicle_trajectories(file_path)