import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    try:
        voltage_values = list(map(float, entry_voltage.get().split(',')))
        current_values = list(map(float, entry_current.get().split(',')))

        plt.figure(figsize=(6, 4))
        plt.plot(voltage_values, current_values, marker='o', linestyle='-', color='b')
        plt.title('Alternating Voltage vs Current')
        plt.xlabel('Voltage')
        plt.ylabel('Current')

        # Embed the plot into the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        status_label.config(text="Please enter comma-separated numerical values")

root = tk.Tk()
root.title("Alternating Voltage vs Current Graph")

# Entry for voltage values
label_voltage = tk.Label(root, text="Enter Voltage Values (comma-separated):")
label_voltage.pack()
entry_voltage = tk.Entry(root)
entry_voltage.pack()

# Entry for current values
label_current = tk.Label(root, text="Enter Current Values (comma-separated):")
label_current.pack()
entry_current = tk.Entry(root)
entry_current.pack()

# Button to plot the graph
plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
