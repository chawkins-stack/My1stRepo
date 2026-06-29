# List Initialization
task_list = ["Database Setup", "UI Design", "API Integration", "Security Audit"]

# Print the original list
print(task_list)

# Task update: change second item
task_list[1] = "Frontend Framework"

# Add "Beta Testing" to the very end of the list
task_list.append("Beta Testing")

# Insert "Critical Hotfix" at the very front of the list
task_list.insert(0, "Critical Hotfix")

# Extract the first task and store it in completed_task
completed_task = task_list.pop(0)

# Remove "Security Audit" from the list
task_list.remove("Security Audit")

# Sort the list in reverse alphabetical order (in place)
task_list.sort(reverse=True)

# Safe search-and-destroy for "API Integration"
if "API Integration" in task_list:
    print("API Integration found — removing it")
    task_list.remove("API Integration")
else:
    print("API Integration not found — skipping removal")

# Final outputs
print("Final task list:", task_list)
print("Completed task:", completed_task)