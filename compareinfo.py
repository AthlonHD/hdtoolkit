# -*- coding=utf-8 -*-

def potential_contacts(person_a, person_b):
    """
    :param person_a: [("name","location",8,0,10,0),()]
    :param person_b:
    :return:
    """

    compare_result = set()

    for i in person_a:
        for j in person_b:
            location_a = i[1]
            location_b = j[1]
            date_a = i[2]
            date_b = j[2]
            begin_hour_a = i[3]
            end_hour_a = i[5]
            begin_hour_b = j[3]
            end_hour_b = j[5]
            begin_min_a = i[4]
            begin_min_b = j[4]
            end_min_a = i[6]
            end_min_b = j[6]

            if location_a == location_b and date_a == date_b:

                if begin_hour_a > begin_hour_b:

                    if begin_hour_a < end_hour_b:

                        if end_hour_a < end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_a, end_min_a)
                            compare_result.add(result_tuple)
                            break

                        if end_hour_a == end_hour_b:
                            if end_min_a <= end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_a, end_min_a)
                                compare_result.add(result_tuple)
                                break
                            if end_min_a > end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_b, end_min_b)
                                compare_result.add(result_tuple)
                                break

                        if end_hour_a > end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_b, end_min_b)
                            compare_result.add(result_tuple)
                            break

                    if begin_hour_a == end_hour_b and begin_min_a < end_min_b:
                        result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_b, end_min_b)
                        compare_result.add(result_tuple)
                        break

                if begin_hour_a == begin_hour_b:

                    if begin_min_a <= begin_min_b:

                        if end_hour_a < end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_a, end_min_a)
                            compare_result.add(result_tuple)
                            break

                        if end_hour_a == end_hour_b:
                            if end_min_a <= end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_a, end_min_a)
                                compare_result.add(result_tuple)
                                break
                            if end_min_a > end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_b, end_min_b)
                                compare_result.add(result_tuple)
                                break

                        if end_hour_a > end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_b, end_min_b)
                            compare_result.add(result_tuple)
                            break

                    if begin_min_a > begin_min_b:
                        if end_hour_a < end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_a, end_min_a)
                            compare_result.add(result_tuple)
                            break

                        if end_hour_a == end_hour_b:
                            if end_min_a <= end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_a, end_min_a)
                                compare_result.add(result_tuple)
                                break
                            if end_min_a > end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_b, end_min_b)
                                compare_result.add(result_tuple)
                                break

                        if end_hour_a > end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_a, begin_min_a, end_hour_b, end_min_b)
                            compare_result.add(result_tuple)
                            break

                if begin_hour_a < begin_hour_b:

                    if end_hour_a > begin_hour_b:

                        if end_hour_a > end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_b, end_min_b)
                            compare_result.add(result_tuple)
                            break

                        if end_hour_a == end_hour_b:
                            if end_min_a <= end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_a, end_min_a)
                                compare_result.add(result_tuple)
                                break
                            if end_min_a > end_min_b:
                                result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_b, end_min_b)
                                compare_result.add(result_tuple)
                                break

                        if end_hour_a < end_hour_b:
                            result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_a, end_min_a)
                            compare_result.add(result_tuple)
                            break

                    if end_hour_a == begin_hour_b and end_min_a > begin_min_b:
                        result_tuple = (location_a, date_a, begin_hour_b, begin_min_b, end_hour_a, end_min_a)
                        compare_result.add(result_tuple)
                        break

    result = (compare_result, (0, 0))
    time_result = (0, 0)
    for k in compare_result:
        begin_hour = k[2]
        begin_min = k[3]
        end_hour = k[4]
        end_min = k[5]

        hour_diff = end_hour - begin_hour
        min_diff = end_min - begin_min
        if min_diff < 0:
            min_diff = 60 - begin_min + end_min
            hour_diff = hour_diff - 1
        time_diff = (hour_diff, min_diff)

        time_result = (time_result[0] + time_diff[0], time_result[1] + time_diff[1])
        while time_result[1] >= 60:
            time_result = (time_result[0] + 1, time_result[1] - 60)

        result = (compare_result, time_result)

    return result


if __name__ == '__main__':
    a = [('Russel', 'Foodigm', 2, 9, 0, 10, 0),
         ('Russel', 'Afforage', 2, 10, 0, 11, 30),
         ('Russel', 'Nutrity', 2, 11, 45, 12, 0),
         ('Russel', 'Liberry', 3, 13, 0, 14, 15)]
    b = []
    test = potential_contacts(a, b)
    print(test)
