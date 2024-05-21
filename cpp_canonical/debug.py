# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    debug.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slaye <slaye@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 11:28:35 by slaye             #+#    #+#              #
#    Updated: 2024/05/21 12:43:44 by slaye            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import color

DEBUG		= color.BOLD + "cppcanonical: "

ERR_ARGV	= DEBUG + color.RED + "wrong usage"
ERR_FORMAT	= DEBUG + color.RED + "wrong format"
ERR_FILE	= DEBUG + color.RED + "file already exist"

SUCCESS		= DEBUG + color.GREEN + "header file created"