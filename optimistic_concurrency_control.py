import threading
import time

# Assume this is the user record in the database
user = {
    'id': 1,
    'name': 'John Doe',
    'version': 1  # Version number for optimistic locking
}

def update_user_record(user_id, new_name):
    print(f"Thread {threading.current_thread().name} is attempting to update the user record.")

    # Simulate some processing time
    time.sleep(2)
    current_version = user['version']
    time.sleep(2)

    # Perform the update operation only if the version hasn't changed
    if current_version == user['version']:
        # Update the user record
        user['name'] = new_name
        user['version'] += 1

        print(f"Thread {threading.current_thread().name} has updated the user record: {user}")
    else:
        print(
            f"Thread {threading.current_thread().name} detected a conflict. The user record has been updated by another thread.")

thread1 = threading.Thread(target=update_user_record, args=(1, 'Jane Smith'))
thread2 = threading.Thread(target=update_user_record, args=(1, 'Alice Johnson'))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Print the final user record
print(f"Final user record: {user}")
