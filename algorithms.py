def greedy_coloring(vertices, color_limit):
  if color_limit < 1:
    print("Error: please input a valid color limit")
    return
  for v in vertices:
    candidate_color = 0
    v.color_with(candidate_color)
    while not v.is_properly_colored():
        candidate_color += 1
        v.color_with(candidate_color)
