import xlrd
import os
import matplotlib.pyplot as plt


def read_file(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    data = [sheet.row_values(row) for row in range(sheet.nrows)]
    return data


def process_data(data):
    sales_data = {}
    for row in data[1:]:
        period, item, sales = row
        if period not in sales_data:
            sales_data[period] = {}
        sales_data[period][item] = int(sales)
    return sales_data


def filter_data(data, threshold):
    filtered_data = {}
    for period, items in data.items():
        filtered_items = {
            item: sales for item, sales in items.items() if sales > threshold
        }
        if filtered_items:
            filtered_data[period] = filtered_items
    return filtered_data


def aggregate_data(data):
    aggregated_data = {}
    for period, items in data.items():
        total_sales = sum(items.values())
        aggregated_data[period] = {"total_sales": total_sales, "items": items}
    return aggregated_data


def visualize_data(aggregated_data, filename):
    periods = list(aggregated_data.keys())
    sales = [aggregated_data[period]["total_sales"] for period in periods]

    plt.figure(figsize=(10, 6))
    plt.bar(periods, sales, color="skyblue")
    plt.xlabel("Периоды")
    plt.ylabel("Объем продаж")
    plt.title(f"Агрегированные данные о продажах для файла '{filename}'")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(file_path, threshold):
    raw_data = read_file(file_path)
    processed_data = process_data(raw_data)
    filtered_data = filter_data(processed_data, threshold)
    aggregated_data = aggregate_data(filtered_data)
    visualize_data(aggregated_data, os.path.basename(file_path))
    total_sales = sum(aggregated_data.values())
    print(f"Суммарный объем продаж для файла '{file_path}': {total_sales}")


def process_sales_files(directory, threshold):
    for filename in os.listdir(directory):
        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            file_path = os.path.join(directory, filename)
            raw_data = read_file(file_path)
            processed_data = process_data(raw_data)
            filtered_data = filter_data(processed_data, threshold)
            aggregated_data = aggregate_data(filtered_data)
            print(f"Данные из файла '{filename}':")
            for period, sales_info in aggregated_data.items():
                total_sales = sales_info["total_sales"]
                items = sales_info["items"]
                print(f"Период: {period}")
                for item, sales in items.items():
                    print(f"  - Товар: {item}, Объем продаж: {sales}")
                print(f"Суммарный объем продаж: {total_sales}")
            visualize_data(aggregated_data, filename)


directory = "C:/Users/mms21/OneDrive/Рабочий стол"
threshold = 100
process_sales_files(directory, threshold)
