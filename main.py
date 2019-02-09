import tkinter
import time
import string
from multiprocessing import Process, Queue
import queue


def start_GUI(message_queue):
    """This function starts the GUI."""
    # Global Variables
    i=0
    pod_status = {0: 'Fault', 1: 'Safe to Approach', 2: 'Ready to Launch', 3: 'Launching',
                  4: 'Coasting', 5: 'Braking', 6: 'Crawling'}

    main_window = tkinter.Tk()
    main_window.title('Cooper Union HyperLoop Monitor')

    # GUI Set-up
    main_window.geometry('580x400')

    tkinter.Label(main_window, text='Summary', font='Helvetica 10 bold').grid(row=0, column=0, columnspan=3)
    tkinter.Label(main_window, text='Pod Status').grid(row=1, sticky='w')
    tkinter.Label(main_window, text='Velocity').grid(row=2, sticky='w')
    tkinter.Label(main_window, text='cm/s').grid(row=2, column=2, sticky='w')
    tkinter.Label(main_window, text='Acceleration(Y)').grid(row=3, sticky='w')
    tkinter.Label(main_window, text='cm/s'+'\u00B2').grid(row=3, column=2, sticky='w')
    tkinter.Label(main_window, text='Position').grid(row=4, sticky='w')
    tkinter.Label(main_window, text='cm').grid(row=4, column=2, sticky='w')
    tkinter.Label(main_window, text='Pod Temperature').grid(row=5, sticky='w')
    tkinter.Label(main_window, text='\u00b0'+'C').grid(row=5, column=2, sticky='w')
    tkinter.Label(main_window, text='Battery Status', font='Helvetica 10 bold').grid(row=6, column=0, columnspan=3)
    tkinter.Label(main_window, text='Battery Voltage').grid(row=7, sticky='w')
    tkinter.Label(main_window, text='mV').grid(row=7, column=2, sticky='w')
    tkinter.Label(main_window, text='Battery Current').grid(row=8, sticky='w')
    tkinter.Label(main_window, text='mA').grid(row=8, column=2, sticky='w')
    tkinter.Label(main_window, text='Battery Temperature').grid(row=9, sticky='w')
    tkinter.Label(main_window, text='\u00b0'+'C').grid(row=9, column=2, sticky='w')
    tkinter.Label(main_window, text='Acceleration', font='Helvetica 10 bold').grid(row=6, column=3, columnspan=3)
    tkinter.Label(main_window, text='X-Acceleration').grid(row=7, column=3)
    tkinter.Label(main_window, text='cm/s'+'\u00B2').grid(row=7, column=5, sticky='w')
    tkinter.Label(main_window, text='Y-Acceleration').grid(row=8, column=3)
    tkinter.Label(main_window, text='cm/s'+'\u00B2').grid(row=8, column=5, sticky='w')
    tkinter.Label(main_window, text='Z-Acceleration').grid(row=9, column=3)
    tkinter.Label(main_window, text='cm/s'+'\u00B2').grid(row=9, column=5, sticky='w')
    tkinter.Label(main_window, text='Control Panel', font='Helvetica 10 bold').grid(row=10, column=0, columnspan=6)

    status = tkinter.StringVar()
    velocity = tkinter.StringVar()
    acceleration = tkinter.StringVar()
    position = tkinter.StringVar()
    pod_temperature = tkinter.StringVar()
    battery_voltage = tkinter.StringVar()
    battery_current = tkinter.StringVar()
    battery_temperature = tkinter.StringVar()
    x_acceleration = tkinter.StringVar()
    y_acceleration = tkinter.StringVar()
    z_acceleration = tkinter.StringVar()
    crawl_distance = tkinter.StringVar()
    crawl_direction = tkinter.StringVar()

    status_field = tkinter.Entry(main_window, textvariable=status)
    velocity_field = tkinter.Entry(main_window, textvariable=velocity)
    acceleration_field = tkinter.Entry(main_window, textvariable=acceleration)
    position_field = tkinter.Entry(main_window, textvariable=position)
    pod_temperature_field = tkinter.Entry(main_window, textvariable=pod_temperature)
    battery_voltage_field = tkinter.Entry(main_window, textvariable=battery_voltage)
    battery_current_field = tkinter.Entry(main_window, textvariable=battery_current)
    battery_temperature_field = tkinter.Entry(main_window, textvariable=battery_temperature)
    x_acceleration_field = tkinter.Entry(main_window, textvariable=x_acceleration)
    y_acceleration_field = tkinter.Entry(main_window, textvariable=y_acceleration)
    z_acceleration_field = tkinter.Entry(main_window, textvariable=z_acceleration)
    crawl_direction_field = tkinter.Entry(main_window, textvariable=crawl_direction)
    crawl_distance_field = tkinter.Entry(main_window, textvariable=crawl_distance)

    status_field.grid(row=1, column=1)
    velocity_field.grid(row=2, column=1)
    acceleration_field.grid(row=3, column=1)
    position_field.grid(row=4, column=1)
    pod_temperature_field.grid(row=5, column=1)
    battery_voltage_field.grid(row=7, column=1)
    battery_current_field.grid(row=8, column=1)
    battery_temperature_field.grid(row=9, column=1)
    x_acceleration_field.grid(row=7, column=4)
    y_acceleration_field.grid(row=8, column=4)
    z_acceleration_field.grid(row=9, column=4)
    crawl_distance_field.grid(row=17, column=3)
    crawl_direction_field.grid(row=17, column=4)

    status.set('')
    velocity.set('')
    acceleration.set('')
    position.set('')
    pod_temperature.set('')
    x_acceleration.set('')
    y_acceleration.set('')
    z_acceleration.set('')
    crawl_direction.set('')
    crawl_distance.set('')

    button_prime_run = tkinter.Button(text="PRIME_RUN", width=20)
    button_stop = tkinter.Button(text="STOP", width=20)
    button_e_stop = tkinter.Button(text="E_STOP", width=20)
    button_dump_debug = tkinter.Button(text="DUMP_DEBUG", width=20)
    button_make_safe = tkinter.Button(text="MAKE_SAFE", width=20)
    button_zero_reading = tkinter.Button(text="ZERO_READING", width=20)
    button_accelerate = tkinter.Button(text="ACCELERATE", width=20)
    button_crawl = tkinter.Button(text="CRAWL", width=20)

    button_prime_run.grid(row=12, column=0, columnspan=3)
    button_stop.grid(row=12, column=3, columnspan=3)
    button_e_stop.grid(row=13, column=0, columnspan=3)
    button_dump_debug.grid(row=13, column=3, columnspan=3)
    button_make_safe.grid(row=14, column=0, columnspan=3)
    button_zero_reading.grid(row=14, column=3, columnspan=3)
    button_accelerate.grid(row=15, column=0, columnspan=3)
    button_crawl.grid(row=16, column=0, columnspan=3)
    tkinter.Label(main_window, text='Distance (cm)').grid(row=16, column=3, sticky='w')
    tkinter.Label(main_window, text='Direction (F/R)').grid(row=16, column=4, sticky='w')

    def update_data():
        """test_status = 1 # This will be replaced by received message later...
        global i
        x_acceleration.set(str(i))
        if test_status in pod_status:
            status.set(pod_status[test_status])
        else:
            status.set('N/A')
        i = i + 1"""
        try:
            message = message_queue.get(timeout=0.1)
        except queue.Empty:
            message = ''
        if message:
            print(message)
            status.set(pod_status[int(message[1])])
            position.set(str(int.from_bytes(message[2:6], byteorder='big', signed=True)))
            velocity.set(str(int.from_bytes(message[6:10], byteorder='big', signed=True)))
            acceleration.set(str(int.from_bytes(message[10:14], byteorder='big', signed=True)))
            battery_voltage.set(str(int.from_bytes(message[14:18], byteorder='big', signed=True)))
            battery_current.set(str(int.from_bytes(message[18:22], byteorder='big', signed=True)))
            battery_temperature.set(str(int.from_bytes(message[22:26], byteorder='big', signed=True)))
            pod_temperature.set(str(int.from_bytes(message[26:30], byteorder='big', signed=True)))
        main_window.after(2000, update_data)
        return update_data
    update_data()
    main_window.mainloop()

