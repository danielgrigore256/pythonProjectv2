import json


jay = json.load(open(r'C:\Users\DGrigore\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\scratch.json5', 'r'))


class HealthInst:
    counter2 = 0

    def __init__(self):

        """
        __init__ method : adds into the instanced object attributes from JSON file
            param current_health : cur attribute from JSON file
                type current_health : int
            param max_sev: maxSev attribute from JSON file
                type max_sev : string
        """
        j = int(HealthInst.counter2)
        self.current_health = int(jay["imdata"][j]["hcloudCtx"]["children"][0]["healthInst"]["attributes"]["cur"])
        self.max_sev = jay["imdata"][j]["hcloudCtx"]["children"][0]["healthInst"]["attributes"]["maxSev"]
        HealthInst.counter2 += 1

    def displayed_health(self):

        """

        compares the value of current_health attribute to 100
        :return: a string

        """
        if int(self.current_health) == 100:
            print("Healthy")
        else:
            print("Unhealthy")


class CloudCtx(HealthInst):
    counter = 0

    def __init__(self):
        """

        __init__ method : adds into the instanced object attributes from JSON file

        param name : name attribute
            type name : string
        param tenant_name : tenant name
            type tenant_name : string
        param description : description attribute
            type description : string
        parm name_alias : name alias attribute
            type name_alias : string
        super().__init__ : calls the initialization method of the parent class HealthInst
        take_from_jay : method to access the json file and index the info to object attribute


        """
        self.name = CloudCtx.take_from_jay(CloudCtx.counter, "name")
        self.tenant_name = CloudCtx.take_from_jay(CloudCtx.counter, "tenantName")
        self.description = CloudCtx.take_from_jay(CloudCtx.counter, "description")
        self.name_alias = CloudCtx.take_from_jay(CloudCtx.counter, "nameAlias")
        self.ctx_profile_name = CloudCtx.take_from_jay(CloudCtx.counter, "ctxProfileName")

        CloudCtx.counter += 1

        super().__init__()

    def take_from_jay(j, cheie):

        """
        :param j : index, connected to the number of entries, needed to index the JSON file
            param type : int
        :param cheie: Index key that is given to to acces the the json entry that suits the attribute
            param type : str
        :return: the information (data) that needs to be stored in the object attribute
        param type : str

        """

        temp = jay["imdata"][j]["hcloudCtx"]["attributes"][cheie]
        if temp == "":
            temp = "-"
        return temp

    def displayctx(self):

        """
        method to display on console all values of the object

        """
        print("Name:", self.name)
        print("Tenant_ame:", self.tenant_name)
        print("Description", self.description)
        print("Name_alias:", self.name_alias)
        print("CTX Profile Nmae:", self.ctx_profile_name)

    def health(self):

        """
        calling the displayed_health method of parent class,HealthInst()

        """
        super().displayed_health()


"""

# creating objects that use CloudCtx and Healthinst values from json
ctx1 = CloudCtx()
ctx2 = CloudCtx()
ctx3 = CloudCtx()


print(ctx1.name, ctx1.tenant_name, ctx1.current_health)
print(ctx2.name, ctx2.tenant_name, ctx2.current_health)
print(ctx3.name, ctx3.tenant_name, ctx3.current_health)

# sorting objects by current health
order = sorted([int(ctx1.current_health), int(ctx2.current_health), int(ctx3.current_health)])
for x in order:
    print(x)
# keeping track of objects
print("We got", CloudCtx.counter, "objects")
"""
ctx1 = CloudCtx()
ctx2 = CloudCtx()
ctx3 = CloudCtx()
ctx4 = CloudCtx()
ctx5 = CloudCtx()

ctx1.displayctx()
ctx2.displayctx()
ctx3.displayctx()
ctx4.displayctx()
ctx5.displayctx()
