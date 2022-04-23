from tkinter import END, NONE, messagebox

from matplotlib.ft2font import HORIZONTAL
from loader import DataLoader
from functools import partial

import tkinter as tk
import threading
import KCenter
import shortestPath

path_dictionary = {}
data = []

#flags
is_data_set_valid = False


def switch_to_output():
    #globals
    global operation_frame
    global output_frame
    createOutputFrame(output_frame)
    output_frame.pack(fill='both', expand=1)
    operation_frame.forget()


def switch_to_operation():
    #globals
    global operation_frame
    global output_frame
    operation_frame.pack(fill='both', expand=1)
    output_frame.forget()


def getShortestPath(cluster_dictionary, key, lock):
    pathObject = shortestPath.pathFinder()
    graph = pathObject.graphGenerator(cluster_dictionary[key])
    distance, pathIndices = pathObject.pathGenerator(graph)
    lock.acquire()
    path_dictionary[key] = (distance, pathIndices)
    lock.release()


def printOutput(cluster_dictionary, key):
    print(f"\nDistance: {path_dictionary[key][0]}")
    print("new path:")
    for index in path_dictionary[key][1]:
        print(cluster_dictionary[key][index].name)


def outputString(cluster_dictionary, key):
    res = "Path x: "
    for index in path_dictionary[key][1]:
        res += cluster_dictionary[key][index].name
        res += ", "
    res+="\n"
    return res


def loadDataCallback(data_label_text, cluster_validity_text):
    #globals
    global data
    global is_data_set_valid
    #Get data from database/test file
    loader = DataLoader()
    data = loader.getData("in.csv")
    is_data_set_valid = True
    data_label_text.set("Data has been loaded successfully.")
    cluster_validity_text.set("Clustering can now be carried out.")


def clusterCallback(current_value, clustering_slider, cluster_result_text):
    #globals
    global data
    global clusters
    global keys
    global is_data_set_valid
    #check if there is valid data to cluster
    if is_data_set_valid == False:
        messagebox.showinfo("No Data", "No valid data to cluster.")
        pass
    #initial clustering class
    clusterer = KCenter.cluster()

    #calculate the optimal centers
    clusters = clusterer.kCenter(data, int(current_value.get()))

    keys = list(clusters.keys())

    cluster_result_text.set(f"{len(keys)} clusters created.")


def shortestPathCallback(path_result_text):
    output_lock = threading.Lock()

    threadList = []
    for key in keys:
        t = threading.Thread(target=getShortestPath, args=(clusters, key, output_lock, ))
        threadList.append(t)
        t.start()

    for t in threadList:
        t.join()

    path_keys = list(path_dictionary.keys())

    for key in path_keys:
        printOutput(clusters, key)

    print("\nOutput Complete")

    path_result_text.set("All shortest paths calculated.")


def createOperationFrame(f):
    data_label_text = tk.StringVar()
    data_label_text.set("Data has not been loaded.")
    data_loading_label = tk.Label(f, textvariable=data_label_text).grid(row=1, column=1, padx=10, pady=10)

    cluster_validity_text = tk.StringVar()
    cluster_validity_text.set("No valid data set to cluster.")
    cluster_validity_label = tk.Label(f, textvariable=cluster_validity_text).grid(row=3, column=0, padx=10, pady=5)

    clustering_slider = tk.Scale(f, from_= 1, to=50, orient="horizontal", variable=current_value).grid(row=2, column=0, padx=10, pady=10)

    cluster_result_text = tk.StringVar()
    cluster_result_text.set("Clustering not carried out yet.")
    cluster_result_label = tk.Label(f, textvariable=cluster_result_text).grid(row=4, column=1, padx=10, pady=10)

    path_result_text = tk.StringVar()
    path_result_text.set("Shortest Paths not calculated.")
    path_result_label = tk.Label(f, textvariable=path_result_text).grid(row=5, column=1, padx=10, pady=10)
    
    data_loading_button = tk.Button(f, text = "Load Data", command = partial(loadDataCallback, data_label_text, cluster_validity_text)).grid(row = 1, column = 0, sticky = "W", padx = 10, pady = 10)
    cluster_button = tk.Button(f, text = "Cluster Nodes", command = partial(clusterCallback, current_value, clustering_slider, cluster_result_text)).grid(row = 4, column = 0, sticky = "W", padx = 10, pady = 10)
    calc_path_button = tk.Button(f, text = "Calculate Shortest Paths", command = partial(shortestPathCallback, path_result_text)).grid(row = 5, column = 0, sticky = "W", padx = 10, pady = 10)
    output_screen_button = tk.Button(f, text = "Go to Output Screen", command = switch_to_output).grid(row = 6, column = 3, sticky="E", padx = 10, pady = 10)

def createOutputFrame(f):
    v = tk.Scrollbar(f)
    v.grid(row = 0, column = 1, sticky="E", padx = 10, pady = 10)
    textBody = tk.Text(f, width = 60, height = 15, wrap = NONE, yscrollcommand = v.set)
    path_keys = list(path_dictionary.keys())

    for key in path_keys:
        textBody.insert(END, outputString(clusters, key))
    
    textBody.grid(row = 0, column = 0, sticky = "W", padx = 10, pady = 10)
    operation_screen_button = tk.Button(f, text = "Go to operation screen", command = switch_to_operation).grid(row = 6, column = 0, sticky = "W", padx = 10, pady = 10)


window = tk.Tk()
window.geometry('600x300')

operation_frame = tk.Frame(window)
output_frame = tk.Frame(window)

current_value=tk.DoubleVar()

createOperationFrame(operation_frame)
createOutputFrame(output_frame)

operation_frame.pack(fill='both', expand = 1)

window.mainloop()