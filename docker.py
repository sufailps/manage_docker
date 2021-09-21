import os
import json

def main_menu():
	print('1.Status of containers')
	print('2.Download new Image')
	print('3.Run container')
	print('4.Delete Container')
	print('5.Network details of container')
	print('6.Modify Network details of contaniner')
	print('7.Exit')

while True:
	main_menu()
	ch = int(input("Enter choice : "))
	if ch == 1:
		print("Docker Status")
		stat=os.popen('docker ps -a').read()
		print(stat)
	elif ch == 2:
		print("Download Image")
		image_name = input("Enter image_name:tag ")
		cmd = f'docker pull {image_name}'
		res = os.popen(cmd).read()
		print(res)
	elif ch == 3:
		print("Run Container")
		image_name = input("Enter image name:tag ")
		container_name = input('Enter name to add as image name')
		cmd = f'docker run --name {container_name} {image_name}'
		os.system(cmd)

	elif ch == 4:
		print("Delete Container")
		container_name = input('Enter container name to delete')
		cmd = f'docker rm {container_name}'
		res = os.popen(cmd).read()
		print(f'{res} Deleted successfully ')
	elif ch == 5:
		print("Network details")
		cmd = 'docker network inspect bridge'
		l = os.popen(cmd).read()
		l = json.loads(l)[0]
		for i in l["Containers"].values():
			print(f'Image Name => {i["Name"]} | Mac address => {i["MacAddress"]} | ipv4 address =>{i["IPv4Address"]}')
	elif ch == 6:
		print("Modifying Network")
		container_name = input('Enter container name for disconnect from bridge network : ')
		cmd = f'docker network disconnect bridge {container_name}'
		print(os.popen(cmd).read())
		print(f'{container_name} container disconnect from bridge network')

		print('creating network')
		network = input('enter a new network name  for docker network creation : ')
		cmd2 = f' sudo docker network create -d bridge --subnet=192.168.1.0/24  {network}'
		print(os.popen(cmd2).read())
		print(f'{network} Network created successfully')

		print('connect our container to newly created network')
		ntwork = input('Enter newly created network name :')
		cmd3 = f'docker network connect {ntwork} {container_name}'
		print(os.popen(cmd3).read())
		print(f'{container_name} container connected to {ntwork} Network')

	elif ch == 7:
		break

	else:
		print('Wrong option')
