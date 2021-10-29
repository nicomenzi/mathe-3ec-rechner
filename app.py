from flask import Flask

def get_angle_from_2(angle1, angle2):
    total = angle1 + angle2
    angle3 = 180 - total
    return angle3




def has_infos(sites, angles):
    print(sites, angles)
    sites_amount = len(sites)
    angle_amount = len(angles)
    print(sites_amount, angle_amount)
    if sites_amount == 3 and angle_amount == 3:
        print("1")
    elif sites_amount == 2 and angle_amount == 1:
        print("2")
    elif sites_amount == 1 and angle_amount == 2:
        print("3")
        angles.append(get_angle_from_2(angles[0], angles[1]))
    elif sites_amount == 3 and angle_amount == 0:
        print("4")
    else:
        print("6")

site_a = 13
site_b = 28
site_c = 34
point_a = 2
point_b = 35
point_c = 26

sites = []
angles = []

sites.append(site_a)
sites.append(site_b)
sites.append(site_c)
angles.append(point_a)
angles.append(point_b)
angles.append(point_c)

print(sites, angles)

has_infos(sites, angles)