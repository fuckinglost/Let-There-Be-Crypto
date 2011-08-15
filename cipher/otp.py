alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_dic_nl = dict(zip(range(26), alpha))
alpha_dic_ln = dict(zip(alpha, range(26)))

message = [28, 14, 19, 28, 39, 4, 31, 28, 18, 11, 36]
hobo = 'hoboesthudofhorror'

def transcode(x, mapping):
    if x is None or x not in mapping:
        return None
    return mapping[x]

def pad_func(x,y):
	if x is None or y is None:
		return None
	return (x-y) % 26

def conv_nl(x):
	if x is None:
		return None
	return dec_nl[x]

def conv_ln(x):
	if x is None:
		return None
	return dec_ln[x]

def alpha_nl(x):
	if x is None:
		return None
	return alpha_dic_nl[x]

def alpha_ln(x):
	if x is None:
		return None
	return alpha_dic_ln[x]

def one_time(message, pad):
	return ''.join(filter(lambda x:x, map(alpha_nl, map(pad_func, message, pad))))

def right_shift(x):
	return x[1:]+[x[0]]

def left_shift(x):
	return x[-1]+[x[:-1]]

def pad_rot(message, pad):
	print one_time(message, pad)
	for i in xrange(len(pad)):
		message = right_shift(message)
		print one_time(message, pad)

def mess_rot(message, pad):
	print one_time(message, pad)
	for i in xrange(len(message)):
		message = right_shift(message)
		print one_time(message, pad)
