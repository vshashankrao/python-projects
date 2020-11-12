'''Shashank Rao
RUID 185005733
This problem involves calculating the grades of students
in a given semester and determining their overall letter
grade based on the percentage and scores of each assignment's
contribution to the total grade'''
import copy
#use of copy function in order to simplify dictionary transfer process
def create_dictionary(idfilename, hwfilename, qzfilename, examfilename):
    '''Creates dictionary of lists for the grades of each of the students'''
    file = open(idfilename, 'r')
    student_dict = {}
    for i in file:
        i.rstrip()
        student_dict[i] = {'hw':list_calculator(i, hwfilename, 4), 'quiz':list_calculator(i, qzfilename, 8), 'exam':list_calculator(i, examfilename, 2)}
    file.close()
    return student_dict

def list_calculator(id_number, listfile, r):
    '''Creates list containing grades of specific students'''
    temp_file = open(listfile, 'r')
    grades = [int(line.split()[1]) for line in temp_file if line.split()[0] == id_number]  
    while len(grades) < r:
        grades.append(0)
    temp_file.close
    return grades
def create_graderoster(sdata_dict, outfilename):
    '''creates a formatted text file for the grades of all the students in the class'''
    temp_outfile = open(outfilename, 'w')
    temp_outfile.write('{:<14} {:>10} {:>10} {:>10} {:>12} {:>10}\n'.format('RUID', 'HW(30)', 'QUIZ(30)', 'EXAM(40)', 'TOTAL(100)', 'GRADE'))
    temp_outfile.write('-' * 71)
    temp_outfile.write('\n')
    sdata_new_dict = sdata_dict.copy()
    student_grade_dict = {'hw':[], 'quiz':[], 'exam':[], 'score':[]}
    for key in sdata_new_dict:
        temp_outfile.write('{:<25} {:>10.2f} {:>10.2f} {:>10} \n'.format(key, grades_calculator(key, sdata_new_dict, student_grade_dict, 1)[0], grades_calculator(key, sdata_new_dict, student_grade_dict, 1)[1], grades_calculator(key, sdata_new_dict, student_grade_dict, 1)[2], grades_calculator(key, sdata_new_dict, student_grade_dict, 1)[3]))
    temp_outfile.write('\n')
    temp_outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Maximum', max(student_grade_dict['hw']), max(student_grade_dict['quiz']), max(student_grade_dict['exam']), max(student_grade_dict['score'])))                                                                     
    temp_outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Minimum', min(student_grade_dict['hw']), min(student_grade_dict['quiz']), min(student_grade_dict['exam']), min(student_grade_dict['score'])))
    temp_outfile.write('{:>14} {:>10.2f} {:>10.2f} {:>10.2f} {:>12.2f} \n'.format('Average', mean(student_grade_dict['hw']), mean(student_grade_dict['quiz']), mean(student_grade_dict['exam']), mean(student_grade_dict['score'])))         
    temp_outfile.close()
    
def letter_grade(score):
    '''calculates the letter grade based on score'''
    if score >= 90:
        grade = 'A'
    elif score >= 85:
        grade = 'B+'
    elif score >= 80:
        grade = 'B'
    elif score >= 75:
        grade = 'C+'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def grades_calculator(key, dictionary, student_data, check_var = 0):
    '''calculates the grade averages for all of the students'''
    temp_dictionary = copy.deepcopy(dictionary)
    '''implementation of deep copy in order to fully import the files from the inputted dictionary'''    
    temp_dictionary[key]['hw'].remove(min(temp_dictionary[key]['hw']))
    hw_average = (sum(temp_dictionary[key]['hw']) / 3) * 0.3
    
    temp_dictionary[key]['quiz'].remove(max(temp_dictionary[key]['hw']))
    temp_dictionary[key]['quiz'].remove(min(temp_dictionary[key]['hw']))
    quiz_average = (sum(temp_dictionary[key]['quiz']) / 6) * 0.6

    exam_average = ((sum(temp_dictionary[key]['exam'])) / 2 * 0.2)
    
    total = hw_average + quiz_average + exam_average
    if check_var == 1:
        student_data['hw'].append(hw_average)
        student_data['quiz'].append(quiz_average)
        student_data['exam'].append(exam_average)
        student_data['score'].append(total)

    return hw_average, quiz_average, exam_average, letter_grade(total)
        

def mean(input_list):
    '''calculates average of list of numbers'''
    x = 0
    for i in input_list:
        x += i
    average = x/len(input_list)
    return average
    

if __name__ == "__main__":
    create_graderoster(create_dictionary('studentids.txt', 'hwscores.txt', 'quizscores.txt', 'examscores.txt'), 'gradeRoster.txt')
        
              
              
        
