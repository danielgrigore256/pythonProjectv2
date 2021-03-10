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
    healthinst_obj_list = []

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