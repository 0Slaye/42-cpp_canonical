# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slaye <slaye@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 11:11:08 by slaye             #+#    #+#              #
#    Updated: 2024/05/21 12:43:40 by slaye            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import debug
import config

def get_define_name(name:str):
	result = name.replace(".", "_")

	result = result.upper()
	return (result)

def execute(name:str):
	fname = name + ".hpp"
	header = config.get_config(name, get_define_name(fname))[0];
	content = config.get_config(name, get_define_name(fname))[1];
	footer = config.get_config(name, get_define_name(fname))[2];

	try:
		file = open(f"{fname}", "x")
	except FileExistsError:
		print(debug.ERR_FILE)
	else:
		for value in header:
			file.write(f"{value}\n")
		for value in content:
			file.write(f"{value}\n")
		for value in footer:
			file.write(f"{value}\n")
		file.close()
		print(debug.SUCCESS)

if __name__ == "__main__":
	argv = sys.argv;

	if (len(argv) != 2):
		print(debug.ERR_ARGV)
	elif (len(argv[1]) == 0):
		print(debug.ERR_FORMAT)
	else:
		execute(str(sys.argv[1]))
