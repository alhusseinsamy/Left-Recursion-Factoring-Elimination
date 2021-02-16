import argparse


def left_factoring(rules):
	to_remove = []
	# new_rules = []

	for rule in rules:
		for i in range(0, len(rule[1])):
			if rule[1][i][0] in [x[0] for x in rule[1][i+1:]]:
				to_remove.append(rule)
				common = rule[1][i][0]
				new_rule_1 = (rule[0], [])
				new_rule_2 = (rule[0]+'’', [])
				betas = []
				for right in rule[1]:
					if common == right[0]:
						# print(right[1:])
						new_rule_2[1].append(right[1:])
					else:
						betas.append(right)

				rules.append(new_rule_2)
				new_rule_1[1].append(common+new_rule_2[0])		
				if betas != []:
					for beta in betas:
						new_rule_1[1].append(beta)
				rules.append(new_rule_1)
				break

				# print(new_rule_1)
				# print(new_rule_2)
				# print('_______________________-----_____')
	
	last_rules = []	
	for rule in rules:
		if rule not in to_remove:
			last_rules.append(rule)

	return last_rules	





if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)

    rules = []
    with open(args.file) as f:
    	for line in f:
    		arr = line.split(':')
    		left_side = arr[0].replace(' ', '')
    		right = arr[1].replace(' ', '').replace('\n', '')
    		right_side = right.split('|')
    		rule_temp = [left_side, right_side]
    		rule = tuple(rule_temp)
    		rules.append(rule)
    	rs = left_factoring(rules)

    	with open('task_4_2_result.txt', 'w') as f:
    		for rule in rs:
	    		f.write(rule[0]+' : ')
	    		for right in rule[1]:
	    			if right != rule[1][-1]:
	    				f.write(right+' | ')
	    			else:
	    				f.write(right)
	    		f.write('\n')