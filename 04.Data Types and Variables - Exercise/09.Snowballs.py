n = int(input())
snowballs = [[int(input()), int(input()), int(input())] for i in range(n)]
balls_and_scores = [[snowballs[j][0], snowballs[j][1], snowballs[j][2],
                     int((snowballs[j][0] / snowballs[j][1]) ** snowballs[j][2])]
                    for j in range(len(snowballs))]
best_score = 0
best_ball = []

for i in range(len(balls_and_scores)):
    current_score = balls_and_scores[i][3]
    if current_score > best_score:
        best_score = current_score
        best_ball = balls_and_scores[i]

print(f"{int(best_ball[0])} : {int(best_ball[1])} = {int(best_ball[3])} ({int(best_ball[2])})")