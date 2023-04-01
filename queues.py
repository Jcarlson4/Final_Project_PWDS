import queue

q = queue.Queue()

attendance_queue = []

attendance_queue.append("Sally Adams")
attendance_queue.append("Bucky Stan")
attendance_queue.append("Jeremiah Carlson")

print(attendance_queue)


attendance_queue.pop()

print(attendance_queue)



#students = ["Sally Adams", "Jeremiah Carlson", "Sally Monroe", "Dakota Pannell", "Xavier Vasquez"]

#for student in students:
    #q.put(students)

#print(q.get())


reservations = []

reservations.append('person01')
reservations.append('person02')
reservations.append('person03')
reservations.append('person04')
reservations.append('person05')
reservations.append('person06')
reservations.append('person07')
reservations.append('person08')
reservations.append('person09')
reservations.append('person10')

print(reservations)

reservations.pop(4)

print(reservations)