# import os
# import subprocess
# #
# # response = os.system("ping -n 1 192.168.1.95")
# #
# # print(response)
# # if response == 0:
# #     print('up')
# # else:
# #     print('down')
#
# ipaddress = '192.168.1.569'
#
# proc = subprocess.Popen(
#     ['ping', '-n', '1', ipaddress],
#     stdout=subprocess.PIPE)
# stdout, stderr = proc.communicate()
# if proc.returncode == 0:
#     print('{} is UP'.format(ipaddress))
#     # print('ping output:')
#     # print(stdout.decode('ASCII'))

print(int(177))