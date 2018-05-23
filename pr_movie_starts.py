# -*- coding: UTF-8 -*-
import xlrd
import csv
import graphlab as gl


def get_pr_input_no_weight_from_original(original_file):
    xlsx_book = xlrd.open_workbook(original_file)
    xlsx_sheet = xlsx_book.sheet_by_index(0)
    csvfile_pr_movie_start = open("output/pr_movie_start.csv", "w")
    writer_pr_movie_start = csv.writer(csvfile_pr_movie_start)
    for movie_star in  xlsx_sheet.col_values(6,1,xlsx_sheet.nrows):
        stars_list = movie_star.split(',')
        for i in range(0, len(stars_list)):
            for j in range(0, len(stars_list)):
                if i != j:
                    writer_pr_movie_start.writerow([stars_list[i].encode('utf-8'), stars_list[j].encode('utf-8')])
    csvfile_pr_movie_start.close()

def get_pr_result_from_input(input_file):
    g = gl.load_sgraph(input_file, format='csv')
    pr = gl.pagerank.create(g)
    pr_out = pr['pagerank']
    csvfile_pr_movie_start_result = open("output/pr_movie_start_result.csv", "w")
    writer_pr_movie_start_result = csv.writer(csvfile_pr_movie_start_result)

    for pr_out_item in pr_out:
        writer_pr_movie_start_result.writerow([pr_out_item['__id'], pr_out_item['pagerank'], pr_out_item['delta']])
    csvfile_pr_movie_start_result.close()

def get_pr_input_with_weight_from_original(original_file):
    xlsx_book = xlrd.open_workbook(original_file)
    xlsx_sheet = xlsx_book.sheet_by_index(0)
    csvfile_pr_movie_start = open("output/pr_movie_start_with_weight.csv", "w")
    writer_pr_movie_start = csv.writer(csvfile_pr_movie_start)


    for index in range(1, xlsx_sheet.nrows):
        print xlsx_sheet.cell_value(index, 6)
        stars_list = xlsx_sheet.cell_value(index, 6).split(',')
        for i in range(0, len(stars_list)):
            for j in range(0, len(stars_list)):
                if i != j:
                    if xlsx_sheet.cell_value(index,12) != "NULL":
                        writer_pr_movie_start.writerow([stars_list[i].encode('utf-8'), stars_list[j].encode('utf-8'),
                                                        int(xlsx_sheet.cell_value(index,12))])
                    else:
                        writer_pr_movie_start.writerow([stars_list[i].encode('utf-8'), stars_list[j].encode('utf-8'), 0])
    csvfile_pr_movie_start.close()

# get_pr_input_no_weight_from_original('input/movie_star_box.xlsx')
# get_pr_result_from_input('output/pr_movie_start.csv')
# get_pr_input_with_weight_from_original('input/movie_star_box.xlsx')
get_pr_result_from_input('output/pr_movie_start_with_weight.csv')

