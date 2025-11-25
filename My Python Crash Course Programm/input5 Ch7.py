base_users=['vkj','rkj','kj','aj','pj']
#unconfirmed_users=['vkj','jkg','nkj','kj','pj','sj']
confirmed_users=[]
while base_users:
    current_user=base_users.pop()
    print("\nVarifying current User:",current_user)
    confirmed_users.append(current_user)
print("Folllowing users have been confirmed")
for conf_user in confirmed_users:
    print(conf_user.title())
