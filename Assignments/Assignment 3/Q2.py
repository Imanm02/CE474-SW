initial_sales = 1500
growth_rate_year_2 = 0.75
growth_rate_year_3 = 0.20
additional_profit_margin = 0.04 

sales_year_2 = initial_sales * (1 + growth_rate_year_2)
sales_year_3 = sales_year_2 * (1 + growth_rate_year_3)

additional_profit_year_1 = initial_sales * additional_profit_margin
additional_profit_year_2 = sales_year_2 * additional_profit_margin
additional_profit_year_3 = sales_year_3 * additional_profit_margin

total_profits_year_1 = initial_sales + additional_profit_year_1
total_profits_year_2 = sales_year_2 + additional_profit_year_2
total_profits_year_3 = sales_year_3 + additional_profit_year_3

initial_salary_costs = 1800
salary_growth_rate = 0.25
server_maintenance_costs = 200

salary_costs_year_2 = initial_salary_costs * (1 + salary_growth_rate)
salary_costs_year_3 = salary_costs_year_2 * (1 + salary_growth_rate)

total_costs_year_1 = initial_salary_costs + server_maintenance_costs
total_costs_year_2 = salary_costs_year_2 + server_maintenance_costs
total_costs_year_3 = salary_costs_year_3 + server_maintenance_costs

net_profits_year_1 = total_profits_year_1 - total_costs_year_1
net_profits_year_2 = total_profits_year_2 - total_costs_year_2
net_profits_year_3 = total_profits_year_3 - total_costs_year_3

discount_rate = 0.10

pv_net_profits_year_1 = net_profits_year_1 / (1 + discount_rate)**1
pv_net_profits_year_2 = net_profits_year_2 / (1 + discount_rate)**2
pv_net_profits_year_3 = net_profits_year_3 / (1 + discount_rate)**3

npv = pv_net_profits_year_1 + pv_net_profits_year_2 + pv_net_profits_year_3

total_investment = initial_sales
total_net_profits = net_profits_year_1 + net_profits_year_2 + net_profits_year_3
roi = (total_net_profits / total_investment) * 100

{
    "sales_year_2": sales_year_2,
    "sales_year_3": sales_year_3,
    "total_profits_year_1": total_profits_year_1,
    "total_profits_year_2": total_profits_year_2,
    "total_profits_year_3": total_profits_year_3,
    "total_costs_year_1": total_costs_year_1,
    "total_costs_year_2": total_costs_year_2,
    "total_costs_year_3": total_costs_year_3,
    "net_profits_year_1": net_profits_year_1,
    "net_profits_year_2": net_profits_year_2,
    "net_profits_year_3": net_profits_year_3,
    "npv": npv,
    "roi": roi
}