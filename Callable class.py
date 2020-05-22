class NoDuplicates:
    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for item in new_items:
            if not item in self.list:
                self.list.append(item)


my_no_dup_list = NoDuplicates()
my_no_dup_list(["rice"])
my_no_dup_list(["salad"])
my_no_dup_list(["rice"])
print(my_no_dup_list.list)
