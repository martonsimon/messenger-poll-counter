print("Messenger poll counter by Me")


# read users
users = []
print("Copy every user, paste and press enter to finish")
while True:
    user = input("user: ")
    if user == "":
        break
    if "vette fel" not in user and "A csoport" not in user:
        users.append(user)
print("------------------------------")


# poll structure
# fields: name, options, users
# user field: name, array of choice values
class Poll_t:
    def __init__(self):
        self.name = ""
        self.options = []
        self.users = []

        self.read_poll_data()
        self.add_users()
        for i in range(len(self.options)):
            self.prompt_choice(i)
    
    def read_poll_data(self):
        print("Paste raw poll information, press enter twice to exit")
        raw = []
        while True:
            raw.append(input("raw: "))
            if raw[-1] == "" and raw[-2] == "":
                break
        
        self.name = raw[1]
        for i in range(3, len(raw) - 2, 2):
            self.options.append(raw[i])
        print("------------------------------")
    
    def add_users(self):
        for user in users:
            self.users.append([user, []])
            self.users[-1][1] = [False] * len(self.options)

    def prompt_choice(self, id):
        print(f"Prompting for choice {self.options[id]}, enter to stop")
        while True:
            user = input("user: ")
            if user == "":
                break
            if user not in users:
                raise Exception(f"Unknown user entered for poll option {self.options[id]}, user: {user}")
            
            found = False
            for i in range(len(self.users)):
                if self.users[i][0] == user:
                    self.users[i][1][id] = True
                    found = True
                    break
        print("------------------------------")
    
    def print_results(self):
        print(f"\n\nPoll results for: {self.name}")
        print("------------------------------")
        
        # header
        print("Name".ljust(25), end="")
        for option in self.options:
            print(option, end="\t")
        print()

        # rows
        for user in self.users:
            print(user[0].ljust(25), end="")
            for choice in user[1]:
                print("X" if choice else " ", end="\t")
            print()
        

# create poll
poll = Poll_t()
poll.print_results()