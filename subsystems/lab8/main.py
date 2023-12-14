import pandas as pd
import matplotlib.pyplot as plt
import logging

class DataVisualizer:
    def __init__(self, csv_file):
        try:
            self.data = pd.read_csv(csv_file, delimiter=';')
        except FileNotFoundError as e:
            print(f"Помилка: файл '{csv_file}' не знайдено.")
            logging.error(f"Помилка: файл '{csv_file}' не знайдено.")
            self.data = None

    def describe_data(self):
        if self.data is not None:
            return self.data.describe()
        else:
            return None

    def plot_line_chart(self, x, y):
        if self.data is not None:
            if x not in self.data.columns or y not in self.data.columns:
                print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                logging.error(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                return
            plt.plot(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'{y} over {x}')
            plt.grid(True)
        else:
            print("Неможливо відобразити графік. Датафрейм не було ініціалізовано.")

    def plot_bar_chart(self, x, y):
        if self.data is not None:
            if x not in self.data.columns or y not in self.data.columns:
                print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                logging.error(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                return
            plt.bar(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'{y} by {x}')
        else:
            print("Неможливо відобразити графік. Датафрейм не було ініціалізовано.")

    def multiple_subplots(self, x, y):
        if self.data is not None:
            if x not in self.data.columns or y not in self.data.columns:
                print(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                logging.error(f"Стовпці '{x}' або '{y}' не знайдені у датафреймі.")
                return
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            ax[0].plot(self.data[x], self.data[y])
            ax[0].set_title(f'Line Chart: {y} over {x}')
            ax[1].bar(self.data[x], self.data[y], color='orange')
            ax[1].set_title(f'Bar Chart: {y} by {x}')
            plt.tight_layout()
            return fig
        else:
            print("Неможливо відобразити графік. Датафрейм не було ініціалізовано.")

def main():
    plt.ion()
    
    visualizer = DataVisualizer('D:/My_Project/Python/SPL/data/lab8/table.csv')
    if visualizer.describe_data() is not None:
        def plot_line_chart():
            plt.figure()
            visualizer.plot_line_chart('Score', 'Year')
            plt.show()

        def plot_bar_chart():
            plt.figure()
            visualizer.plot_bar_chart('Score', 'Year')
            plt.show()

        def save_multiple_subplots():
            fig = visualizer.multiple_subplots('Score', 'Year')
            if fig is not None:
                fig.savefig('my_visualization.png')

        # Тепер викликаємо функції візуалізації
        plot_line_chart()
        plot_bar_chart()
        save_multiple_subplots()
    
    plt.ioff() 

if __name__ == '__main__':
    main()
