# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slaye <slaye@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 12:13:54 by slaye             #+#    #+#              #
#    Updated: 2024/05/21 12:48:20 by slaye            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def get_config(name:str, fname:str):
	brackets = ('{', '}')
	header = [
		f"#ifndef {fname}",
		f"# define {fname}",
		f""
	]
	content = [
		f"class {name} {brackets[0]}",
		f"	public:",
		f"		{name}(void); // canonical",
		f"		{name}({name} const &ref); // canonical",
		f"		~{name}(void); // canonical",
		f"",
		f"		{name}	&operator=({name} const &ref); // canonical",
		f"{brackets[1]};",
		f""
	]
	footer = [
		f"#endif"
	]
	return ((header, content, footer))