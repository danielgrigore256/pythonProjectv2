import json
from CloudCtx import CloudCtx
from HealthInst import HealthInst

# importing the contents of JSON file into the program
jay = json.load(open(r'C:\Users\DGrigore\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\scratch.json5', 'r'))


def take_from_hcloudctx(j, entry_index):

        """
            ***GETTING ATTRIBUTES FROM JSON FILE TO CloudCtx objects
        :param j : index for the JSON file hcloudctx entry
            param type : int
        :param entry_index: Index key that is given to to acces the the json entry that suits the attribute
            param type : str
        :return: the information (data) that needs to be stored in the object attribute
        param type : str

        """

        temp = jay["imdata"][j]["hcloudCtx"]["attributes"][entry_index]

        return temp

def take_from_child(k, child_key):

    """
    ***Function to read values from child entryes in JSON and adding them to HealthInst class objects attributes
    :param k: index for hcloudctx childs possition
        :type: int
    :param child_key: key of the entry that holds the value for HealthInst attributes
        :type: string
    :return: a string from JSON file
    """
    if jay["imdata"][i]["hcloudCtx"]["children"] == []:
        child_value = "0"
    else :
        child_value = jay["imdata"][k]["hcloudCtx"]["children"][0]["healthInst"]["attributes"][child_key]
    return child_value

"""
Creating the loop to parse the json file and add contents from it to our classes
Using variables like get_(attribute_name) to temporary store data from json and move to object's attribute

"""

for i in range(int(jay["totalCount"])):

    # Creating temporary objects to store data that position "i"
    obj_healthinst = HealthInst(int(take_from_child(i,"cur")), take_from_child(i,"maxSev"))

    obj_cloudctx = CloudCtx(take_from_hcloudctx(i, "name"),
                            take_from_hcloudctx(i, "tenantName"),
                            take_from_hcloudctx(i, "description"),
                            take_from_hcloudctx(i, "nameAlias"),
                            take_from_hcloudctx(i, "ctxProfileName"),
                            obj_healthinst.displayed_health(),
                            take_from_hcloudctx(i, "modTs"))

    # populating list with the instanced objects
    HealthInst.healthinst_obj_list.append(obj_healthinst)
    CloudCtx.cloudctx_obj_list.append(obj_cloudctx)

# 9.  Display CloudCtx attributes
for object_cloud in CloudCtx.cloudctx_obj_list:
    object_cloud.display_ctx()

# 11. Display objects in order
HealthInst.order_health()

# 12. Keep track of the number of objects
print("There are", CloudCtx.counter, "objects created")

# 15. display items in order
CloudCtx.display_last_modified()
