import filecmp

###################################################################################################
#       TESTING                                                                                   #
###################################################################################################

DEBUG = False

#with open("./104/12-02-00-24-2022.txt", "r", encoding="utf-8") as f:
#    latest_scan = f.readlines()
#with open("./104/12-02-00-24-2021.txt", "r", encoding="utf-8") as f:
#    previous_scan = f.readlines()

latest_scan = "./104/12-02-00-24-2022.txt"
previous_scan = "./104/12-02-00-24-2021.txt"

result = filecmp.cmp(latest_scan, previous_scan, shallow=False)
if result != True:
    print(result)
    """Do weird shit"""