import pygal
f1 = open('scores.txt', 'r')
stu_numbers = []
stu_names = []
usual_performances = []
exam_performances = []
final_scores = []
for line in f1.readlines():
    if line[:-1].strip():
        stu_numbers.append(line.split('\t')[1])
        stu_names.append(line.split('\t')[2])
        usual_performances.append(line.split('\t')[5])
        exam_performances.append(line.split('\t')[4])
        final_scores.append(line.split('\t')[7])

frequencies = [0, 0, 0, 0, 0]
for value in final_scores:
    if int(value) >= 0 and int(value) < 60:
        frequencies[0] += 1
    elif int(value) >= 60 and int(value) < 70:
        frequencies[1] += 1
    elif int(value) >= 70 and int(value) < 80:
        frequencies[2] += 1
    elif int(value) >= 80 and int(value) < 90:
        frequencies[3] += 1
    elif int(value) >= 90 and int(value) <= 100:
        frequencies[4] += 1
    else:
        print("Score error!")
        break

final_score_bar = pygal.Bar()
final_score_bar.title = "Final score analysis"
final_score_bar.x_labels = [
    'Fail', '60 - 70', '70 - 80', '80 - 90', '90 - 100'
]
final_score_bar._x_title = "Final score interval"
final_score_bar._y_title = "Final score frequency"
final_score_bar.add("sub-total", frequencies)
final_score_bar.render_to_file('Final_score.svg')
