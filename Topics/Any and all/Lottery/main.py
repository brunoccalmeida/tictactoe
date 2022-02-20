# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_condition = 44  # or greater
winning_tickets = [i >= winning_condition for i in tickets]
tickets_bool = any(winning_tickets)
