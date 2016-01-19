__author__ = 'dev12'
def my_year_rang_with_bug(start,end,step=1):
    result = start
    while result < end:
        yield result
        result += step
def print_years(start,end,step=1,per_line=10):
    year = start
    count = 1
    for year in range(start,end+1,step):
        end_char = "\n" if count % per_line == 0 else "\t"
        print(year,end=end_char)
        count += 1
def main():
    """
    program entry point
    """
    start = 1800
    end = 2014
    step = 1
    per_line = 10

    year = start
    count = 1
    # 1. while 반복
    # while year <= end:
    #     if count % per_line == 0:
    #         print(year,end="\n")
    #     else :
    #         print(year,end="\t")
    #     # 위 축약 구문
    #     # end_char = "\n" if count % per_line == 0 else "\t"
    #     year += step
    #     count += 1

    # 2. interator 사용
    # for year in my_year_rang_with_bug(start,end+1):
    #     end_char = "\n" if count % per_line == 0 else "\t"
    #     print(year,end=end_char)
    #     year += step
    #     count += 1

    # 3. 함수 호출
    # print_years(start,end,step,per_line)

    #4. list 이용 if 절도 추가 가능하다!!
    years = range(start,end+1,step)
    years_to_print = [str(y) + "\n" if ( (years.index(y) + 1) % per_line == 0) else str(y) + "\t" for y in years ]
    print("".join(years_to_print))


if __name__ == '__main__':main()
