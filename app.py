def generate_html_table(rows, cols):
    table = "<table border='1'>\n"
    for row in range(rows):
        table += "<tr>\n"
        for col in range(cols):
            table += f"<td>Row {row+1}, Col {col+1}</td>\n"
        table += "</tr>\n"
    table += "</table>"
    return table

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print(generate_html_table(rows, cols))
