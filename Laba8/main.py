import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file, delimiter=';')

    def describe_data(self):
        return self.data.describe()

    def plot_line_chart(self, x, y):
        if x not in self.data.columns or y not in self.data.columns:
            print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
            return
        plt.plot(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{y} over {x}')
        plt.grid(True)

    def plot_bar_chart(self, x, y):
        if x not in self.data.columns or y not in self.data.columns:
            print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
            return
        plt.bar(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f'{y} by {x}')

    def multiple_subplots(self, x, y):
        if x not in self.data.columns or y not in self.data.columns:
            print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
            return
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].plot(self.data[x], self.data[y])
        ax[0].set_title(f'Line Chart: {y} over {x}')
        ax[1].bar(self.data[x], self.data[y], color='orange')
        ax[1].set_title(f'Bar Chart: {y} by {x}')
        plt.tight_layout()
        return fig

visualizer = DataVisualizer('D:/My_Project/Python/Labu/Laba8/table.csv')
print(visualizer.describe_data())

def main():
    plt.figure()
    visualizer.plot_line_chart('Score', 'Year')
    plt.show()

    plt.figure()
    visualizer.plot_bar_chart('Score', 'Year')
    plt.show()

    fig = visualizer.multiple_subplots('Score', 'Year')
    fig.savefig('my_visualization.png')
    
if __name__ == '__main__':
    main()
