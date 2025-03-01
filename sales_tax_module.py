#module
tax_rate = 0.06

def calculate_sales_tax(total):
    return round(total * tax_rate, 2)

def calculate_total_after_tax(total):
    return round(total + calculate_sales_tax(total), 2)