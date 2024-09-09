import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values)

    plt.savefig('./app/bar_chart.png')
    plt.close()

def generate_line_chart(x, y, title, xlabel, ylabel):
    # Create a line chart
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # Add a title
    plt.title(title)
    
    # Label the x-axis
    plt.xlabel(xlabel)
    
    # Label the y-axis
    plt.ylabel(ylabel)

    plt.savefig('./app/line_chart.png')
    plt.close()

def generate_pie_chart(labels, values):
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.savefig('./app/pie_chart.png')
    plt.close()

if __name__ == '__main__':
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    values = [1, 2, 1, 3, 2, 2, 1]
    generate_bar_chart(labels, values)

    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 2, 1, 3, 2, 2, 1]
    title = 'Apples Eaten Per Day'
    xlabel = 'Day'
    ylabel = 'Apples Eaten'
    generate_line_chart(x, y, title, xlabel, ylabel)

    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    values = [20, 30, 40, 10]
    generate_pie_chart(labels, values)


