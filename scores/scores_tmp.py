import numpy as np
import pygal
import os

# global variables
stu_numbers = []  # student campus number
stu_names = []  # student name
usual_performances = []  # usual performance
exam_performances = []  # final exam performance
final_scores = []  # score summary
frequencies = [0, 0, 0, 0, 0]  # frequencies of score levels
scores_1 = []  # scores of level 1
scores_2 = []  # scores of level 2
scores_3 = []  # scores of level 3
scores_4 = []  # scores of level 4
scores_5 = []  # scores of level 5
mean = []  # list of mean values
std = []  # list of standard deviations


def fileOpen():  # filter all txt files in current path
    global currentPath, files, txtFiles
    currentPath = os.getcwd()
    files = os.listdir(currentPath)
    txtFiles = []
    for txt in files:
        if 'txt' in txt:    # filter all txt files
            txtFiles.append(txt)


def mainProc():
    for txt in txtFiles:
        f = open(txt, 'r')
        for line in f.readlines():
            try:
                if line[:-1].strip():
                    stu_numbers.append(line.split()[1])
                    stu_names.append(line.split()[2])
                    usual_performances.append(int(line.split()[5]))
                    exam_performances.append(int(line.split()[4]))
                    final_scores.append(int(line.split()[7]))
            except ValueError:
                if line.split()[0] == '序号':
                    continue
                else:
                    print(line.split()[1] + ' ' + line.split()[2] +
                          ' abnormal data!!!')
            else:
                continue
            for value in final_scores:
                if int(value) >= 0 and int(value) < 60:
                    scores_1.append(value)
                    frequencies[0] += 1  # frequency of level 1
                elif int(value) >= 60 and int(value) < 70:
                    scores_2.append(value)
                    frequencies[1] += 1  # frequency of level 2
                elif int(value) >= 70 and int(value) < 80:
                    scores_3.append(value)
                    frequencies[2] += 1  # frequency of level 3
                elif int(value) >= 80 and int(value) < 90:
                    scores_4.append(value)
                    frequencies[3] += 1  # frequency of level 4
                elif int(value) >= 90 and int(value) <= 100:
                    scores_5.append(value)
                    frequencies[4] += 1  # frequency of level 5
                else:
                    print("Score error!")
                    break

            mean = [
                np.mean(scores_1),
                np.mean(scores_2),
                np.mean(scores_3),
                np.mean(scores_4),
                np.mean(scores_5)
            ]  # mean of levels
            std = [
                np.std(scores_1),
                np.std(scores_2),
                np.std(scores_3),
                np.std(scores_4),
                np.std(scores_5)
            ]  # standard deviations of levels

        print(txt)
        f.close()


def chartPlotting():
    # bar chart 1
    final_score_bar1 = pygal.Bar()
    final_score_bar1.title = "Final score intervals"
    final_score_bar1.x_labels = [
        'Fail', '60 - 70', '70 - 80', '80 - 90', '90 - 100']
    final_score_bar1._x_title = "Final score intervals"
    final_score_bar1._y_title = "Final score frequency"
    final_score_bar1.add("Sub-total", frequencies)
    final_score_bar1.render_to_file('Final_score_bar1.svg')

    # bar chart 2
    final_score_bar2 = pygal.Bar()
    final_score_bar2.title = "Final score means and standard deviations"
    final_score_bar2.x_labels = [
        'Fail', '60 - 70', '70 - 80', '80 - 90', '90 - 100']
    final_score_bar2._x_title = "Final score intervals"
    final_score_bar2._y_title = "Final score means and STD.s"
    final_score_bar2.add("Mean", mean)
    final_score_bar2.add("STD.", std)
    final_score_bar2.render_to_file('Final_score_bar2.svg')

    # pie chart
    final_score_pie = pygal.Pie()
    final_score_pie.title = "Final score percentage (%)"
    final_score_pie.add('90 - 100', frequencies[4] / len(stu_numbers) * 100)
    final_score_pie.add('80 - 90', frequencies[3] / len(stu_numbers) * 100)
    final_score_pie.add('70 - 80', frequencies[2] / len(stu_numbers) * 100)
    final_score_pie.add('60 - 70', frequencies[1] / len(stu_numbers) * 100)
    final_score_pie.add('Fail', frequencies[0] / len(stu_numbers) * 100)
    final_score_pie.render_to_file('Final_score_pie.svg')


fileOpen()
mainProc()
chartPlotting()
