import graphlab as gl

g = gl.load_sgraph('input/test.txt', format='snap')
pr = gl.pagerank.create(g)
pr_out = pr['pagerank']

print "#########"
for pr_out_index in pr_out:
    print pr_out_index

