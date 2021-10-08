from flask import Flask

def has_infos(sites, points):
    print(sites, points)
    sites_amount = len(sites)
    points_amount = len(points)
    print(sites_amount, points_amount)
    if sites_amount == 3 and points_amount == 3:
        print("1")
    elif sites_amount == 2 and points_amount == 1:
        print("2")
    elif sites_amount == 1 and points_amount == 2:
        print("3")
    elif sites_amount == 3 and points_amount == 0:
        print("4")
    elif sites_amount == 0 and points_amount == 3:
        print("5")
    else:
        print("6")

site_a = 13
site_b = 28
site_c = 34
point_a = 2
point_b = 35
point_c = 26

sites = []
points = []

sites.append(site_a)
sites.append(site_b)
sites.append(site_c)
points.append(point_a)
points.append(point_b)
points.append(point_c)

print(sites, points)

has_infos(sites, points)