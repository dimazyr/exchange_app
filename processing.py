from datetime import datetime as dt
import datetime
def greatest_window(data: list, exchange_class: str, step_window = 1):
    """
    method that returns the largest number of trades on certain exchange
    :param data: the list of exchanges with time/price/size/exchange
    :param exchange_class: string of choosen exchange_market
    :param step_window: the certain size of slicing window(in this case: 1 sec)
    :return: the time in which the largest number of trades took place, start point of time, end point of time
    """
    sum=0
    step_window = datetime.timedelta(seconds=step_window)
    start_timepoint =dt.strptime(data[1][0], '%H:%M:%S.%f')
    check = dt.strptime(data[1][0], '%H:%M:%S.%f')
    index = 1
    #caclucalations of first sum(first window)
    while check < start_timepoint + step_window:
        if data[index][3] == exchange_class:
            sum += int(data[index][2])
        index+=1
        check = dt.strptime(data[index+1][0], '%H:%M:%S.%f')

    index_tail = 1
    max_sum=sum
    #moving of slicing window and comparing tail and head to update max_sum
    for i in range(index, len(data)):
        if data[i][3] == exchange_class:
            head = data[i][2]
            tail, index_tail = tail_sum(data, exchange_class,  data[i][0],step_window, index_tail)
            tail = int(tail)
            head = int(head)
            sum=sum-tail+head
            if(head>tail)&(sum>max_sum):
                max_sum=sum
                index_of_last_element = i
                first_element = dt.strftime((dt.strptime(data[index_of_last_element][0], '%H:%M:%S.%f' )-step_window), '%H:%M:%S.%f')[:-3]

    return max_sum,first_element, data[index_of_last_element][0]






def tail_sum(data:list, exchange_class: str ,time:str, step_window:dt , index_tail:int):
    """
    method that return the sum on tail elements that were been included in previous slicing window
    but aren`t included in new one
    :param data: list of instances with exchange info
    :param exchange_class: list of available classes
    :param time: string of current data of new instance
    :param step_window: the lenght of slicing window(step of window)
    :param index_tail: index of last element of the previous tail
    :return: the sum(number) of tail`s elements
    """
    time = dt.strptime(time, '%H:%M:%S.%f')
    timestamp = time - step_window
    sum_of_tail = 0
    while dt.strptime(data[index_tail][0], '%H:%M:%S.%f' ) < timestamp:
        if data[index_tail][3] == exchange_class:
            sum_of_tail +=int(data [index_tail][2])
        index_tail+=1
    return sum_of_tail, index_tail




def time_diff(starttime:str, endtime:str):
    """
    method that calculates the difference between two time points
    :param starttime: string that contains the start timedate
    :param endtime: string that contains the end timedate
    :return: the datetime type difference between two input dates
    """
    starttime = dt.strptime(starttime,'%H:%M:%S.%f')
    endtime = dt.strptime(endtime,'%H:%M:%S.%f')
    return starttime - endtime

