import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Create figure and axis
fig, ax = plt.subplots()

# Define the dates for x-axis and values for y-axis
dates = [datetime.date(2022, 1, 1), datetime.date(2022, 1, 3)]
values = [2, 4]

# Plot lines with dates
ax.plot(dates, values, color='b', marker='o')

# Add another line with different dates and values
dates2 = [datetime.date(2022, 1, 3), datetime.date(2022, 1, 4)]
values2 = [4, 0]
ax.plot(dates2, values2, color='b', marker='o')

# Format the x-axis to display dates
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set labels and title
ax.set_xlabel('Fecha')
ax.set_ylabel('Eje Y')
ax.set_title('Ejemplo de Línea Diagonal')

# Adjust y-axis limits if needed
ax.set_ylim(0, 5)

# Rotate date labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

# Display the plot
plt.show()
