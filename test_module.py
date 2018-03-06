from Agent_property import Agent
a = Agent()
a.add_property()
a.add_property()
#In class rental and purchase are different attributes fpr
a.display_properties()
print(len(a.property_list))
a.buy_property()
print(len(a.property_list))
print('Commit')