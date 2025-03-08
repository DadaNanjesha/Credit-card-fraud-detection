# List all the functions to check for the rules
def rules_check(UCL,score,speed,amount):
	if amount < UCL:
            if score > 200:
                if speed > 0 and speed < 1000:
					return True
					
	return False