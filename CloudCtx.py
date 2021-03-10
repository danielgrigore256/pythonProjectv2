from datetime import datetime

class CloudCtx:

    counter = 0
    date_values_list = []
    cloudctx_obj_list = []

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
        method to display on console all attributes values of the object

        """
        print("""
        Name : {}
        Tenant_ame: {}
        Description : {}
        Name_alias: {}
        CTX Profile Name: {} 
        Health Status: {} """.format(self.name, self.tenant_name, self.description,
                                     self.name_alias, self.ctx_profile_name, self.displayed_health ))

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