weight = 41.5
cost = ""
total = ""

#ground shipping
if weight <= 2:
  ground_cost = 1.50
elif weight <= 6 and weight > 2:
  ground_cost = 3.00 
elif weight <= 10 and weight > 6:
  ground_cost = 4.00
else:
  ground_cost = 4.75

#drone shipping
if weight <= 2:
  drone_cost = 4.50
elif weight <= 6 and weight > 2:
  drone_cost = 9.00 
elif weight <= 10 and weight > 6:
  drone_cost = 12.00
else:
  drone_cost = 14.25


drone_shipping = weight * drone_cost
ground_shipping = weight * ground_cost + 20.00
premium_ground_shipping = 125.00

print('Weight: ' + str(weight) + ' lb.\n' )

print('Ground Shipping:')
print('Standard')
print('${:,.2f}'.format(ground_shipping) + ' (@ '+ '${:,.2f}'.format(ground_cost) + 'per/lb)\n')
print('Premium')
print('${:,.2f}'.format(premium_ground_shipping) +'\n')
print('Drone Shipping:')
print('${:,.2f}'.format(drone_shipping) + ' (@ '+ '${:,.2f}'.format(drone_cost) + 'per/lb)')


