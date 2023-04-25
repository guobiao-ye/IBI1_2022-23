# The class triathlon:
class triathlon:
    # Construct attributes in the class
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.fn = first_name
        self.ln = last_name
        self.l = location
        self.st = swim_time
        self.ct = cycle_time
        self.rt = run_time
        # Caculate the total time
        self.total_time = swim_time + cycle_time + run_time
    # Print all these details in a single line
    def print_information(self):
        print(f"name: {self.fn} {self.ln} \ location: {self.l} \ swim time: {self.st}s, cycle time: {self.ct}s, run time: {self.rt}s \ total time: {self.total_time}s")



# An example of using this class:
# Save the information (do not need to save the total time) in athlete1
athlete1 = triathlon("John", "Doe", "Los Angeles", 1800, 4000, 2500)
# Call the function within the class to print all these details (include the total time) in a single line
athlete1.print_information()