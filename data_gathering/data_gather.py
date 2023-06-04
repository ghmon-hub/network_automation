import datetime
import time
import sys
sys.path.append("/var/www/")
from www.codes.my_projects.db_functions.db_rd_cre_brd import db_rd_cr_br
from www.codes.my_projects.db_functions.db_int_device_clean import db_ne_l3_clean
from www.codes.my_projects.db_functions.db_neighbor_dev_clean import db_ne_dev_clean
from www.codes.my_projects.data_gathering.collect_interface_devices import inter_find
from www.codes.my_projects.data_gathering.collect_neighbor import m_th_ssh_nei
from www.codes.my_projects.data_gathering.collect_neighbor import m_th_nei_file
from www.codes.my_projects.data_gathering.collect_neighbor import col_nei
from www.codes.my_projects.backup.backup import m_th_ssh_b
from www.codes.my_projects.backup.backup import m_th_ssh_a
from www.codes.my_projects.data_gathering.collect_route import route_find
from www.codes.my_projects.analysis.neighbor_device import draw_nei

csc_list = set()
forti_list = set()
juni_list = set()
cs_nei_list = set()
forti_nei_list = set()
juni_nei_list = set()
cs_rt_list = set()
forti_rt_list = set()
juni_rt_list = set()

def data_g(d_n):
    try:
        #domain_name = str(input('Please Enter The domain-name : '))
        domain_name = str(d_n)
        out_file = m_th_ssh_b(db_rd_cr_br()[0], db_rd_cr_br()[1], db_rd_cr_br()[2], db_rd_cr_br()[3], db_rd_cr_br()[4], domain_name)
        csc_list = out_file[0]
        forti_list = out_file[1]
        juni_list = out_file[2]
        forti_rt_list = out_file[3]
        juni_rt_list = out_file[4]
        csc_vrf_list = out_file[5]
        out_rt_csc = m_th_ssh_a(db_rd_cr_br()[0], db_rd_cr_br()[1], db_rd_cr_br()[2], db_rd_cr_br()[3], db_rd_cr_br()[4], csc_vrf_list)
        cs_rt_list = out_rt_csc
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        route_find(cs_rt_list, forti_rt_list, juni_rt_list)
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        db_ne_l3_clean()
        inter_find(csc_list, forti_list, juni_list)
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        #m_th_ssh_nei(db_rd_cr_br()[0], db_rd_cr_br()[1], db_rd_cr_br()[2], db_rd_cr_br()[3], db_rd_cr_br()[4])
        #time.sleep(60)
        #out_file = m_th_nei_file(db_rd_cr_br()[0], db_rd_cr_br()[1], db_rd_cr_br()[2], db_rd_cr_br()[3], db_rd_cr_br()[4])
        #cs_nei_list = out_file[1]
        #forti_nei_list = out_file[0]
        #juni_nei_list = out_file[2]
        #time.sleep(5)
        #db_ne_dev_clean()
        #col_nei(cs_nei_list, juni_nei_list, forti_nei_list)
        draw_nei()
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    return "Finish"
