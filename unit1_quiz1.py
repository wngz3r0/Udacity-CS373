def get_probability(p,i):
    return p[i]

num_boxes = 5
p = list(map(lambda _: 1 / num_boxes, range(num_boxes)))
print (get_probability(p,3))
