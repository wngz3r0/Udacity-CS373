def get_probability(p,i):
    return p[i]

num_boxes = 5
# python2.7 version: p = map(lamda_:1.0 / num_boxes, range(num_boxes))
p = list(map(lambda _: 1 / num_boxes, range(num_boxes)))
print (get_probability(p,3))
