import tkinter
import time
import string


if __name__ == '__main__':
    #Global Variables
    i=0
    pod_status = {0: 'Fault', 1: 'Safe to Approach', 2: 'Ready to Launch', 3: 'Launching',
                  4: 'Coasting', 5: 'Braking', 6: 'Crawling'}


    main_window = tkinter.Tk()
    main_window.title('Cooper Union HyperLoop Monitor')

    #GUI Set-up
    main_window.geometry('550x250')

    tkinter.Label(main_window, text='Summary', font='Helvetica 10 bold').grid(row=0, column=0, columnspan=3)
    tkinter.Label(main_window, text='Pod Status').grid(row=1, sticky='w')
    tkinter.Label(main_window, text='Velocity').grid(row=2, sticky='w')
    tkinter.Label(main_window, text='cm/s').grid(row=2, column=2, sticky='w')
    tkinter.Label(main_window, text='Acceleration(X)').grid(row=3, sticky='w')
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

    status.set('')
    velocity.set('')
    acceleration.set('')
    position.set('')
    pod_temperature.set('')
    x_acceleration.set('')
    y_acceleration.set('')
    z_acceleration.set('')

    def update_data():
        test_status = 1 # This will be replaced by received message later...
        global i
        x_acceleration.set(str(i))
        if test_status in pod_status:
            status.set(pod_status[test_status])
        else:
            status.set('N/A')
        i = i + 1


        main_window.after(2000, update_data)
        return update_data
    update_data()
    main_window.mainloop()


