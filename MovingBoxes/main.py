import math

num_test_cases = int(input())

for case in range(1, num_test_cases+1):
    print("Case " + str(case))
    b, m, c = input().strip().split()
    b = int(b)
    m = int(m)
    c = int(c)
    companies = []
    company_list = {}
    for i in range(c):
        company_name, charge_1, charge_2 = input().strip().split()
        charge_1 = int(charge_1)
        charge_2 = int(charge_2)
        temp = [company_name, charge_1, charge_2]
        companies.append(temp)
    for company in companies:
        total_cost = 0
        boxes_to_ship = b
        while boxes_to_ship != 0:
            half_boxes = int(math.ceil(boxes_to_ship/2))
            cost_of_shipping_half = company[2]
            cost_of_shipping_one = company[1]
            cost_of_shipping_one_by_one = cost_of_shipping_one * half_boxes
            if boxes_to_ship - half_boxes > m:
                if cost_of_shipping_half <= cost_of_shipping_one_by_one:
                    boxes_to_ship -= half_boxes
                    total_cost += company[2]
            elif boxes_to_ship - 1 >= m:
                boxes_to_ship -= 1
                total_cost += company[1]
            if boxes_to_ship == m:
                break
        company_list[company[0]] = total_cost
        #print(company[0] + " " + str(total_cost))
    company_list = dict(sorted(company_list.items(), key=lambda item: item[1]))
    #print(company_list)
    for key, value in company_list.items():
        print(key, value)


