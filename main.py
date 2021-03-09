import json
from datetime import datetime

# importing the contents of JSON file into the program
jay = json.load(open(r'C:\Users\DGrigore\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\scratch.json5', 'r'))


class CloudCtx:
    counter = 0
    date_values_list = []

    def __init__(self, name, tenant_name, description, name_alias, ctx_profile_name, displayed_health, last_modified):
        """

               __init__ method : adds into the instanced object attributes from JSON file

               :param name : name attribute
                   :type name : string
               :param tenant_name : tenant name
                   :type tenant_name : string
               :param description : description attribute
                   :type description : string
               :parm name_alias : name alias attribute
                   :type name_alias : string
               :param ctx_profile_name : ctx profile name
                   :type : string
               :param last_modified : the date Json entry was last modified
                    :type : DateTime Format

                using checkifnull() method we check if entry is empty ("")
                    :return  replace empty records with ("-")


        """

        self.name = CloudCtx.check_if_null(name)
        self.tenant_name = CloudCtx.check_if_null(tenant_name)
        self.description = CloudCtx.check_if_null(description)
        self.name_alias = CloudCtx.check_if_null(name_alias)
        self.ctx_profile_name = CloudCtx.check_if_null(ctx_profile_name)
        self.last_modified = CloudCtx.date_format(last_modified)
        """
            extra values taken from Healthinst class (method displayed_health)
                :param : displayed_health : enum "Healthy"/"Unhealthy"
                    :type : string
        """
        self.displayed_health = displayed_health

        CloudCtx.counter += 1
        CloudCtx.date_values_list.append(self.last_modified)

    def display_ctx(self):
        """
        method to display on console all values of the object

        """
        print("Name:", self.name)
        print("Tenant_ame:", self.tenant_name)
        print("Description", self.description)
        print("Name_alias:", self.name_alias)
        print("CTX Profile Name:", self.ctx_profile_name)
        print("Health Status:", self.displayed_health)

    @staticmethod
    def check_if_null(attribute):
        """
        check if Cloud Ctx attribute is null ( = "" )
        :return: new attribute value ("-")
        """
        if attribute == "":
            attribute = "-"
        return attribute

    @staticmethod
    def date_format(date_string):
        """

        :param date_string: the JSON entry we want to transform in last_modified CloudCtx object
        :return: a DateTime type variable, formated
        """
        # cutting the extra info from JSON string
        cutted_date_string = date_string[0:19]
        # converting JSON string into a datetime data type
        string_to_date = datetime.strptime(cutted_date_string, "%Y-%m-%dT%H:%M:%S")
        # specifying the order of date info from original to our preferences
        format_type = "%d-%m-%Y %H:%M:%S %p"
        # using strftime() to change the format of date info
        date_attribute = string_to_date.strftime(format_type)
        # giving the result to the instance of the class
        return date_attribute

    @staticmethod
    def display_last_modified():
        print(sorted(CloudCtx.date_values_list, reverse=True))


class HealthInst:
    """
    class variables :
        :param: counter2 : increments at each new instance created
            :type : int
        :param: healthlist : list that stores all current_health values
            :type : list
    """
    counter2 = 0
    healthlist = []

    def __init__(self, current_health, max_sev):

        """
        __init__ method : adds into the instanced object attributes from JSON file
            param current_health : cur attribute from JSON file
                type current_health : int
            param max_sev: maxSev attribute from JSON file
                type max_sev : string
        """

        self.current_health = current_health
        self.max_sev = max_sev

        HealthInst.counter2 += 1
        HealthInst.healthlist.append(self.current_health)

    def displayed_health(self):

        """
        compares the value of current_health attribute to 100
        :return: a string
        """

        if int(self.current_health) == 100:
            return "Healthy"
        else:
            return "Unhealthy"

    @staticmethod
    def order_health():
        """
        orders the current health values of the Healthinst objects attributes
        :return: prints the lowest to highest value (of health ) in a sorted healthlist[object.current_health]
        """

        for index in sorted(HealthInst.healthlist):
            print(index)


"""
Creating the loop to parse the json file and add contents from it to our classes
Using variables like get_(attribute_name) to temporary store data from json and move to object's attribute

"""
# creating two lists that will hold our objects , one for each class
cloudctx_obj_list = []
healthinst_obj_list = []

for i in range(int(jay["totalCount"])):

    # getting Healthinst attributes
    # 13. Checking if children list is empty first
    if jay["imdata"][i]["hcloudCtx"]["children"] == []:
        get_current_health = 0
        get_max_sev = "-"
    else:
        get_current_health = int(jay["imdata"][i]["hcloudCtx"]["children"][0]["healthInst"]["attributes"]["cur"])
        get_max_sev = jay["imdata"][i]["hcloudCtx"]["children"][0]["healthInst"]["attributes"]["maxSev"]

    # getting Cloud Ctx attributes
    get_name = jay["imdata"][i]["hcloudCtx"]["attributes"]["name"]
    get_tenant_name = jay["imdata"][i]["hcloudCtx"]["attributes"]["tenantName"]
    get_description = jay["imdata"][i]["hcloudCtx"]["attributes"]["description"]
    get_name_alias = jay["imdata"][i]["hcloudCtx"]["attributes"]["nameAlias"]
    get_ctx_profile_name = jay["imdata"][i]["hcloudCtx"]["attributes"]["ctxProfileName"]
    get_last_modified = jay["imdata"][i]["hcloudCtx"]["attributes"]["modTs"]
    # Creating temporary objects to store data that position "i"
    obj_healthinst = HealthInst(get_current_health, get_max_sev)
    obj_cloudctx = CloudCtx(get_name, get_tenant_name, get_description,
                            get_name_alias, get_ctx_profile_name,
                            obj_healthinst.displayed_health(), get_last_modified)

    # populating list with the instanced objects
    healthinst_obj_list.append(obj_healthinst)
    cloudctx_obj_list.append(obj_cloudctx)

# 9.  Display CloudCtx attributes
for object_cloud in cloudctx_obj_list:
    object_cloud.display_ctx()

# 11. Display objects in order
HealthInst.order_health()

# 12. Keep track of the number of objects
print("There are", CloudCtx.counter, "objects created")

# 15. display items in order
CloudCtx.display_last_modified()
