def tax_calculator():
    print('welcome!')

    on = True

    while on:

        # This app takes in the cost and tax rate of an item and returns the tax and cost plus tax.

        cost = float(input('please enter the cost: '))

        tax = float(input('please enter the tax rate of your country or state: '))

        tax_on_cost = (cost / 100) * tax

        cost_plus_tax = tax_on_cost + cost

        print(f"Tax on cost = {tax_on_cost}\nCost plus tax = {cost_plus_tax}")

        on = input('do you want to continue Y- N: ').upper()

        if on == 'Y':
            on = True
        else:
            on = False


tax_calculator()
