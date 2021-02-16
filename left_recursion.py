import argparse



def left_recursion(rules):
	starts = []
	new_rules = []
	to_remove = []
	for rule in rules:
		start = []
		for right in rule[1]:
			start.append(right[0])
		starts.append(start)		

	for i in range(0, len(rules)):
		new_rule = (rules[i][0], rules[i][1])
		for j in range(0, i):
			if rules[j][0] in starts[i]:
				lit = rules[j][0]
				new_right = []
				for right in rules[i][1]:
					if right[0] == lit:
						sub_right = []
						for r in rules[j][1]:
							sub_right.append(right.replace(lit, r))
						for s in sub_right:	
							new_right.append(s)
					else:
						new_right.append(right)
				new_rule = (rules[i][0], new_right)

		if new_rule[0] not in [x[0] for x in new_rule[1]]:
			new_rules.append(new_rule)
		else:	
			new_rule_1 = (new_rule[0], [])
			new_rule_2 = (new_rule[0]+'’', [])
			for right in new_rule[1]:
				if new_rule[0] != right[0]:
					new_rule_1[1].append(right+new_rule_2[0])
				else:
					new_rule_2[1].append(right[1:]+new_rule_2[0])
			new_rule_2[1].append('epsilon')			
			new_rules.append(new_rule_1)
			new_rules.append(new_rule_2)		





						

		# new_rules.append(new_rule)		
	return new_rules				








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

    	rs = left_recursion(rules)	

    	with open('task_4_1_result.txt', 'w') as f:
	    	for rule in rs:
	    		f.write(rule[0]+' : ')
	    		for right in rule[1]:
	    			if right != rule[1][-1]:
	    				f.write(right+' | ')
	    			else:
	    				f.write(right)
	    		f.write('\n')			
