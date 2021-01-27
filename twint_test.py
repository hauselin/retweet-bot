# import twint

# # import nest_asyncio

# # nest_asyncio.apply()

# c = twint.Config()
# c.Username = "my_random_crap"
# # c.Store_object = True
# # c.User_full = True
# # c
# twint.run.Followers(c)

# print(twint.output.users_list)


import twint

c = twint.Config()
c.Username = "my_random_crap"
c.Store_csv = True
c.User_full = True
c.Output = "users.csv"
twint.run.Followers(c)