def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    adult = 37550.0 * no_of_adults
    childrens = (37550.0 * 1/3) * no_of_children
    adult_child = adult + childrens
    a = adult_child * 0.07
    tax = adult_child + a
    b = tax * 0.1
    total_ticket_cost = tax - b
    
    return total_ticket_cost

total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
