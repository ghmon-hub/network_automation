import sys

def db_backup_in(ip, time_act, backup, brand):
    path_1 = '/var/www/codes/my_projects/backup/bk/'
    with open(path_1+brand+"_"+ip+"_"+time_act+".txt", 'a+') as f:
        f.write(backup)

def db_backup_rt(ip, time_act, rt_out, brand):
    path_1 = '/var/www/codes/my_projects/backup/bk/'
    with open(path_1+"rt_"+brand+"_"+ip+"_"+time_act+".txt", 'a+') as f:
        f.write(rt_out)

def db_backup_nei(ip, time_act, nei_out, brand):
    path_1 = '/var/www/codes/my_projects/backup/bk/'
    with open(path_1+"nei_"+brand+"_"+ip+"_"+time_act+".txt", 'a+') as f:
        f.write(nei_out)

def db_backup_vrf(ip, time_act, vrf_out, brand):
    path_1 = '/var/www/codes/my_projects/backup/bk/'
    with open(path_1+"vrf_"+brand+"_"+ip+"_"+time_act+".txt", 'a+') as f:
        f.write(vrf_out)
