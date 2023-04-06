class IncomeStatement:

    def __init__(self):
        self.sales = 0.0  # need calculations
        self.cost_of_goods_sold = 0.0
        self.gross_margin = 0.0
        self.variable_sell_admin_cost = 0.0
        self.fixed_sell_admin_cost = 0.0
        self.sell_admin_cost = 0.0
        self.net_income = 0.0

    def get_is(self,
               selling_price,
               units_sold,
               units_produced,
               unit_product_cost,
               prev_unit_product_cost,
               beginning_inventory,
               variable_sell_admin,
               fixed_sell_admin):
        self.sales = selling_price * units_sold
        if units_produced > units_sold:
            self.cost_of_goods_sold = unit_product_cost * units_sold
        elif units_produced < units_sold:
            cog_1 = prev_unit_product_cost * beginning_inventory
            cog_2 = unit_product_cost * units_produced
            self.cost_of_goods_sold = cog_1 + cog_2
        self.gross_margin = self.sales - self.cost_of_goods_sold
        self.variable_sell_admin_cost = variable_sell_admin * units_sold
        self.fixed_sell_admin_cost = fixed_sell_admin
        self.sell_admin_cost = self.variable_sell_admin_cost + self.fixed_sell_admin_cost
        self.net_income = self.gross_margin - self.sell_admin_cost

    def print_is(self, year):
        print(f"Income Statement Year {year}\n"
              f"Sales ${self.sales:,.0f}\n"
              f"Cost of Goods Sold ${self.cost_of_goods_sold:,.0f}\n"
              f"Gross Margin ${self.gross_margin:,.0f}\n"
              f"Selling and Admin\n"
              f"  Variable ${self.variable_sell_admin_cost:,.0f}\n"
              f"  Fixed ${self.fixed_sell_admin_cost:,.0f}\n"
              f"Net Operating Income ${self.net_income:,.0f}")


class ContributionIncomeStatement(IncomeStatement):

    def __init__(self):
        IncomeStatement.__init__(self)
        self.cost_of_goods_sold = 0.0
        self.variable_expenses = 0.0
        self.contribution_margin = 0.0
        self.fixed_manufacturing_overhead = 0.0
        self.fixed_expenses = 0.0
        self.net_income = 0.0

    def get_cis(self, selling_price, units_sold, unit_product_cost, variable_sell_admin, fixed_moh, fixed_sell_admin):
        self.sales = units_sold * selling_price
        self.cost_of_goods_sold = units_sold * unit_product_cost
        self.variable_sell_admin_cost = units_sold * variable_sell_admin
        self.variable_expenses = self.cost_of_goods_sold + self.variable_sell_admin_cost
        self.contribution_margin = self.sales - self.variable_expenses
        self.fixed_manufacturing_overhead = fixed_moh
        self.fixed_sell_admin_cost = fixed_sell_admin
        self.fixed_expenses = self.fixed_manufacturing_overhead + self.fixed_sell_admin_cost
        self.net_income = self.contribution_margin - self.fixed_expenses

    def print_cis(self, year):
        print(f"Contribution Income Statement Year {year}")
        print(f"Sales ${self.sales:,.0f}")
        print(f"Variable Expenses")
        print(f"  Cost of Goods Sold ${self.cost_of_goods_sold:,.0f}")
        print(f"  Selling and Administrative ${self.variable_sell_admin_cost:,.0f}")
        print(f"Contribution Margin ${self.contribution_margin:,.0f}")
        print(f"Fixed Expenses")
        print(f"  Manufacturing Overhead ${self.fixed_manufacturing_overhead:,.0f}")
        print(f"  Selling and Administrative ${self.fixed_sell_admin_cost:,.0f}")
        print(f"Net Operating Income ${self.net_income:,.0f}")


if __name__ == "__main__":
    selling_price = float(input("Enter selling price: $"))

    # Variable Costs per unit
    direct_materials = float(input("Enter cost of Direct materials per unit: $"))
    direct_labor = float(input("Enter cost of Direct labor per units: $"))
    variable_moh = float(input("Enter cost of Variable Manufacturing Overhead pet unit: $"))
    variable_sell_admin = float(input("Enter cost of Variable Selling and Administrative per unit: $"))

    # Fixed Costs per year
    fixed_moh = float(input("Enter cost of Fixed Manufacturing overhead: $"))
    fixed_sell_admin = float(input("Enter cost of Fixed Selling and Administrative combined: $"))

    # Stores Units produced & sold, Ending inventory (if any), and Fixed MOH per unit in each year
    production_selling = {}
    num_years = int(input("Enter amount of years: "))
    for i in range(1, num_years+1):
        print(f"Enter units produced for year {i}: ", end="")
        units_produced = int(input())
        print(f"Enter units sold for year {i}: ", end="")
        units_sold = int(input())
        fixed_moh_per_unit = fixed_moh / units_produced

        production = dict()
        production["Produced"] = units_produced
        production["Sold"] = units_sold
        if units_produced > units_sold:
            production["Beginning Inventory"] = 0
            production["Ending Inventory"] = units_produced - units_sold
        elif units_produced < units_sold:
            production["Beginning Inventory"] = units_sold - units_produced
            production["Ending Inventory"] = production["Beginning Inventory"] + units_produced - units_sold
        production["Fixed MOH Per Unit"] = f"{fixed_moh_per_unit:.2f}"

        product_costs = dict()
        product_costs["Variable"] = direct_materials + direct_labor + variable_moh
        product_costs["Absolute"] = direct_materials + direct_labor + variable_moh + fixed_moh_per_unit
        production["Costing Methods"] = product_costs
        production_selling[i] = production
    print()

    cis_net_income = []
    for i in range(1, num_years+1):
        year = ContributionIncomeStatement()
        year.get_cis(selling_price,
                     production_selling[i]["Sold"],
                     production_selling[i]["Costing Methods"]["Variable"],
                     variable_sell_admin,
                     fixed_moh,
                     fixed_sell_admin)
        year.print_cis(i)
        cis_net_income.append(year.net_income)
        print()

    is_net_income = []
    for i in range(1, num_years+1):
        year = IncomeStatement()
        try:
            prev_unit_product_cost = production_selling[i-1]["Costing Methods"]["Absolute"]

            year.get_is(selling_price,
                        production_selling[i]["Sold"],
                        production_selling[i]["Produced"],
                        production_selling[i]["Costing Methods"]["Absolute"],
                        prev_unit_product_cost,
                        production_selling[i]["Beginning Inventory"],
                        variable_sell_admin,
                        fixed_sell_admin)
            year.print_is(i)

            is_net_income.append(year.net_income)
        except KeyError:
            prev_unit_product_cost = production_selling[i]["Costing Methods"]["Absolute"]

            year.get_is(selling_price,
                        production_selling[i]["Sold"],
                        production_selling[i]["Produced"],
                        production_selling[i]["Costing Methods"]["Absolute"],
                        prev_unit_product_cost,
                        production_selling[i]["Beginning Inventory"],
                        variable_sell_admin,
                        fixed_sell_admin)
            year.print_is(i)
            is_net_income.append(year.net_income)

        print()

    print("Reconciliation")
    for i in range(num_years):
        print(f"Year {i+1}")
        print(f"Variable Cost Net Income ${cis_net_income[i]:,.0f}")
        if is_net_income[i] > cis_net_income[i]:
            print(f"Fixed MOH Cost Deferred in Inventory ${is_net_income[i] - cis_net_income[i]:,.0f}")
        else:
            print(f"Fixed MOH Cost Released From Inventory (${cis_net_income[i] - is_net_income[i]:,.0f})")
        print(f"Absolute Cost Net Income ${is_net_income[i]:,.0f}")
        print()
